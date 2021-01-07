---
description: The ControlCondition table enables an author to specify special actions to be applied to controls based on the result of a conditional statement. For example, using this table the author could choose to hide a control based on the VersionNT property.
ms.assetid: e36d20ec-cd7b-494f-b517-c07b40d2a338
title: ControlCondition Table
ms.topic: article
ms.date: 05/31/2018
---

# ControlCondition Table

The ControlCondition table enables an author to specify special actions to be applied to controls based on the result of a conditional statement. For example, using this table the author could choose to hide a control based on the [**VersionNT**](versionnt.md) property.

The ControlCondition table has the following columns.



| Column    | Type                         | Key | Nullable |
|-----------|------------------------------|-----|----------|
| Dialog\_  | [Identifier](identifier.md) | Y   | N        |
| Control\_ | [Identifier](identifier.md) | Y   | N        |
| Action    | [Text](text.md)             | Y   | N        |
| Condition | [Condition](condition.md)   | Y   | N        |



 

## Columns

<dl> <dt>

<span id="Dialog_"></span><span id="dialog_"></span><span id="DIALOG_"></span>Dialog\_
</dt> <dd>

An external key to the first column of the [Dialog table](dialog-table.md). Combining this field with the Control\_ field identifies a unique control.

</dd> <dt>

<span id="Control_"></span><span id="control_"></span><span id="CONTROL_"></span>Control\_
</dt> <dd>

An external key to the second column of the [Control table](control-table.md). Combining this field the Dialog\_ field identifies a unique control.

</dd> <dt>

<span id="Action"></span><span id="action"></span><span id="ACTION"></span>Action
</dt> <dd>

The action that is to be taken on the control. The possible actions are shown in the following table.



| Value   | Meaning                     |
|---------|-----------------------------|
| Default | Set control as the default. |
| Disable | Disable the control.        |
| Enable  | Enable the control.         |
| Hide    | Hide the control.           |
| Show    | Display the control.        |



 

</dd> <dt>

<span id="Condition"></span><span id="condition"></span><span id="CONDITION"></span>Condition
</dt> <dd>

A conditional statement that specifies under which conditions the action should be triggered. This column may not be left blank. If this statement does not evaluate to TRUE, the action does not take place. If it is set to 1, the action is always applied. For information on the syntax of conditional statements, see [Conditional Statement Syntax](conditional-statement-syntax.md).

</dd> </dl>

## Remarks

If you want to hide and disable a [PushButton control](pushbutton-control.md) or [CheckBox control](checkbox-control.md) based on a conditional statement in the Condition field of the ControlCondition table, you should use four records for each control to disable as well as hide the control. PushButton or CheckBox controls that have only been hidden can still be accessed by shortcut keys.

For example, the following records hide and disable ControlA on DialogA when the product is installed. The control will be visible and enabled when the product is not installed.



| Dialog  | Control  | Action  | Condition                      |
|---------|----------|---------|--------------------------------|
| DialogA | ControlA | Hide    | [**Installed**](installed.md) |
| DialogA | ControlA | Disable | Installed                      |
| DialogA | ControlA | Show    | NOT Installed                  |
| DialogA | ControlA | Enable  | NOT Installed                  |



 

## Validation

<dl>

[ICE03](ice03.md)  
[ICE06](ice06.md)  
[ICE17](ice17.md)  
[ICE32](ice32.md)  
[ICE46](ice46.md)  
[ICE79](ice79.md)  
[ICE86](ice86.md)  
</dl>

 

 



