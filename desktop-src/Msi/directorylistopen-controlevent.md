---
description: This event selects and highlights a directory in the DirectoryList control that the user has chosen to open. For related information, see Browse Dialog.
ms.assetid: 95cdf345-e1bb-41d8-b1e0-2acf97e33110
title: DirectoryListOpen ControlEvent
ms.topic: article
ms.date: 05/31/2018
---

# DirectoryListOpen ControlEvent

This event selects and highlights a directory in the [DirectoryList control](directorylist-control.md) that the user has chosen to open. For related information, see [Browse Dialog](browse-dialog.md).

This event should be published by a [PushButton Control](pushbutton-control.md) located on the same dialog box as the control subscribing to this event. The event should be authored in the [ControlEvent table](controlevent-table.md).

This ControlEvent requires the user interface to be run at the [*full UI*](f-gly.md) level. This event will not work with a [*reduced UI*](r-gly.md) or [*basic UI*](b-gly.md). For information, see [User Interface Levels](user-interface-levels.md).

If no directory has been selected in the [DirectoryList control](directorylist-control.md), a DirectoryListOpen event disables any other controls that publish a DirectoryListOpen event.

## Published By

[DirectoryList](directorylist-control.md)

## Argument

This ControlEvent does not use an argument.

## Action on Subscribers

This ControlEvent performs no action on subscribers.

## Typical Use

A [PushButton](pushbutton-control.md) control on the same modal dialog box as the DirectoryList is used to trigger stepping down in the path.

 

 



