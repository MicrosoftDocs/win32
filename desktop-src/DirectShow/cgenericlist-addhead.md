---
Description: The AddHead method adds an item to the front of the list.
ms.assetid: 8f0012b7-bbc2-407c-ae5a-9843c2f692dc
title: CGenericList.AddHead method
ms.topic: article
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- CGenericList.AddHead
api_type: 
- COM
api_location: 
- Strmbase.lib
- Strmbase.dll
- Strmbasd.lib
- Strmbasd.dll
---

# CGenericList.AddHead method

The `AddHead` method adds an item to the front of the list.

## Syntax


```C++
POSITION AddHead(
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

Returns a POSITION value indicating the new head position. If the method fails, the return value is **NULL**.

## Requirements



|                    |                                                                                                                                                                                            |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Wxlist.h (include Streams.h)</dt> </dl>                                                                                    |
| Library<br/> | <dl> <dt>Strmbase.lib (retail builds); </dt> <dt>Strmbasd.lib (debug builds)</dt> </dl> |



## See also

<dl> <dt>

[**CGenericList Class**](cgenericlist.md)
</dt> </dl>

 

 




