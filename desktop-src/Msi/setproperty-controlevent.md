---
description: 'The syntax for the SetProperty event is different than for other ControlEvents In place of the name of the event one puts the property in square brackets: \[property\_name\].'
ms.assetid: a8e80d14-8d62-4398-9e53-9a0119a62d70
title: SetProperty ControlEvent
ms.topic: article
ms.date: 05/31/2018
---

# SetProperty ControlEvent

The syntax for the SetProperty event is different than for other ControlEvents In place of the name of the event one puts the property in square brackets: \[property\_name\]. The argument is the new value of the property. To unset the property, the argument must be {}. This is necessary, because the argument is a primary key in the table and so cannot be null. The argument will be formatted using the FormatText method, therefore the argument can contain any expression that the FormatText method can handle. The property values are evaluated at the moment of the ControlEvent.

This event can be published by a [PushButton Control](pushbutton-control.md), [CheckBox Control](checkbox-control.md), or a [SelectionTree control](selectiontree-control.md). This event should be authored into the [ControlEvent table](controlevent-table.md).

This ControlEvent requires the user interface to be run at the [*full UI*](f-gly.md) level. This event will not work with a [*reduced UI*](r-gly.md) or [*basic UI*](b-gly.md). For information, see [User Interface Levels](user-interface-levels.md).

## Published By

This ControlEvent is published by the installer.

## Argument

The new value of the property. {} for null.

## Action on Subscribers

None.

## Typical Use

A [PushButton](pushbutton-control.md) control on a dialog box linked to this event so it changes a property when the button is pushed.

 

 



