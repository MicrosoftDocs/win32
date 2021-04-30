---
description: A constructor method that provides the mapping between old-style multimedia format DWORD types and GUID subtypes. This method uses no parameters.
ms.assetid: 2152803c-f45f-43b0-9207-4eaeddf5eeb6
title: FOURCCMap::FOURCCMap constructor (Fourcc.h) - No parameters
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- FOURCCMap.FOURCCMap
api_type: 
- COM
api_location: 
- Strmbase.lib
- Strmbase.dll
- Strmbasd.lib
- Strmbasd.dll
---

# FOURCCMap::FOURCCMap constructor (Fourcc.h) - No parameters

Constructor method. The constuctor provides the mapping between old-style multimedia format **DWORD** types and **GUID** subtypes.

## Syntax


```C++
FOURCCMap();
```



## Parameters

This constructor has no parameters.

## Remarks

If this object is constructed with the **FOURCC** code, a **GUID** is created to match it. If this object is created with an existing **GUID**, the **FOURCC** value of the object is set to zero. Thereafter, the **FOURCC** value can be set or retrieved using the [**SetFOURCC**](fourccmap-setfourcc.md) and [**GetFOURCC**](fourccmap-getfourcc.md) member functions, respectively.

## Requirements


| Requirement | Value |
|-|-|
| Header  | Fourcc.h (include Streams.h) |
| Library | Strmbase.lib (retail builds); Strmbasd.lib (debug builds) |



## See also

<dl> <dt>

[**FOURCCMap Class**](fourccmap.md)
</dt> </dl>

 

 




