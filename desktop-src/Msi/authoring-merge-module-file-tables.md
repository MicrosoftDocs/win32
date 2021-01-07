---
description: A File Table is required in every merge module, and should have a record for each file that is being delivered to the target installation package by the merge module.
ms.assetid: 436933c7-6e5d-4b4e-9147-c60a26871dbe
title: Authoring Merge Module File Tables
ms.topic: article
ms.date: 05/31/2018
---

# Authoring Merge Module File Tables

A [File Table](file-table.md) is required in every merge module, and should have a record for each file that is being delivered to the target installation package by the merge module. When the merge module is merged into a .msi file, every file in the merge module File Table is stored inside a [*cabinet file*](c-gly.md) in the .msm file. The name of the cabinet in a merge module is always the following: MergeModule.CABinet.

For more information, see [Generating MergeModule.CABinet Cabinet Files](generating-mergemodule-cabinet-cabinet-files.md).

-   Because the files of a merge module are always stored inside a cabinet file, it is not necessary to set the **msidbFileAttributesNoncompressed** or **msidbFileAttributesCompressed** bit flags in the Attributes column of the [File Table](file-table.md).
-   The names of files in MergeModule.CABinet must match the primary key in the merge module's [File Table](file-table.md).

    The File column is the primary key of the [File Table](file-table.md) and the entries in this field must follow the convention that is described in [Naming Primary Keys in Merge Module Databases](naming-primary-keys-in-merge-module-databases.md).

-   File sequence numbers are specified in the Sequence column of the [File Table](file-table.md).

    Files must be listed in the merge module's [File Table](file-table.md) in the same sequence that they are stored in MergeModule.CABinet. The sequence numbers of files do not need to be consecutive, but they must follow the same sequence as the files that are stored inside the cabinet. For example, the first, second, and third files stored in the cabinet can have the sequence numbers 100, 200, and 300.

-   The Installer skips extra files included in MergeModule.CABinet that are not listed in the [File Table](file-table.md).

    One cabinet file can contain all the files necessary for a merge module that supports multiple languages using transforms. All the language files can be given a unique sequence number in the cabinet, and then a transform can add or remove files from the [File Table](file-table.md) when needed for a specific language. For more information, see [Authoring Multiple Language Merge Modules](authoring-multiple-language-merge-modules.md).

For more information, see [File Table](file-table.md).

 

 



