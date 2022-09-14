---
description: The SelectionTree control uses the SelectionPath event to publish the path for the highlighted item.
ms.assetid: 755e5bf2-42c4-4213-9bb7-4f15ad22041f
title: SelectionPath ControlEvent
ms.topic: article
ms.date: 05/31/2018
---

# SelectionPath ControlEvent

The [SelectionTree control](selectiontree-control.md) uses the SelectionPath event to publish the path for the highlighted item. If the item is selected to run from source, then this is the path of the source. If the item is selected to be absent, then the string is the **AbsentPath** string from the [UIText table](uitext-table.md). This event should be authored in the [EventMapping table](eventmapping-table.md).

This ControlEvent requires the user interface to be run at the [*full UI*](f-gly.md) level. This event will not work with a [*reduced UI*](r-gly.md) or [*basic UI*](b-gly.md). For information, see [User Interface Levels](user-interface-levels.md).

This event can only affect controls that are located on the same dialog box as the SelectionTree control.

## Published By

[SelectionTree](selectiontree-control.md)

## Argument

None.

## Action on Subscribers

None.

## Typical Use

A [Text](text-control.md) control on the same modal dialog as the SelectionTree should subscribe to the event via the [EventMapping table](eventmapping-table.md). The Text Control displays the path of the highlighted item.

 

 



