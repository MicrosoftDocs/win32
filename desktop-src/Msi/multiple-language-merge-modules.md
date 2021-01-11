---
description: Multiple language modules can deliver components with several different languages as a single compound file.
ms.assetid: 'b3a0b635-49c7-4f95-b31f-6c8688466dd2'
title: Multiple Language Merge Modules
ms.topic: article
ms.date: 05/31/2018
---

# Multiple Language Merge Modules

Multiple language modules can deliver components with several different languages as a single compound file. The design and functionality of multiple language merge modules is similar to single language modules. A multiple language merge module has more than one language listed in the [**Template Summary**](template-summary.md) Property. The database of a multiple language merge module contains all the setup information for multiple languages. The MergeModule.CABinet cabinet inside a multiple language merge module contains all the files for all the supported languages.

When applying a multiple language .msm file to an .msi file, you must indicate the final language of the installation package after the merge. In the case of a single language merge module, the merge module's [File table](file-table.md) lists every file present in the MergeModule.CABinet cabinet. In the case of a multiple language merge module, MergeModule.CABinet contains all the files for every language supported by the module, but only the subset of files for the final language goes into the module's File table. The merge tool must ensure that the module provides the subset of information and files required for the requested final language.

Every merge module has a default language specified in the Language column of the [ModuleSignature table](modulesignature-table.md). The default language of a merge module is also shown as the first, or only, language in the [**Template Summary**](template-summary.md) Property. Depending on the requested final language and the module's default language, the merge tool may apply language transforms to a multiple language merge module so that it can be opened in the requested language, or an approximation of the requested language. The language transforms are embedded inside the merge module. Merge tools must apply language transforms in adherence to the following general rules:

-   If the default and final languages are the same, the module can be merged without using language transforms.
-   If the default language is 0 (a language neutral module), the module can be merged without using language transforms.
-   If the final language is not the default language, the merge tool must apply one of the language transforms embedded in the module to change the module to the final language, or to an approximation of the final language.

For example, no language transforms are required if the final language is 1033 (US English) and the default language of the module is 1033 (US English), 0 (language neutral), or 9 (generic English).

Language transforms are required if the final language is 1033 (US English) and the default language is 1031 (German). In this case, the merge tool may first search the multiple language module for an embedded language transform to 1033 (US English). If that fails it may then search for a transform to a language with a matching primary LANGID, even if the secondary LANGID does not match. For example, if the tool cannot find a transform to 1033 (US English), it searches for a transform to 9 (Generic English). If this fails the merge tool searches for a transform to 0 (language neutral). If all these searches for a suitable transform fail, the module fails to open.

For more information, see [Authoring Multiple Language Merge Modules](authoring-multiple-language-merge-modules.md).

 

 



