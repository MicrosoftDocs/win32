---
description: This event notifies the installer, while keeping the present dialog running, that a feature or all features are to be run from source.
ms.assetid: fd8d6433-87cc-4544-9f4f-57a90e5f2ea5
title: AddSource ControlEvent
ms.topic: article
ms.date: 05/31/2018
---

# AddSource ControlEvent

This event notifies the installer, while keeping the present dialog running, that a feature or all features are to be run from source. This event can be published by a [PushButton Control](pushbutton-control.md), [Checkbox Control](checkbox-control.md), or a [SelectionTree control](selectiontree-control.md). This event should be authored into the [ControlEvent table](controlevent-table.md).

This ControlEvent requires the user interface to be run at the [*full UI*](f-gly.md) level. This event will not work with a [*reduced UI*](r-gly.md) or [*basic UI*](b-gly.md). For information, see [User Interface Levels](user-interface-levels.md).

## Published By

This ControlEvent is published by the installer.

## Argument

A string, either the name of the feature or "ALL".

## Action on Subscribers

This ControlEvent does not perform an action on subscribers.

## Typical Use

A [PushButton](pushbutton-control.md) control on a modal dialog box is tied to this event and used to notify the installer without stopping the dialog box.

 

 



