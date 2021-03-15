---
description: The AddHead method adds a list to the front of the list.
ms.assetid: 9a344bed-d871-4082-9bbb-330f2ff42cca
title: CGenericList.AddHead method (Wxlist.h) (2)
ms.topic: reference
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

# CGenericList.AddHead method (Wxlist.h)

The `AddHead` method adds a list to the front of the list.

## Syntax


```C++
BOOL AddHead(
   CGenericList<OBJECT> *pList
);
```



## Parameters

<dl> <dt>

*pList* 
</dt> <dd>

Pointer to the list of items to add.

</dd> </dl>

## Return value

Returns **TRUE** if successful, or **FALSE** otherwise.

## Requirements



|                    |                                                                                                                                                                                            |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Wxlist.h (include Streams.h)</dt> </dl>                                                                                    |
| Library<br/> | <dl> <dt>Strmbase.lib (retail builds); </dt> <dt>Strmbasd.lib (debug builds)</dt> </dl> |



## See also

<dl> <dt>

[**CGenericList Class**](cgenericlist.md)
</dt> </dl>

 

 




