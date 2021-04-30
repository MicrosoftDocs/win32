---
description: This event notifies the DirectoryList control that the user wants to select the parent of the present directory. For related information, see Browse Dialog.
ms.assetid: 83fdb160-ce3b-42e1-8688-42d3ba39d6dd
title: DirectoryListUp ControlEvent
ms.topic: article
ms.date: 05/31/2018
---

# DirectoryListUp ControlEvent

This event notifies the [DirectoryList control](directorylist-control.md) that the user wants to select the parent of the present directory. For related information, see [Browse Dialog](browse-dialog.md).

This event should be published by a [PushButton Control](pushbutton-control.md) located on the same dialog box as the control subscribing to this event. The event should be authored in the [ControlEvent table](controlevent-table.md).

This ControlEvent requires the user interface to be run at the [*full UI*](f-gly.md) level. This event will not work with a [*reduced UI*](r-gly.md) or [*basic UI*](b-gly.md). For information, see [User Interface Levels](user-interface-levels.md).

If the current directory is the root directory of the drive, a DirectoryListUp event disables any other controls that publish a DirectoryListUp event.

## Published By

[DirectoryList](directorylist-control.md)

## Argument

This ControlEvent does not use an argument.

## Action on Subscribers

This ControlEvent does not perform an action on subscribers.

## Typical Use

A [PushButton](pushbutton-control.md) control on the same modal dialog box as the DirectoryList is used to trigger stepping up in the path.

 

 



