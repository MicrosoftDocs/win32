---
description: A Plug and Play device was removed or became available again.
ms.assetid: 0640ba96-22a5-4b82-bd9f-117b67dee311
title: EC_DEVICE_LOST (Dshow.h)
ms.topic: reference
ms.date: 05/31/2018
---

# EC\_DEVICE\_LOST

A Plug and Play device was removed or became available again.

## Parameters

<dl> <dt>

<span id="lParam1"></span><span id="lparam1"></span><span id="LPARAM1"></span>*lParam1*
</dt> <dd>

(**IUnknown**\*) Pointer to the **IUnknown** interface of the filter that represents the device.

</dd> <dt>

<span id="lParam2"></span><span id="lparam2"></span><span id="LPARAM2"></span>*lParam2*
</dt> <dd>

Zero if the device was removed, or 1 if the device is available again.

</dd> </dl>

## Default Action

None.

## Remarks

When the device becomes available again, the previous state of the device filter is no longer valid. The application must rebuild the graph in order to use the device.

## Requirements



| Requirement | Value |
|-------------------|------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Dshow.h</dt> </dl> |



## See also

<dl> <dt>

[Device Removal Notification](device-removal-notification.md)
</dt> <dt>

[Event Notification Codes](event-notification-codes.md)
</dt> <dt>

[Event Notification in DirectShow](event-notification-in-directshow.md)
</dt> </dl>

 

 




