---
description: The IgnoreChange ControlEvent is published by the DirectoryList control when the selected folder is changed from one directory to another directory in the control. This event should be authored in the EventMapping table.
ms.assetid: 4d3128a1-cbe3-457c-83b5-8f6ec1a7ba29
title: IgnoreChange ControlEvent
ms.topic: article
ms.date: 05/31/2018
---

# IgnoreChange ControlEvent

The IgnoreChange ControlEvent is published by the [DirectoryList control](directorylist-control.md) when the selected folder is changed from one directory to another directory in the control. This event should be authored in the [EventMapping table](eventmapping-table.md).

This ControlEvent requires the user interface to be run at the [*full UI*](f-gly.md) level. This event will not work with a [*reduced UI*](r-gly.md) or [*basic UI*](b-gly.md). For information, see [User Interface Levels](user-interface-levels.md).

## Published By

[DirectoryList](directorylist-control.md)

## Argument

This ControlEvent does not use an argument.

## Action on Subscribers

This ControlEvent does not perform an action on subscribers.

## Typical Use

The [DirectoryCombo control](directorycombo-control.md) commonly employs the IgnoreChange ControlEvent.

 

 



