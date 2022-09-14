---
title: BlobGetter (D2d1effecthelpers.h)
description: Calls a member-function property getter callback for a blob-type property.
ms.assetid: 55A41BE4-2AAE-480B-A143-86E8E7533210
keywords:
- BlobGetter Direct2D
topic_type:
- apiref
api_name:
- BlobGetter
api_location:
- d2d1effecthelpers.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# BlobGetter

Calls a member-function property getter callback for a blob-type property.

``` syntax
template<typename T, T P, typename I>
HRESULT CALLBACK BlobGetter(
    _In_ const IUnknown *effect,
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

[**Direct2D::BlobSetter**](blobsetter.md)
</dt> </dl>

 

 





