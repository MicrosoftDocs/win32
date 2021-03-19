---
title: DeducingBlobSetter (D2d1effecthelpers.h)
description: Deduces the class and arguments and then calls a member-function property setter callback for a blob-type property.
ms.assetid: 4B8B871D-FE5E-4EF3-AEED-A3D92C10E8C6
keywords:
- DeducingBlobSetter Direct2D
topic_type:
- apiref
api_name:
- DeducingBlobSetter
api_location:
- d2d1effecthelpers.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# DeducingBlobSetter

Deduces the class and arguments and then calls a member-function property setter callback for a blob-type property.

> [!Note]  
> DeducingBlobSetter should not be called directly.

 

``` syntax
template<class C, typename I>  
HRESULT DeducingBlobSetter(  
    _In_ HRESULT (C::*callback)(const BYTE *, UINT32),  
    _In_ I *effect,  
    _In_reads_(dataSize) const BYTE *data,  
    UINT32 dataSize,  
    ) 
```

## Requirements



| Requirement | Value |
|-------------------|------------------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>D2d1effecthelpers.h</dt> </dl> |



## See also

<dl> <dt>

[**Direct2D::DeducingBlobGetter**](deducingblobgetter.md)
</dt> </dl>

 

 





