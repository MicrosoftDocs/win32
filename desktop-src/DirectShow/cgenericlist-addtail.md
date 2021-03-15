---
description: The AddTail method appends an item to the end of the list.
ms.assetid: e365a23e-7447-42ec-b836-21dd68962db1
title: CGenericList.AddTail method (Wxlist.h) - pObj parameter
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- CGenericList.AddTail
api_type: 
- COM
api_location: 
- Strmbase.lib
- Strmbase.dll
- Strmbasd.lib
- Strmbasd.dll
---

# CGenericList.AddTail method (Wxlist.h) - pObj parameter

The `AddTail` method appends an item to the end of the list.

## Syntax


```C++
POSITION AddTail(
   OBJECT *pObj
);
```



## Parameters

<dl> <dt>

*pObj* 
</dt> <dd>

Pointer to an object of type **OBJECT** (the template type).

</dd> </dl>

## Return value

Returns a POSITION value for the new tail position. If the method fails, it returns **NULL**.

## Requirements

| Requirement | Value |
|-|-|
| Header | Wxlist.h (include Streams.h) |
| Library| Strmbase.lib (retail builds); Strmbasd.lib (debug builds) |

## See also

<dl> <dt>

[**CGenericList Class**](cgenericlist.md)
</dt> </dl>

 

 




