---
description: To determine the device event type when processing a WM\_DEVICECHANGE message, examine the wParam parameter.
ms.assetid: 17078548-879d-4a11-a268-27d1f30180ab
title: Device Event Types
ms.topic: article
ms.date: 05/31/2018
---

# Device Event Types

To determine the device event type when processing a [**WM\_DEVICECHANGE**](wm-devicechange.md) message, examine the *wParam* parameter. The value of *wParam* determines the meaning of the event-specific data in the *lParam* parameter. In general, the event-specific data identifies the device and provides additional detail about the event. The format of this data depends on the device type, but the first few bytes always have the same format as the [**DEV\_BROADCAST\_HDR**](/windows/desktop/api/Dbt/ns-dbt-dev_broadcast_hdr) structure. To determine the format of the data, check the **dbch\_devicetype** member.

The system broadcasts a device event of type [DBT\_DEVICEARRIVAL](dbt-devicearrival.md) (that is, a [**WM\_DEVICECHANGE**](wm-devicechange.md) message with *wParam* set to DBT\_DEVICEARRIVAL) whenever a device has been inserted and is available for use. Applications typically check the device type and begin using the device immediately if it is appropriate.

The system broadcasts a [DBT\_DEVICEQUERYREMOVE](dbt-devicequeryremove.md) device event to request permission to remove a device. To determine whether it needs the device, an application can display a dialog box to prompt the user for instructions. If an application determines that it needs the device, it can deny this request and cancel the removal by returning BROADCAST\_QUERY\_DENY. If the application does not need the device, it must return **TRUE**. The system immediately sends a [DBT\_DEVICEQUERYREMOVEFAILED](dbt-devicequeryremovefailed.md) message if any application or driver canceled a previous request to remove a device.

The system broadcasts a [DBT\_DEVICEREMOVEPENDING](dbt-deviceremovepending.md) device event as a last warning before a device is removed. At this point, the application cannot cancel the removal, so if it is using the device it must prepare for its removal to prevent loss of data. This is especially important when a network connection is being removed. The application must determine whether any of its open files or pipes are on that connection. It can do this by comparing the network resource identifier in the event-specific data of the message with the resource identifiers previously obtained for the files and pipes. The system broadcasts a [DBT\_DEVICEREMOVECOMPLETE](dbt-deviceremovecomplete.md) device event when a device has been removed and is no longer available.

The system broadcasts a [DBT\_QUERYCHANGECONFIG](dbt-querychangeconfig.md) device event to request permission to change the current configuration (dock or undock). Any application can return BROADCAST\_QUERY\_DENY to deny the request and cancel the change. If an application denies the request, the system sends a [DBT\_CONFIGCHANGECANCELED](dbt-configchangecanceled.md) message. If the current configuration has changed, due to a dock or undock, the system sends a [DBT\_CONFIGCHANGED](dbt-configchanged.md) message.

The system broadcasts a [DBT\_DEVICETYPESPECIFIC](dbt-devicetypespecific.md) device event whenever a device-specific event occurs.

Drivers can create their own custom event types. Custom events are sent only to application that have registered for device-event notification on a particular device, and can only be initiated by kernel-mode drivers. For more information, see [DBT\_CUSTOMEVENT](dbt-customevent.md).

 

 



