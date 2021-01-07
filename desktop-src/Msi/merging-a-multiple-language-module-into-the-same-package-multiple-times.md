---
description: When a module supports multiple languages, you can merge it into the same Windows Installer database multiple times, but make sure that each merge uses a different language.
ms.assetid: 816b1f52-1ca2-4332-9a9b-462ea372c3bb
title: Merging a Multiple Language Module into the Same Package Multiple Times
ms.topic: article
ms.date: 05/31/2018
---

# Merging a Multiple Language Module into the Same Package Multiple Times

When a module supports multiple languages, you can merge it into the same Windows Installer database multiple times, but make sure that each merge uses a different language. Before each merge, request a different language from the module. The resulting .msi database then has a record in the [ModuleSignature Table](modulesignature-table.md) for each merge of the module. Components that are shared between languages exist only one time in the [Component Table](component-table.md), but are associated with each language in the [ModuleComponents Table](modulecomponents-table.md).

When merging multiple languages of a module into the same package, each merge must satisfy the same restrictions on code pages as single-language modules. The modules cannot contain strings in different code pages.

When merging a module multiple times into a single .msi file, you may need to modify the order of the files in the [File Table](file-table.md) to use the existing .cab from the module directly in your installation. The order of files in the File Table must match the order of files in the .cab. When merging a module multiple times into an installation database the sequence may be modified, because files shared between the languages may already exist in the module from a prior merge, and they have a different relative sequence number.

 

 



