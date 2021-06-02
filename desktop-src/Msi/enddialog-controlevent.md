---
description: This event notifies the installer to remove a modal dialog box. In all cases the installer removes the present dialog box.
ms.assetid: 74a28696-6387-4d62-8955-4708ba5872bb
title: EndDialog ControlEvent
ms.topic: article
ms.date: 05/31/2018
---

# EndDialog ControlEvent

This event notifies the installer to remove a modal dialog box. In all cases the installer removes the present dialog box.

This event can be published by a [PushButton Control](pushbutton-control.md)or a [SelectionTree control](selectiontree-control.md). This event should be authored into the [ControlEvent table](controlevent-table.md).

This ControlEvent requires the user interface to be run at the [*full UI*](f-gly.md) level. This event will not work with a [*reduced UI*](r-gly.md) or [*basic UI*](b-gly.md). For information, see [User Interface Levels](user-interface-levels.md).

The following table lists the action of the event resulting from different arguments entered into the [ControlEvent table](controlevent-table.md).



| Argument | Action by the installer                                                                                                                                                             |
|----------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Exit     | The wizard sequence is closed and the control returns to the installer with the UserExit value. This argument cannot be used in a dialog box that is a child of another dialog box. |
| Retry    | The wizard sequence is closed and the control returns to the installer with the Suspend value. This argument cannot be used in a dialog box that is a child of another dialog box.  |
| Ignore   | The wizard sequence is closed and the control returns to the installer with the Finished value. This argument cannot be used in a dialog box that is a child of another dialog box. |
| Return   | The control returns to the parent of the present dialog box, or if there is no parent, the control returns to the installer with the Success value.                                 |



 

## Published By

This ControlEvent is published by the installer.

## Argument

On regular dialog boxes the Argument column of the [ControlEvent table](controlevent-table.md) can be "Return", "Exit", "Retry", or "Ignore".

On error dialog boxes the Argument column of the [ControlEvent table](controlevent-table.md) can be "ErrorOk", "ErrorCancel", "ErrorAbort", "ErrorRetry", "ErrorIgnore", "ErrorYes", or "ErrorNo".

## Action on Subscribers

None.

## Typical Use

A [PushButton](pushbutton-control.md) control on a modal dialog is tied to this event in the [ControlEvent](controlevent-table.md) table to close a dialog box.

 

 



