---
title: IDXCoreAdapter1::GetPropertyWithInput
description: TBD
ms.topic: reference
ms.date: 09/27/2024
---

# IDXCoreAdapter1::GetPropertyWithInput method

TBD

## Syntax

```cpp
virtual HRESULT STDMETHODCALLTYPE GetPropertyWithInput(
    DXCoreAdapterProperty property,
    size_t inputPropertyDetailsSize,
    _In_reads_bytes_opt_(inputPropertyDetailsSize) const void *inputPropertyDetails,
    size_t outputBufferSize,
    _Out_writes_bytes_(outputBufferSize) void *outputBuffer) = 0;

template <class T1, class T2>
HRESULT GetPropertyWithInput(
        DXCoreAdapterProperty property,
        _In_reads_bytes_opt_(sizeof(T1)) const T1 *inputPropertyDetails,
        _Out_writes_bytes_(sizeof(T2)) T2 *outputBuffer);
```

## Parameters

### property

Type: **TBD**

TBD

### inputPropertyDetailsSize

Type: **TBD**

TBD

### inputPropertyDetails

Type: **TBD**

TBD

### outputBufferSize

Type: **TBD**

TBD

### outputBuffer

Type: **TBD**

TBD

## Returns

Type: **[HRESULT](../../com/structure-of-com-error-codes.md)**

If the function succeeds, it returns **S_OK**. Otherwise, it returns an [**HRESULT**](../../com/structure-of-com-error-codes.md) [error code](../../com/com-error-codes-10.md).

## See also

[IDXCoreAdapter1](./nn-dxcore_interface-idxcoreadapter1.md), [DXCore reference](../dxcore-reference.md), [Using DXCore to enumerate adapters](../dxcore-enum-adapters.md)
