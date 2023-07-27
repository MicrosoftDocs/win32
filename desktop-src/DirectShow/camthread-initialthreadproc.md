---
description: The InitialThreadProc method calls the main thread procedure.
ms.assetid: 1546c214-7ea9-4484-974b-dbd4b2b3e296
title: CAMThread.InitialThreadProc method (Wxutil.h)
ms.topic: reference
ms.date: 4/26/2023
topic_type: 
- APIRef
- kbSyntax
api_name: 
- CAMThread.InitialThreadProc
api_type: 
- COM
api_location: 
- Strmbase.lib
- Strmbase.dll
- Strmbasd.lib
- Strmbasd.dll
ms.custom: UpdateFrequency5
---

# CAMThread.InitialThreadProc method

\[The feature associated with this page, [DirectShow](/windows/win32/directshow/directshow), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer), [IMFMediaEngine](/windows/win32/api/mfmediaengine/nn-mfmediaengine-imfmediaengine), and [Audio/Video Capture in Media Foundation](/windows/win32/medfound/audio-video-capture-in-media-foundation). Those features have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer**, **IMFMediaEngine** and **Audio/Video Capture in Media Foundation** instead of **DirectShow**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

The `InitialThreadProc` method calls the main thread procedure.

## Syntax


```C++
DWORD InitialThreadProc(
   LPVOID pv
);
```



## Parameters

<dl> <dt>

*pv* 
</dt> <dd>

`this` pointer.

</dd> </dl>

## Return value

Returns the **DWORD** returned by [**CAMThread::ThreadProc**](camthread-threadproc.md). The derived class defines this value.

## Remarks

The [**CAMThread::Create**](camthread-create.md) method uses this method for the thread procedure when it creates the thread. It uses the `this` pointer as the thread argument.

This method calls the [**CAMThread::CoInitializeHelper**](camthread-coinitializehelper.md) method and then ThreadProc.

## Requirements



| Requirement | Value |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Wxutil.h (include Streams.h)</dt> </dl>                                                                                    |
| Library<br/> | <dl> <dt>Strmbase.lib (retail builds); </dt> <dt>Strmbasd.lib (debug builds)</dt> </dl> |



## See also

<dl> <dt>

[**CAMThread Class**](camthread.md)
</dt> </dl>

 

 




