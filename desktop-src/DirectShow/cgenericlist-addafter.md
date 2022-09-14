---
description: "The AddAfter method inserts an item after the specified position, and uses 'p' and 'pObj' parameters."
ms.assetid: 3e1f27c5-3e04-424a-8fe3-9bfde4e3824b
title: CGenericList.AddAfter method (Wxlist.h) - p, pObj parameters
ms.topic: reference
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

# CGenericList.AddAfter method (Wxlist.h) - p, pObj parameters

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

| Requirement | Value |
|-|-|
| Header | Wxlist.h (include Streams.h) |
| Library| Strmbase.lib (retail builds); Strmbasd.lib (debug builds) |

## See also

<dl> <dt>

[**CGenericList Class**](cgenericlist.md)
</dt> </dl>

 

 




