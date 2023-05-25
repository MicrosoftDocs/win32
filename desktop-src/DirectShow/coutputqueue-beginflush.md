---
description: COutputQueue.BeginFlush method - The BeginFlush method begins a flush operation.
ms.assetid: d37b611e-742f-4bdf-bd72-a91cd1c473b3
title: COutputQueue.BeginFlush method (Outputq.h)
ms.topic: reference
ms.date: 4/26/2023
topic_type: 
- APIRef
- kbSyntax
api_name: 
- COutputQueue.BeginFlush
api_type: 
- COM
api_location: 
- Strmbase.lib
- Strmbase.dll
- Strmbasd.lib
- Strmbasd.dll
ms.custom: UpdateFrequency5
---

# COutputQueue.BeginFlush method

\[The feature associated with this page, [DirectShow](/windows/win32/directshow/directshow), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer) and [IMFMediaEngine](/windows/win32/api/mfmediaengine/nn-mfmediaengine-imfmediaengine). **MediaPlayer** and **IMFMediaEngine** have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** and **IMFMediaEngine** instead of **DirectShow**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

The `BeginFlush` method begins a flush operation.

## Syntax


```C++
void BeginFlush();
```



## Parameters

This method has no parameters.

## Return value

This method does not return a value.

## Remarks

This method sets the [**COutputQueue::m\_bFlushing**](coutputqueue-m-bflushing.md) member variable to **TRUE**. If the object is using a thread, the thread calls the [**COutputQueue::FreeSamples**](coutputqueue-freesamples.md) method to free any pending samples. Otherwise, the object calls **FreeSamples** during the [**COutputQueue::EndFlush**](coutputqueue-endflush.md) method. This method also sets the [**COutputQueue::m\_hr**](coutputqueue-m-hr.md) member variable to S\_FALSE, which causes the object to discard all new samples.

The object passes the flush notification downstream by calling the [**IPin::BeginFlush**](/windows/desktop/api/Strmif/nf-strmif-ipin-beginflush) method on the input pin.

## Requirements



| Requirement | Value |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Outputq.h (include Streams.h)</dt> </dl>                                                                                   |
| Library<br/> | <dl> <dt>Strmbase.lib (retail builds); </dt> <dt>Strmbasd.lib (debug builds)</dt> </dl> |



## See also

<dl> <dt>

[**COutputQueue Class**](coutputqueue.md)
</dt> </dl>

 

 




