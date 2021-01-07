---
description: The DoAction ControlEvent notifies the installer to execute a custom action. This event can be published by a PushButton control, CheckBox control, or a SelectionTree control. This event should be authored into the ControlEvent table.
ms.assetid: 9a855330-8241-4912-84da-4fca43f1d240
title: DoAction ControlEvent
ms.topic: article
ms.date: 05/31/2018
---

# DoAction ControlEvent

The DoAction ControlEvent notifies the installer to execute a custom action. This event can be published by a [PushButton](pushbutton-control.md) control, [CheckBox](checkbox-control.md) control, or a [SelectionTree](selectiontree-control.md) control. This event should be authored into the [ControlEvent](controlevent-table.md) table.

Note that custom actions launched by a DoAction ControlEvent can send a message with the [**Message Method**](session-message.md), but cannot send a message with [**MsiProcessMessage**](/windows/desktop/api/Msiquery/nf-msiquery-msiprocessmessage). On systems prior to Windows Server 2003, custom actions launched by a DoAction ControlEvent cannot send messages with **MsiProcessMessage** or **Message Method**. For more information, see [Sending Messages to Windows Installer Using MsiProcessMessage](sending-messages-to-windows-installer-using-msiprocessmessage.md).

This ControlEvent requires the user interface to be run at the [*full UI*](f-gly.md) level. This event will not work with a [*reduced UI*](r-gly.md) or [*basic UI*](b-gly.md). For more information, see [User Interface Levels](user-interface-levels.md).

## Published By

This ControlEvent is published by the installer.

## Argument

A string, the name of the custom action to be executed.

## Action on Subscribers

This ControlEvent does not perform an action on subscribers.

## Typical Use

A [PushButton](pushbutton-control.md) control on a dialog box is tied to this event in the [ControlEvent](controlevent-table.md) table to invoke a custom action.

 

 



