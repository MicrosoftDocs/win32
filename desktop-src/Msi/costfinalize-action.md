---
description: The CostFinalize action ends the internal installation costing process begun by the CostInitialize action.
ms.assetid: ae69ad03-5acc-4a62-ba71-3a4e477d34ab
title: CostFinalize Action
ms.topic: article
ms.date: 05/31/2018
---

# CostFinalize Action

The CostFinalize action ends the internal installation [*costing*](c-gly.md) process begun by the [CostInitialize](costinitialize-action.md) action.

## Sequence Restrictions

Any standard or [custom actions](custom-actions.md) that affect costing should be sequenced before the [CostInitialize](costinitialize-action.md) action. Call the [FileCost](filecost-action.md) action immediately following the CostInitialize action and then call the CostFinalize action to make all final cost calculations available to the installer through the [Component](component-table.md) table.

The CostFinalize action must be executed before starting any user interface sequence which allows the user to view or modify [Feature](feature-table.md) table selections or directories.

## ActionData Messages

There are no ActionData messages.

## Remarks

The CostFinalize action queries the [Condition](condition-table.md) table to determine which features are scheduled to be installed. Costing is done for each component in the [Component](component-table.md) table.

The CostFinalize action also verifies that all the target directories are writable before allowing the installation to continue.

> [!Note]  
> During an [administrative installation](administrative-installation.md), CostFinalize sets all features for installation except features having 0 authored in the Level column of the [Feature table](feature-table.md).

 

## Related topics

<dl> <dt>

[File Costing](file-costing.md)
</dt> </dl>

 

 



