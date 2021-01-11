---
description: Merge modules only operate with components and not with features. However, some tables in merge modules, such as the PublishComponent table, contain fields that refer to features.
ms.assetid: f2891457-efef-4319-bd09-5de7fcf32d21
title: Referencing Features in Merge Modules
ms.topic: article
ms.date: 05/31/2018
---

# Referencing Features in Merge Modules

Merge modules only operate with components and not with features. However, some tables in merge modules, such as the [PublishComponent table](publishcomponent-table.md), contain fields that refer to features.

A null GUID: {00000000-0000-0000-0000-000000000000} must be authored into any field of a merge module database that references a feature. When the merge module is merged into an installation package, the merge tool replaces the null GUID with the feature specified in the installation package, except for tables that require special handling, such as the [ModuleSignature table](modulesignature-table.md) and the ModuleSequence tables.

Note that if a null GUID is used as a primary key, it is not guaranteed that the value substituted by the merge tool is unique. Authors of merge modules are responsible for ensuring that no existing primary key in the user's interface is duplicated when the merge tool replaces null GUIDs with features.

 

 



