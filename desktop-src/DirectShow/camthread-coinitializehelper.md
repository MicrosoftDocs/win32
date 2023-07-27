---
description: The CoInitializeHelper method calls the CoInitializeEx function at the start of the thread.
ms.assetid: 1a981e1e-c059-4e51-81d8-33bcb39ee580
title: CAMThread.CoInitializeHelper method (Wxutil.h)
ms.topic: reference
ms.date: 4/26/2023
topic_type: 
- APIRef
- kbSyntax
api_name: 
- CAMThread.CoInitializeHelper
api_type: 
- COM
api_location: 
- Strmbase.lib
- Strmbase.dll
- Strmbasd.lib
- Strmbasd.dll
ms.custom: UpdateFrequency5
---

# CAMThread.CoInitializeHelper method

\[The feature associated with this page, [DirectShow](/windows/win32/directshow/directshow), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer), [IMFMediaEngine](/windows/win32/api/mfmediaengine/nn-mfmediaengine-imfmediaengine), and [Audio/Video Capture in Media Foundation](windows/win32/medfound/audio-video-capture-in-media-foundation). Those features have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer**, **IMFMediaEngine** and **Audio/Video Capture in Media Foundation** instead of **DirectShow**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

The `CoInitializeHelper` method calls the CoInitializeEx function at the start of the thread.

## Syntax


```C++
static HRESULT CoInitializeHelper();
```



## Parameters

This method has no parameters.

## Return value

Returns an **HRESULT** value. The following are possible values.



| Return code                                                                             | Description                                              |
|-----------------------------------------------------------------------------------------|----------------------------------------------------------|
| <dl> <dt>**S\_FALSE**</dt> </dl> | The CoInitializeEx function is not available.<br/> |
| <dl> <dt>**S\_OK**</dt> </dl>    | Success.<br/>                                      |
| <dl> <dt>**E\_FAIL**</dt> </dl>  | Failure.<br/>                                      |



 

## Remarks

The [**CAMThread::InitialThreadProc**](camthread-initialthreadproc.md) method calls this helper method, which calls the CoInitializeEx function. It uses the COINIT\_DISABLE\_OLE1DDE flag, to disable Dynamic Data Exchange (DDE). For more information, see the Platform SDK.

## Requirements



| Requirement | Value |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Wxutil.h (include Streams.h)</dt> </dl>                                                                                    |
| Library<br/> | <dl> <dt>Strmbase.lib (retail builds); </dt> <dt>Strmbasd.lib (debug builds)</dt> </dl> |



## See also

<dl> <dt>

[**CAMThread Class**](camthread.md)
</dt> </dl>

 

 




