---
description: Allows the author to initiate a reinstall of some or all features, while the current dialog box is running.
ms.assetid: bc667f20-3abe-4ef3-b51e-dc74da63f651
title: Reinstall ControlEvent
ms.topic: article
ms.date: 05/31/2018
---

# Reinstall ControlEvent

The Reinstall ControlEventallows the author to initiate a reinstall of some or all features, while the current dialog box is running.

This event can be published by a [PushButton control](pushbutton-control.md) or a [SelectionTree control](selectiontree-control.md). This event should be authored into the [ControlEvent table](controlevent-table.md), and requires the user interface to be run at the [*full UI*](f-gly.md) level. This event does not work with a [*reduced UI*](r-gly.md) or [*basic UI*](b-gly.md). For more information, see [User Interface Levels](user-interface-levels.md).

## Published By

This ControlEvent is published by the installer.

## Argument

A string that is either the name of the feature or "ALL".

## Action on Subscribers

This ControlEvent does not perform an action on subscribers.

## Typical Use

This event is tied to a [PushButton](pushbutton-control.md) control on a modal dialog box. The same [PushButton](pushbutton-control.md) control should also be tied to a [ReinstallMode](reinstallmode-controlevent.md) ControlEvent.

 

 



