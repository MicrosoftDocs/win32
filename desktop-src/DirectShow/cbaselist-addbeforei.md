---
description: The AddBeforeI method inserts an item before the specified position.
ms.assetid: d310e303-889a-43a6-bda5-2e7b805b25d1
title: CBaseList.AddBeforeI method (Wxlist.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- CBaseList.AddBeforeI
api_type: 
- COM
api_location: 
- Strmbase.lib
- Strmbase.dll
- Strmbasd.lib
- Strmbasd.dll
---

# CBaseList.AddBeforeI method

The `AddBeforeI` method inserts an item before the specified position.

## Syntax


```C++
POSITION AddBeforeI(
   POSITION pos,
   void     *pObj
);
```



## Parameters

<dl> <dt>

*pos* 
</dt> <dd>

Position before which to add the item.

</dd> <dt>

*pObj* 
</dt> <dd>

Pointer to the item.

</dd> </dl>

## Return value

Returns the position indicator for the inserted item.

## Remarks

If *pos* is **NULL**, this method adds the item to the tail of the list (equivalent to calling the [**CBaseList::AddTailI**](cbaselist-addtaili.md) method).

## Requirements



| Requirement | Value |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Wxlist.h (include Streams.h)</dt> </dl>                                                                                    |
| Library<br/> | <dl> <dt>Strmbase.lib (retail builds); </dt> <dt>Strmbasd.lib (debug builds)</dt> </dl> |



## See also

<dl> <dt>

[**CBaseList Class**](cbaselist.md)
</dt> </dl>

 

 




