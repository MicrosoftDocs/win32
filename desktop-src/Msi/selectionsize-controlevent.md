---
description: The SelectionTree control uses the SelectionSize event to publish the size of the highlighted item.
ms.assetid: 1ef161b6-f127-45ad-a312-d2adcb5124ef
title: SelectionSize ControlEvent
ms.topic: article
ms.date: 05/31/2018
---

# SelectionSize ControlEvent

The [SelectionTree control](selectiontree-control.md) uses the SelectionSize event to publish the size of the highlighted item. If it is a parent item, then the number of children selected is also published. The string is one of the **SelChildCostPos**, **SelChildCostNeg**, **SelParentCostPosPos**, **SelParentCostPosNeg**, **SelParentCostNegPos** or **SelParentCostNegNeg** strings from the [UIText table](uitext-table.md). This event should be authored in the [EventMapping table](eventmapping-table.md).

This ControlEvent requires the user interface to be run at the [*full UI*](f-gly.md) level. This event will not work with a [*reduced UI*](r-gly.md) or [*basic UI*](b-gly.md). For information, see [User Interface Levels](user-interface-levels.md).

This event can only affect controls that are located on the same dialog box as the SelectionTree control.

## Published By

[SelectionTree](selectiontree-control.md)

## Argument

None.

## Action on Subscribers

None.

## Typical Use

A [Text](text-control.md) control on the same modal dialog as the SelectionTree Control via the [EventMapping table](eventmapping-table.md). The Text Control uses this event to display the size of the highlighted item.

 

 



