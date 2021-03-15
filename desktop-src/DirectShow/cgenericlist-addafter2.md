---
description: "The AddAfter method inserts a list after the specified position, and uses 'pos' and 'plist' parameters."
ms.assetid: 99214667-8478-40e5-b55b-6ac47b1fb4d2
title: CGenericList.AddAfter method (Wxlist.h) - pos, plist parameters
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

# CGenericList.AddAfter method (Wxlist.h) - pos, plist parameters

The `AddAfter` method inserts a list after the specified position.

## Syntax


```C++
BOOL AddAfter(
   POSITION             pos,
   CGenericList<OBJECT> *pList
);
```



## Parameters

<dl> <dt>

*pos* 
</dt> <dd>

Position to insert the list. The list is inserted after this position.

</dd> <dt>

*pList* 
</dt> <dd>

Pointer to the list to insert.

</dd> </dl>

## Return value

Returns **TRUE** if successful, or **FALSE** otherwise.

## Requirements

| Requirement | Value |
|-|-|
| Header | Wxlist.h (include Streams.h) |
| Library| Strmbase.lib (retail builds); Strmbasd.lib (debug builds) |

## See also

<dl> <dt>

[**CGenericList Class**](cgenericlist.md)
</dt> </dl>

 

 




