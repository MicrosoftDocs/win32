---
description: The AllocateRegistrySpace action ensures that the amount of free registry space specified by the AVAILABLEFREEREG property exists in the registry.
ms.assetid: bb6ac685-5ad8-48e6-9c03-9ca42268d727
title: AllocateRegistrySpace Action
ms.topic: article
ms.date: 05/31/2018
---

# AllocateRegistrySpace Action

The AllocateRegistrySpace action ensures that the amount of free registry space specified by the [**AVAILABLEFREEREG**](availablefreereg.md) property exists in the registry.

## Sequence Restrictions

The AllocateRegistrySpace action must be called after [InstallInitialize](installinitialize-action.md). It is advisable to schedule the AllocateRegistrySpace before all other actions to ensure there is enough registry space available to continue.

## ActionData Messages



| Field | Description of action data     |
|-------|--------------------------------|
| \[1\] | Registry space required in KB. |



 

 

 



