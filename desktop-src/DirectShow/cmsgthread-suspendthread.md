---
description: Uses the Microsoft Win32 SuspendThread function to suspend the operation of a running thread.
ms.assetid: 07d919a2-797d-47c3-83e3-c8e2d2b2cddd
title: CMsgThread.SuspendThread method (Msgthrd.h)
ms.topic: reference
ms.date: 4/26/2023
topic_type: 
- APIRef
- kbSyntax
api_name: 
- CMsgThread.SuspendThread
api_type: 
- COM
api_location: 
- Strmbase.lib
- Strmbase.dll
- Strmbasd.lib
- Strmbasd.dll
ms.custom: UpdateFrequency5
---

# CMsgThread.SuspendThread method

\[The feature associated with this page, [DirectShow](/windows/win32/directshow/directshow), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer), [IMFMediaEngine](/windows/win32/api/mfmediaengine/nn-mfmediaengine-imfmediaengine), and [Audio/Video Capture in Media Foundation](/windows/win32/medfound/audio-video-capture-in-media-foundation). Those features have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer**, **IMFMediaEngine** and **Audio/Video Capture in Media Foundation** instead of **DirectShow**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

Uses the Microsoft Win32 **SuspendThread** function to suspend the operation of a running thread.

## Syntax


```C++
DWORD SuspendThread();
```



## Parameters

This method has no parameters.

## Return value

If the member function succeeds, the return value is the previous suspend count of the thread. If the member function fails, the return value is 0xFFFFFFFF. To obtain extended error information, call the Microsoft Win32 **GetLastError** function.

## Remarks

The client thread calls this member function to suspend the operation of the worker thread. The worker thread remains suspended and will not execute until an additional call to the [**CMsgThread::ResumeThread**](cmsgthread-resumethread.md) member function is made.

## Requirements



| Requirement | Value |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Msgthrd.h (include Streams.h)</dt> </dl>                                                                                   |
| Library<br/> | <dl> <dt>Strmbase.lib (retail builds); </dt> <dt>Strmbasd.lib (debug builds)</dt> </dl> |



## See also

<dl> <dt>

[**CMsgThread Class**](cmsgthread.md)
</dt> </dl>

 

 




