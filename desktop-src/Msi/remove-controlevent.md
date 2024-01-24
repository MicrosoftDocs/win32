---
description: The installer is notified through this event when a feature or all features are selected for removal while keeping the present dialog box running.
ms.assetid: dabe44f7-97dd-4037-80e5-f289bab6d4b3
title: Remove ControlEvent
ms.topic: article
ms.date: 05/31/2018
---

# Remove ControlEvent

The installer is notified through this event when a feature or all features are selected for removal while keeping the present dialog box running.

This event can be published by a [PushButton control](pushbutton-control.md), [CheckBox control](checkbox-control.md), or a [SelectionTree control](selectiontree-control.md). This event should be authored into the [ControlEvent table](controlevent-table.md).

This ControlEvent requires the user interface to be run at the [*full UI*](f-gly.md) level. This event will not work with a [*reduced UI*](r-gly.md) or [*basic UI*](b-gly.md). For information, see [User Interface Levels](user-interface-levels.md).

## Published By

This ControlEvent is published by the installer.

## Argument

A string that is either the name of the feature or "ALL".

## Action on Subscribers

This ControlEvent does not perform an action on subscribers.

## Action by Publisher When Subscriber Activated

The installer keeps the present dialog box running and notifies the installer.

## Typical Use

A [PushButton](pushbutton-control.md) control on a modal dialog box tied to this event.

 

 



