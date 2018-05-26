---
Description: The system broadcasts a set of default device change events to all applications and services.
ms.assetid: 672ad753-210b-41c3-b8c7-e041ce7b1671
title: Device Notifications
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Device Notifications

The system broadcasts a set of default device change events to all applications and services. You do not need to register to receive these default events. See the Remarks section in [**RegisterDeviceNotification**](/windows/win32/Winuser/nf-winuser-registerdevicenotificationa?branch=master) for details. To specify other events your application or service should receive, use the **RegisterDeviceNotification** function.

When an application or service calls [**RegisterDeviceNotification**](/windows/win32/Winuser/nf-winuser-registerdevicenotificationa?branch=master), it also specifies the window that will receive the notification events. Services can specify a service status handle instead of a window handle. If a service specifies its service status handle, its service control handler will receive the notification events. For more information, see [**HandlerEx**](https://msdn.microsoft.com/library/windows/desktop/ms683241).

Be sure to handle Plug and Play device events as quickly as possible. Otherwise, the system may become unresponsive. If your event handler is to perform an operation that may block execution (such as I/O), it is best to start another thread to perform the operation asynchronously.

Device notification handles returned by [**RegisterDeviceNotification**](/windows/win32/Winuser/nf-winuser-registerdevicenotificationa?branch=master) must be closed by calling the [**UnregisterDeviceNotification**](/windows/win32/Winuser/nf-winuser-unregisterdevicenotification?branch=master) function when they are no longer needed.

## Related topics

<dl> <dt>

[Registering for Device Notification](registering-for-device-notification.md)
</dt> </dl>

 

 



