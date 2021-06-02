---
description: The AdminUISequence table lists actions that the installer calls when it executes the top-level ADMIN action and the internal user interface level is set to full UI or reduced UI.
ms.assetid: f23bd5c2-1d7f-485f-a22b-99436dfab6bf
title: Importing the AdminUISequence
ms.topic: article
ms.date: 05/31/2018
---

# Importing the AdminUISequence

The [AdminUISequence table](adminuisequence-table.md) lists actions that the installer calls when it executes the top-level [ADMIN action](admin-action.md) and the internal user interface level is set to full UI or reduced UI. The installer skips the actions in this table if the user interface level is set to basic UI or no UI. See [User Interface](user-interface.md) and [User Interface Levels](user-interface-levels.md). See [Installation Procedure Tables Group](installation-procedure-tables-group.md), [Using a Sequence Table](using-a-sequence-table.md), and the [Sequence Table Detailed Example](sequence-table-detailed-example.md).

If in the section [Importing a Blank Database](importing-a-blank-database.md) you used uisample.msi from the Windows Installer SDK, the sequence tables in your copy of MNP2000.msi already contains the suggested action sequences described in [Using a Sequence Table](using-a-sequence-table.md). No changes to these sequences should be necessary to install the Notepad sample.

Use your database editor to open MNP2000.msi and enter the following data into the AdminExecuteSequence table.

[AdminUISequence Table](adminuisequence-table.md)



| Action          | Condition | Sequence |
|-----------------|-----------|----------|
| AdminWelcomeDlg |           | 1230     |
| CostFinalize    |           | 1000     |
| CostInitialize  |           | 800      |
| ExecuteAction   |           | 1300     |
| ExitDlg         |           | -1       |
| FatalErrorDlg   |           | -3       |
| FileCost        |           | 900      |
| PrepareDlg      |           | 140      |
| ProgressDlg     |           | 1280     |
| UserExitDlg     |           | -2       |



 

[Continue](importing-the-advtexecutesequence.md)

 

 



