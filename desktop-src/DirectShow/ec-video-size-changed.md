---
description: The native video size has changed.
ms.assetid: 276f37b3-f981-4a01-bb37-1ee77248668f
title: EC_VIDEO_SIZE_CHANGED (Dshow.h)
ms.topic: reference
ms.date: 05/31/2018
---

# EC\_VIDEO\_SIZE\_CHANGED

The native video size has changed.

## Parameters

<dl> <dt>

<span id="lParam1"></span><span id="lparam1"></span><span id="LPARAM1"></span>*lParam1*
</dt> <dd>

(**DWORD**) Low-order WORD specifies the new width, in pixels; high-order WORD specifies the new height, in pixels.

</dd> <dt>

<span id="lParam2"></span><span id="lparam2"></span><span id="LPARAM2"></span>*lParam2*
</dt> <dd>

Zero.

</dd> </dl>

## Default Action

None.

## Remarks

Video renderers may send this event if they detect a change in the native video size.

The [Video Mixing Renderer 7](video-mixing-renderer-filter-7.md) (VMR-7) and the [Video Mixing Renderer 9](video-mixing-renderer-filter-9.md) (VMR-9) send this event in windowed mode, but not in windowless mode or renderless mode. For more information about windowed mode in the VMR, see [Video Rendering](video-rendering.md).

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

 

 




