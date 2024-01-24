---
description: The authoring of the sequence tables is an essential part of developing an installer package because these tables specify the order of execution for the standard actions that control the installation process and display the user interface dialog boxes.
ms.assetid: db9a9cae-2a66-4e0d-a981-8de66d7c2a13
title: Using a Sequence Table
ms.topic: article
ms.date: 05/31/2018
---

# Using a Sequence Table

The authoring of the sequence tables is an essential part of developing an installer package because these tables specify the order of execution for the [standard actions](standard-actions.md) that control the installation process and display the user interface dialog boxes.

There are three modes of installation and two types of sequence tables for each mode.

The three separate installation modes currently supported by the installer are:

-   Simple Installation
-   Administrative Installation
-   Advertisement Installation

The sequence tables each have three fields: Action, Condition, and Sequence. The Action field names either a standard or custom action or a user defined dialog box or sequence the installer executes. The Condition field allows the author to specify a logical expression that controls whether an action or user-defined dialog is executed or displayed. If the Condition field is blank or contains an expression that evaluates to True, the action or dialog is executed or displayed. The action or dialog is skipped if the expression evaluates to False. The Sequence field specifies the order of execution of each action or user-defined dialog in the table.

Each of these installation modes processes the user interface sequence tables and the execute sequence tables. The user interface sequence tables are only processed if the installer was initialized with the user interface display level set to Reduced or Full. See the [**MsiSetInternalUI**](/windows/desktop/api/Msi/nf-msi-msisetinternalui) reference for more information about user interface display levels.

The user interface sequence tables typically contains standard actions related to collecting system information that are displayed to the user through the user interface. The user interface is displayed by recording the foreign keys to the names of dialog boxes in the [dialog table](dialog-table.md) in the Action field of the user interface sequence table. The user then has the opportunity to modify or accept the system information and begin the installation, which occurs when the execute sequence table is processed.

During a simple installation, the [INSTALL](install-action.md) top-level action is executed which in turn processes the [InstallUISequence table](installuisequence-table.md) and the [InstallExecuteSequence table](installexecutesequence-table.md).

An Administrative Installation is typically initiated by a network administrator to assign and install applications for individual users and groups of users. During this type of installation, the [ADMIN](admin-action.md) top-level action is executed which processes the [AdminUISequence table](adminuisequence-table.md) and the [AdminExecuteSequence table](adminexecutesequence-table.md).

To [advertise](advertisement.md) an application or feature, the installer must be initiated with the [ADVERTISE](advertise-action.md) action. During this type of installation the [AdvtExecuteSequence table](advtexecutesequence-table.md) is processed.

When authoring any sequence table, it is good practice to use the sequence number for standard actions from the suggested sequences in the topics below. For standard actions which have no standard position in the sequence table such as [ForceReboot](forcereboot-action.md), [ValidateProductID](validateproductid-action.md), and [InstallExecute](installexecute-action.md), use a sequence number that is a multiple of ten to identify the action as a standard action. For custom actions, use a sequence number that is not a multiple of ten to differentiate it from standard actions in the sequence table.

For suggested action sequences for each sequence table, see the following topics:

-   [Suggested InstallUISequence](suggested-installuisequence.md)
-   [Suggested InstallExecuteSequence](suggested-installexecutesequence.md)
-   [Suggested AdminUISequence](suggested-adminuisequence.md)
-   [Suggested AdminExecuteSequence](suggested-adminexecutesequence.md)
-   [Suggested AdvtUISequence](suggested-advtuisequence.md)
-   [Suggested AdvtExecuteSequence](suggested-advtexecutesequence.md)

For a detailed description of sequence tables and how standard actions are executed, see the [sequence table detailed example](sequence-table-detailed-example.md).

**Windows Installer 3.0 and later:  **

Beginning with Windows Installer 3.0, a patch package can contain the [MsiPatchSequence table](msipatchsequence-table.md). This table contains all the information the installer requires to determine the sequence of the application of a small update patch relative to all other patches. For more information, see [Patching and Upgrades](patching-and-upgrades.md).

> [!Note]
>
> [Merge Modules](merge-modules.md) may contain [Merge Module Database Tables](merge-module-database-tables.md) that modify the action sequence tables of the target .msi file. Merging the module into a database can modify the information in the sequence table, but does not add these tables to the .msi file. For more information, see [Authoring Merge Module Sequence Tables](authoring-merge-module-sequence-tables.md).

 

 

 



