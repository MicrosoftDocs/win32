---
description: When a module is merged into an database that has a different default language, the merge tool may need to apply a language transform to the module to provide the final language. For more information, see Multiple Language Merge Modules.
ms.assetid: 51e8774e-f358-423f-a283-ad7beeabbbdb
title: Authoring a Language Transform for a Multiple Language Merge Module
ms.topic: article
ms.date: 05/31/2018
---

# Authoring a Language Transform for a Multiple Language Merge Module

When a module is merged into an database that has a different default language, the merge tool may need to apply a language transform to the module to provide the final language. For more information, see [Multiple Language Merge Modules](multiple-language-merge-modules.md).

The language transforms are stored in the module's .msm file and must have the name and format: MergeModule.Lang\#\#\#\#. The \#\#\#\# represents the up-to four digit [LANGID](localizing-the-error-and-actiontext-tables.md) of the final language. For example, MergeModule.Lang1033, MergeModule.Lang9, and MergeModule.Lang0 for transforms to US English, world English, and language neutral. These are the same as [Embedded Transforms](embedded-transforms.md) and you can add them to substorages in the .msm file.

The language transform should do the following:

-   Change the default language in the Language column of the [ModuleSignature table](modulesignature-table.md) to the new language of the module.
-   Change the default language in the Language column of the [ModuleComponents table](modulecomponents-table.md) to the new language of the module. The transform may add or remove rows from this table.
-   If necessary, change the language in the RequiredLanguage column, or add or delete rows, to the [ModuleDependency table](moduledependency-table.md).
-   If necessary, change the language in the ExcludedLanguage column, or add or delete rows, to the [ModuleExclusion table](moduleexclusion-table.md).
-   The transform may perform any valid transform operations on the module, including adding or removing components, files, registry entries, or actions.

Note that applying a language transform when opening the module does not change the default language or the languages supported by the module, it just changes the language that is being requested. Therefore the [**Template Summary**](template-summary.md) property does not change, it should already list all of the languages supported by the module with the default language listed first.

All files needed by all possible language transforms are commonly stored in a single cabinet file included with the module. Because it is not practical to have the language transform modify this cabinet file, it is best to use a global file sequence in the cabinet file, [File table](file-table.md), and language transform. For details, see [Ordering the File Sequence in the CAB of a Multiple Language Merge Module](ordering-the-file-sequence-in-the-cab-of-a-multiple-language-merge-module.md)

 

 



