---
description: The video renderer is switching out of full-screen mode.
ms.assetid: f720a9b6-930a-4ed7-9798-1c72fa7a11ff
title: EC_FULLSCREEN_LOST (Dshow.h)
ms.topic: reference
ms.date: 05/31/2018
---

# EC\_FULLSCREEN\_LOST

The video renderer is switching out of full-screen mode.

## Parameters

<dl> <dt>

<span id="lParam1"></span><span id="lparam1"></span><span id="LPARAM1"></span>*lParam1*
</dt> <dd>

Zero.

</dd> <dt>

<span id="lParam2"></span><span id="lparam2"></span><span id="LPARAM2"></span>*lParam2*
</dt> <dd>

(**IUnknown**\*) Pointer to the video renderer's [**IBaseFilter**](/windows/desktop/api/Strmif/nn-strmif-ibasefilter) interface, or **NULL**.

</dd> </dl>

## Default Action

None.

## Remarks

When the [Full Screen Renderer](full-screen-renderer-filter.md) loses activation, it sends this event. When another video renderer switches out of full-screen mode, the filter graph manager sends this event, in response to an [**EC\_ACTIVATE**](ec-activate.md) event from the renderer.

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

 

 




