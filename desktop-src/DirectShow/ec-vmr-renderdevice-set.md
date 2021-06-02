---
description: Sent when the VMR has selected its rendering mechanism.
ms.assetid: 815d1254-c6e3-4a6c-ba4a-bf3da7d35d1f
title: EC_VMR_RENDERDEVICE_SET (Dshow.h)
ms.topic: reference
ms.date: 05/31/2018
---

# EC\_VMR\_RENDERDEVICE\_SET

Sent when the VMR has selected its rendering mechanism.

## Parameters

<dl> <dt>

<span id="lParam1"></span><span id="lparam1"></span><span id="LPARAM1"></span>*lParam1*
</dt> <dd>

May be one of the following values:



| Value                        | Meaning                                                  |
|------------------------------|----------------------------------------------------------|
| VMR\_RENDER\_DEVICE\_OVERLAY | The VMR will render to the overlay surface (VMR-7 only). |
| VMR\_RENDER\_DEVICE\_VIDMEM  | The VMR will render to video memory.                     |
| VMR\_RENDER\_DEVICE\_SYSMEM  | The VMR will render to system memory (VMR-7 only).       |



 

</dd> <dt>

<span id="lParam2"></span><span id="lparam2"></span><span id="LPARAM2"></span>*lParam2*
</dt> <dd>

Not used.

</dd> </dl>

## Remarks

This event is sent by both the VMR-7 and the VMR-9 and it is forwarded to applications. Note that the VMR-9 only supports video memory render targets.

## Requirements



| Requirement | Value |
|-------------------|------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Dshow.h</dt> </dl> |



## See also

<dl> <dt>

[Event Notification Codes](event-notification-codes.md)
</dt> <dt>

[Event Notification in DirectShow](event-notification-in-directshow.md)
</dt> </dl>

 

 




