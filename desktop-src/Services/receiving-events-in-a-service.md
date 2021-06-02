---
description: A service that is a console application can register a console control handler to receive notification when a user logs off.
ms.assetid: 86ace8b8-c1cb-4646-bc92-86bd578a82c5
title: Receiving Events in a Service
ms.topic: article
ms.date: 05/31/2018
---

# Receiving Events in a Service

A service that is a console application can register a [console control handler](/windows/console/console-control-handlers) to receive notification when a user logs off. However, there is no console event sent when an interactive user logs on. For information on receiving notification when a user logs on, see [Creating a Winlogon Notification Package](/windows/desktop/SecAuthN/creating-a-winlogon-notification-package).

The system broadcasts device change events to all services. These events can be received by a service in a window procedure or in its service control handler. To specify which events your service should receive, use the [**RegisterDeviceNotification**](/windows/desktop/api/winuser/nf-winuser-registerdevicenotificationa) function.

Be sure to handle Plug and Play device events as quickly as possible. Otherwise, the system may become unresponsive. If your event handler is to perform an operation that may block execution (such as I/O), it is best to start another thread to perform the operation asynchronously.

When a service calls [**RegisterDeviceNotification**](/windows/desktop/api/winuser/nf-winuser-registerdevicenotificationa), the service also specifies either a window handle or a service status handle. If a service specifies a window handle, the window procedure receives the notification events. If a service specifies its service status handle, its service control handler receives the notification events. For more information, see [**HandlerEx**](/windows/desktop/api/WinSvc/nc-winsvc-lphandler_function_ex).

Device notification handles returned by [**RegisterDeviceNotification**](/windows/desktop/api/winuser/nf-winuser-registerdevicenotificationa) must be closed by calling the [**UnregisterDeviceNotification**](/windows/desktop/api/winuser/nf-winuser-unregisterdevicenotification) function when they are no longer needed.

 

 
