---
description: The ActivateWindow method sizes the window according to the requirements of the derived class.
ms.assetid: 39e23080-e4ae-46d5-bb3f-306c92bbfe14
title: CBaseWindow.ActivateWindow method (Winutil.h)
ms.topic: reference
ms.date: 4/26/2023
topic_type: 
- APIRef
- kbSyntax
api_name: 
- CBaseWindow.ActivateWindow
api_type: 
- COM
api_location: 
- Strmbase.lib
- Strmbase.dll
- Strmbasd.lib
- Strmbasd.dll
ms.custom: UpdateFrequency5
---

# CBaseWindow.ActivateWindow method

\[The feature associated with this page, [DirectShow](/windows/win32/directshow/directshow), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer), [IMFMediaEngine](/windows/win32/api/mfmediaengine/nn-mfmediaengine-imfmediaengine), and [Audio/Video Capture in Media Foundation](/windows/win32/medfound/audio-video-capture-in-media-foundation). Those features have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer**, **IMFMediaEngine** and **Audio/Video Capture in Media Foundation** instead of **DirectShow**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

The `ActivateWindow` method sizes the window according to the requirements of the derived class.

## Syntax


```C++
virtual HRESULT ActivateWindow();
```



## Parameters

This method has no parameters.

## Return value

Returns one of the **HRESULT** values shown in the following table.



| Return code                                                                             | Description                              |
|-----------------------------------------------------------------------------------------|------------------------------------------|
| <dl> <dt>**S\_FALSE**</dt> </dl> | Window was already activated.<br/> |
| <dl> <dt>**S\_OK**</dt> </dl>    | Success.<br/>                      |



 

## Remarks

This methods calls the [**CBaseWindow::GetDefaultRect**](cbasewindow-getdefaultrect.md) method to determine the window size. The derived class should override **GetDefaultRect** to return the size of the images that will be displayed.

If the window is already active, calling `ActivateWindow` moves the window to the top of the Z order, but does not resize the window. The same is true if the window has a parent.

## Requirements



| Requirement | Value |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Winutil.h (include Streams.h)</dt> </dl>                                                                                   |
| Library<br/> | <dl> <dt>Strmbase.lib (retail builds); </dt> <dt>Strmbasd.lib (debug builds)</dt> </dl> |



## See also

<dl> <dt>

[**CBaseWindow Class**](cbasewindow.md)
</dt> </dl>

 

 




