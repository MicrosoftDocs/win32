---
description: Multiple-language merge modules, language transforms, and cabinet files must be authored such that the order of the files matches the order specified in the File table.
ms.assetid: c6ddf5fc-a7c5-49c1-899b-ff9fdff9c028
title: Ordering the File Sequence in the CAB of a Multiple Language Merge Module
ms.topic: article
ms.date: 05/31/2018
---

# Ordering the File Sequence in the CAB of a Multiple Language Merge Module

Multiple-language merge modules, language transforms, and cabinet files must be authored such that the order of the files in the .cab matches the installation order of files specified in the [File Table](file-table.md), even after the application of the language transform. If the order in the module and in the .cab do not match, the merge module cannot be used.

Assign to each file in the module, a unique sequence number that is independent of its language, and then always use that sequence number for the file. Use the same sequence when building the cabinet file and authoring a language transform.

Because the Installer only installs the files listed in the [File Table](file-table.md), the use of a global file sequence in the cabinet, [File Table](file-table.md), and language transform enables the merge tool to skip any extra files stored in the cabinet that are not listed in the [File Table](file-table.md). Other files may exist in the cabinet, but they must not be listed in the [File Table](file-table.md). For example, a module installing Code.dll, English.dat, German.dat, and French.dat can use the following global file sequence order.



| File        | Sequence |
|-------------|----------|
| Code.Dll    | 1        |
| English.Dat | 2        |
| German.Dat  | 3        |
| French.Dat  | 4        |



 

Language transforms can then be authored to modify the [File Table](file-table.md) of the module for English, German, or French.

[File Table](file-table.md) (partial for English)



| File        | Sequence |
|-------------|----------|
| Code.Dll    | 1        |
| English.Dat | 2        |



 

[File Table](file-table.md) (partial for German)



| File       | Sequence |
|------------|----------|
| Code.Dll   | 1        |
| German.Dat | 3        |



 

[File Table](file-table.md) (partial for French)



| File       | Sequence |
|------------|----------|
| Code.Dll   | 1        |
| French.Dat | 4        |



 

For more information, see [Authoring a Language Transform for a Multiple Language Merge Module](authoring-a-language-transform-for-a-multiple-language-merge-module.md) and [Authoring Merge Module File Tables](authoring-merge-module-file-tables.md).

 

 



