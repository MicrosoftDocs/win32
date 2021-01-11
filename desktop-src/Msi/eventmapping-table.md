---
description: The EventMapping Table lists the controls that subscribe to some control events, and lists the attribute to be changed when the event is published by another control or the Windows Installer.
ms.assetid: 63c9ba3e-aa8a-475b-8360-4aec78ed19db
title: EventMapping Table
ms.topic: article
ms.date: 05/31/2018
---

# EventMapping Table

The EventMapping Table lists the controls that subscribe to some control events, and lists the attribute to be changed when the event is published by another control or the Windows Installer.

The EventMapping Table has the following columns.



| Column    | Type                         | Key | Nullable |
|-----------|------------------------------|-----|----------|
| Dialog\_  | [Identifier](identifier.md) | Y   | N        |
| Control\_ | [Identifier](identifier.md) | Y   | N        |
| Event     | [Identifier](identifier.md) | Y   | N        |
| Attribute | [Identifier](identifier.md) | N   | N        |



 

## Columns

<dl> <dt>

<span id="Dialog_"></span><span id="dialog_"></span><span id="DIALOG_"></span>Dialog\_
</dt> <dd>

An external key to the first column of the [Dialog Table](dialog-table.md). This field and the Control\_ field together identify a control.

</dd> <dt>

<span id="Control_"></span><span id="control_"></span><span id="CONTROL_"></span>Control\_
</dt> <dd>

An external key to the second column of the [Control Table](control-table.md). This field and the Dialog\_ field together identify a control.

</dd> <dt>

<span id="Event"></span><span id="event"></span><span id="EVENT"></span>Event
</dt> <dd>

This field is an identifier that specifies the type of event that is subscribed to by the control. For more information, see [ControlEvent Overview](controlevent-overview.md).

</dd> <dt>

<span id="Attribute"></span><span id="attribute"></span><span id="ATTRIBUTE"></span>Attribute
</dt> <dd>

The name of the Control\_ attribute that is set when the event in the Event column is received. The Argument of the event is passed as the argument of the attribute call to change this attribute of the control.

</dd> </dl>

## Remarks

The [ControlEvent Table](controlevent-table.md) specifies the control events that are started when a user interacts with a [PushButton Control](pushbutton-control.md), [CheckBox Control](checkbox-control.md), or [SelectionTree Control](selectiontree-control.md). These are the only controls that a user can use to initiate control events.

More than one control on a dialog box can subscribe to the same event.

The following list identifies the typical uses for the EventMapping Table:

-   To subscribe a [Text Control](text-control.md) to an [ActionText ControlEvent](actiontext-controlevent.md), [ActionData ControlEvent](actiondata-controlevent.md), [ScriptInProgress ControlEvent](scriptinprogress-controlevent.md) or [TimeRemaining ControlEvent](timeremaining-controlevent.md) published by the Windows Installer.
-   To subscribe a [ProgressBar Control](progressbar-control.md) or [Billboard Control](billboard-control.md) to a [SetProgress ControlEvent](setprogress-controlevent.md).
-   To subscribe a [DirectoryCombo Control](directorycombo-control.md) to an [IgnoreChange ControlEvent](ignorechange-controlevent.md).
-   To automatically disable a [PushButton Control](pushbutton-control.md) located on the same dialog with a [SelectionTree Control](selectiontree-control.md). To disable the push button when no features are listed in the [SelectionTree Control](selectiontree-control.md), use the EventMapping Table to subscribe the PushButton control to a [SelectionNoItems ControlEvent](selectionnoitems-controlevent.md). Enter **Enable** in the Attributes field of the EventMapping Table.
-   To display a [Text Control](text-control.md) that shows the path to the installation location for the feature that is selected in a [SelectionTree Control](selectiontree-control.md) on the same dialog. Use the EventMapping Table to subscribe the [Text Control](text-control.md) to both a [SelectionPathOn ControlEvent](selectionpathon-controlevent.md) and [SelectionPath ControlEvent](selectionpath-controlevent.md) published by the [SelectionTree Control](selectiontree-control.md).
-   To display a [Text Control](text-control.md) that shows a description of the item highlighted in a [SelectionTree Control](selectiontree-control.md) located on the same dialog, use the EventMapping Table to subscribe the [Text Control](text-control.md) to a [SelectionDescription ControlEvent](selectiondescription-controlevent.md), [SelectionSize ControlEvent](selectionsize-controlevent.md) or [SelectionAction ControlEvent](selectionaction-controlevent.md). Enter **Text** in the Attribute field of the EventMapping Table.

## Validation

<dl>

[ICE03](ice03.md)  
[ICE06](ice06.md)  
[ICE32](ice32.md)  
</dl>

 

 



