---
description: The ValidateProductID event sets the ProductID property to the full Product ID. If the validation is unsuccessful, then this event puts up an error message and modal dialog box for a user entry of the Product ID.
ms.assetid: 44002cae-154a-4938-a15c-456c293e94fb
title: ValidateProductID ControlEvent
ms.topic: article
ms.date: 05/31/2018
---

# ValidateProductID ControlEvent

The ValidateProductID event sets the [**ProductID**](productid.md) property to the full Product ID. If the validation is unsuccessful, then this event puts up an error message and modal dialog box for a user entry of the Product ID.

This event can be published by a [PushButton Control](pushbutton-control.md)or a [SelectionTree control](selectiontree-control.md). This event should be authored into the [ControlEvent table](controlevent-table.md).

This ControlEvent requires the user interface to be run at the [*full UI*](f-gly.md) level. This event will not work with a [*reduced UI*](r-gly.md) or [*basic UI*](b-gly.md). For information, see [User Interface Levels](user-interface-levels.md).

## Published By

This ControlEvent is published by the installer.

## Argument

None.

## Action on Subscribers

None.

## Typical Use

A [PushButton](pushbutton-control.md) control on a modal dialog box is tied to this event and is used to check the user's entry of the Product ID. If the user's entry is valid, then the next dialog box will open.

 

 



