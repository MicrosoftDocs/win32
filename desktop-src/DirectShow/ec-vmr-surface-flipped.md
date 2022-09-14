---
description: Sent when the VMR-7's allocator presenter has called the DirectDraw Flip method on the surface being presented. This allows the VMR to keep its DirectXVA table of surfaces synchronized with DirectDraw's flipping chain.
ms.assetid: e298857b-0579-48b4-add0-72320bc52d63
title: EC_VMR_SURFACE_FLIPPED (Dshow.h)
ms.topic: reference
ms.date: 05/31/2018
---

# EC\_VMR\_SURFACE\_FLIPPED

Sent when the VMR-7's allocator presenter has called the DirectDraw Flip method on the surface being presented. This allows the VMR to keep its DirectXVA table of surfaces synchronized with DirectDraw's flipping chain.

## Parameters

<dl> <dt>

<span id="lParam1"></span><span id="lparam1"></span><span id="LPARAM1"></span>*lParam1*
</dt> <dd>

(**HRESULT**) Status code returned from the DirectDraw Flip method.

</dd> <dt>

<span id="lParam2"></span><span id="lparam2"></span><span id="LPARAM2"></span>*lParam2*
</dt> <dd>

Not used.

</dd> </dl>

## Remarks

Custom allocator-presenters for the VMR-7 should send this event. This event is not forwarded to applications and it is not used with allocator-presenters for the VMR-9.

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

 

 




