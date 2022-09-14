---
description: The AdvtExecuteSequence table lists actions the installer calls when the top-level ADVERTISE action is executed.
ms.assetid: 8873c161-a709-48b8-a66f-fe2ee9be859f
title: AdvtExecuteSequence Table
ms.topic: article
ms.date: 05/31/2018
---

# AdvtExecuteSequence Table

The AdvtExecuteSequence table lists actions the installer calls when the top-level [ADVERTISE action](advertise-action.md) is executed.

Only the following actions can be used in the AdvtExecuteSequence table. Custom actions cannot be used in this table.

[CostFinalize](costfinalize-action.md)

[CostInitialize](costinitialize-action.md)

[CreateShortcuts](createshortcuts-action.md)

[InstallFinalize](installfinalize-action.md)

[InstallInitialize](installinitialize-action.md)

[InstallValidate](installvalidate-action.md)

[MsiPublishAssemblies](msipublishassemblies-action.md)

[PublishComponents](publishcomponents-action.md)

[PublishFeatures](publishfeatures-action.md)

[PublishProduct](publishproduct-action.md)

[RegisterClassInfo](registerclassinfo-action.md)

[RegisterExtensionInfo](registerextensioninfo-action.md)

[RegisterMIMEInfo](registermimeinfo-action.md)

[RegisterProgIdInfo](registerprogidinfo-action.md)

The columns are identical to those of the [InstallExecuteSequence table](installexecutesequence-table.md). The AdvtExecuteSequence table has the following columns.



| Column    | Type                         | Key | Nullable |
|-----------|------------------------------|-----|----------|
| Action    | [Identifier](identifier.md) | Y   | N        |
| Condition | [Condition](condition.md)   | N   | Y        |
| Sequence  | [Integer](integer.md)       | N   | Y        |



 

## Columns

<dl> <dt>

<span id="Action"></span><span id="action"></span><span id="ACTION"></span>Action
</dt> <dd>

Name of the [standard action](standard-actions.md) the installer is to execute. This is the primary key of the table.

</dd> <dt>

<span id="Condition"></span><span id="condition"></span><span id="CONDITION"></span>Condition
</dt> <dd>

Logical expression. If the expression evaluates to false, the action is skipped. If the expression syntax is invalid, the sequence terminates, returning iesBadActionData. For information on the syntax of conditional statements, see [Conditional Statement Syntax](conditional-statement-syntax.md).

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
[ICE27](ice27.md)  
[ICE46](ice46.md)  
[ICE72](ice72.md)  
[ICE79](ice79.md)  
[ICE82](ice82.md)  
[ICE83](ice83.md)  
[ICE84](ice84.md)  
[ICE86](ice86.md)  
[ICEM04](icem04.md)  
</dl>

 

 



