---
description: The display mode has changed.
ms.assetid: 1f5b066b-6d5d-44bb-851a-424b2bd389c0
title: EC_DISPLAY_CHANGED (Dshow.h)
ms.topic: reference
ms.date: 05/31/2018
---

# EC\_DISPLAY\_CHANGED

The display mode has changed.

## Parameters

<dl> <dt>

<span id="lParam1"></span><span id="lparam1"></span><span id="LPARAM1"></span>*lParam1*
</dt> <dd>

(**IUnknown**\*) Pointer to an array of [**IPin**](/windows/desktop/api/Strmif/nn-strmif-ipin) interfaces for the video renderer's input pins. If *lParam2* is zero, this parameter can be **NULL**.

</dd> <dt>

<span id="lParam2"></span><span id="lparam2"></span><span id="LPARAM2"></span>*lParam2*
</dt> <dd>

If *lParam2* is zero, *lParam1* contains a single **IPin** pointer or equals **NULL**. If *lParam2* is greater than zero, *lParam1* contains an array of **IPin** pointers, and the number of elements in the array is given by *lParam2*.

</dd> </dl>

## Default Action

The filter graph manager temporarily stops the graph, and then disconnects and reconnects the video renderer. It does not pass the event to the application.

## Remarks

Video renderers can send this event in response to a [**WM\_DISPLAYCHANGE**](/windows/desktop/gdi/wm-displaychange) message. The **WM\_DISPLAYCHANGE** message indicates that the user has changed the display resolution.

During pin connection, most video renderers pick a format based on the current display mode. If the display mode changes, the video renderer might need to choose another format. By sending this message, the renderer signals to the filter graph manager that it needs to be reconnected. During the reconnection, the renderer can select a new format. If the reconnection fails, the filter graph manager sends an [**EC\_ERRORABORT**](ec-errorabort.md) event to the application.

### Enhanced Video Renderer

A custom presenter for the [**Enhanced Video Renderer**](enhanced-video-renderer-filter.md) (EVR) should send this event to the EVR if the presenter's Direct3D device changes. Set *lParam1* and *lParam2* to zero; the EVR ignores the event parameters.

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

 

