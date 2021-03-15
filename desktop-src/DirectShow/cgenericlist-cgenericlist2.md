---
description: "Learn about the constructor method for CGenericList.CGenericList (Wxlist.h). This method uses the 'pName' parameter."
ms.assetid: 6311d84d-1723-4607-87f8-7cd2ad2582f3
title: CGenericList.CGenericList constructor (Wxlist.h) - pName parameter
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- CGenericList.CGenericList
api_type: 
- COM
api_location: 
- Strmbase.lib
- Strmbase.dll
- Strmbasd.lib
- Strmbasd.dll
---

# CGenericList.CGenericList constructor (Wxlist.h) - pName parameter

Constructor method.

## Syntax


```C++
CGenericList(
   TCHAR *pName
);
```



## Parameters

<dl> <dt>

*pName* 
</dt> <dd>

Pointer to the name of the list.

</dd> </dl>

## Remarks

For efficiency, the `CGenericList` class maintains a cache of list nodes. This version of the constructor uses a default cache size.

## Requirements

| Requirement | Value |
|-|-|
| Header | Wxlist.h (include Streams.h) |
| Library| Strmbase.lib (retail builds); Strmbasd.lib (debug builds) |

## See also

<dl> <dt>

[**CGenericList Class**](cgenericlist.md)
</dt> </dl>

 

 




