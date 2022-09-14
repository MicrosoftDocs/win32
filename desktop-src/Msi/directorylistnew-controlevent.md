---
description: This event notifies the DirectoryList control that a new folder must be created; it creates the new folder, and selects the name field of the folder for editing.
ms.assetid: dc5859b9-f4b4-4ed7-93d5-369a3d2b9805
title: DirectoryListNew ControlEvent
ms.topic: article
ms.date: 05/31/2018
---

# DirectoryListNew ControlEvent

This event notifies the [DirectoryList control](directorylist-control.md) that a new folder must be created; it creates the new folder, and selects the name field of the folder for editing. The default name of the new folder may be authored in the [UIText table](uitext-table.md). Enter "NewFolder" into the Key column. Enter the value for the default name of the new folder into the Text column. This value must be in the form of a [Filename](filename.md) column data type and use the SFN\|LFN syntax. If this value is not present in the UIText table or is an invalid value, the installer uses a default value of "Fldr\|New Folder." For related information, see [Browse Dialog](browse-dialog.md).

This event should be published by a [PushButton Control](pushbutton-control.md) located on the same dialog box as the control subscribing to this event. The event should be authored in the [ControlEvent table](controlevent-table.md).

This ControlEvent requires the user interface to be run at the [*full UI*](f-gly.md) level. This event will not work with a [*reduced UI*](r-gly.md) or [*basic UI*](b-gly.md). For information, see [User Interface Levels](user-interface-levels.md).

Note that if this ControlEvent is called again when a new folder already exists, a second new folder will not be created. In this case, calling DirectoryListNew selects the existing new folder's name for editing.

## Published By

[DirectoryList](directorylist-control.md)

## Argument

This ControlEvent does not use an argument.

## Action on Subscribers

This ControlEvent does not perform an action on subscribers.

## Typical Use

A [PushButton](pushbutton-control.md) control on the same modal dialog box as the DirectoryList is used to trigger the creation of a new folder.

 

 



