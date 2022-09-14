---
description: The AMOVIESETUP\_FILTER structure contains information for registering a filter.
ms.assetid: 72e58f33-e480-4b32-b3d5-8f6c8eb2d5a3
title: AMOVIESETUP_FILTER structure (Combase.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- AMOVIESETUP_FILTER
api_type: 
- HeaderDef
api_location: 
- combase.h
---

# AMOVIESETUP\_FILTER structure

The **AMOVIESETUP\_FILTER** structure contains information for registering a filter.

## Syntax


```C++
typedef struct _AMOVIESETUP_FILTER {
  const  CLSID           *clsID;
  const  WCHAR           *strName;
  DWORD                  dwMerit;
  UINT                   nPins;
  const  AMOVIESETUP_PIN *lpPin;
} AMOVIESETUP_FILTER, *PAMOVIESETUP_FILTER, *FAR LPAMOVIESETUP_FILTER;
```



## Members

<dl> <dt>

**clsID**
</dt> <dd>

Class identifier of the filter.

</dd> <dt>

**strName**
</dt> <dd>

Name of the filter.

</dd> <dt>

**dwMerit**
</dt> <dd>

Filter merit. Used by the [**IGraphBuilder**](/windows/desktop/api/Strmif/nn-strmif-igraphbuilder) interface when constructing a filter graph. For a list of merit values, see [Merit](merit.md).

</dd> <dt>

**nPins**
</dt> <dd>

Number of elements in the *lpPin* array. If *lpPin* is **NULL**, set this member to zero.

</dd> <dt>

**lpPin**
</dt> <dd>

Pointer to an array of [**AMOVIESETUP\_PIN**](amoviesetup-pin.md) structures, of size *nPins*. Each member of this array describes a pin on the filter.

</dd> </dl>

## Remarks

For information about using this structure, see [How to Register DirectShow Filters](how-to-register-directshow-filters.md). Use this structure only for filters that are registered in the default filter category (CLSID\_LegacyAmFilterCategory). To register a filter in a different category, use the [**IFilterMapper2::RegisterFilter**](/windows/desktop/api/Strmif/nf-strmif-ifiltermapper2-registerfilter) method, as described in [Implementing DllRegisterServer](implementing-dllregisterserver.md).

> [!Note]  
> The header file combase.h is provided with the [DirectShow Base Classes](directshow-base-classes.md).

 

## Requirements



| Requirement | Value |
|-------------------|----------------------------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Combase.h (include Streams.h)</dt> </dl> |



## See also

<dl> <dt>

[DirectShow Structures](directshow-structures.md)
</dt> </dl>

 

 




