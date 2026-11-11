# Simply AI Ready

Liza Tinker's Copilot readiness consulting site for SharePoint, Teams and OneDrive. Live at https://simplyaiready.com

## How it fits together
- **Site:** static pages built by `build.py` into `docs/`. GitHub Pages serves `docs/` (same setup as Tech Style Bytes).
- **Assessment:** Tally form `M1D0QM`, embedded on `/assessment/`. Scoring, result levels and the recommended package live in Tally.
- **Email:** Kit. Assessment results and follow-ups, plus the weekly newsletter form on `/newsletter/`.
- **Payments:** Stripe deposit (in Tally or Kit). **Bookings:** 15-minute chat link.

## Edit or publish (for Claude)
1. Page content lives in `pages/*.html` (body only; header and footer come from `build.py`).
2. Blog posts: `posts/YYYY-MM-DD-slug.md` with front matter `title`, `date`, `excerpt`, `keywords`, optional `cover` and `draft: true`. Write in Liza's voice, Australian English; every post ends with the assessment call to action automatically.
3. SEO: buyer-intent titles ("Is your SharePoint ready for Copilot?"), a clear `excerpt` (used as the meta description) and `keywords`.
4. `pip install markdown`, then `python3 build.py` (`--drafts` to preview drafts). Commit and push to `main`.
5. Keep `CUSTOM_DOMAIN_LIVE = True` so `docs/CNAME` stays.

Brand: navy #0d1b3e, pink #ff0876, teal #0a8086, yellow #f0c808; DM Serif Display, Oswald, Poppins (self-hosted in `static/fonts`). Never name clients or Liza's employer.
