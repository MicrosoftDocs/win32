---
Description: The CurrentRate method retrieves the segment rate, set by the CBasePinNewSegment method.
ms.assetid: 19780dd2-2dcf-4e5d-8a70-a46be05e040c
title: CBasePin.CurrentRate method
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# CBasePin.CurrentRate method

The `CurrentRate` method retrieves the segment rate, set by the [**CBasePin::NewSegment**](cbasepin-newsegment.md) method.

## Syntax


```C++
double CurrentRate();
```



## Parameters

This method has no parameters.

## Return value

Returns the value of [**CBasePin::m\_dRate**](cbasepin-m-drate.md).

## Requirements



|                    |                                                                                                                                                                                            |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Amfilter.h (include Streams.h)</dt> </dl>                                                                                  |
| Library<br/> | <dl> <dt>Strmbase.lib (retail builds); </dt> <dt>Strmbasd.lib (debug builds)</dt> </dl> |



## See also

<dl> <dt>

[**CBasePin Class**](cbasepin.md)
</dt> </dl>

 

 




