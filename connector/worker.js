// Simply AI Ready connector: Tally assessment -> Kit
// Runs on Cloudflare Workers (free plan). Tally sends each finished assessment here by webhook;
// this adds the person to Kit with their results and tags.
//
// Settings in Cloudflare (Worker > Settings > Variables and Secrets):
//   KIT_API_KEY           (secret) Kit v4 API key: Kit > Settings > Developer > API keys
//   TALLY_SIGNING_SECRET  (secret) the signing secret you set on the Tally webhook
//
// Tags it adds (they must already exist in Kit):
//   marketing-ok (only if the email box was ticked), assessment-taken,
//   one result tag (ready / nearly-ready / foundations-needed / not-ready),
//   one package tag (rec-snapshot / rec-blueprint-small / rec-blueprint-growth / rec-blueprint-plus)
// marketing-ok is added BEFORE assessment-taken, because the Kit automation starts on
// assessment-taken and immediately checks for marketing-ok.

const RESULT_TAGS = {
  "ready": "ready",
  "nearly ready": "nearly-ready",
  "foundations needed": "foundations-needed",
  "not ready": "not-ready",
};

function packageTag(pkg) {
  const p = (pkg || "").toLowerCase();
  if (p.includes("plus")) return "rec-blueprint-plus";
  if (p.includes("growth")) return "rec-blueprint-growth";
  if (p.includes("small")) return "rec-blueprint-small";
  if (p.includes("snapshot")) return "rec-snapshot";
  return null;
}

export default {
  async fetch(request, env) {
    if (request.method !== "POST") {
      return new Response("Simply AI Ready connector is running.", { status: 200 });
    }
    const raw = await request.text();

    if (env.TALLY_SIGNING_SECRET) {
      const sig = request.headers.get("tally-signature") || "";
      if (!(await validSignature(raw, sig, env.TALLY_SIGNING_SECRET))) {
        return new Response("Signature does not match", { status: 401 });
      }
    }

    let payload;
    try {
      payload = JSON.parse(raw);
    } catch {
      return new Response("Not JSON", { status: 400 });
    }

    try {
      const result = await handle(payload, env);
      return Response.json(result);
    } catch (err) {
      console.error(err && err.stack ? err.stack : String(err));
      // A 500 tells Tally to retry the webhook later.
      return new Response("Error: " + (err && err.message ? err.message : String(err)), { status: 500 });
    }
  },
};

export async function handle(payload, env) {
  const fields = (payload && payload.data && payload.data.fields) || [];
  const find = (label) =>
    fields.find((f) => (f.label || "").trim().toLowerCase() === label.toLowerCase());
  const text = (label) => {
    const f = find(label);
    return f ? displayValue(f) : "";
  };

  const email = text("Work email").trim();
  if (!email) return { skipped: "no email in submission" };

  const fullName = text("Your name").trim();
  const firstName = fullName.split(/\s+/)[0] || "";

  const consent = fields.some(
    (f) => (f.label || "").trim().toLowerCase().startsWith("staying in touch") && isTicked(f.value)
  );

  const band = text("band");
  const pkg = text("package");

  // 1. Create or update the subscriber with their results.
  await kit(env, "/subscribers", "POST", {
    email_address: email,
    first_name: firstName,
    state: "active",
    fields: {
      score: text("total"),
      result: band,
      package: pkg,
      price: text("package_price"),
      deposit: text("package_deposit"),
      organisation: text("Organisation"),
    },
  });

  // 2. Tags, marketing-ok first.
  const tags = [];
  if (consent) tags.push("marketing-ok");
  const resultTag = RESULT_TAGS[band.trim().toLowerCase()];
  if (resultTag) tags.push(resultTag);
  const pTag = packageTag(pkg);
  if (pTag) tags.push(pTag);
  tags.push("assessment-taken"); // last: this one starts the Kit automation

  const tagIds = await loadTagIds(env);
  const applied = [];
  const missing = [];
  for (const name of tags) {
    const id = tagIds[name.toLowerCase()];
    if (!id) {
      missing.push(name);
      continue;
    }
    await kit(env, `/tags/${id}/subscribers`, "POST", { email_address: email });
    applied.push(name);
  }
  if (missing.includes("assessment-taken")) {
    throw new Error("The tag 'assessment-taken' does not exist in Kit");
  }
  return { ok: true, email, firstName, consent, applied, missing };
}

function displayValue(f) {
  const v = f.value;
  if (v === null || v === undefined) return "";
  if (Array.isArray(v)) {
    if (Array.isArray(f.options)) {
      return v
        .map((id) => {
          const o = f.options.find((opt) => opt.id === id);
          return o ? o.text : String(id);
        })
        .join(", ");
    }
    return v.join(", ");
  }
  if (Array.isArray(f.options) && typeof v === "string") {
    const o = f.options.find((opt) => opt.id === v);
    if (o) return o.text;
  }
  return String(v);
}

function isTicked(v) {
  if (Array.isArray(v)) return v.length > 0;
  return v === true || v === "true";
}

async function kit(env, path, method, body) {
  const res = await fetch("https://api.kit.com/v4" + path, {
    method,
    headers: {
      "X-Kit-Api-Key": env.KIT_API_KEY,
      "Content-Type": "application/json",
      Accept: "application/json",
    },
    body: body ? JSON.stringify(body) : undefined,
  });
  const t = await res.text();
  if (!res.ok) throw new Error(`Kit ${method} ${path} returned ${res.status}: ${t}`);
  return t ? JSON.parse(t) : {};
}

async function loadTagIds(env) {
  const ids = {};
  let after = null;
  do {
    const q = "/tags?per_page=1000" + (after ? "&after=" + encodeURIComponent(after) : "");
    const res = await kit(env, q, "GET");
    for (const t of res.tags || []) ids[(t.name || "").toLowerCase()] = t.id;
    after = res.pagination && res.pagination.has_next_page ? res.pagination.end_cursor : null;
  } while (after);
  return ids;
}

async function validSignature(raw, signature, secret) {
  const enc = new TextEncoder();
  const key = await crypto.subtle.importKey(
    "raw", enc.encode(secret), { name: "HMAC", hash: "SHA-256" }, false, ["sign"]
  );
  const mac = await crypto.subtle.sign("HMAC", key, enc.encode(raw));
  const b64 = btoa(String.fromCharCode(...new Uint8Array(mac)));
  return b64 === signature;
}
