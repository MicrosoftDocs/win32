---
description: The DoneWithWindow method destroys the window.
ms.assetid: 03c97884-7d91-4b59-b867-dda231d2a184
title: CBaseWindow.DoneWithWindow method (Winutil.h)
ms.topic: reference
ms.date: 4/26/2023
topic_type: 
- APIRef
- kbSyntax
api_name: 
- CBaseWindow.DoneWithWindow
api_type: 
- COM
api_location: 
- Strmbase.lib
- Strmbase.dll
- Strmbasd.lib
- Strmbasd.dll
ms.custom: UpdateFrequency5
---

# CBaseWindow.DoneWithWindow method

\[The feature associated with this page, [DirectShow](/windows/win32/directshow/directshow), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer), [IMFMediaEngine](/windows/win32/api/mfmediaengine/nn-mfmediaengine-imfmediaengine), and [Audio/Video Capture in Media Foundation](/windows/win32/medfound/audio-video-capture-in-media-foundation). Those features have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer**, **IMFMediaEngine** and **Audio/Video Capture in Media Foundation** instead of **DirectShow**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

The `DoneWithWindow` method destroys the window.

## Syntax


```C++
virtual HRESULT DoneWithWindow();
```



## Parameters

This method has no parameters.

## Return value

Returns S\_OK.

## Remarks

Call this method from the derived object's destructor method.

If this method is called from the same thread that created the window, the method performs the following actions:

-   Calls the [**CBaseWindow::InactivateWindow**](cbasewindow-inactivatewindow.md) method, which deactivates the window.
-   Calls the [**CBaseWindow::UninitialiseWindow**](cbasewindow-uninitialisewindow.md) method, which releases resources used by the window.
-   Destroys the window.

If the thread calling `DoneWithWindow` is not the thread that created the window, the method sends a private "destroy" message to the window. When the window receives this message, it calls `DoneWithWindow` on itself. (If [**CBaseWindow::m\_bDoPostToDestroy**](cbasewindow-m-bdoposttodestroy.md) is **TRUE**, the window posts the message.)

## Requirements



| Requirement | Value |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Winutil.h (include Streams.h)</dt> </dl>                                                                                   |
| Library<br/> | <dl> <dt>Strmbase.lib (retail builds); </dt> <dt>Strmbasd.lib (debug builds)</dt> </dl> |



## See also

<dl> <dt>

[**CBaseWindow Class**](cbasewindow.md)
</dt> </dl>

 

 




