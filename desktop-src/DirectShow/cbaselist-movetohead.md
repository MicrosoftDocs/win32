---
Description: The MoveToHead method splits the list and inserts the tail portion at the head of another list.
ms.assetid: 46e4f8fe-6707-44c6-9d49-0168b35d2364
title: CBaseList.MoveToHead method
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# CBaseList.MoveToHead method

The `MoveToHead` method splits the list and inserts the tail portion at the head of another list.

## Syntax


```C++
BOOL MoveToHead(
   POSITION  pos,
   CBaseList *pList
);
```



## Parameters

<dl> <dt>

*pos* 
</dt> <dd>

Position indicator that marks the split in the list.

</dd> <dt>

*pList* 
</dt> <dd>

Pointer to another list.

</dd> </dl>

## Return value

Returns **TRUE** if successful, or **FALSE** otherwise.

## Remarks

This method splits the list before the position specified by the *pos* parameter. The head portion remains in the list. The tail portion is inserted at the head of the other list.

## Requirements



|                    |                                                                                                                                                                                            |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Wxlist.h (include Streams.h)</dt> </dl>                                                                                    |
| Library<br/> | <dl> <dt>Strmbase.lib (retail builds); </dt> <dt>Strmbasd.lib (debug builds)</dt> </dl> |



## See also

<dl> <dt>

[**CBaseList Class**](cbaselist.md)
</dt> </dl>

 

 




