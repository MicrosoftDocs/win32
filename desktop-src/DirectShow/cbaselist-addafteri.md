---
description: The AddAfterI method inserts an item after the specified position.
ms.assetid: 6da6c1ed-5f22-4364-b636-64b5a0ce1560
title: CBaseList.AddAfterI method (Wxlist.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- CBaseList.AddAfterI
api_type: 
- COM
api_location: 
- Strmbase.lib
- Strmbase.dll
- Strmbasd.lib
- Strmbasd.dll
---

# CBaseList.AddAfterI method

The `AddAfterI` method inserts an item after the specified position.

## Syntax


```C++
POSITION AddAfterI(
   POSITION pos,
   void     *pObj
);
```



## Parameters

<dl> <dt>

*pos* 
</dt> <dd>

Position after which to add the item.

</dd> <dt>

*pObj* 
</dt> <dd>

Pointer to the item to add.

</dd> </dl>

## Return value

Returns the position indicator of the inserted item.

## Remarks

If *pos* is **NULL**, this method adds the item to the head of the list (equivalent to calling the [**CBaseList::AddHeadI**](cbaselist-addheadi.md) method).

## Requirements



| Requirement | Value |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Wxlist.h (include Streams.h)</dt> </dl>                                                                                    |
| Library<br/> | <dl> <dt>Strmbase.lib (retail builds); </dt> <dt>Strmbasd.lib (debug builds)</dt> </dl> |



## See also

<dl> <dt>

[**CBaseList Class**](cbaselist.md)
</dt> </dl>

 

 




