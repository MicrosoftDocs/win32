---
description: The SelectionTree control uses the SelectionDescription event to publish a string that contains the description for the highlighted item. This string is the Description field of the Feature table. This event should be authored in the EventMapping table.
ms.assetid: 29ae9aec-764f-4ff2-9c08-805538130cb1
title: SelectionDescription ControlEvent
ms.topic: article
ms.date: 05/31/2018
---

# SelectionDescription ControlEvent

The [SelectionTree control](selectiontree-control.md) uses the SelectionDescription event to publish a string that contains the description for the highlighted item. This string is the **Description** field of the [Feature table](feature-table.md). This event should be authored in the [EventMapping table](eventmapping-table.md).

This event can only affect controls that are located on the same dialog box as the [SelectionTree control](selectiontree-control.md).

This ControlEvent requires the user interface to be run at the [*full UI*](f-gly.md) level. This event will not work with a [*reduced UI*](r-gly.md) or [*basic UI*](b-gly.md). For more information, see [User Interface Levels](user-interface-levels.md).

## Published By

[SelectionTree](selectiontree-control.md)

## Argument

None.

## Action on Subscribers

None.

## Typical Use

A [Text](text-control.md) control on the same modal dialog as the SelectionTree subscribes to this ControlEvent via the [EventMapping table](eventmapping-table.md). The Text Control uses this event to display the description of the highlighted item.

 

 



