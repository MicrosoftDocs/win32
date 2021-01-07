---
description: Allows the author to specify the validation mode or modes during a reinstallation, and while the current dialog box is running.
ms.assetid: d7cd41c6-c019-49d6-b593-a1d31c8f5a81
title: ReinstallMode ControlEvent
ms.topic: article
ms.date: 05/31/2018
---

# ReinstallMode ControlEvent

The ReinstallMode ControlEventallows the author to specify the validation mode or modes during a reinstallation, and while the current dialog box is running.

This event can be published by a [PushButton Control](pushbutton-control.md) or a [SelectionTree control](selectiontree-control.md). This event should be authored into the [ControlEvent table](controlevent-table.md), and requires the user interface to be run at the [*full UI*](f-gly.md) level. This event does not work with a [*reduced UI*](r-gly.md) or [*basic UI*](b-gly.md). For more information, see [User Interface Levels](user-interface-levels.md).

## Published By

This ControlEvent is published by the installer.

## Argument

A string. For a list of possible values, see [**REINSTALLMODE**](reinstallmode.md) property.

## Action on Subscribers

This ControlEvent does not perform an action on subscribers.

## Typical Use

This event is tied to a [PushButton](pushbutton-control.md) control on a modal dialog box. The same [PushButton](pushbutton-control.md) control should also be tied to a [Reinstall](reinstall-controlevent.md) ControlEvent.

 

 



