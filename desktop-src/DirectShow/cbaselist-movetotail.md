---
Description: The MoveToTail method splits the list and appends the head portion to the tail of another list.
ms.assetid: f5cefe7c-075c-433b-9ece-aa10217344fa
title: CBaseList.MoveToTail method
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# CBaseList.MoveToTail method

The `MoveToTail` method splits the list and appends the head portion to the tail of another list.

## Syntax


```C++
BOOL MoveToTail(
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

This method splits the list after the position specified by the *pos* parameter. The tail portion remains in the list. The head portion is appended to the tail of the other list.

## Requirements



|                    |                                                                                                                                                                                            |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Wxlist.h (include Streams.h)</dt> </dl>                                                                                    |
| Library<br/> | <dl> <dt>Strmbase.lib (retail builds); </dt> <dt>Strmbasd.lib (debug builds)</dt> </dl> |



## See also

<dl> <dt>

[**CBaseList Class**](cbaselist.md)
</dt> </dl>

 

 




