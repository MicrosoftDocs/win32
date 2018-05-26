---
Description: Destructor method.
ms.assetid: e0a04d93-fb77-4dc1-9bc8-7d3965bc6803
title: CMemAllocator.~CMemAllocator destructor
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# CMemAllocator.~CMemAllocator destructor

Destructor method.

## Syntax


```C++
~CMemAllocator();
```



## Remarks

This method overrides the base-class destructor to call [**CBaseAllocator::Decommit**](cbaseallocator-decommit.md) and [**CMemAllocator::ReallyFree**](cmemallocator-reallyfree.md).

## Requirements



|                    |                                                                                                                                                                                            |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Amfilter.h (include Streams.h)</dt> </dl>                                                                                  |
| Library<br/> | <dl> <dt>Strmbase.lib (retail builds); </dt> <dt>Strmbasd.lib (debug builds)</dt> </dl> |



## See also

<dl> <dt>

[**CMemAllocator Class**](cmemallocator.md)
</dt> </dl>

 

 




