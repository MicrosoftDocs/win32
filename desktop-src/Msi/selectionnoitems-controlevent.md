---
description: The SelectionTree control uses the SelectionNoItems event to delete obsolete item description text or to disable buttons that have become useless. This event should be authored in the EventMapping table.
ms.assetid: a79abd77-a6e5-4a1f-8a63-51644151404a
title: SelectionNoItems ControlEvent
ms.topic: article
ms.date: 05/31/2018
---

# SelectionNoItems ControlEvent

The [SelectionTree control](selectiontree-control.md) uses the SelectionNoItems event to delete obsolete item description text or to disable buttons that have become useless. This event should be authored in the [EventMapping table](eventmapping-table.md).

This ControlEvent requires the user interface to be run at the [*full UI*](f-gly.md) level. This event will not work with a [*reduced UI*](r-gly.md) or [*basic UI*](b-gly.md). For information, see [User Interface Levels](user-interface-levels.md).

This event can only affect controls that are located on the same dialog box as the SelectionTree control.

## Published By

[SelectionTree control](selectiontree-control.md) if the selection has no nodes.

## Argument

None.

## Action on Subscribers

Deletes obsolete item description text or disables obsolete buttons.

## Typical Use

May be used to disable the Next, Reset, and DiskCost buttons on the [Selection Dialog](selection-dialog.md) when a selection has no nodes and these buttons become useless.

 

 



