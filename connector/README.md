# Tally → Kit connector

`worker.js` runs on Cloudflare Workers (free). Tally posts each AI Ready Assessment submission to it by webhook; it creates or updates the Kit subscriber (first name, score, result, package, price, deposit, organisation) and adds tags: `marketing-ok` (only if the email box was ticked), the result tag, the package tag, then `assessment-taken`, which starts the Kit automation.

Secrets on the Worker: `KIT_API_KEY` (Kit v4 API key) and `TALLY_SIGNING_SECRET` (the same value set on the Tally webhook).
To update: paste the new `worker.js` into the Worker's code editor in Cloudflare and click Deploy.

The same Worker also handles the 2-minute **SharePoint Ready Scorecard** (Tally form X5odvL). It spots the form by its name, saves `scorecard_score`, `scorecard_result` and `scorecard_for`, and adds `marketing-ok` (if ticked), `scorecard-org` or `scorecard-me`, then `scorecard-taken`. It never adds `assessment-taken`. Point that form's webhook at the same Worker URL with the same signing secret.
