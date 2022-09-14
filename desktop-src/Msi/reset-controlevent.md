---
description: The dialog box is reset. In other words, all the controls on the dialog box are called to undo the property changes they have performed. This event resets all the property values to what they were when the dialog box was created.
ms.assetid: 6449abb8-54cb-4400-9eb2-b7e7f1564747
title: Reset ControlEvent
ms.topic: article
ms.date: 05/31/2018
---

# Reset ControlEvent

The dialog box is reset. In other words, all the controls on the dialog box are called to undo the property changes they have performed. This event resets all the property values to what they were when the dialog box was created.

This event can be published by a [PushButton Control](pushbutton-control.md)or a [SelectionTree control](selectiontree-control.md). This event should be authored into the [ControlEvent table](controlevent-table.md).

This ControlEvent requires the user interface to be run at the [*full UI*](f-gly.md) level. This event will not work with a [*reduced UI*](r-gly.md) or [*basic UI*](b-gly.md). For information, see [User Interface Levels](user-interface-levels.md).

There is a case, which should occur rarely in practice, that is not handled properly by this ControlEvent. If there are two or more controls on the same dialog box linked indirectly to the same property and at least one of them started having some other property, then this property value will sometimes be reset to its second value.

## Published By

This ControlEvent is published by the installer.

## Argument

None.

## Action on Subscribers

None.

## Typical Use

A [PushButton](pushbutton-control.md) control on a modal dialog box is used to reset all the values on the dialog box and to cancel all the changes on the page.

 

 



