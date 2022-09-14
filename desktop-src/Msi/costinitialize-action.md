---
description: The CostInitialize action initiates the installation costing process.
ms.assetid: be9a8382-c892-44ae-8b59-c665b5cca2d2
title: CostInitialize Action
ms.topic: article
ms.date: 05/31/2018
---

# CostInitialize Action

The CostInitialize action initiates the installation [*costing*](c-gly.md) process.

## Sequence Restrictions

Any standard or [custom](custom-actions.md) actions that affect costing should be sequenced before the CostInitialize action. Call the [FileCost](filecost-action.md) action immediately following the CostInitialize action. Then call the [CostFinalize](costfinalize-action.md) action following the CostInitialize action action to make all final cost calculations available to the installer through the [Component](component-table.md) table.

## ActionData Messages

There are no ActionData messages.

## Remarks

The CostInitialize action loads the Component table and [Feature](feature-table.md) table into memory.

For more information on the [*costing*](c-gly.md) process in the installer, see [File Costing](file-costing.md).

## Related topics

<dl> <dt>

[File Costing](file-costing.md)
</dt> </dl>

 

 



