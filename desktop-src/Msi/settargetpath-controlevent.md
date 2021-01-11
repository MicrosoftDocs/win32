---
description: The SetTargetPath event notifies the installer to check and set the selected path. If the path is not valid to be written to, then the installer blocks further ControlEvents associated with the control.
ms.assetid: 5649da99-1541-47ab-9d2e-b33a705998ec
title: SetTargetPath ControlEvent
ms.topic: article
ms.date: 05/31/2018
---

# SetTargetPath ControlEvent

The SetTargetPath event notifies the installer to check and set the selected path. If the path is not valid to be written to, then the installer blocks further ControlEvents associated with the control.

This event can be published by a [PushButton Control](pushbutton-control.md)or a [SelectionTree control](selectiontree-control.md). This event should be authored into the [ControlEvent table](controlevent-table.md).

This ControlEvent requires the user interface to be run at the [*full UI*](f-gly.md) level. This event will not work with a [*reduced UI*](r-gly.md) or [*basic UI*](b-gly.md). For information, see [User Interface Levels](user-interface-levels.md).

## Published By

This ControlEvent is published by the installer.

## Argument

The name of the property containing the path. If the property is indirected, then the property name is enclosed in square brackets.

## Action on Subscribers

None.

## Typical Use

A [PushButton](pushbutton-control.md) control on a browse dialog is tied to this event in the [ControlEvent](controlevent-table.md) table to check the selected path before returning to the selection dialog.

## Remarks

Do not attempt to configure the target path if the components using those paths are already installed for the current user or for a different user. Check the [**ProductState**](productstate.md) property before publishing the SetTargetPath ControlEvent to determine if the product containing the component is installed.

 

 



