---
Description: Flag to override batch processing. Setting this flag to TRUE overrides the COutputQueuem\_bBatchExact flag and delivers all pending samples.
ms.assetid: 95ea6973-65c0-40c9-be22-c2a20a60b459
title: COutputQueuem\_bSendAnyway member
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# COutputQueue::m\_bSendAnyway member

Flag to override batch processing. Setting this flag to **TRUE** overrides the [**COutputQueue::m\_bBatchExact**](coutputqueue-m-bbatchexact.md) flag and delivers all pending samples.

## Syntax


```C++
BOOL m_bSendAnyway;
```



## Requirements



|                    |                                                                                                                                                                                            |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Outputq.h (include Streams.h)</dt> </dl>                                                                                   |
| Library<br/> | <dl> <dt>Strmbase.lib (retail builds); </dt> <dt>Strmbasd.lib (debug builds)</dt> </dl> |



## See also

<dl> <dt>

[**COutputQueue Class**](coutputqueue.md)
</dt> </dl>

 

 




