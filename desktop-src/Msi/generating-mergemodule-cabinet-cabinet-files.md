---
description: Every file that is delivered to the target installation package by the merge module must be stored inside of a cabinet file embedded as a stream inside the .msm file. The name of this cabinet is always MergeModule.CABinet.
ms.assetid: 884df249-977e-4e8e-8978-15331a7c1d8a
title: Generating MergeModule.CABinet Cabinet Files
ms.topic: article
ms.date: 05/31/2018
---

# Generating MergeModule.CABinet Cabinet Files

Every file that is delivered to the target installation package by the merge module must be stored inside of a cabinet file embedded as a stream inside the .msm file. The name of this cabinet is always MergeModule.CABinet.

The names of files in MergeModule.CABinet must match the primary keys used in the merge module's [File table](file-table.md) and must adhere to the convention described in [Naming Primary Keys in Merge Module Databases](naming-primary-keys-in-merge-module-databases.md).

The installer skips extra files included in MergeModule.CABinet that are not listed in the merge module's [File table](file-table.md). The sequence numbers of files specified in the File table do not need to be consecutive, but they must follow the same sequence as the files stored inside MergeModule.CABinet. For more information, see [Authoring Merge Module File Tables](authoring-merge-module-file-tables.md).

This means that a single cabinet file can contain all the files needed for a merge module to support multiple languages. All the language files can be given unique sequence numbers in the cabinet and then a language transform can be used to add or remove files from the File table to obtain a merge module for a particular language. For details, see [Authoring Multiple Language Merge Modules](authoring-multiple-language-merge-modules.md).

MergeModule.CABinet can be added to the merge module by opening a temporary [\_Streams Table](-streams-table.md). For example, the tool Msidb.exe provided with the Windows Installer SDK can be used to add the MergeModule.CABinet to the merge module. For more information, see [Including a Cabinet File in an Installation](including-a-cabinet-file-in-an-installation.md).

 

 



