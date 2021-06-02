---
description: The order of action execution is determined by the sequence of actions that have been authored into the sequence tables and by the order in which the installer runs the sequence tables.
ms.assetid: f4666f49-4ea1-42fb-b32d-ce77de79b212
title: Action Execution Order
ms.topic: article
ms.date: 05/31/2018
---

# Action Execution Order

The order of action execution is determined by the sequence of actions that have been authored into the [*sequence tables*](s-gly.md) and by the order in which the installer runs the sequence tables. For details, see the suggested action sequences in [Using a Sequence Table](using-a-sequence-table.md).

The installer runs sequence tables in response to a request for an installation, [advertisement](advertisement.md), or an [administrative installation](administrative-installation.md). For example, in response to using the /I, /J, or /A [command line options](command-line-options.md), the [INSTALL](install-action.md), [ADVERTISE](advertise-action.md), and [ADMIN](admin-action.md) actions are not called from within the action sequence. These high-level actions are instead passed to the installer when the installer is initialized.

If the installer is passed the INSTALL action and the installation package has been authored with a user interface, the installer first runs the actions in [InstallUISequence table](installuisequence-table.md) and then executes the actions in the [InstallExecuteSequence table](installexecutesequence-table.md) in order. If the package has no user interface, the installer executes the actions in the InstallExecuteSequence table in order.

If the installer is passed the ADMIN action, and the installation package has been authored with a user interface, the installer first runs the [AdminUISequence table](adminuisequence-table.md) and then runs the [AdminExecuteSequence table](adminexecutesequence-table.md). If the package has no user interface, the installer runs the AdminExecute table.

If the installer is passed the ADVERTISE action, the installer runs the [AdvtExecuteSequence](advtexecutesequence-table.md) table.

> [!Note]  
> The installer does not use the [AdvtUISequence](advtuisequence-table.md) table. The AdvtUISequence table should not exist in the installation database or it should be left empty.

 

When the installer runs a sequence table, it executes actions in the order of the sequence numbers listed in the Sequence column. The action order is always linear with no branching or looping. Package developers can conditionally prevent a particular action from being executed by authoring a logical expression into the Condition column. The installer skips the action whenever the condition evaluates to False. See [Using a Sequence Table](using-a-sequence-table.md) and [Conditional Statement Syntax](conditional-statement-syntax.md).

All sequence tables have the following columns.



| Column    | Description                                                                                                                                                                                                                                   |
|-----------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Action    | The primary key for the table; the action name must be unique.                                                                                                                                                                                |
| Condition | A Boolean expression used to determine whether to perform the action. The action is executed if this field is either blank or contains an expression that evaluates to True. The action is not executed if the expression evaluates to False. |
| Sequence  | A relative sequence number used to determine the order in which actions are executed.                                                                                                                                                         |



 

 

 



