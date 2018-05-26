---
Description: Constructor method.
ms.assetid: c1282676-6f2b-438a-850e-17bb6d7a2c68
title: CRefTime.CRefTime constructor
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# CRefTime.CRefTime constructor

Constructor method.

## Syntax


```C++
CRefTime(
   REFERENCE_TIME rt
);
```



## Parameters

<dl> <dt>

*rt* 
</dt> <dd>

Time in 100-nanosecond units.

</dd> </dl>

## Remarks

The reference time defaults to zero.

## Requirements



|                    |                                                                                                                                                                                            |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Reftime.h (include Streams.h)</dt> </dl>                                                                                   |
| Library<br/> | <dl> <dt>Strmbase.lib (retail builds); </dt> <dt>Strmbasd.lib (debug builds)</dt> </dl> |



 

 




