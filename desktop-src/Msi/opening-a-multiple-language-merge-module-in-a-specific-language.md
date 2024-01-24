---
description: When merging a module into an installation database, there are two important languages.
ms.assetid: e815854f-a379-497a-ae37-b13de39dd516
title: Opening a Multiple-Language Merge Module in a Specific Language
ms.topic: article
ms.date: 05/31/2018
---

# Opening a Multiple-Language Merge Module in a Specific Language

When merging a module into an installation database, there are two important languages. The first is the language of the target installation package specified by [**ProductLanguage**](productlanguage.md) in the [Property Table](property-table.md). The second is the language of the merge module that appears in the Language column of the [ModuleSignature Table](modulesignature-table.md).

The language of the installation package can be passed to the module by the merge tool when the package is opened for a merge. However, sometimes it may be necessary to disregard the language of the target, and request that the module be opened in another language, for example, an English package installing both the English and German resources from the module.

When opening a module with a language request, the merge tool checks the requested language against the languages that are specified in the Language column of the [ModuleSignature Table](modulesignature-table.md).

The following process is used to determine which language to use.

**To determine which language to use**

1.  If the language in the [ModuleSignature Table](modulesignature-table.md) is equal or more general than the requested language, the module opens.
2.  If the module supports the exact language requested, that language is used.
3.  If the module supports the language group of the language requested that language group is used, for example, check 9 if 1033 was requested but not found in step 2.
4.  Check if there is a language transform that changes the module to neutral.
5.  If none of the previous steps succeed, the module does not support the requested language and the merge fails.

 

 



