---
description: The UnregisterTypeLibraries action unregisters type libraries from the system. This action is applied to each file listed in the TypeLib table that is triggered to be uninstalled.
ms.assetid: fea5bdc1-ac27-4d02-bcea-5c97366dd394
title: UnregisterTypeLibraries Action
ms.topic: article
ms.date: 05/31/2018
---

# UnregisterTypeLibraries Action

The UnregisterTypeLibraries action unregisters type libraries from the system. This action is applied to each file listed in the [TypeLib](typelib-table.md) table that is triggered to be uninstalled.

## Sequence Restrictions

The UnregisterTypeLibraries action must come before the [RemoveFiles](removefiles-action.md) action.

## ActionData Messages



| Field | Description of action data                        |
|-------|---------------------------------------------------|
| \[1\] | [GUID](guid.md) of an unregistered type library. |



 

 

 



