---
description: The suggested action sequences for a basic InstalUISequence table in a Windows Installer database.
ms.assetid: f1ddad1e-c075-4054-aa24-f1acdc72da96
title: Suggested InstallUISequence
ms.topic: article
ms.date: 05/31/2018
---

# Suggested InstallUISequence



| Action                                          | Condition                                                                                                  | Sequence |
|-------------------------------------------------|------------------------------------------------------------------------------------------------------------|----------|
| FatalErrorDlg                                   |                                                                                                            | -3       |
| UserExitDlg                                     |                                                                                                            | -2       |
| ExitDlg                                         |                                                                                                            | -1       |
| [LaunchConditions](launchconditions-action.md) |                                                                                                            | 100      |
| PrepareDlg                                      |                                                                                                            | 140      |
| [AppSearch](appsearch-action.md)               |                                                                                                            | 400      |
| [CCPSearch](ccpsearch-action.md)               | NOT [**Installed**](installed.md)                                                                         | 500      |
| [RMCCPSearch](rmccpsearch-action.md)           | NOT [**Installed**](installed.md)                                                                         | 600      |
| [CostInitialize](costinitialize-action.md)     |                                                                                                            | 800      |
| [FileCost](filecost-action.md)                 |                                                                                                            | 900      |
| [CostFinalize](costfinalize-action.md)         |                                                                                                            | 1000     |
| WelcomeDlg                                      | NOT [**Installed**](installed.md)                                                                         | 1230     |
| ResumeDlg                                       | [**Installed**](installed.md) AND ( [**RESUME**](resume.md) OR [**Preselected**](preselected.md))       | 1240     |
| MaintenanceWelcomeDlg                           | [**Installed**](installed.md) AND NOT [**RESUME**](resume.md) AND NOT [**Preselected**](preselected.md) | 1250     |
| ProgressDlg                                     |                                                                                                            | 1280     |
| [ExecuteAction](executeaction-action.md)       |                                                                                                            | 1300     |



 

 

 



