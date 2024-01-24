---
description: The installer uses this event to publish data on the latest action. The data can be displayed on a dialog box by a Text Control that subscribes to this ControlEvent. This event should be authored in the EventMapping table.
ms.assetid: 3c0ab7d0-35f2-4966-8eff-f9f0419d8eed
title: ActionData ControlEvent
ms.topic: article
ms.date: 05/31/2018
---

# ActionData ControlEvent

The installer uses this event to publish data on the latest action. The data can be displayed on a dialog box by a [Text Control](text-control.md) that subscribes to this ControlEvent. This event should be authored in the [EventMapping table](eventmapping-table.md).

This ControlEvent can be handled by a user interface run at the [*basic UI*](b-gly.md), [*reduced UI*](r-gly.md), or [*full UI*](f-gly.md) levels. For information about UI levels, see [User Interface Levels](user-interface-levels.md).

## Published By

This ControlEvent is published by the installer.

## Argument

This ControlEvent does not use an argument.

## Action on Subscribers

The subscribers are hidden when a new action starts and shown when new action data arrives from the installer.

## Typical Use

A [Text Control](text-control.md) on a modeless dialog box subscribes to this event through the [EventMapping table](eventmapping-table.md). The [Text Control Attribute](text-control-attribute.md) is listed in the Attributes field of this table to receive the current action data. Typically used to display the names of the files copied during file copy.

 

 



