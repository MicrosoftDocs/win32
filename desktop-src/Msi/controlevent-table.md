---
description: The ControlEvent table allows the author to specify the Control Events started when a user interacts with a PushButton Control, CheckBox Control, or SelectionTree Control.
ms.assetid: e34d17e9-cd6b-4a21-9abc-9562ee648c59
title: ControlEvent Table
ms.topic: article
ms.date: 05/31/2018
---

# ControlEvent Table

The ControlEvent table allows the author to specify the [Control Events](control-events.md) started when a user interacts with a [PushButton Control](pushbutton-control.md), [CheckBox Control](checkbox-control.md), or [SelectionTree Control](selectiontree-control.md). These are the only controls users can use to initiate control events. Each control can publish multiple control events. The installer starts each event in the order specified in the Ordering column. For example, a push button control can publish events to initiate a transition to another dialog box, exit the dialog box sequence, and begin file installation.

The exception to note is that each control can publish a most one [NewDialog](newdialog-controlevent.md) or one [SpawnDialog](spawndialog-controlevent.md) event. If you need to author multiple NewDialog and SpawnDialog control events in this table, also include conditional statements in the Condition fields that ensure at most one event is published. If multiple NewDialog and SpawnDialog control events are selected for the same control, only the event with the largest value in the Ordering column gets published when the control is activated.

The ControlEvent table has the following columns.



| Column    | Type                         | Key | Nullable |
|-----------|------------------------------|-----|----------|
| Dialog\_  | [Identifier](identifier.md) | Y   | N        |
| Control\_ | [Identifier](identifier.md) | Y   | N        |
| Event     | [Formatted](formatted.md)   | Y   | N        |
| Argument  | [Formatted](formatted.md)   | Y   | N        |
| Condition | [Condition](condition.md)   | Y   | Y        |
| Ordering  | [Integer](integer.md)       | N   | Y        |



 

## Columns

<dl> <dt>

<span id="Dialog_"></span><span id="dialog_"></span><span id="DIALOG_"></span>Dialog\_
</dt> <dd>

An external key to the first column of the [Dialog table](dialog-table.md). Combining this field with the Control\_ field identifies a unique control.

</dd> <dt>

<span id="Control_"></span><span id="control_"></span><span id="CONTROL_"></span>Control\_
</dt> <dd>

An external key to the second column of the [Control table](control-table.md). Combining this field with the Dialog\_ field identifies a unique control.

</dd> <dt>

<span id="Event"></span><span id="event"></span><span id="EVENT"></span>Event
</dt> <dd>

An identifier that specifies the type of event that should take place when the user interacts with the control specified by Dialog\_ and Control\_. For a list of possible values see [ControlEvent Overview](controlevent-overview.md).

To set a property with a control, put \[Property\_Name\] in this field and the new value in the argument field. Put { } into the argument field to enter the null value.

</dd> <dt>

<span id="Argument"></span><span id="argument"></span><span id="ARGUMENT"></span>Argument
</dt> <dd>

A value used as a modifier when triggering a particular event.

For example, the argument of the [NewDialog ControlEvent](newdialog-controlevent.md) or the [SpawnDialog ControlEvent](spawndialog-controlevent.md) is the name of the dialog box and the argument of the [Install action](install-action.md) is a number defining the install level.

</dd> <dt>

<span id="Condition"></span><span id="condition"></span><span id="CONDITION"></span>Condition
</dt> <dd>

A conditional statement that determines whether the installer activates the event in the Event column. The installer triggers the event if the conditional statement in the Condition field evaluates to True. Therefore put a 1 in this column to ensure that the installer triggers the event. The installer does not trigger the event if the Condition field contains a statement that evaluates to False. The installer does not trigger an event with a blank in the Condition field unless no other events of the control evaluate to True. If none of the Condition fields for the control named in the Control\_ field evaluate to True, the installer triggers the one event having a blank Condition field, and if more than one Condition field is blank it triggers the one event of these with the largest value in the Ordering field. See [Conditional Statement Syntax](conditional-statement-syntax.md).

</dd> <dt>

<span id="Ordering"></span><span id="ordering"></span><span id="ORDERING"></span>Ordering
</dt> <dd>

An integer used to order several events tied to the same control. This must be a non-negative number. This field may be left blank.

</dd> </dl>

## Remarks

The [EventMapping table](eventmapping-table.md) lists the controls that subscribe to some control event and lists the control attribute to be changed when that event is published by the another control or the installer.

On Windows XP or earlier operating systems, users can publish a control event only by interacting with a [Checkbox Control](checkbox-control.md) or [Pushbutton Control](pushbutton-control.md). With Windows Server 2003, users can publish a control event only by interacting with a [Checkbox Control](checkbox-control.md), [SelectionTree Control](selectiontree-control.md), and [Pushbutton Control](pushbutton-control.md). Listing other controls in the Control\_ field has no effect.

## Validation

<dl>

[ICE03](ice03.md)  
[ICE06](ice06.md)  
[ICE17](ice17.md)  
[ICE20](ice20.md)  
[ICE32](ice32.md)  
[ICE44](ice44.md)  
[ICE46](ice46.md)  
[ICE79](ice79.md)  
[ICE86](ice86.md)  
</dl>

 

 



