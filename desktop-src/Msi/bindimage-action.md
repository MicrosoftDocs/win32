---
description: The BindImage action binds each executable or DLL that must be bound to the DLLs imported by it.
ms.assetid: bf90acc0-4e90-4180-9df7-268b63a66538
title: BindImage Action
ms.topic: article
ms.date: 05/31/2018
---

# BindImage Action

The BindImage action binds each executable or DLL that must be bound to the DLLs imported by it. The BindImage action acts on each file in the [BindImage](bindimage-table.md) table, but only those that are to be installed locally. The installer computes the virtual address of each function imported from all DLLs, then saves the computed virtual address in the importing image's [*import address table*](i-gly.md) (IAT).

The BindImage Action internally calls the **BindImageEx** Windows API.

## Sequence Restrictions

The BindImage action must come after the [InstallFiles](installfiles-action.md) action.

## ActionData Messages



| Field | Description of action data     |
|-------|--------------------------------|
| \[1\] | File identifier of executable. |



 

 

 



