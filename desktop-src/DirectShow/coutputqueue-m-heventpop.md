---
Description: Optional event that is signaled whenever the object removes a sample from the queue. The value is initially NULL. Call the COutputQueueSetPopEvent method to specify an event handle.
ms.assetid: f2602532-b045-4384-b87c-b28cc34c81b0
title: COutputQueuem\_hEventPop member
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# COutputQueue::m\_hEventPop member

Optional event that is signaled whenever the object removes a sample from the queue. The value is initially **NULL**. Call the [**COutputQueue::SetPopEvent**](coutputqueue-setpopevent.md) method to specify an event handle.

## Syntax


```C++
HANDLE m_hEventPop;
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

 

 




