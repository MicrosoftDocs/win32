---
description: The put\_Width method sets the window width.
ms.assetid: eb5ad1c2-ba39-4c06-84d2-6708dc8796d8
title: CBaseControlWindow.put_Width method (Ctlutil.h)
ms.topic: reference
ms.date: 4/26/2023
topic_type: 
- APIRef
- kbSyntax
api_name: 
- CBaseControlWindow.put_Width
api_type: 
- COM
api_location: 
- Strmbase.lib
- Strmbase.dll
- Strmbasd.lib
- Strmbasd.dll
ms.custom: UpdateFrequency5
---

# CBaseControlWindow.put\_Width method

\[The feature associated with this page, [DirectShow](/windows/win32/directshow/directshow), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer), [IMFMediaEngine](/windows/win32/api/mfmediaengine/nn-mfmediaengine-imfmediaengine), and [Audio/Video Capture in Media Foundation](/windows/win32/medfound/audio-video-capture-in-media-foundation). Those features have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer**, **IMFMediaEngine** and **Audio/Video Capture in Media Foundation** instead of **DirectShow**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

The `put_Width` method sets the window width.

## Syntax


```C++
HRESULT put_Width(
   long Width
);
```



## Parameters

<dl> <dt>

*Width* 
</dt> <dd>

New window width, in pixels.

</dd> </dl>

## Return value

Returns an **HRESULT** value.

## Remarks

The window has a position on the desktop. This is expressed in pixels by four coordinates (left, top, right, and bottom). Interfaces that are automated by OLE typically express this position through left, top, width, and height; this is the convention used in DirectShow. All coordinates are expressed in pixels and changing any coordinate will update the window immediately.

Setting the left or top coordinates moves the window left or up respectively; these coordinates have no effect on the width and height of the window. Likewise, setting the width and height does not affect the left and top coordinates.

## Requirements



| Requirement | Value |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Ctlutil.h (include Streams.h)</dt> </dl>                                                                                   |
| Library<br/> | <dl> <dt>Strmbase.lib (retail builds); </dt> <dt>Strmbasd.lib (debug builds)</dt> </dl> |



## See also

<dl> <dt>

[**CBaseControlWindow Class**](cbasecontrolwindow.md)
</dt> </dl>

 

 




