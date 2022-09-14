---
description: The user interface sequence is imported into the sample database.
ms.assetid: 750e4dc6-91ff-4d9a-a968-abc2515e3b7c
title: Importing the InstallUISequence
ms.topic: article
ms.date: 05/31/2018
---

# Importing the InstallUISequence

The [InstallUISequence table](installuisequence-table.md) lists actions that are executed when the top-level [INSTALL action](install-action.md) is executed and the internal user interface level is set to full UI or reduced UI. The installer skips the actions in this table if the user interface level is set to basic UI or to no UI. See [User Interface](user-interface.md) and [User Interface Levels](user-interface-levels.md). See [Installation Procedure Tables Group](installation-procedure-tables-group.md), [Using a Sequence Table](using-a-sequence-table.md), and the [Sequence Table Detailed Example](sequence-table-detailed-example.md).

If in the section [Importing a Blank Database](importing-a-blank-database.md) you used uisample.msi from the Windows Installer SDK, the sequence tables in your copy of MNP2000.msi already contains the suggested action sequences described in [Using a Sequence Table](using-a-sequence-table.md). No changes to these sequences should be necessary to author the Notepad installation package.

Use your database editor to open MNP2000.msi and enter the following data into the InstallUISequence table.

[InstallUISequence Table](installuisequence-table.md)



| Action                | Condition                                    | Sequence |
|-----------------------|----------------------------------------------|----------|
| AppSearch             |                                              | 400      |
| CCPSearch             | NOT Installed                                | 500      |
| CostFinalize          |                                              | 1000     |
| CostInitialize        |                                              | 800      |
| ExecuteAction         |                                              | 1300     |
| ExitDlg               |                                              | -1       |
| FatalErrorDlg         |                                              | -3       |
| FileCost              |                                              | 900      |
| LaunchConditions      |                                              | 100      |
| MaintenanceWelcomeDlg | Installed AND NOT RESUME AND NOT Preselected | 1250     |
| PrepareDlg            |                                              | 140      |
| ProgressDlg           |                                              | 1280     |
| ResumeDlg             | Installed AND (RESUME OR Preselected)        | 1240     |
| RMCCPSearch           | NOT Installed                                | 600      |
| UserExitDlg           |                                              | -2       |
| WelcomeDlg            | NOT Installed                                | 1230     |
| MigrateFeatureStates  |                                              | 1200     |
| FindRelatedProducts   |                                              | 200      |



 

[Continue](importing-the-adminexecutesequence.md)

 

 



