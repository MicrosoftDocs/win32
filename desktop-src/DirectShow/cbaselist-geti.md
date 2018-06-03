---
Description: The GetI method retrieves the item at the specified position.
ms.assetid: fc775230-491a-49b6-b631-e7d5b8c82d8c
title: CBaseList.GetI method
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# CBaseList.GetI method

The `GetI` method retrieves the item at the specified position.

## Syntax


```C++
void* GetI(
   POSITION pos
);
```



## Parameters

<dl> <dt>

*pos* 
</dt> <dd>

Position indicator for the item to retrieve.

</dd> </dl>

## Return value

Returns a pointer to the item.

## Remarks

If *pos* is **NULL**, the method returns **NULL**.

## Requirements



|                    |                                                                                                                                                                                            |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Wxlist.h (include Streams.h)</dt> </dl>                                                                                    |
| Library<br/> | <dl> <dt>Strmbase.lib (retail builds); </dt> <dt>Strmbasd.lib (debug builds)</dt> </dl> |



## See also

<dl> <dt>

[**CBaseList Class**](cbaselist.md)
</dt> </dl>

 

 




