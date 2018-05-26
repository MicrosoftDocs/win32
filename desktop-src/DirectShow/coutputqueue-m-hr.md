---
Description: HRESULT value that indicates whether the object will accept samples. If the value is S\_OK, the object will accept samples. Otherwise, it rejects samples.
ms.assetid: e05d4d2e-cc3e-4b83-8531-bc4bd6d665ac
title: COutputQueuem\_hr member
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# COutputQueue::m\_hr member

**HRESULT** value that indicates whether the object will accept samples. If the value is S\_OK, the object will accept samples. Otherwise, it rejects samples.

## Syntax


```C++
HRESULT m_hr;
```



## Remarks

This member variable is used to coordinate activities across threads. If the downstream input pin rejects a sample, or if the object begins flushing, the value is set to S\_FALSE or an error code. The object will not deliver any more samples until flushing is complete, or until the [**COutputQueue::Reset**](coutputqueue-reset.md) method is called.

## Requirements



|                    |                                                                                                                                                                                            |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Outputq.h (include Streams.h)</dt> </dl>                                                                                   |
| Library<br/> | <dl> <dt>Strmbase.lib (retail builds); </dt> <dt>Strmbasd.lib (debug builds)</dt> </dl> |



## See also

<dl> <dt>

[**COutputQueue Class**](coutputqueue.md)
</dt> </dl>

 

 




