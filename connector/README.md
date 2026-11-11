# Tally → Kit connector

`worker.js` runs on Cloudflare Workers (free). Tally posts each AI Ready Assessment submission to it by webhook; it creates or updates the Kit subscriber (first name, score, result, package, price, deposit, organisation) and adds tags: `marketing-ok` (only if the email box was ticked), the result tag, the package tag, then `assessment-taken`, which starts the Kit automation.

Secrets on the Worker: `KIT_API_KEY` (Kit v4 API key) and `TALLY_SIGNING_SECRET` (the same value set on the Tally webhook).
To update: paste the new `worker.js` into the Worker's code editor in Cloudflare and click Deploy.
