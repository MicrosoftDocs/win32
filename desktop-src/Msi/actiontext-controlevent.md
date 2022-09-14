---
description: The installer uses this event to publish the name of the present action. The name can be displayed on a dialog box by a Text Control that subscribes to this ControlEvent. This event should be authored in the EventMapping table.
ms.assetid: 2b4928fe-2d5c-46c1-8a31-cbebbc78d304
title: ActionText ControlEvent
ms.topic: article
ms.date: 05/31/2018
---

# ActionText ControlEvent

The installer uses this event to publish the name of the present action. The name can be displayed on a dialog box by a [Text Control](text-control.md) that subscribes to this ControlEvent. This event should be authored in the [EventMapping table](eventmapping-table.md).

This ControlEvent can be handled by a user interface run at the [*basic UI*](b-gly.md), [*reduced UI*](r-gly.md), or [*full UI*](f-gly.md) levels. For information about UI levels, see [User Interface Levels](user-interface-levels.md).

## Published By

This ControlEvent is published by the installer.

## Argument

This ControlEvent does not use an argument.

## Action on Subscribers

The subscribers are shown when a new progress data arrives from the installer.

## Typical Use

A [Text Control](text-control.md) on a modeless dialog subscribes to this event through the [EventMapping table](eventmapping-table.md). The [Text Control Attribute](text-control-attribute.md) should be listed in the Attributes field of this table to receive the name of the current action.

 

 



