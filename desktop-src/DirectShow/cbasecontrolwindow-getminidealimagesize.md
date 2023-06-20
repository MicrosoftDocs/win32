---
description: The GetMinIdealImageSize method retrieves the minimum ideal image size.
ms.assetid: f2f2d10e-ee2c-4f8a-91ce-576319038e0d
title: CBaseControlWindow.GetMinIdealImageSize method (Ctlutil.h)
ms.topic: reference
ms.date: 4/26/2023
topic_type: 
- APIRef
- kbSyntax
api_name: 
- CBaseControlWindow.GetMinIdealImageSize
api_type: 
- COM
api_location: 
- Strmbase.lib
- Strmbase.dll
- Strmbasd.lib
- Strmbasd.dll
ms.custom: UpdateFrequency5
---

# CBaseControlWindow.GetMinIdealImageSize method

\[The feature associated with this page, [DirectShow](/windows/win32/directshow/directshow), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer) and [IMFMediaEngine](/windows/win32/api/mfmediaengine/nn-mfmediaengine-imfmediaengine). **MediaPlayer** and **IMFMediaEngine** have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** and **IMFMediaEngine** instead of **DirectShow**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

The `GetMinIdealImageSize` method retrieves the minimum ideal image size.

## Syntax


```C++
HRESULT GetMinIdealImageSize(
   long *pWidth,
   long *pHeight
);
```



## Parameters

<dl> <dt>

*pWidth* 
</dt> <dd>

Pointer to the minimum ideal width, in pixels.

</dd> <dt>

*pHeight* 
</dt> <dd>

Pointer to the minimum ideal height, in pixels.

</dd> </dl>

## Return value

Returns an **HRESULT** value.

## Remarks

Various renderers have performance restrictions on the size of images they can display. Although they should still function properly when requested to display images larger than the specified maximum, renderers can nominate the minimum and maximum ideal sizes through the [**IVideoWindow**](/windows/desktop/api/Control/nn-control-ivideowindow) interface. This interface can be called only when the filter graph is paused or running, because it is not until then that resources are allocated and the renderer can recognize its restrictions. If no restrictions exist, the renderer fills in the *pWidth* and *pHeight* parameters with the native video dimensions and returns S\_FALSE. If restrictions do exist, the restricted width and height are entered, and the member function returns S\_OK.

The dimensions apply to the size of the destination video and not to the overall window size. So, when calculating the size of the window to set, account for the current window styles (for example, WS\_CAPTION and WS\_BORDER).

## Requirements



| Requirement | Value |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Ctlutil.h (include Streams.h)</dt> </dl>                                                                                   |
| Library<br/> | <dl> <dt>Strmbase.lib (retail builds); </dt> <dt>Strmbasd.lib (debug builds)</dt> </dl> |



## See also

<dl> <dt>

[**CBaseControlWindow Class**](cbasecontrolwindow.md)
</dt> </dl>

 

 




