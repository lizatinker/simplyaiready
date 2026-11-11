#!/usr/bin/env python3
"""Simply AI Ready — static site builder (same setup as Tech Style Bytes).

Pages:          pages/<name>.html   (body content only; header and footer are added here)
Blog post:      posts/YYYY-MM-DD-slug.md  (front matter + markdown body)
Images:         images/  (web-sized, location data stripped)
Build:          python3 build.py            -> docs/  (GitHub Pages serves this folder)
Preview drafts: python3 build.py --drafts

Post front matter keys (one per line, `key: value`):
  title, date (YYYY-MM-DD), excerpt, cover (images/x.jpg), keywords (comma list), draft (true/false)
"""
import datetime, html, os, re, shutil, sys
import markdown

SITE = {
    "name": "Simply AI Ready",
    "url": "https://simplyaiready.com",
    "author": "Liza Tinker",
    "description": "Copilot readiness for SharePoint, Teams and OneDrive. Find out what Copilot will see, fix what it shouldn't, and get a blueprint anyone can build. By Liza Tinker, Microsoft MVP.",
}
ASSESSMENT_URL = "/assessment/"
ROOT = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(ROOT, "docs")
DRAFTS = "--drafts" in sys.argv
CUSTOM_DOMAIN_LIVE = True  # keeps docs/CNAME so GitHub Pages serves simplyaiready.com

PAGES = {
    # file in pages/: (output path, title, description)
    "index.html": ("", "", SITE["description"]),
    "assessment.html": ("assessment/", "Free AI Ready Assessment", "30 questions, about 12 minutes. Get your Copilot readiness score for SharePoint, Teams and OneDrive, your biggest risks, five quick wins and the right next step."),
    "packages.html": ("packages/", "Packages and pricing", "AI Ready Snapshot, Blueprint and Blueprint Plus: fixed-price Copilot readiness packages for SharePoint, Teams and OneDrive, plus build and support plans."),
    "newsletter.html": ("newsletter/", "The SharePoint Edit – weekly newsletter", "One email a week from Liza Tinker, Microsoft MVP: what changed in SharePoint, Teams, OneDrive and Copilot, and one thing worth fixing."),
}


def esc(s):
    return html.escape(str(s or ""))


def header():
    return """<header style="background:#ffffff;border-bottom:4px solid #ff0876">
<div style="max-width:1200px;margin:0 auto;padding:20px 24px;display:flex;flex-wrap:wrap;gap:16px 32px;align-items:center;justify-content:space-between">
<a href="/" style="text-decoration:none;display:flex;flex-direction:column;gap:2px">
<span style="font-family:'Oswald','Arial Narrow',sans-serif;font-weight:500;font-size:26px;letter-spacing:1px;color:#0d1b3e">SIMPLY AI READY</span>
<span style="font-size:12px;color:#41515a">with Liza Tinker, Microsoft MVP</span>
</a>
<nav aria-label="Main" style="display:flex;flex-wrap:wrap;gap:8px 28px;align-items:center;font-size:15px">
<a href="/#how" style="text-decoration:none">How it works</a>
<a href="/packages/" style="text-decoration:none">Packages</a>
<a href="/blog/" style="text-decoration:none">Blog</a>
<a href="/newsletter/" style="text-decoration:none">Newsletter</a>
<a href="/assessment/" style="text-decoration:none;background:#0d1b3e;color:#ffffff;padding:12px 20px;font-weight:600;min-height:44px;box-sizing:border-box;display:inline-flex;align-items:center">Take the assessment</a>
</nav>
</div>
</header>"""


def footer():
    year = datetime.date.today().year
    return f"""<footer style="background:#ffffff;border-top:1px solid #d9dce3">
<div style="max-width:1200px;margin:0 auto;padding:28px 24px;display:flex;flex-wrap:wrap;gap:12px 24px;justify-content:space-between;align-items:center;font-size:14px;color:#41515a">
<span>SharePoint, simply sorted. · © {year} Liza Tinker</span>
<span><a href="/assessment/">Assessment</a> · <a href="/newsletter/">Newsletter</a> · <a href="/blog/">Blog</a> · All prices AUD, ex GST</span>
</div>
</footer>"""


def page(title, body, path, desc, og_type="website", extra_head=""):
    t = esc(f"{title} · {SITE['name']}" if title else f"{SITE['name']} · Copilot readiness for SharePoint, Teams and OneDrive")
    url = f"{SITE['url']}/{path}"
    return f"""<!DOCTYPE html>
<html lang="en-AU"><head>
<meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<title>{t}</title>
<meta name="description" content="{esc(desc)}">
<link rel="canonical" href="{url}">
<meta name="robots" content="index, follow, max-image-preview:large">
<meta property="og:title" content="{t}"><meta property="og:description" content="{esc(desc)}">
<meta property="og:url" content="{url}"><meta property="og:type" content="{og_type}"><meta property="og:site_name" content="{SITE['name']}">
<link rel="stylesheet" href="/static/style.css">
{extra_head}
</head><body>
{header()}
<main>
{body}
</main>
{footer()}
</body></html>
"""


def load_posts():
    posts, d = [], os.path.join(ROOT, "posts")
    for fn in sorted(os.listdir(d)):
        if not fn.endswith(".md"):
            continue
        raw = open(os.path.join(d, fn), encoding="utf-8").read()
        m = re.match(r"^---\s*\n(.*?)\n---\s*\n(.*)$", raw, re.S)
        meta, body = {}, raw
        if m:
            for line in m.group(1).splitlines():
                if ":" in line:
                    k, v = line.split(":", 1)
                    meta[k.strip()] = v.strip()
            body = m.group(2)
        if meta.get("draft", "false").lower() == "true" and not DRAFTS:
            continue
        meta["slug"] = re.sub(r"^\d{4}-\d{2}-\d{2}-", "", fn[:-3])
        meta["date"] = datetime.date.fromisoformat(meta.get("date") or fn[:10])
        meta["html"] = markdown.markdown(body, extensions=["extra", "smarty"])
        posts.append(meta)
    return sorted(posts, key=lambda p: p["date"], reverse=True)


CTA = """<aside class="cta">
<p class="eyebrow">WHERE DOES YOUR ORGANISATION STAND?</p>
<p class="cta-title">Take the free AI Ready Assessment</p>
<p>30 questions, about 12 minutes. Your score, your biggest risks, five quick wins and the right next step.</p>
<p><a class="btn" href="/assessment/">Start the assessment</a> <a class="btn ghost" href="/newsletter/">Or get the weekly newsletter</a></p>
</aside>"""


def post_page(p):
    import json
    ld = json.dumps({
        "@context": "https://schema.org", "@type": "BlogPosting",
        "headline": p.get("title", ""), "description": p.get("excerpt", ""),
        "datePublished": p["date"].isoformat(), "author": {"@type": "Person", "name": SITE["author"]},
        "publisher": {"@type": "Organization", "name": SITE["name"]},
        "mainEntityOfPage": f"{SITE['url']}/blog/{p['slug']}/",
        "keywords": p.get("keywords", ""),
    })
    body = f"""<article class="post">
<p class="eyebrow"><time datetime="{p['date'].isoformat()}">{p['date'].strftime('%-d %B %Y')}</time> · Liza Tinker, Microsoft MVP</p>
<h1>{esc(p.get('title'))}</h1>
{('<p class="excerpt">' + esc(p.get('excerpt')) + '</p>') if p.get('excerpt') else ''}
<div class="prose">{p['html']}</div>
{CTA}
</article>"""
    return page(p.get("title", ""), body, f"blog/{p['slug']}/", p.get("excerpt") or SITE["description"], "article",
                f'<script type="application/ld+json">{ld}</script>')


def blog_index(posts):
    items = "".join(f"""<a class="postcard" href="/blog/{p['slug']}/"><time>{p['date'].strftime('%-d %B %Y')}</time><h2>{esc(p.get('title'))}</h2><p>{esc(p.get('excerpt'))}</p></a>""" for p in posts)
    if not items:
        items = '<p>The first posts are on their way. <a href="/newsletter/">Get them by email</a>.</p>'
    body = f"""<section class="bloghead"><p class="eyebrow">THE BLOG</p><h1>Copilot readiness, explained simply</h1>
<p>Practical guides to getting SharePoint, Teams and OneDrive ready for Copilot, from Liza Tinker, Microsoft MVP.</p></section>
<section class="postlist">{items}</section>{CTA}"""
    return page("Blog", body, "blog/", "Practical guides to getting SharePoint, Teams and OneDrive ready for Copilot, by Liza Tinker, Microsoft MVP.")


def write(rel, content):
    path = os.path.join(OUT, rel)
    os.makedirs(os.path.dirname(path), exist_ok=True)
    open(path, "w", encoding="utf-8").write(content)


def main():
    if os.path.isdir(OUT):
        shutil.rmtree(OUT)
    os.makedirs(OUT)
    shutil.copytree(os.path.join(ROOT, "static"), os.path.join(OUT, "static"))
    if os.path.isdir(os.path.join(ROOT, "images")):
        shutil.copytree(os.path.join(ROOT, "images"), os.path.join(OUT, "images"))
    urls = []
    for fn, (path, title, desc) in PAGES.items():
        body = open(os.path.join(ROOT, "pages", fn), encoding="utf-8").read()
        write(path + "index.html", page(title, body, path, desc))
        urls.append(path)
    posts = load_posts()
    for p in posts:
        write(f"blog/{p['slug']}/index.html", post_page(p))
        urls.append(f"blog/{p['slug']}/")
    write("blog/index.html", blog_index(posts))
    urls.append("blog/")
    write("404.html", page("Page not found", '<section class="bloghead"><h1>That page has moved</h1><p><a href="/">Go to the home page</a> or <a href="/assessment/">take the assessment</a>.</p></section>', "404.html", SITE["description"]))
    today = datetime.date.today().isoformat()
    write("sitemap.xml", '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n' +
          "".join(f"<url><loc>{SITE['url']}/{u}</loc><lastmod>{today}</lastmod></url>\n" for u in urls) + "</urlset>\n")
    write("robots.txt", f"User-agent: *\nAllow: /\nSitemap: {SITE['url']}/sitemap.xml\n")
    if CUSTOM_DOMAIN_LIVE:
        write("CNAME", "simplyaiready.com\n")
    write(".nojekyll", "")
    print(f"Built {len(urls)} pages into docs/")


if __name__ == "__main__":
    main()
