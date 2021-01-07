---
description: The SelectionTree control uses this event to publish a string describing the highlighted item. The string is one of the &\#0034;Sel\*&\#0034; strings from the UIText table. This event should be authored in the EventMapping table.
ms.assetid: 7770b46f-21c7-459f-9778-a86de70d467f
title: SelectionAction ControlEvent
ms.topic: article
ms.date: 05/31/2018
---

# SelectionAction ControlEvent

The [SelectionTree control](selectiontree-control.md) uses this event to publish a string describing the highlighted item. The string is one of the "Sel\*" strings from the [UIText table](uitext-table.md). This event should be authored in the [EventMapping table](eventmapping-table.md).

This ControlEvent requires the user interface to be run at the [*full UI*](f-gly.md) level. This event will not work with a [*reduced UI*](r-gly.md) or [*basic UI*](b-gly.md). For information, see [User Interface Levels](user-interface-levels.md).

This event can only affect controls that are located on the same dialog box as the SelectionTree control.

## Published By

[SelectionTree](selectiontree-control.md)

## Argument

None.

## Action on Subscribers

None.

## Typical Use

A [Text](text-control.md) control in the same modal dialog box as the SelectionTree should subscribe to this event via the [EventMapping table](eventmapping-table.md). The Text Control displays the explanation of the selected item.

 

 



