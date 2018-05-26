---
Description: The FindI method retrieves the first position that holds the specified item.
ms.assetid: a95fac19-0f93-4bb4-8e76-0da82745a1d2
title: CBaseList.FindI method
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# CBaseList.FindI method

The `FindI` method retrieves the first position that holds the specified item.

## Syntax


```C++
POSITION FindI(
   void *pObj
);
```



## Parameters

<dl> <dt>

*pObj* 
</dt> <dd>

Pointer to the item.

</dd> </dl>

## Return value

Returns a POSITION value, or **NULL** if the item is not in the list.

## Requirements



|                    |                                                                                                                                                                                            |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Wxlist.h (include Streams.h)</dt> </dl>                                                                                    |
| Library<br/> | <dl> <dt>Strmbase.lib (retail builds); </dt> <dt>Strmbasd.lib (debug builds)</dt> </dl> |



## See also

<dl> <dt>

[**CBaseList Class**](cbaselist.md)
</dt> </dl>

 

 




