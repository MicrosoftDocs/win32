---
description: The AdvtExecuteSequence table lists actions the installer calls when it executes the top-level ADVERTISE action. See Installation Procedure Tables Group, Using a Sequence Table, and the Sequence Table Detailed Example.
ms.assetid: 269bd28c-fa45-42b8-a610-1c4c5fcabc19
title: Importing the AdvtExecuteSequence
ms.topic: article
ms.date: 05/31/2018
---

# Importing the AdvtExecuteSequence

The [AdvtExecuteSequence table](advtexecutesequence-table.md) lists actions the installer calls when it executes the top-level [ADVERTISE action](advertise-action.md). See [Installation Procedure Tables Group](installation-procedure-tables-group.md), [Using a Sequence Table](using-a-sequence-table.md), and the [Sequence Table Detailed Example](sequence-table-detailed-example.md).

If in the section [Importing a Blank Database](importing-a-blank-database.md) you used uisample.msi from the Windows Installer SDK, the sequence tables in your copy of MNP2000.msi already contains the suggested action sequences described in [Using a Sequence table](using-a-sequence-table.md). No changes to these sequences should be necessary to author the Notepad sample installation package.

Use your database editor to open MNP2000.msi and enter the following data into the [AdvtExecuteSequence table](advtexecutesequence-table.md).

[AdvtExecuteSequence Table](advtexecutesequence-table.md)



| Action                | Condition | Sequence |
|-----------------------|-----------|----------|
| CostFinalize          |           | 1000     |
| CostInitialize        |           | 800      |
| CreateShortcuts       |           | 4500     |
| InstallFinalize       |           | 6600     |
| InstallInitialize     |           | 1500     |
| InstallValidate       |           | 1400     |
| PublishComponents     |           | 6200     |
| PublishFeatures       |           | 6300     |
| PublishProduct        |           | 6400     |
| RegisterClassInfo     |           | 4600     |
| RegisterExtensionInfo |           | 4700     |
| RegisterMIMEInfo      |           | 4900     |
| RegisterProgIdInfo    |           | 4800     |



 

The [AdvtUISequence table](advtuisequence-table.md) is not used by the installer. This table should not exist or be left empty in the installation database.

[Continue](adding-summary-information.md)

 

 



