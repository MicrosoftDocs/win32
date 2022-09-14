---
description: The RegisterTypeLibraries action registers type libraries with the system. This action is applied to each file referred to in the TypeLib table that is scheduled for install.
ms.assetid: 374450bb-316c-4fe6-abb1-cd8a8a31f284
title: RegisterTypeLibraries Action
ms.topic: article
ms.date: 05/31/2018
---

# RegisterTypeLibraries Action

The RegisterTypeLibraries action registers type libraries with the system. This action is applied to each file referred to in the [TypeLib table](typelib-table.md) that is scheduled for install.

## Sequence Restrictions

The RegisterTypeLibraries action must come after the [InstallFiles](installfiles-action.md) action.

## ActionData Messages



| Field | Description of action data                   |
|-------|----------------------------------------------|
| \[1\] | [GUID](guid.md) of registered type library. |



 

## Remarks

The RegisterTypeLibraries action requires that the type library language be correctly authored in the Language field of the TypeLib table. Incorrect authoring of the Language field can cause the installer to fail to register an otherwise valid type library.

 

 



