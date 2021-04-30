---
description: "A constructor method that provides the mapping between old-style multimedia format DWORD types and GUID subtypes. This method uses the 'Fourcc' parameter."
ms.assetid: 35344aae-ed87-4e5e-8824-84f5482b332e
title: FOURCCMap::FOURCCMap constructor (Fourcc.h) - Fourcc parameter
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

# FOURCCMap::FOURCCMap constructor (Fourcc.h) - Fourcc parameter

Constructor method. The constuctor provides the mapping between old-style multimedia format **DWORD** types and **GUID** subtypes.

## Syntax


```C++
FOURCCMap(
   DWORD Fourcc
);
```



## Parameters

<dl> <dt>

*Fourcc* 
</dt> <dd>

**DWORD** that specifies the FOURCC.

</dd> </dl>

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

 

 




