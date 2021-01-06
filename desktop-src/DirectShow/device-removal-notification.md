---
description: Device Removal Notification
ms.assetid: 0b96231a-f990-4c1c-8d00-cafeb3985ab3
title: Device Removal Notification
ms.topic: article
ms.date: 05/31/2018
---

# Device Removal Notification

If the user removes a Plug and Play device that the graph was using, the filter graph manager posts an [**EC\_DEVICE\_LOST**](ec-device-lost.md) event. If the device becomes available again, the filter graph manager posts another **EC\_DEVICE\_LOST** event. However, the previous state of the capture filter is no longer valid. The application must rebuild the graph to use the device.

DirectShow does not send any event when a new device is plugged in. To learn when a new device is available, the application can monitor WM\_DEVICECHANGE window messages. For more information, see "Device Management" in the Platform SDK documentation.

## Related topics

<dl> <dt>

[Event Notification in DirectShow](event-notification-in-directshow.md)
</dt> </dl>

 

 



