---
description: The suggested action sequences for a basic AdminUISequence table in a Windows Installer database.
ms.assetid: a5371133-7d55-4041-8e1f-ecc8245c8d3a
title: Suggested AdminUISequence
ms.topic: article
ms.date: 05/31/2018
---

# Suggested AdminUISequence



| Action                                      | Condition | Sequence |
|---------------------------------------------|-----------|----------|
| FatalErrorDlg                               |           | -3       |
| UserExitDlg                                 |           | -2       |
| ExitDlg                                     |           | -1       |
| PrepareDlg                                  |           | 140      |
| [CostInitialize](costinitialize-action.md) |           | 800      |
| [FileCost](filecost-action.md)             |           | 900      |
| [CostFinalize](costfinalize-action.md)     |           | 1000     |
| AdminWelcomeDlg                             |           | 1230     |
| ProgressDlg                                 |           | 1280     |
| [ExecuteAction](executeaction-action.md)   |           | 1300     |



 

 

 



