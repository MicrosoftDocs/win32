---
title: BlobSetter (D2d1effecthelpers.h)
description: Calls a member-function property setter callback for a blob-type property.
ms.assetid: 29411D53-1D27-4040-A3C0-B1511E627A32
keywords:
- BlobSetter Direct2D
topic_type:
- apiref
api_name:
- BlobSetter
api_location:
- d2d1effecthelpers.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# BlobSetter

Calls a member-function property setter callback for a blob-type property.

``` syntax
template<typename T, T P, typename I>
HRESULT CALLBACK BlobSetter(
    _In_ IUnknown *effect,
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

[**Direct2D::BlobGetter**](blobgetter.md)
</dt> </dl>

 

 





