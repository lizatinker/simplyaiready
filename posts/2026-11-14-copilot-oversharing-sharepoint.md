---
title: Copilot oversharing in SharePoint: how to find it and fix it
date: 2026-11-14
excerpt: Copilot doesn't break your SharePoint permissions, it reveals them. Here is what oversharing means, the four places it hides, how to find it and the order to fix it in.
keywords: Copilot oversharing, SharePoint oversharing, Copilot SharePoint permissions, Everyone except external users, data access governance reports, Restricted Content Discovery
---

"Could Copilot show someone a document they shouldn't see?"

It's the first question leaders ask me, and the answer has two halves. No, Copilot can't open anything a person doesn't already have access to. And yes, it can absolutely show them something you never meant them to see, because they had access all along and nobody knew.

That gap between what people can open and what you meant them to open has a name: oversharing. Here's how to find it and fix it.

## What oversharing actually is

Oversharing is content that more people can open than need to. Nobody did it on purpose. It builds up from years of small, reasonable decisions: a quick share to get something done, a site created with the default settings, a folder opened up for a project that finished long ago.

Before Copilot, oversharing was mostly harmless because people only found what they went looking for. Microsoft states that Copilot [only surfaces data a user has at least view permission to](https://learn.microsoft.com/en-us/sharepoint/sharepoint-copilot-best-practices). The trouble is that Copilot searches everything that user can reach, for every question. A salary spreadsheet in an overshared folder used to be safe through obscurity. Now it's one question away.

## The four places oversharing hides

### 1. "Everyone except external users"

This is a built-in group that contains every person in your organisation. When it's added to a site, a library or a single file, that content is open to all staff. It's the most common cause of oversharing I find, and it's often added by someone who just wanted a colleague to be able to open a file.

### 2. Sharing links

Every time someone clicks **Share**, they create a link. "Anyone with the link" works for people outside your organisation. "People in your organisation" works for every staff member who gets hold of it. These links don't expire unless you set them to, and they outlive the reason they were created.

### 3. Public teams and sites

A team in Microsoft Teams set to **Public** can be joined by anyone in the organisation, and its files are open to all of them. Many teams were created public simply because that was the option on screen.

### 4. Broken inheritance

SharePoint lets you give a single folder or file different permissions from the site it lives in. Each one is an exception somebody has to remember. After a few years there are hundreds, and nobody can say who has access to what without checking each one.

## How to find it

### If you have Copilot licences

Once at least one Copilot licence is assigned, your SharePoint admins get SharePoint Advanced Management. Its [data access governance reports](https://learn.microsoft.com/en-us/sharepoint/data-access-governance-reports) are built for exactly this job. In the SharePoint admin center, go to **Reports**, then **Data access governance**. Three reports matter most:

- **Site permissions across your organisation** shows which sites the most people can reach.
- **Sharing links** shows where the most "Anyone" and "People in your organisation" links were created recently.
- **Shared with Everyone except external users** shows where content has been opened to all staff.

Start with the site permissions report. It gives you a ranked list, so you can deal with the ten riskiest sites first instead of auditing hundreds.

### If you don't have Copilot licences yet

You can still learn a lot from what's included with Microsoft 365:

1. In the SharePoint admin center, open **Sites**, then **Active sites**. Add the **External sharing** and **Teams** columns and export the list.
2. Open your most sensitive sites one at a time. Go to **Settings**, then **Site permissions**, and look for "Everyone except external users".
3. In the Teams admin center, list your teams and filter by privacy to find the public ones.
4. In the Microsoft Entra admin center, filter users by **User type: Guest** to see every external person with an account.

It's slower, but for a small or mid-sized organisation it's a perfectly good first pass.

## The order to fix it in

Don't try to fix everything. Fix it in this order.

**1. Stop it getting worse.** Change the default sharing link to **Specific people** in the SharePoint admin center under **Policies**, then **Sharing**. From that moment, new shares go only to the people named.

**2. Protect the crown jewels.** List the content that would really hurt if the wrong person saw it: HR, payroll, board, legal, anything about individual clients or members. Check the permissions on those sites by hand and remove "Everyone except external users" wherever it appears.

**3. Buy time on risky sites.** If a sensitive site needs more work than you can do this week, [Restricted Content Discovery](https://learn.microsoft.com/en-us/sharepoint/restricted-content-discovery) keeps it out of Copilot and organisation-wide search without changing who can open it. It's a holding measure, not a fix. Note that the older Restricted SharePoint Search feature is being retired, so plan around Restricted Content Discovery instead.

**4. Clean up links and guests.** Remove "Anyone" links that are no longer needed and guests who haven't signed in for 90 days.

**5. Make public teams private** unless there's a reason for the whole organisation to see them.

## Why it keeps coming back

Here's what the reports won't tell you. Oversharing is a symptom. People overshare when they can't work out where something belongs or who should see it. If your sites are organised by whoever happened to create them, with one giant library for everything, then sharing file by file is the only way to get work done.

Fix the structure and most oversharing stops at the source. When each team has one clear home, and each site has an owner and a defined audience, access is decided once at the site level and people stop inventing workarounds. My [10-point readiness checklist](/blog/sharepoint-copilot-readiness-checklist/) covers the structural checks alongside the security ones.

That is why I treat oversharing as an information architecture problem as much as a security one. Tidy permissions on a messy structure don't stay tidy.
