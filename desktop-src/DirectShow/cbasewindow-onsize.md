---
description: The OnSize method handles WM\_SIZE messages.
ms.assetid: 21d867a4-4321-478a-9beb-5d3053569369
title: CBaseWindow.OnSize method (Winutil.h)
ms.topic: reference
ms.date: 4/26/2023
topic_type: 
- APIRef
- kbSyntax
api_name: 
- CBaseWindow.OnSize
api_type: 
- COM
api_location: 
- Strmbase.lib
- Strmbase.dll
- Strmbasd.lib
- Strmbasd.dll
ms.custom: UpdateFrequency5
---

# CBaseWindow.OnSize method

\[The feature associated with this page, [DirectShow](/windows/win32/directshow/directshow), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer) and [IMFMediaEngine](/windows/win32/api/mfmediaengine/nn-mfmediaengine-imfmediaengine). **MediaPlayer** and **IMFMediaEngine** have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** and **IMFMediaEngine** instead of **DirectShow**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

The `OnSize` method handles WM\_SIZE messages.

## Syntax


```C++
virtual BOOL OnSize(
   LONG Width,
   LONG Height
);
```



## Parameters

<dl> <dt>

*Width* 
</dt> <dd>

Width of the client area, in pixels.

</dd> <dt>

*Height* 
</dt> <dd>

Height of the client area, in pixels.

</dd> </dl>

## Return value

Returns **TRUE**.

## Remarks

This method stores the new width and height. To retrieve these values, call the [**CBaseWindow::GetWindowHeight**](cbasewindow-getwindowheight.md) and [**CBaseWindow::GetWindowWidth**](cbasewindow-getwindowwidth.md) methods.

## Requirements



| Requirement | Value |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Winutil.h (include Streams.h)</dt> </dl>                                                                                   |
| Library<br/> | <dl> <dt>Strmbase.lib (retail builds); </dt> <dt>Strmbasd.lib (debug builds)</dt> </dl> |



## See also

<dl> <dt>

[**CBaseWindow Class**](cbasewindow.md)
</dt> </dl>

 

 




