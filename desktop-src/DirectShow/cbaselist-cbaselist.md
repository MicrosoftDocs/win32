---
description: CBaseList.CBaseList(TCHAR\*, INT) constructor - Constructor method.
ms.assetid: 2d48cb66-45d2-4d2d-ba7e-ae759b6d2aa4
title: CBaseList.CBaseList(TCHAR*, INT) constructor (Wxlist.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- CBaseList.CBaseList
api_type: 
- COM
api_location: 
- Strmbase.lib
- Strmbase.dll
- Strmbasd.lib
- Strmbasd.dll
---

# CBaseList.CBaseList(TCHAR\*, INT) constructor

Constructor method.

## Syntax


```C++
CBaseList(
   TCHAR *pName,
   INT   iItems
);
```



## Parameters

<dl> <dt>

*pName* 
</dt> <dd>

Pointer to the name of the list.

</dd> <dt>

*iItems* 
</dt> <dd>

Size of the node cache.

</dd> </dl>

## Remarks

For efficiency, the `CBaseList` class maintains a cache of list nodes. If you know approximately how many items the list will hold, use this version of the constructor.

## Requirements



| Requirement | Value |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Wxlist.h (include Streams.h)</dt> </dl>                                                                                    |
| Library<br/> | <dl> <dt>Strmbase.lib (retail builds); </dt> <dt>Strmbasd.lib (debug builds)</dt> </dl> |



## See also

<dl> <dt>

[**CBaseList Class**](cbaselist.md)
</dt> </dl>

 

 




