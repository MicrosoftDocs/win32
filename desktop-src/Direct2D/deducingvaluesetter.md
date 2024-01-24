---
title: DeducingValueSetter (D2d1effecthelpers.h)
description: Deduces the class and arguments and then calls a member-function property setter callback for a value-type property.
ms.assetid: 4C3D64A8-0CC0-405A-A5B3-627C2DF25EA1
keywords:
- DeducingValueSetter Direct2D
topic_type:
- apiref
api_name:
- DeducingValueSetter
api_location:
- d2d1effecthelpers.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# DeducingValueSetter

Deduces the class and arguments and then calls a member-function property setter callback for a value-type property.

> [!Note]  
> DeducingValueSetter should not be called directly.

 

``` syntax
template<class C, typename P, typename I>
HRESULT DeducingValueSetter(
    _In_ HRESULT (C::*callback)(P),
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

[**Direct2D::DeducingValueGetter**](deducingvaluegetter.md)
</dt> </dl>

 

 





