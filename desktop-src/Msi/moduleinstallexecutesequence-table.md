---
description: A merge tool evaluates the ModuleInstallExecuteSequence table and then inserts the calculated actions into the InstallExecuteSequence table with a correct sequence number.
ms.assetid: 6cd04d9a-5489-4fde-951e-aa962e9bd755
title: ModuleInstallExecuteSequence Table
ms.topic: article
ms.date: 05/31/2018
---

# ModuleInstallExecuteSequence Table

A merge tool evaluates the ModuleInstallExecuteSequence table and then inserts the calculated actions into the [InstallExecuteSequence table](installexecutesequence-table.md) with a correct sequence number.

The ModuleInstallExecuteSequence table contains the following columns.



| Column     | Type                         | Key | Nullable |
|------------|------------------------------|-----|----------|
| Action     | [Identifier](identifier.md) | Y   | N        |
| Sequence   | [Integer](integer.md)       |     | Y        |
| BaseAction | [Identifier](identifier.md) |     | Y        |
| After      | [Integer](integer.md)       |     | Y        |
| Condition  | [Condition](condition.md)   |     | Y        |



 

## Columns

<dl> <dt>

<span id="Action"></span><span id="action"></span><span id="ACTION"></span>Action
</dt> <dd>

Action to insert into sequence. Refers to one of the installer [standard actions](standard-actions.md), or an entry in the merge module's [CustomAction table](customaction-table.md), or [Dialog table](dialog-table.md).

If a [standard action](standard-actions.md) is used in the Action column of a merge module sequence table, the BaseAction and After columns of that record must be null.

</dd> <dt>

<span id="Sequence"></span><span id="sequence"></span><span id="SEQUENCE"></span>Sequence
</dt> <dd>

The sequence number of a standard action. If a custom action or dialog is entered into the Action column of this row, this field must be set to null.

When using [standard actions](standard-actions.md) in merge module sequence tables, the value in the Sequence column should be the recommended action sequence number. If the sequence number in the merge module differs from that for the same action in the .msi file sequence table, the merge tool uses the sequence number from the .msi file. See the suggested sequences in [Using a Sequence Table](using-a-sequence-table.md) for the recommended sequence numbers of standard actions.

</dd> <dt>

<span id="BaseAction"></span><span id="baseaction"></span><span id="BASEACTION"></span>BaseAction
</dt> <dd>

The BaseAction column may contain a standard action, a custom action specified in the merge module's custom action table, or a dialog specified in the module's dialog table. The BaseAction column is a key into the Action column of this table. It cannot be a foreign key into another merge table or table in the Windows Installer file. This means that every standard action, custom action, or dialog listed in the BaseAction column must also be listed in the Action column of another record in this table.

</dd> <dt>

<span id="After"></span><span id="after"></span><span id="AFTER"></span>After
</dt> <dd>

Boolean for whether Action comes before or after BaseAction.



| Value | Meaning                          |
|-------|----------------------------------|
| 0     | Action to come before BaseAction |
| 1     | Action to come after BaseAction  |



 

</dd> <dt>

<span id="Condition"></span><span id="condition"></span><span id="CONDITION"></span>Condition
</dt> <dd>

A conditional statement that indicates if the action is to be executed. A null value evaluates to true.

</dd> </dl>

## Remarks

If the [ModuleInstallExecuteSequence table](installexecutesequence-table.md) is present, the [InstallExecuteSequence table](installexecutesequence-table.md) must also be present in the merge module.

 

 



