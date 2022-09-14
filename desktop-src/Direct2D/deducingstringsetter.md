---
title: DeducingStringSetter (D2d1effecthelpers.h)
description: Deduces the class and arguments and then calls a member-function property setter callback for a string-type property.
ms.assetid: D3075B7B-D253-4F85-9FD2-3487C4207122
keywords:
- DeducingStringSetter Direct2D
topic_type:
- apiref
api_name:
- DeducingStringSetter
api_location:
- d2d1effecthelpers.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# DeducingStringSetter

Deduces the class and arguments and then calls a member-function property setter callback for a string-type property.

> [!Note]  
> DeducingStringSetter should not be called directly.

 

``` syntax
template<class C, typename I>  
HRESULT DeducingStringSetter(  
    _In_ HRESULT (C::*callback)(PCWSTR string),
    _In_ I *effect,
    _In_reads_(dataSize) const BYTE *data,
    UINT32 dataSize  
    ) 
```

## Requirements



| Requirement | Value |
|-------------------|------------------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>D2d1effecthelpers.h</dt> </dl> |



## See also

<dl> <dt>

[**Direct2D::DeducingStringGetter**](deducingstringgetter.md)
</dt> </dl>

 

 





