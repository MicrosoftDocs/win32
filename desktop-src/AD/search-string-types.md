---
title: Initial, Medial, and Final Search Strings
description: There are three types of wildcard searches that are referenced throughout the documentation about construction search string queries. These wildcard searches are initial-, medial-, and final-search strings. This topics describes these searches.
ms.assetid: 23cc4771-2dd6-478c-9c7a-43052594cb71
ms.tgt_platform: multiple
ms.topic: article
ms.date: 05/31/2018
---

# Initial, Medial, and Final Search Strings

There are three types of wildcard searches that are referenced throughout the documentation about construction search string queries. These wildcard searches are: initial-, medial-, and final-search strings. This topics describes these searches.

## Initial Search Strings

Initial-search strings match a given set of characters at the beginning of a string, followed by a wildcard. For example, the initial-search string `Act*` would match "Active Directory".

## Medial-Search Strings

Medial-search strings match a given set of characters in the middle of a string, preceded by and/or followed by a wildcard. The medial-search strings `*Dir*`, `*ive*Dir*`, and `*ve*Dir*tor*` would all match "Active Directory".

## Final-search Strings

Final-search strings match a given set of characters at the end of a string, preceded by a wildcard. For example, the final-search string `*ory` would match "Active Directory".

 

 




