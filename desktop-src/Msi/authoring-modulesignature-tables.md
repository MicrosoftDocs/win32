---
description: The ModuleSignature table contains all the information needed to identify the merge module.
ms.assetid: 5f0b4590-dac3-4528-b714-ff760ae8d123
title: Authoring ModuleSignature Tables
ms.topic: article
ms.date: 05/31/2018
---

# Authoring ModuleSignature Tables

The [ModuleSignature table](modulesignature-table.md) contains all the information needed to identify the merge module.

The ModuleID field is the primary key for this table and must follow the convention described in [Naming Primary Keys in Merge Module Databases](naming-primary-keys-in-merge-module-databases.md). For example, if the readable name of the merge module is MyLibrary and the GUID for the merge module is {880DE2F0-CDD8-11D1-A849-006097ABDE17}, the entry in the ModuleID column of the ModuleSignature table becomes MyLibrary.880DE2F0\_CDD8\_11D1\_A849\_006097ABDE17.

Enter the decimal identifier for the default language of the merge module into the Language field of the ModuleSignature table.

Enter the version of the merge module into the Version field.

 

 



