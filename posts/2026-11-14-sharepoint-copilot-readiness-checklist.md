---
title: Is your SharePoint ready for Copilot? 10 checks to run before you switch it on
date: 2026-11-14
excerpt: A plain-English SharePoint Copilot readiness checklist: ten checks to see what Copilot will find, what it shouldn't, and what to fix first.
keywords: SharePoint Copilot readiness, Copilot readiness checklist, is SharePoint ready for Copilot, Microsoft 365 Copilot preparation, Copilot SharePoint best practices
---

Microsoft 365 Copilot doesn't arrive with its own knowledge of your organisation. It reads yours. Every answer it gives is built from the documents, pages and chats your people can already open in SharePoint, Teams and OneDrive.

That is the whole readiness question in one sentence: **is what your people can open the same as what you'd want Copilot to quote?**

For most organisations the honest answer is "not quite". The good news is that you can find out in an afternoon. Here are the ten checks I run first.

## First, how Copilot decides what to show

Copilot respects permissions. Microsoft is clear that it [only surfaces organisational data that the individual user has at least view permission to](https://learn.microsoft.com/en-us/sharepoint/sharepoint-copilot-best-practices). It will not show Sam something Sam can't open.

The catch is that most people can open far more than anyone realises. A folder shared with "everyone" three years ago. A team site that was set to public by default. Search has always been able to find those files, but people rarely went looking. Copilot goes looking for them, every time someone asks a question.

So Copilot doesn't create a security problem. It finds the one you already have.

## The 10 checks

### 1. Does every team have one clear home?

Ask three people in the same team where the current version of a key document lives. If you get three answers, Copilot has three places to answer from. Each team needs one site that is the obvious home for its documents.

### 2. Who can see your confidential folders?

Not who should. Who can. Open the site that holds HR, finance or board content, go to **Settings**, then **Site permissions**, and read the list. Look for "Everyone except external users". If it's there, every person in your organisation can open that content, and so can their Copilot.

### 3. What is your default sharing link?

In the SharePoint admin center, go to **Policies**, then **Sharing**. If the default link type is "Anyone" or "People in your organisation", every casual share widens access. Change the default to **Specific people**. It is the single most valuable setting change you can make this week.

### 4. How many guests still have access?

Guests are external people you invited once and forgot. In the Microsoft Entra admin center, filter users by **User type: Guest** and sort by last sign-in. Anyone who hasn't signed in for 90 days is a candidate for removal.

### 5. Which version is the real one?

If your leave policy exists as "Leave Policy", "Leave Policy v2" and "Leave Policy FINAL", Copilot has no way of knowing which one is current. It will pick one, confidently. Pick one home for each policy and delete or archive the copies.

### 6. Are documents described, or just named?

A file called "Agreement_final.docx" in a folder called "Misc" tells Copilot almost nothing. The same file with a **Document Type** of Contract, a **Document Status** of Approved and a **Document Owner** tells it a great deal. Microsoft's own guidance says [simple information architecture, clear document structure and detailed metadata lead to higher quality answers](https://learn.microsoft.com/microsoft-365/copilot/employee-self-service/optimization-sharepoint). I cover this properly in [metadata vs folders](/blog/sharepoint-metadata-vs-folders-copilot/).

### 7. How deep do your folders go?

Count the clicks to reach a typical document. More than three levels deep usually means the folder path is doing the job that metadata should do, and paths that long are where duplicates hide.

### 8. Does every site and team have an owner?

Sites without owners don't get cleaned up, and nobody answers when access needs reviewing. Every team in Microsoft Teams should have at least two owners, so one person leaving doesn't orphan it.

### 9. When did you last archive anything?

Old content is the most common source of wrong answers. A 2019 price list is still a price list as far as Copilot is concerned. In the SharePoint admin center, the **Active sites** list shows the last activity date for every site. Sort by it. The sites nobody has touched in a year are your first archive candidates.

### 10. Have you told Copilot what it should never touch?

Some content should never appear in an answer, whatever the permissions say: HR casework, board papers, legal matters. Name those areas first. Then protect them with tighter permissions and sensitivity labels. If your organisation has Copilot licences, SharePoint Advanced Management also gives you [Restricted Content Discovery](https://learn.microsoft.com/en-us/sharepoint/restricted-content-discovery), which keeps a site out of Copilot and organisation-wide search without changing who can open it.

## What a good result looks like

You don't need a perfect score on all ten before you switch Copilot on. You need to know your answer to each one, and to have fixed the two or three that carry real risk. In my experience those are almost always check 2 (who can see confidential content), check 3 (the default sharing link) and check 5 (duplicate versions).

## The tools Microsoft gives you

If you have at least one Copilot licence assigned, your SharePoint admins get access to SharePoint Advanced Management. Its [data access governance reports](https://learn.microsoft.com/en-us/sharepoint/data-access-governance-reports) show which sites have the broadest access, the most sharing links, and content shared with everyone in the organisation. Microsoft's guide to [getting ready for Copilot with SharePoint Advanced Management](https://learn.microsoft.com/sharepoint/get-ready-copilot-sharepoint-advanced-management) walks through them.

The reports tell you where the problems are. They don't tell you how your sites should be organised so the problems don't come back. That part is information architecture, and it's why I keep saying there is no AI without IA.

## Where to start

Run checks 2, 3 and 4 today. They take under an hour and they close the biggest gaps.

Then, if you'd like a score for all six areas of readiness, the free AI Ready Assessment takes about 12 minutes and gives you your biggest risks and five quick wins on the spot.
