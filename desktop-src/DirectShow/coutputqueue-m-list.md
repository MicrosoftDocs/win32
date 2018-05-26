---
Description: Media sample queue.
ms.assetid: 910f1c0c-2ce9-452f-a97b-aa424da9a93e
title: COutputQueuem\_List member
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# COutputQueue::m\_List member

Media sample queue.

## Syntax


```C++
CSampleList *m_List;
```



## Remarks

This member variable is a pointer to a [**CGenericList**](cgenericlist.md) object that holds [**IMediaSample**](/windows/win32/Strmif/nn-strmif-imediasample?branch=master) pointers. The **CSampleList** type is defined as follows:

``` syntax
typedef CGenericList<IMediaSample> CSampleList;
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

 

 




