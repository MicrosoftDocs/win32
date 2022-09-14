---
title: DeducingValueGetter (D2d1effecthelpers.h)
description: Deduces the class and arguments and then calls a member-function property getter callback for a value-type property.
ms.assetid: E2E5CCC3-B112-4D3C-8840-121A55C4F1A2
keywords:
- DeducingValueGetter Direct2D
topic_type:
- apiref
api_name:
- DeducingValueGetter
api_location:
- d2d1effecthelpers.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# DeducingValueGetter

Deduces the class and arguments and then calls a member-function property getter callback for a value-type property.

> [!Note]  
> DeducingValueGetter should not be called directly.

 

``` syntax
template<class C, typename P, typename I>
HRESULT DeducingValueGetter(
    _In_ P (C::*callback)() const,
    _In_ const I *effect,
    _Out_writes_opt_(dataSize) BYTE *data,
    UINT32 dataSize,
    _Out_opt_ UINT32 *actualSize  
    ) 
```

## Requirements



| Requirement | Value |
|-------------------|------------------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>D2d1effecthelpers.h</dt> </dl> |



## See also

<dl> <dt>

[**Direct2D::DeducingValueSetter**](deducingvaluesetter.md)
</dt> </dl>

 

 





