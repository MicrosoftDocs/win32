---
description: This event notifies the installer to transition a modal dialog box to another dialog box. The installer removes the present dialog box and creates the new one with the name indicated in the argument.
ms.assetid: bd1aa465-55a0-4983-8c71-7e7075ee9dfb
title: NewDialog ControlEvent
ms.topic: article
ms.date: 05/31/2018
---

# NewDialog ControlEvent

This event notifies the installer to transition a modal dialog box to another dialog box. The installer removes the present dialog box and creates the new one with the name indicated in the argument.

This event can be published by a [PushButton Control](pushbutton-control.md)or a [SelectionTree control](selectiontree-control.md). This event should be authored into the [ControlEvent table](controlevent-table.md).

This ControlEvent requires the user interface to be run at the [*full UI*](f-gly.md) level. This event will not work with a [*reduced UI*](r-gly.md) or [*basic UI*](b-gly.md). For information, see [User Interface Levels](user-interface-levels.md).

## Published By

This ControlEvent is published by the installer.

## Argument

A string that is the name of the new dialog.

## Action on Subscribers

This ControlEvent does not perform an action on subscribers.

## Typical Use

A [PushButton](pushbutton-control.md) control on a modal dialog box is tied to this event in the [ControlEvent](controlevent-table.md) table to signal a transition to the next or previous dialog box of the same wizard sequence.

 

 



