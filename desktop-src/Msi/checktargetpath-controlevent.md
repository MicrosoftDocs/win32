---
description: This event notifies the installer that it has to verify that the selected path is valid. If the path is not valid, then this event blocks further ControlEvents associated with the control.
ms.assetid: b7c1de6e-5738-4ecb-a033-9379d79dddb9
title: CheckTargetPath ControlEvent
ms.topic: article
ms.date: 05/31/2018
---

# CheckTargetPath ControlEvent

This event notifies the installer that it has to verify that the selected path is valid. If the path is not valid, then this event blocks further ControlEvents associated with the control.

This event can be published by a [PushButton Control](pushbutton-control.md)or a [SelectionTree control](selectiontree-control.md). This event should be authored into the [ControlEvent table](controlevent-table.md).

This ControlEvent requires the user interface to be run at the [*full UI*](f-gly.md) level. This event will not work with a [*reduced UI*](r-gly.md) or [*basic UI*](b-gly.md). For information, see [User Interface Levels](user-interface-levels.md).

## Published By

This ControlEvent is published by the installer.

## Argument

The name of the property containing the path. If the property is indirected, then the property name is enclosed in square brackets.

## Action on Subscribers

This ControlEvent does not perform an action on subscribers.

## Typical Use

A [PushButton](pushbutton-control.md) control on a browse dialog box is tied to this event in the [ControlEvent](controlevent-table.md) table to check the selected path before returning to the selection dialog box.

 

 



