---
description: The DoGetWindowStyle method retrieves the current normal or extended window styles.
ms.assetid: 1a854896-4bcb-49d0-92e4-40d1923712f9
title: CBaseControlWindow.DoGetWindowStyle method (Ctlutil.h)
ms.topic: reference
ms.date: 4/26/2023
topic_type: 
- APIRef
- kbSyntax
api_name: 
- CBaseControlWindow.DoGetWindowStyle
api_type: 
- COM
api_location: 
- Strmbase.lib
- Strmbase.dll
- Strmbasd.lib
- Strmbasd.dll
ms.custom: UpdateFrequency5
---

# CBaseControlWindow.DoGetWindowStyle method

\[The feature associated with this page, [DirectShow](/windows/win32/directshow/directshow), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer), [IMFMediaEngine](/windows/win32/api/mfmediaengine/nn-mfmediaengine-imfmediaengine), and [Audio/Video Capture in Media Foundation](/windows/win32/medfound/audio-video-capture-in-media-foundation). Those features have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer**, **IMFMediaEngine** and **Audio/Video Capture in Media Foundation** instead of **DirectShow**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

The `DoGetWindowStyle` method retrieves the current normal or extended window styles.

## Syntax


```C++
HRESULT DoGetWindowStyle(
   long *pStyle,
   long WindowLong
);
```



## Parameters

<dl> <dt>

*pStyle* 
</dt> <dd>

Pointer to a variable that receives the style information.

</dd> <dt>

*WindowLong* 
</dt> <dd>

Value specifying which styles to retrieve. Must be one of the following:



| Label | Value |
|--------------|--------------------------------------|
| GWL\_STYLE   | Retrieve the window styles.          |
| GWL\_EXSTYLE | Retrieve the extended window styles. |



 

</dd> </dl>

## Return value

Returns an **HRESULT** value.

## Remarks

This member function calls the Win32 **GetWindowLong** function to retrieve the window style. It is called by the [**CBaseControlWindow::get\_WindowStyle**](cbasecontrolwindow-get-windowstyle.md) and [**CBaseControlWindow::get\_WindowStyleEx**](cbasecontrolwindow-get-windowstyleex.md) member functions.

## Requirements



| Requirement | Value |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Ctlutil.h (include Streams.h)</dt> </dl>                                                                                   |
| Library<br/> | <dl> <dt>Strmbase.lib (retail builds); </dt> <dt>Strmbasd.lib (debug builds)</dt> </dl> |



## See also

<dl> <dt>

[**CBaseControlWindow Class**](cbasecontrolwindow.md)
</dt> </dl>

 

 




