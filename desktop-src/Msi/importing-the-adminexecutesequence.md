---
description: The AdminExecuteSequence table lists actions that the installer executes when it calls the top-level ADMIN action. See Installation Procedure Tables Group, Using a Sequence Table, and the Sequence Table Detailed Example.
ms.assetid: 8b1da4a3-0b82-4b71-8a32-59e90025cbfa
title: Importing the AdminExecuteSequence
ms.topic: article
ms.date: 05/31/2018
---

# Importing the AdminExecuteSequence

The [AdminExecuteSequence table](adminexecutesequence-table.md) lists actions that the installer executes when it calls the top-level [ADMIN action](admin-action.md). See [Installation Procedure Tables Group](installation-procedure-tables-group.md), [Using a Sequence Table](using-a-sequence-table.md), and the [Sequence Table Detailed Example](sequence-table-detailed-example.md).

If in the section [Importing a Blank Database](importing-a-blank-database.md) you used uisample.msi from the Windows Installer SDK, the sequence tables in your copy of MNP2000.msi already contains the suggested action sequences described in [Using a Sequence Table](using-a-sequence-table.md). No changes to these sequences should be necessary to author the Notepad sample installation package.

Use your database editor to open MNP2000.msi and enter the following data into the AdminExecuteSequence table.

[AdminExecuteSequence Table](adminexecutesequence-table.md)



| Action              | Condition | Sequence |
|---------------------|-----------|----------|
| CostFinalize        |           | 1000     |
| CostInitialize      |           | 800      |
| FileCost            |           | 900      |
| InstallAdminPackage |           | 3900     |
| InstallFiles        |           | 4000     |
| InstallFinalize     |           | 6600     |
| InstallInitialize   |           | 1500     |
| InstallValidate     |           | 1400     |



 

[Continue](importing-the-adminuisequence.md)

 

 



