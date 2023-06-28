---
description: The Reply method replies to a request.
ms.assetid: 90e91b99-6a1c-46a2-b83d-eba483f1832a
title: CAMThread.Reply method (Wxutil.h)
ms.topic: reference
ms.date: 4/26/2023
topic_type: 
- APIRef
- kbSyntax
api_name: 
- CAMThread.Reply
api_type: 
- COM
api_location: 
- Strmbase.lib
- Strmbase.dll
- Strmbasd.lib
- Strmbasd.dll
ms.custom: UpdateFrequency5
---

# CAMThread.Reply method

\[The feature associated with this page, [DirectShow](/windows/win32/directshow/directshow), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer) and [IMFMediaEngine](/windows/win32/api/mfmediaengine/nn-mfmediaengine-imfmediaengine). **MediaPlayer** and **IMFMediaEngine** have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** and **IMFMediaEngine** instead of **DirectShow**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

The `Reply` method replies to a request.

## Syntax


```C++
void Reply(
   DWORD dw
);
```



## Parameters

<dl> <dt>

*dw* 
</dt> <dd>

Value to return in the [**CAMThread::CallWorker**](camthread-callworker.md) method.

</dd> </dl>

## Return value

This method does not return a value.

## Remarks

The CallWorker method blocks until this method is called. The *dw* parameter supplies the return value for CallWorker. Call this method in your thread procedure after you retrieve a request, to release the requesting thread.

## Requirements



| Requirement | Value |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Wxutil.h (include Streams.h)</dt> </dl>                                                                                    |
| Library<br/> | <dl> <dt>Strmbase.lib (retail builds); </dt> <dt>Strmbasd.lib (debug builds)</dt> </dl> |



## See also

<dl> <dt>

[**CAMThread Class**](camthread.md)
</dt> </dl>

 

 




