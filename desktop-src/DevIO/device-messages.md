---
description: Device messages are system messages that notify applications and other features of device change events.
ms.assetid: 4d1ace87-2d02-4ba4-9bcc-da86cf3481db
title: Device Messages
ms.topic: article
ms.date: 05/31/2018
---

# Device Messages

Device messages are system messages that notify applications and other features of device change events. These events occur whenever the system detects a change to the system hardware, such as when the user docks and undocks a laptop computer, or inserts or removes a device such as a PCMCIA card. Device events can occur while the system is running or when the system resumes operation after temporarily being suspended.

To help ensure that applications do not lose data when devices become unavailable, the system monitors the hardware configuration and sends device messages to the applications to notify them of the changes and to give them the opportunity to prepare for the changes before they occur.

For each device event, the system broadcasts a [**WM\_DEVICECHANGE**](wm-devicechange.md) message to all applications. In this message, the *wParam* parameter identifies the [device event type](device-event-types.md) and the *lParam* parameter is a pointer to event-specific data.

 

 



