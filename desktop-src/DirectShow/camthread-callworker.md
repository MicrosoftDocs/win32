---
description: The CallWorker method signals the thread with a request.
ms.assetid: 51431688-bf55-4778-afc0-91b6ab336aa3
title: CAMThread.CallWorker method (Wxutil.h)
ms.topic: reference
ms.date: 4/26/2023
topic_type: 
- APIRef
- kbSyntax
api_name: 
- CAMThread.CallWorker
api_type: 
- COM
api_location: 
- Strmbase.lib
- Strmbase.dll
- Strmbasd.lib
- Strmbasd.dll
ms.custom: UpdateFrequency5
---

# CAMThread.CallWorker method

\[The feature associated with this page, [DirectShow](/windows/win32/directshow/directshow), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer), [IMFMediaEngine](/windows/win32/api/mfmediaengine/nn-mfmediaengine-imfmediaengine), and [Audio/Video Capture in Media Foundation](/windows/win32/medfound/audio-video-capture-in-media-foundation). Those features have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer**, **IMFMediaEngine** and **Audio/Video Capture in Media Foundation** instead of **DirectShow**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

The `CallWorker` method signals the thread with a request.

## Syntax


```C++
DWORD CallWorker(
   DWORD dwParam
);
```



## Parameters

<dl> <dt>

*dwParam* 
</dt> <dd>

Request parameter. The derived class defines the meaning of the parameter.

</dd> </dl>

## Return value

Returns a value that is defined by the derived class.

## Remarks

The [**CAMThread::GetRequest**](camthread-getrequest.md) and [**CAMThread::CheckRequest**](camthread-checkrequest.md) methods retrieve the value of the *dwParam* parameter. The GetRequest method blocks until `CallWorker` is called.

This method blocks until the [**CAMThread::Reply**](camthread-reply.md) method is called. The return value is the parameter given to Reply.

This method holds the [**CAMThread::m\_AccessLock**](camthread-m-accesslock.md) lock to serialize requests. Therefore, do call this method from the thread itself or from any member function that executes in the context of the thread.

## Requirements



| Requirement | Value |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Wxutil.h (include Streams.h)</dt> </dl>                                                                                    |
| Library<br/> | <dl> <dt>Strmbase.lib (retail builds); </dt> <dt>Strmbasd.lib (debug builds)</dt> </dl> |



## See also

<dl> <dt>

[**CAMThread Class**](camthread.md)
</dt> </dl>

 

 




