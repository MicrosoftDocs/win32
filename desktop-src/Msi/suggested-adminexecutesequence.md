---
description: The suggested action sequences for a basic AdminExecuteSequence table in a Windows Installer database.
ms.assetid: c54181d3-a16a-4007-a9ac-03ace98b637e
title: Suggested AdminExecuteSequence
ms.topic: article
ms.date: 05/31/2018
---

# Suggested AdminExecuteSequence



| Action                                                | Condition | Sequence |
|-------------------------------------------------------|-----------|----------|
| [CostInitialize](costinitialize-action.md)           |           | 800      |
| [FileCost](filecost-action.md)                       |           | 900      |
| [CostFinalize](costfinalize-action.md)               |           | 1000     |
| [InstallValidate](installvalidate-action.md)         |           | 1400     |
| [InstallInitialize](installinitialize-action.md)     |           | 1500     |
| [InstallAdminPackage](installadminpackage-action.md) |           | 3900     |
| [InstallFiles](installfiles-action.md)               |           | 4000     |
| [InstallFinalize](installfinalize-action.md)         |           | 6600     |



 

 

 



