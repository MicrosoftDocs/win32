---
Description: The GetFilterGraph method retrieves a pointer to the filter graph manager.
ms.assetid: 80b41272-2ca1-40db-8624-0d99d66f3c34
title: CBaseFilter.GetFilterGraph method
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# CBaseFilter.GetFilterGraph method

The `GetFilterGraph` method retrieves a pointer to the filter graph manager.

## Syntax


```C++
IFilterGraph* GetFilterGraph();
```



## Parameters

This method has no parameters.

## Return value

Returns the value of [**CBaseFilter::m\_pGraph**](cbasefilter-m-pgraph.md).

## Requirements



|                    |                                                                                                                                                                                            |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Amfilter.h (include Streams.h)</dt> </dl>                                                                                  |
| Library<br/> | <dl> <dt>Strmbase.lib (retail builds); </dt> <dt>Strmbasd.lib (debug builds)</dt> </dl> |



## See also

<dl> <dt>

[**CBaseFilter Class**](cbasefilter.md)
</dt> </dl>

 

 




