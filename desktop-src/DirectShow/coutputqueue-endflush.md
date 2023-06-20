---
description: COutputQueue.EndFlush method - The EndFlush method ends a flush operation.
ms.assetid: 9171a62a-9072-49a3-8e83-f66d7e1483da
title: COutputQueue.EndFlush method (Outputq.h)
ms.topic: reference
ms.date: 4/26/2023
topic_type: 
- APIRef
- kbSyntax
api_name: 
- COutputQueue.EndFlush
api_type: 
- COM
api_location: 
- Strmbase.lib
- Strmbase.dll
- Strmbasd.lib
- Strmbasd.dll
ms.custom: UpdateFrequency5
---

# COutputQueue.EndFlush method

\[The feature associated with this page, [DirectShow](/windows/win32/directshow/directshow), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer) and [IMFMediaEngine](/windows/win32/api/mfmediaengine/nn-mfmediaengine-imfmediaengine). **MediaPlayer** and **IMFMediaEngine** have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** and **IMFMediaEngine** instead of **DirectShow**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

The `EndFlush` method ends a flush operation.

## Syntax


```C++
void EndFlush();
```



## Parameters

This method has no parameters.

## Return value

This method does not return a value.

## Remarks

If the object is using a thread, this method waits for the [**COutputQueue::m\_evFlushComplete**](coutputqueue-m-evflushcomplete.md) event. The thread signals this event after it frees any pending samples. If the object is not using a thread, this method calls the [**COutputQueue::FreeSamples**](coutputqueue-freesamples.md) method. Then the `EndFlush` method calls the [**IPin::EndFlush**](/windows/desktop/api/Strmif/nf-strmif-ipin-endflush) method on the input pin.

## Requirements



| Requirement | Value |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Outputq.h (include Streams.h)</dt> </dl>                                                                                   |
| Library<br/> | <dl> <dt>Strmbase.lib (retail builds); </dt> <dt>Strmbasd.lib (debug builds)</dt> </dl> |



## See also

<dl> <dt>

[**COutputQueue Class**](coutputqueue.md)
</dt> </dl>

 

 




