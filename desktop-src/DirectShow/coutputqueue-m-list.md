---
Description: Media sample queue.
ms.assetid: 910f1c0c-2ce9-452f-a97b-aa424da9a93e
title: COutputQueue::m\_List member
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# COutputQueue::m\_List member

Media sample queue.

## Syntax


```C++
CSampleList *m_List;
```



## Remarks

This member variable is a pointer to a [**CGenericList**](cgenericlist.md) object that holds [**IMediaSample**](/windows/desktop/api/Strmif/nn-strmif-imediasample) pointers. The **CSampleList** type is defined as follows:

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

 

 




