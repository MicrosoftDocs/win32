---
description: Merge modules are essentially simplified .msi files, which is the file name extension for a Windows Installer installation package. A standard merge module has an .msm file name extension.
ms.assetid: 580fe58a-4636-4f9a-a68d-4fd0e281e949
title: About Merge Modules
ms.topic: article
ms.date: 05/31/2018
---

# About Merge Modules

Merge modules are essentially simplified .msi files, which is the file name extension for a Windows Installer installation package. A standard merge module has an .msm file name extension.

A merge module cannot be installed alone because its lacks some vital database tables that are present in an installation database. Merge modules also contain additional tables that are unique to themselves. To install the information delivered by a merge module with an application, the module must first be merged into the application's .msi file.

A merge module consists of the following parts:

-   A [Merge Module Database](merge-module-database.md) containing the installation properties and setup logic being delivered by the merge module.
-   A [Merge Module Summary Information Stream Reference](merge-module-summary-information-stream-reference.md) describing the module.
-   A [MergeModule.CABinet](mergemodule-cabinet.md) cabinet file stored as a stream inside the merge module. This cabinet contains all the files required by the components delivered by the merge module.

[Multiple language merge modules](multiple-language-merge-modules.md) can deliver components to an installation package in multiple languages. In a multiple language merge module the database contains the installation properties and logic for more than one language and the MergeModule.CABinet cabinet includes all the files necessary to install components with all the languages supported by the module.

 

 



