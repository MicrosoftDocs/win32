---
description: The InstallExecuteSequence table lists actions that are executed when the top-level INSTALL action is executed.
ms.assetid: '995d4159-bfc9-48b2-8328-3ae8251d785d'
title: InstallExecuteSequence Table
ms.topic: article
ms.date: 05/31/2018
---

# InstallExecuteSequence Table

The InstallExecuteSequence table lists actions that are executed when the top-level [INSTALL action](install-action.md) is executed.

Actions in the install sequence up to the [InstallValidate action](installvalidate-action.md), and any exit dialog boxes, are located in the [InstallUISequence table](installuisequence-table.md). All actions from the InstallValidate through the end of the install sequence are in the InstallExecuteSequence table. Because the InstallExecuteSequence table needs to stand alone, it has any necessary initialization actions such as the [LaunchConditions](launchconditions-action.md), [CostInitialize](costinitialize-action.md), [FileCost](filecost-action.md), and [CostFinalize](costfinalize-action.md) actions.

[Custom actions](custom-actions.md) requiring a user interface should use [**MsiProcessMessage**](/windows/desktop/api/Msiquery/nf-msiquery-msiprocessmessage) instead of authored dialog boxes created using the [Dialog table](dialog-table.md).

The InstallExecuteSequence table has the following columns.



| Column    | Type                         | Key | Nullable |
|-----------|------------------------------|-----|----------|
| Action    | [Identifier](identifier.md) | Y   | N        |
| Condition | [Condition](condition.md)   | N   | Y        |
| Sequence  | [Integer](integer.md)       | N   | Y        |



 

## Columns

<dl> <dt>

<span id="Action"></span><span id="action"></span><span id="ACTION"></span>Action
</dt> <dd>

Name of the action to execute. This is either a built-in action or a custom action.

Primary table key.

</dd> <dt>

<span id="Condition"></span><span id="condition"></span><span id="CONDITION"></span>Condition
</dt> <dd>

This field contains a conditional expression. If the expression evaluates to False, then the action is skipped. If the expression syntax is invalid, then the sequence terminates, returning iesBadActionData. For information on the syntax of conditional statements, see [Conditional Statement Syntax](conditional-statement-syntax.md).

</dd> <dt>

<span id="Sequence"></span><span id="sequence"></span><span id="SEQUENCE"></span>Sequence
</dt> <dd>

Number that determines the sequence position in which this action is to be executed.

A positive value represents the sequence position. A Null value indicates that the action is not executed. The following negative values indicate that this action is to be executed if the installer returns the associated termination flag. Each termination flag (negative value) can be used with no more than one action. Multiple actions can have termination flags, but they must be different flags. Termination flags (negative values) are typically used with [Dialog Boxes](dialog-boxes.md).



| Termination flag          | Value | Description                                                                          |
|---------------------------|-------|--------------------------------------------------------------------------------------|
| msiDoActionStatusSuccess  | -1    | Successful completion. Used with [Exit](exit-dialog.md) dialog boxes.               |
| msiDoActionStatusUserExit | -2    | User terminates install. Used with [UserExit](userexit-dialog.md) dialog boxes.     |
| msiDoActionStatusFailure  | -3    | Fatal exit terminates. Used with a [FatalError](fatalerror-dialog.md) dialog boxes. |
| msiDoActionStatusSuspend  | -4    | Install is suspended.                                                                |



 

Zero, all other negative numbers, or a Null value indicate that the action is never run.

</dd> </dl>

## Remarks

Localized text for progress display or logging is specified in the [ActionText table](actiontext-table.md).

For an example of a sequence table, see [Using a Sequence Table](using-a-sequence-table.md).

## Validation

<dl>

[ICE03](ice03.md)  
[ICE06](ice06.md)  
[ICE12](ice12.md)  
[ICE13](ice13.md)  
[ICE26](ice26.md)  
[ICE27](ice27.md)  
[ICE28](ice28.md)  
[ICE46](ice46.md)  
[ICE63](ice63.md)  
[ICE75](ice75.md)  
[ICE77](ice77.md)  
[ICE79](ice79.md)  
[ICE82](ice82.md)  
[ICE83](ice83.md)  
[ICE84](ice84.md)  
[ICE86](ice86.md)  
</dl>

 

 



