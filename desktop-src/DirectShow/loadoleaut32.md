---
description: The LoadOLEAut32 function loads the Automation dynamic-link library (OleAut32.dll).
ms.assetid: af907341-1e2c-4c63-bf4e-d6c49b4f6a6e
title: LoadOLEAut32 function (Combase.h)
ms.topic: reference
ms.date: 4/26/2023
topic_type: 
- APIRef
- kbSyntax
api_name: 
- LoadOLEAut32
api_type: 
- LibDef
api_location: 
- Strmbase.lib
- Strmbase.dll
- Strmbasd.lib
- Strmbasd.dll
ms.custom: UpdateFrequency5
---

# LoadOLEAut32 function

\[The feature associated with this page, [DirectShow](/windows/win32/directshow/directshow), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer), [IMFMediaEngine](/windows/win32/api/mfmediaengine/nn-mfmediaengine-imfmediaengine), and [Audio/Video Capture in Media Foundation](/windows/win32/medfound/audio-video-capture-in-media-foundation). Those features have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer**, **IMFMediaEngine** and **Audio/Video Capture in Media Foundation** instead of **DirectShow**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

The **LoadOLEAut32** function loads the Automation dynamic-link library (OleAut32.dll).

## Syntax


```C++
HINSTANCE LoadOLEAut32(void);
```



## Parameters

This function has no parameters.

## Return value

Returns a handle to an Automation DLL instance.

## Remarks

When the [**CBaseObject**](cbaseobject.md) destructor destroys the object that loaded OleAut32.dll, it will unload the library if it is still loaded.

## Requirements



| Requirement | Value |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Combase.h (include Streams.h)</dt> </dl>                                                                                   |
| Library<br/> | <dl> <dt>Strmbase.lib (retail builds); </dt> <dt>Strmbasd.lib (debug builds)</dt> </dl> |



## See also

<dl> <dt>

[**COM Helper Functions**](com-helper-functions.md)
</dt> </dl>

 

 




