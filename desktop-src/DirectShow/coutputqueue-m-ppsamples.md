---
description: Array of samples of size COutputQueue::m\_lBatchSize.
ms.assetid: 5c4b904d-480b-4393-a799-63989669ea1c
title: COutputQueue::m_ppSamples member (Outputq.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- m_ppSamples
api_type: 
- LibDef
api_location: 
- Strmbase.lib
- Strmbase.dll
- Strmbasd.lib
- Strmbasd.dll
---

# COutputQueue::m\_ppSamples member

Array of samples of size [**COutputQueue::m\_lBatchSize**](coutputqueue-m-lbatchsize.md).

## Syntax


```C++
IMediaSample **m_ppSamples;
```



## Remarks

The worker thread pulls samples from the queue and places them in this array. It passes the array to the [**IMemInputPin::ReceiveMultiple**](/windows/desktop/api/Strmif/nf-strmif-imeminputpin-receivemultiple) method. If the object is not using a worker thread, the object places samples directly into this array. The [**COutputQueue::m\_List**](coutputqueue-m-list.md) member variable holds the queue.

## Requirements



| Requirement | Value |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Outputq.h (include Streams.h)</dt> </dl>                                                                                   |
| Library<br/> | <dl> <dt>Strmbase.lib (retail builds); </dt> <dt>Strmbasd.lib (debug builds)</dt> </dl> |



## See also

<dl> <dt>

[**COutputQueue Class**](coutputqueue.md)
</dt> </dl>

 

 




