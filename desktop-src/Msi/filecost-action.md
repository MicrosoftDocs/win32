---
description: The FileCostaction initiates dynamic costingof standard installation actions.
ms.assetid: 1b3f2baf-6191-452e-955d-8ac903edc1b7
title: FileCost Action
ms.topic: article
ms.date: 05/31/2018
---

# FileCost Action

The FileCostaction initiates dynamic [*costing*](c-gly.md)of standard installation actions.

## ActionData Messages

There are no ActionData messages.

## Sequence Restrictions

Any standard or [custom actions](custom-actions.md) that affect costing should sequenced before the [CostInitialize](costinitialize-action.md) action. Call the FileCost action immediately following the CostInitialize action. Then call the [CostFinalize](costfinalize-action.md) action following the CostInitialize action to make all final cost calculations available to the installer through the [Component](component-table.md) table.

The [CostInitialize](costinitialize-action.md) action must be executed before the FileCost action. The installer then determines the disk-space cost of every file in the [File](file-table.md) table, on a per-component basis (See [Component Table](component-table.md)), taking both [*volume*](v-gly.md) clustering and the presence of existing files that may need to be overwritten into account. All actions that consume or release disk space are also considered. If an existing file is found, a file version check is performed to determine whether the new file actually needs to be installed or not. If the existing file is of an equal or greater version number, the existing file is not overwritten and no disk-space cost is incurred. In all cases, the installer uses the results of version number checking to set the installation state of each file.

The FileCost action initializes cost calculation with theinstaller. Actual dynamic [*costing*](c-gly.md) does not occur until the [CostFinalize](costfinalize-action.md) action is executed.

## Related topics

<dl> <dt>

[File Costing](file-costing.md)
</dt> </dl>

 

 



