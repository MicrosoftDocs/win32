---
description: The SpawnDialog ControlEvent notifies the installer to create a child of a modal dialog box while keeping the present dialog box running.
ms.assetid: 2a341039-60dd-4e6c-9ef3-bf482ca53917
title: SpawnDialog ControlEvent
ms.topic: article
ms.date: 05/31/2018
---

# SpawnDialog ControlEvent

The SpawnDialog ControlEvent notifies the installer to create a child of a modal dialog box while keeping the present dialog box running.

This event can be published by a [PushButton Control](pushbutton-control.md)or a [SelectionTree control](selectiontree-control.md). This event should be authored into the [ControlEvent table](controlevent-table.md).

This ControlEvent requires the user interface to be run at the [*full UI*](f-gly.md) level. This event will not work with a [*reduced UI*](r-gly.md) or [*basic UI*](b-gly.md). For information, see [User Interface Levels](user-interface-levels.md).

## Published By

This ControlEvent is published by the installer.

## Argument

A string that is the name of the new dialog box.

## Action on Subscribers

None.

## Typical Use

A [PushButton](pushbutton-control.md) control on a modal dialog is tied to this event in the [ControlEvent](controlevent-table.md) table to create a child dialog, such as an "Are you sure you want to cancel?" dialog box.

 

 



