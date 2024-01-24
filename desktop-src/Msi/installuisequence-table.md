---
description: The InstallUISequence table lists actions that are executed when the top-level INSTALL action is executed and the internal user interface level is set to full UI or reduced UI.
ms.assetid: 076d7c14-e302-4465-aed5-27a4b1f70ac8
title: InstallUISequence Table
ms.topic: article
ms.date: 05/31/2018
---

# InstallUISequence Table

The InstallUISequence table lists actions that are executed when the top-level [INSTALL action](install-action.md) is executed and the internal user interface level is set to full UI or reduced UI. The installer skips the actions in this table if the user interface level is set to basic UI or no UI. See [About the User Interface](about-the-user-interface.md).

Actions in the install sequence up to the [InstallValidate action](installvalidate-action.md), and the exit dialog boxes, are located in the InstallUISequence table. All actions from the InstallValidate through the end of the install sequence are in the [InstallExecuteSequence table](installexecutesequence-table.md). Because the InstallExecuteSequence table needs to stand alone, it has any necessary initialization actions such as the [LaunchConditions](launchconditions-action.md), [CostInitialize](costinitialize-action.md), [FileCost](filecost-action.md), and the [CostFinalize](costfinalize-action.md), and [ExecuteAction action](executeaction-action.md).

The InstallUISequence table has the following columns.



| Column    | Type                         | Key | Nullable |
|-----------|------------------------------|-----|----------|
| Action    | [Identifier](identifier.md) | Y   | N        |
| Condition | [Condition](condition.md)   | N   | Y        |
| Sequence  | [Integer](integer.md)       | N   | Y        |



 

## Columns

<dl> <dt>

<span id="Action"></span><span id="action"></span><span id="ACTION"></span>Action
</dt> <dd>

Name of the action to execute. This is either a built-in action, a custom action, or a user interface wizard.

Primary table key.

</dd> <dt>

<span id="Condition"></span><span id="condition"></span><span id="CONDITION"></span>Condition
</dt> <dd>

This field contains a conditional expression. If the expression evaluates to False, then the action is skipped. If the expression syntax is invalid, then the sequence terminates, returning iesBadActionData. For information on the syntax of conditional statements, see [Conditional Statement Syntax](conditional-statement-syntax.md).

</dd> <dt>

<span id="Sequence"></span><span id="sequence"></span><span id="SEQUENCE"></span>Sequence
</dt> <dd>

The number in this column determines the sequence position in which this action is run.

A positive value represents the sequence position. A Null value indicates that the action is never run. The following negative values indicate that this action is executed if the installer returns the associated termination flag. Each termination flag (negative value) can be used with no more than one action. Multiple actions can have termination flags, but they must be different flags. Termination flags (negative values) are typically used with [Dialog Boxes](dialog-boxes.md).



| Termination flag          | Value | Description                                                                          |
|---------------------------|-------|--------------------------------------------------------------------------------------|
| msiDoActionStatusSuccess  | -1    | Successful completion. Used with [Exit](exit-dialog.md) dialog boxes.               |
| msiDoActionStatusUserExit | -2    | User terminates install. Used with [UserExit](userexit-dialog.md) dialog boxes.     |
| msiDoActionStatusFailure  | -3    | Fatal exit terminates. Used with a [FatalError](fatalerror-dialog.md) dialog boxes. |
| msiDoActionStatusSuspend  | -4    | Install is suspended.                                                                |



 

Zero, all other negative numbers, or a Null value indicate that the action is never run.

</dd> </dl>

## Remarks

Associated localized text for progress display or logging is specified in the [ActionText table](actiontext-table.md).

For an example of a sequence table, see [Using a Sequence Table](using-a-sequence-table.md).

## Validation

<dl>

[ICE03](ice03.md)  
[ICE06](ice06.md)  
[ICE12](ice12.md)  
[ICE13](ice13.md)  
[ICE20](ice20.md)  
[ICE26](ice26.md)  
[ICE27](ice27.md)  
[ICE28](ice28.md)  
[ICE46](ice46.md)  
[ICE75](ice75.md)  
[ICE79](ice79.md)  
[ICE82](ice82.md)  
[ICE86](ice86.md)  
</dl>

 

 



