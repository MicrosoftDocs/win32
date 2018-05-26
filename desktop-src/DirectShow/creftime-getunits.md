---
Description: The GetUnits method retrieves the reference time in 100-nanosecond units.
ms.assetid: f27dada1-67a6-424a-8bf5-979ad375736f
title: CRefTime.GetUnits method
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# CRefTime.GetUnits method

The `GetUnits` method retrieves the reference time in 100-nanosecond units.

## Syntax


```C++
LONGLONG GetUnits();
```



## Parameters

This method has no parameters.

## Return value

Returns the value of [**CRefTime::m\_time**](creftime-m-time.md).

## Requirements



|                    |                                                                                                                                                                                            |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Reftime.h (include Streams.h)</dt> </dl>                                                                                   |
| Library<br/> | <dl> <dt>Strmbase.lib (retail builds); </dt> <dt>Strmbasd.lib (debug builds)</dt> </dl> |



 

 




