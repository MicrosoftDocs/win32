---
description: The SelectionTree control uses the SelectionBrowse event to spawn a Browse dialog box making it possible to modify the path of the highlighted item.
ms.assetid: 10a5af2e-3144-4b51-8295-294e56cdf801
title: SelectionBrowse ControlEvent
ms.topic: article
ms.date: 05/31/2018
---

# SelectionBrowse ControlEvent

The [SelectionTree control](selectiontree-control.md) uses the SelectionBrowse event to spawn a **Browse** dialog box making it possible to modify the path of the highlighted item.

This event should be published by a [PushButton Control](pushbutton-control.md) located on the same dialog box as the control subscribing to this event. The event should be authored in the [ControlEvent table](controlevent-table.md).

This ControlEvent requires the user interface to be run at the [*full UI*](f-gly.md) level. This event will not work with a [*reduced UI*](r-gly.md) or [*basic UI*](b-gly.md). For information, see [User Interface Levels](user-interface-levels.md).

Any controls that publish a SelectionBrowse event become disabled if a feature has been selected that is already installed, not configurable, or not selected for local installation. To be configurable, the feature must have a [public property](public-properties.md) entered in the Directory\_ field of the [Feature table](feature-table.md).

## Published By

[SelectionTree](selectiontree-control.md)

## Argument

The name of the dialog to be spawned.

## Action on Subscribers

None.

## Typical Use

A [PushButton](pushbutton-control.md) control on the same modal dialog box as the SelectionTree uses this event to trigger the **Browse** dialog box.

 

 



