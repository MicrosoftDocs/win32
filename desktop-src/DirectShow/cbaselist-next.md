---
Description: The Next method retrieves the next position in the list.
ms.assetid: ba9753b0-c82e-4772-84a7-e9982de3b8ad
title: CBaseList.Next method
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# CBaseList.Next method

The `Next` method retrieves the next position in the list.

## Syntax


```C++
POSITION Next(
   POSITION pos
);
```



## Parameters

<dl> <dt>

*pos* 
</dt> <dd>

POSITION value.

</dd> </dl>

## Return value

Returns the position indicator that follows the position specified by *pos*.

## Remarks

If *pos* is the last position in the list, the method returns **NULL**. If *pos* is **NULL**, the method returns the first position in the list.

## Requirements



|                    |                                                                                                                                                                                            |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Wxlist.h (include Streams.h)</dt> </dl>                                                                                    |
| Library<br/> | <dl> <dt>Strmbase.lib (retail builds); </dt> <dt>Strmbasd.lib (debug builds)</dt> </dl> |



## See also

<dl> <dt>

[**CBaseList Class**](cbaselist.md)
</dt> </dl>

 

 




