---
title: Metadata vs folders in SharePoint: what Copilot actually needs
date: 2026-11-14
excerpt: Folders tell Copilot where a file is. Metadata tells it what the file is. Why that decides your Copilot answers, and the four columns to start with.
keywords: SharePoint metadata vs folders, SharePoint metadata Copilot, SharePoint information architecture, SharePoint columns best practice, term store, there is no AI without IA
---

Open almost any SharePoint library and you'll find the same thing: folders inside folders inside folders. Client, then year, then project, then "Drafts", then "Old", then "Old - do not use".

Folders feel safe because they look like the file server everyone grew up with. For people, they more or less work. For Copilot, they hide most of what it needs to know.

## What a folder tells Copilot (not much)

A folder path answers one question: where is this file? `Clients / Acme / 2024 / Contracts / Final` tells a person a fair amount, because a person reads the whole path and fills in the gaps.

The folder says nothing about the file itself. Is it approved or a draft? Who owns it? Is it a contract or a quote? Is it still current? A person guesses from the name. Copilot has to guess too, and when there are five similar files in five similar folders, it sometimes guesses wrong.

## What metadata tells Copilot (a lot)

Metadata is information about a document, stored in columns next to it. Instead of burying a file in `Contracts / 2024 / Final`, you store it once and describe it:

| Column | Value |
|---|---|
| Document Type | Contract |
| Document Status | Approved |
| Department | Legal |
| Document Owner | Priya Shah |

Now the question "what's our current approved contract with Acme?" has an answer that doesn't depend on anyone's folder habits.

Microsoft's guidance on optimising SharePoint for Copilot says it directly: [simple information architecture, clear document structure, detailed metadata and well-governed access translate into higher quality, citation-backed answers](https://learn.microsoft.com/microsoft-365/copilot/employee-self-service/optimization-sharepoint). The same guidance notes that managed metadata allows more granular search and filtering, which matters more as your environment grows.

## The four columns to start with

You don't need fifty columns. Most organisations get most of the benefit from four, applied consistently across every library:

1. **Document Type**: what kind of thing it is. Policy, Procedure, Contract, Template, Report, Minutes.
2. **Document Status**: where it is in its life. Draft, In Review, Approved, Superseded.
3. **Department**: which part of the organisation it belongs to.
4. **Document Owner**: the person responsible for keeping it right.

Document Status is the one that changes Copilot's answers most. If only one version of a policy is marked Approved, there's no longer a contest between "v2", "FINAL" and "FINAL_revised".

## Use the term store so the values match

Columns only help if everyone uses the same values. If one library says "HR", another says "Human Resources" and a third says "People and Culture", you have three departments as far as search is concerned.

The term store fixes this. It's a central list of approved terms, managed in the SharePoint admin center under **Content services**, then **Term store**. You define your departments and document types once, and every site uses the same list. Change a term in one place and it changes everywhere.

It takes an hour or two to set up and it's the difference between metadata that works and metadata that slowly drifts.

## "But nobody will fill in the columns"

This is the objection I hear in every workshop, and it's fair. People won't tag every file by hand, and you shouldn't ask them to. Three things make metadata close to automatic:

- **Default values.** A library for approved policies can set Document Type to Policy for everything saved there. Nobody types anything.
- **Folder defaults.** You can set column defaults per folder, so a file dropped into a folder picks up its values automatically. People keep the drag-and-drop habit they like, and the metadata fills itself in.
- **Document sets and content types.** Group related documents so they share the same properties, set once for the whole set.

Set up this way, people save files the way they always have, and the documents come out described.

## So are folders bad?

No. A shallow folder structure is fine, and for some teams it's the right choice. The rule I use:

- **Two or three levels deep at most.** Past that, the path is doing a job metadata should do.
- **One type of content per library.** A library for contracts and another for policies beats one library for everything.
- **Folders for grouping, metadata for describing.** Use a folder to keep a project's files together. Use columns to say what each file is and whether it's current.

The aim is to stop using folders as the only source of meaning. Deleting them all was never the point.

## How to make the change without a big project

1. **Pick one library that matters.** Policies and procedures is the usual winner, because it's where wrong answers do the most damage.
2. **Add the four columns** using terms from the term store.
3. **Set defaults** on the library and its folders so existing habits keep working.
4. **Mark what's current.** Set Document Status to Approved on the live versions and Superseded on the rest.
5. **Create two views:** one showing only Approved documents, one grouped by Document Type.
6. **Test it.** Ask Copilot, or Microsoft Search, the questions your staff ask. Compare the answers with what you got before.

When one library works, the pattern is easy to repeat.

## The bigger picture

Metadata is one part of information architecture, alongside how your sites are organised and who can see what. If you want the security side, I've written about [finding and fixing oversharing](/blog/copilot-oversharing-sharepoint/), and the [10-point readiness checklist](/blog/sharepoint-copilot-readiness-checklist/) pulls it all together.

Copilot can only be as clear as the information you give it. Describe your documents well and it has something solid to work with. There is no AI without IA.
