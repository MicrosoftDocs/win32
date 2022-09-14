---
description: The AdminExecuteSequence table lists actions that the installer calls in sequence when the top-level ADMIN action is executed.
ms.assetid: 33a2ef50-519b-424e-b510-55c21c5706a3
title: AdminExecuteSequence Table
ms.topic: article
ms.date: 05/31/2018
---

# AdminExecuteSequence Table

The AdminExecuteSequence table lists actions that the installer calls in sequence when the top-level [ADMIN action](admin-action.md) is executed.

ADMIN actions in the install sequence, up to the [InstallValidate action](installvalidate-action.md) and any exit dialog boxes, are located in the [AdminUISequence table](adminuisequence-table.md).

ADMIN actions from the InstallValidate action through the end of the install sequence are in the AdminExecuteSequence table. Because the AdminExecuteSequence table needs to stand alone, it also contains any necessary initialization actions such as [LaunchConditions](launchconditions-action.md), [CostInitialize](costinitialize-action.md), [FileCost](filecost-action.md), and [CostFinalize](costfinalize-action.md).

[Custom actions](custom-actions.md) requiring a user interface should use [**MsiProcessMessage**](/windows/desktop/api/Msiquery/nf-msiquery-msiprocessmessage) instead of authored dialog boxes created using the [Dialog table](dialog-table.md).

The columns are identical to those of the [InstallExecuteSequence table](installexecutesequence-table.md). The AdminExecuteSequence table has the following columns.



| Column    | Type                         | Key | Nullable |
|-----------|------------------------------|-----|----------|
| Action    | [Identifier](identifier.md) | Y   | N        |
| Condition | [Condition](condition.md)   | N   | Y        |
| Sequence  | [Integer](integer.md)       | N   | Y        |



 

## Columns

<dl> <dt>

<span id="Action"></span><span id="action"></span><span id="ACTION"></span>Action
</dt> <dd>

Name of the action to execute. This is either a standard action or a custom action listed in the [CustomAction table](customaction-table.md).

Primary table key.

</dd> <dt>

<span id="Condition"></span><span id="condition"></span><span id="CONDITION"></span>Condition
</dt> <dd>

Logical expression. If the expression evaluates to false, the action is skipped. If the expression syntax is invalid, the sequence terminates, returning iesBadActionData. For information on the syntax of conditional statements see [Conditional Statement Syntax](conditional-statement-syntax.md).

</dd> <dt>

<span id="Sequence"></span><span id="sequence"></span><span id="SEQUENCE"></span>Sequence
</dt> <dd>

A positive value indicates the sequence position of the action. The following negative values indicate that the action is called if the installer returns the termination flag. Each termination flag (negative value) can be used with no more than one action. Multiple actions can have termination flags, but they must be different flags. Termination flags (negative values) are typically used with [Dialog Boxes](dialog-boxes.md).



| Termination flag          | Value | Description                                                                          |
|---------------------------|-------|--------------------------------------------------------------------------------------|
| msiDoActionStatusSuccess  | -1    | Successful completion. Used with [Exit](exit-dialog.md) dialog boxes.               |
| msiDoActionStatusUserExit | -2    | User terminates install. Used with [UserExit](userexit-dialog.md) dialog boxes.     |
| msiDoActionStatusFailure  | -3    | Fatal exit terminates. Used with a [FatalError](fatalerror-dialog.md) dialog boxes. |
| msiDoActionStatusSuspend  | -4    | Install is suspended.                                                                |



 

Zero, all other negative numbers, or a null value indicate that the action is never called.

</dd> </dl>

## Validation

<dl>

[ICE03](ice03.md)  
[ICE06](ice06.md)  
[ICE12](ice12.md)  
[ICE13](ice13.md)  
[ICE26](ice26.md)  
[ICE27](ice27.md)  
[ICE28](ice28.md)  
[ICE75](ice75.md)  
[ICE77](ice77.md)  
[ICE79](ice79.md)  
[ICE82](ice82.md)  
[ICE84](ice84.md)  
[ICE86](ice86.md)  
[ICEM04](icem04.md)  
</dl>

 

 



