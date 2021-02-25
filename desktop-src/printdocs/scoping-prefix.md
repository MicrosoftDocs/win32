---
description: This topic is not current. For the most current information, see the Print Schema Specification.
ms.assetid: 4bad85d7-a933-43fe-9d79-4835d92c82d6
title: Scoping Prefix
ms.topic: article
ms.date: 05/31/2018
---

# Scoping Prefix

This topic is not current. For the most current information, see the [Print Schema Specification](https://download.microsoft.com/download/D/E/C/DECA6E6B-3E81-48E7-B7EF-6D92A547D03C/print-schema-spec-2-0.zip).

A scope prefix is a textual label pre-appended to a schema keyword to provide a contextual scope. This allows ascribing a specific and well-understood context to keywords in a predefined manner. Print Schema Feature, ParameterDef, ParameterInit, and ParameterRef and root-level Property keyword Elements MUST have one of the following scope prefixes: "Job", "Document", or "Page".

## Interpretation of the Scoping Prefix with PrintTicket Content

The PrintTicket can be broken down into three content levels representing the high level job, the documents in the job, and the pages in each document. These levels are ranked according to specificity; the Job Level is most general, then the Document Level and then the Page Level is most specific. A job consists of one or more documents and a document consists of one or more pages.

## Job level Prefix

A Job Level ticket contains all job formatting settings intended to apply to an entire job. Any Elements with scope prefixes of "Job", "Document" or "Page" are permitted in a Job Level ticket.

The "Document" and "Page" prefixed settings specified in a Job Level ticket will be automatically applied to the Document and Page Level tickets.

## Document level Prefix

The Document Level ticket incorporates any job formatting settings intended to apply to one or more documents in a job. These may include settings previously specified in the Job Level ticket. Only Elements with scope prefixes of "Document" or "Page" are allowed in a Document Level ticket.

A Document Level Ticket may contain Document-prefixed settings previously specified by the Job level Ticket.

## Page level Prefix

The Page Level ticket incorporates any job formatting settings intended to apply to one or more pages a job (not limited to a single document). These may include settings previously specified in the Job or Document Level ticket. Only Elements with scope prefixes of "Page" are allowed in a Page Level ticket.

A Page Level Ticket may contain "Page" prefixed settings previously specified by the Job Level Ticket and/or the Document level ticket.

## Prefix Usage within a PrintTicket or Print Capabilities Document

PrintTicket and PrintCapabilities documents MUST NOT contain multiple keywords that differ only in the scoping prefix.? For example, a PrintCapabilities document MUST NOT have both JobInputBin and PageInputBin specified.? However, a Print Capabilities document MAY have both JobDuplexAllDocumentsContiguously and DocumentDuplex specified because these are considered different features, as they exhibit differing behavior.? This example is also true for a single PrintTicket.

## Prefix Conflict Management

A keyword conflict between settings is defined as, the same root level Print Schema Element denoted by the XML Attribute "name", appearing in multiple Level tickets. If there is no conflict, a prefix scoped Element may be pushed down, or inherited, from a more general ticket to a more specific ticket. If there is a conflict, then the setting from the most specific ticket takes precedence. That is, per page settings in a Page Level ticket override the identical per page settings in a Document or Job Level ticket. Similarly, document settings in the Document Level ticket take precedence over document settings in the Job Level ticket.

## Related topics

<dl> <dt>

[Print Schema Specification](https://download.microsoft.com/download/D/E/C/DECA6E6B-3E81-48E7-B7EF-6D92A547D03C/print-schema-spec-2-0.zip)
</dt> </dl>

 

 



