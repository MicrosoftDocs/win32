---
description: The put\_WindowStyleEx method sets the extended window styles.
ms.assetid: 3c5928fe-7cd3-4e1c-9a3f-fa6d7a73dbc3
title: CBaseControlWindow.put_WindowStyleEx method (Ctlutil.h)
ms.topic: reference
ms.date: 4/26/2023
topic_type: 
- APIRef
- kbSyntax
api_name: 
- CBaseControlWindow.put_WindowStyleEx
api_type: 
- COM
api_location: 
- Strmbase.lib
- Strmbase.dll
- Strmbasd.lib
- Strmbasd.dll
ms.custom: UpdateFrequency5
---

# CBaseControlWindow.put\_WindowStyleEx method

\[The feature associated with this page, [DirectShow](/windows/win32/directshow/directshow), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer), [IMFMediaEngine](/windows/win32/api/mfmediaengine/nn-mfmediaengine-imfmediaengine), and [Audio/Video Capture in Media Foundation](/windows/win32/medfound/audio-video-capture-in-media-foundation). Those features have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer**, **IMFMediaEngine** and **Audio/Video Capture in Media Foundation** instead of **DirectShow**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

The `put_WindowStyleEx` method sets the extended window styles.

## Syntax


```C++
HRESULT put_WindowStyleEx(
  [in] long WindowStyleEx
);
```



## Parameters

<dl> <dt>

*WindowStyleEx* \[in\]
</dt> <dd>

Value that specifies the style of the control window.

</dd> </dl>

## Return value

Returns NOERROR.

## Remarks

This method uses extended window styles. For a complete list of extended window styles, see the Microsoft Win32 **CreateWindowEx** function. To change the window style, retrieve the current window style, and then add or remove the necessary bit fields.

Do not use the following window styles because they are not validated.

-   WS\_DISABLED
-   WS\_HSCROLL
-   WS\_ICONIC
-   WS\_MAXIMIZE
-   WS\_MINIMIZE
-   WS\_VSCROLL

With some exceptions (noted here), the acceptable flags are the same as those allowed by the Win32 **CreateWindow** function.

## Requirements



| Requirement | Value |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Ctlutil.h (include Streams.h)</dt> </dl>                                                                                   |
| Library<br/> | <dl> <dt>Strmbase.lib (retail builds); </dt> <dt>Strmbasd.lib (debug builds)</dt> </dl> |



## See also

<dl> <dt>

[**CBaseControlWindow Class**](cbasecontrolwindow.md)
</dt> </dl>

 

 




