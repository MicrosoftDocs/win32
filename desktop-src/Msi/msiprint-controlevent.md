---
description: This event is published by the ScrollableText Control to enable the user to print the contents of that control.
ms.assetid: 8cb91b21-f6db-4f49-827d-1ec739ff4f45
title: MsiPrint ControlEvent
ms.topic: article
ms.date: 05/31/2018
---

# MsiPrint ControlEvent

This event is published by the [ScrollableText Control](scrollabletext-control.md) to enable the user to print the contents of that control.

**[Windows Installer 4.5 or earlier](not-supported-in-windows-installer-4-5.md):** Not supported. This ControlEvent is available beginning with Windows Installer 5.0.

This event should be subscribed to by a [PushButton Control](pushbutton-control.md) located on the same dialog box as the [ScrollableText Control](scrollabletext-control.md). TheMsiPrint ControlEvent should be authored in the [ControlEvent table](controlevent-table.md).

## Published By

[ScrollableText](scrollabletext-control.md)

## Argument

This ControlEvent does not use an argument.

## Action on Subscribers

This ControlEvent does not perform an action on subscribers.

## Typical Use

A [PushButton](pushbutton-control.md) control on the same dialog box as the [ScrollableText Control](scrollabletext-control.md) can be used to display a modal dialog box enabling the user to print the contents of the ScrollableText Control.

 

 



