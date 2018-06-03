---
Description: Optional event that is signaled whenever the object removes a sample from the queue. The value is initially NULL. Call the COutputQueue::SetPopEvent method to specify an event handle.
ms.assetid: f2602532-b045-4384-b87c-b28cc34c81b0
title: COutputQueue::m\_hEventPop member
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
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

 

 




