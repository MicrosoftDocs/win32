---
description: Constructs a CMsg object.
ms.assetid: b7ee0643-73e4-450d-bff4-ca5006fdcc14
title: CMsg.CMsg constructor (Msgthrd.h)
ms.topic: reference
ms.date: 4/26/2023
topic_type: 
- APIRef
- kbSyntax
api_name: 
- CMsg.CMsg
api_type: 
- COM
api_location: 
- Strmbase.lib
- Strmbase.dll
- Strmbasd.lib
- Strmbasd.dll
ms.custom: UpdateFrequency5
---

# CMsg.CMsg constructor

\[The feature associated with this page, [DirectShow](/windows/win32/directshow/directshow), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer), [IMFMediaEngine](/windows/win32/api/mfmediaengine/nn-mfmediaengine-imfmediaengine), and [Audio/Video Capture in Media Foundation](windows/win32/medfound/audio-video-capture-in-media-foundation). Those features have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer**, **IMFMediaEngine** and **Audio/Video Capture in Media Foundation** instead of **DirectShow**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

Constructs a [**CMsg**](cmsg.md) object.

## Syntax


```C++
CMsg(
   UINT     u,
   DWORD    dw,
   LPVOID   lp,
   CAMEvent *pEvent
);
```



## Parameters

<dl> <dt>

*u* 
</dt> <dd>

Request code, defined by the client of the thread class and understood by the overridden worker thread function.

</dd> <dt>

*dw* 
</dt> <dd>

Flag parameter to the request code.

</dd> <dt>

*lp* 
</dt> <dd>

Pointer to data required by the worker thread as parameter or return values. This data should not be stack-based, as it will be referenced some time after completing the queuing operation.

</dd> <dt>

*pEvent* 
</dt> <dd>

Pointer to the event object that a worker thread can signal to indicate the completion of the operation.

</dd> </dl>

## Remarks

This member function contains a request for a [**CMsgThread**](cmsgthread.md) worker thread to act on. All the parameters are passed to the worker thread function as parameters when this message gets processed. The meanings of the parameters are defined by the client function that calls the worker thread and the derived class that supplies the worker thread's execution function.

## Requirements



| Requirement | Value |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Msgthrd.h (include Streams.h)</dt> </dl>                                                                                   |
| Library<br/> | <dl> <dt>Strmbase.lib (retail builds); </dt> <dt>Strmbasd.lib (debug builds)</dt> </dl> |



 

 




