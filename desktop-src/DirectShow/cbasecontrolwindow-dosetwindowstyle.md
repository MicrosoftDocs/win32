---
description: The DoSetWindowStyle method changes the typical or extended window styles.
ms.assetid: 4a9a97fb-b527-44ce-af8c-e5ea832ed4c4
title: CBaseControlWindow.DoSetWindowStyle method (Ctlutil.h)
ms.topic: reference
ms.date: 4/26/2023
topic_type: 
- APIRef
- kbSyntax
api_name: 
- CBaseControlWindow.DoSetWindowStyle
api_type: 
- COM
api_location: 
- Strmbase.lib
- Strmbase.dll
- Strmbasd.lib
- Strmbasd.dll
ms.custom: UpdateFrequency5
---

# CBaseControlWindow.DoSetWindowStyle method

\[The feature associated with this page, [DirectShow](/windows/win32/directshow/directshow), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer), [IMFMediaEngine](/windows/win32/api/mfmediaengine/nn-mfmediaengine-imfmediaengine), and [Audio/Video Capture in Media Foundation](windows/win32/medfound/audio-video-capture-in-media-foundation). Those features have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer**, **IMFMediaEngine** and **Audio/Video Capture in Media Foundation** instead of **DirectShow**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

The `DoSetWindowStyle` method changes the typical or extended window styles.

## Syntax


```C++
HRESULT DoSetWindowStyle(
   long Style,
   long WindowLong
);
```



## Parameters

<dl> <dt>

*Style* 
</dt> <dd>

Appropriate window styles.

</dd> <dt>

*WindowLong* 
</dt> <dd>

Value specifying which styles to set. Must be one of the following:



| Label | Value |
|--------------|--------------------------------------|
| GWL\_STYLE   | Retrieve the window styles.          |
| GWL\_EXSTYLE | Retrieve the extended window styles. |



 

</dd> </dl>

## Return value

Returns an **HRESULT** value.

## Remarks

This member function calls the Win32 **SetWindowLong** function to set the window style, and then redisplays the window in the current position. This member function is called by the [**CBaseControlWindow::put\_WindowStyle**](cbasecontrolwindow-put-windowstyle.md) and [**CBaseControlWindow::put\_WindowStyleEx**](cbasecontrolwindow-put-windowstyleex.md) member functions.

## Requirements



| Requirement | Value |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Ctlutil.h (include Streams.h)</dt> </dl>                                                                                   |
| Library<br/> | <dl> <dt>Strmbase.lib (retail builds); </dt> <dt>Strmbasd.lib (debug builds)</dt> </dl> |



## See also

<dl> <dt>

[**CBaseControlWindow Class**](cbasecontrolwindow.md)
</dt> </dl>

 

 




