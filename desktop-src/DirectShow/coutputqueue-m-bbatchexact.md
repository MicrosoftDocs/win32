---
description: Flag that specifies whether the object delivers samples in exact batches.
ms.assetid: 1a37c78f-4499-4ebb-92b4-b71ba3ff1a02
title: COutputQueue::m_bBatchExact member (Outputq.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- m_bBatchExact
api_type: 
- LibDef
api_location: 
- Strmbase.lib
- Strmbase.dll
- Strmbasd.lib
- Strmbasd.dll
---

# COutputQueue::m\_bBatchExact member

Flag that specifies whether the object delivers samples in exact batches.

## Syntax


```C++
const BOOL m_bBatchExact;
```



## Remarks

If the value is **TRUE**, the object waits until it has a complete batch of media samples before delivering any. Otherwise, it delivers samples as they arrive. The [**COutputQueue::m\_lBatchSize**](coutputqueue-m-lbatchsize.md) member variable defines the batch size.

## Requirements



| Requirement | Value |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Outputq.h (include Streams.h)</dt> </dl>                                                                                   |
| Library<br/> | <dl> <dt>Strmbase.lib (retail builds); </dt> <dt>Strmbasd.lib (debug builds)</dt> </dl> |



## See also

<dl> <dt>

[**COutputQueue Class**](coutputqueue.md)
</dt> </dl>

 

 




