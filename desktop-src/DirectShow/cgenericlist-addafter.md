---
Description: The AddAfter method inserts an item after the specified position.
ms.assetid: 3e1f27c5-3e04-424a-8fe3-9bfde4e3824b
title: CGenericList.AddAfter method
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- CGenericList.AddAfter
api_type: 
- COM
api_location: 
- Strmbase.lib
- Strmbase.dll
- Strmbasd.lib
- Strmbasd.dll
---

# CGenericList.AddAfter method

The `AddAfter` method inserts an item after the specified position.

## Syntax


```C++
POSITION AddAfter(
   POSITION p,
   OBJECT   *pObj
);
```



## Parameters

<dl> <dt>

*p* 
</dt> <dd>

Position after which to add the item. If *p* is **NULL**, the method adds the item to the head of the list.

</dd> <dt>

*pObj* 
</dt> <dd>

Pointer to an object of type **OBJECT** (the template type).

</dd> </dl>

## Return value

Returns the position indicator of the inserted item.

## Requirements



|                    |                                                                                                                                                                                            |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Wxlist.h (include Streams.h)</dt> </dl>                                                                                    |
| Library<br/> | <dl> <dt>Strmbase.lib (retail builds); </dt> <dt>Strmbasd.lib (debug builds)</dt> </dl> |



## See also

<dl> <dt>

[**CGenericList Class**](cgenericlist.md)
</dt> </dl>

 

 




