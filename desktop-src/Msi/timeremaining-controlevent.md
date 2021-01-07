---
description: The installer uses the TimeRemaining event to publish the approximate time remaining, in seconds, for the current progress sequence.
ms.assetid: ec5fc2b3-13a9-4681-89f0-fd39bab1de5f
title: TimeRemaining ControlEvent
ms.topic: article
ms.date: 05/31/2018
---

# TimeRemaining ControlEvent

The installer uses the TimeRemaining event to publish the approximate time remaining, in seconds, for the current progress sequence. The time remaining can be displayed on a dialog box by a [Text Control](text-control.md) that subscribes to this ControlEvent. This event should be authored in the [EventMapping table](eventmapping-table.md).

This ControlEvent can be handled by a user interface run at the [*basic UI*](b-gly.md), [*reduced UI*](r-gly.md), or [*full UI*](f-gly.md) levels. For information about UI levels, see [User Interface Levels](user-interface-levels.md).

## Published By

This ControlEvent is published by the installer.

## Argument

None.

## Action on Subscribers

None.

## Typical Use

A [Text Control](text-control.md) on a modeless dialog box subscribes to this event through the [EventMapping table](eventmapping-table.md) and uses the [TimeRemaining attribute](timeremaining-control-attribute.md) to display the time remaining.

The same text control that subscribes to the TimeRemaining ControlEvent can also subscribe to the [ScriptInProgress ControlEvent](scriptinprogress-controlevent.md). In this case, as the preliminary ScriptInProgress message string, it is replaced by the "Time Remaining: xx minutes" string.

 

 



