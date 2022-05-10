---
title: IDXCoreAdapter::GetPropertySize
description: For a specified adapter property, retrieves the size of buffer, in bytes, that is required for a call to [GetProperty](./nf-dxcore_interface-idxcoreadapter-getproperty.md).
ms.topic: reference
ms.date: 06/20/2019
---

# IDXCoreAdapter::GetPropertySize method

For a specified adapter property, retrieves the size of buffer, in bytes, that is required for a call to [GetProperty](./nf-dxcore_interface-idxcoreadapter-getproperty.md). Before calling **GetPropertySize** for a property type, call [IsPropertySupported](./nf-dxcore_interface-idxcoreadapter-ispropertysupported.md) to confirm that the property type is available for this adapter and operating system (OS).

## Syntax

```cpp
virtual HRESULT STDMETHODCALLTYPE GetPropertySize(
  DXCoreAdapterProperty property,
  _Out_ size_t *bufferSize) = 0;
```

## Parameters

### property

Type: **[DXCoreAdapterProperty](./ne-dxcore_interface-dxcoreadapterproperty.md)**

The type of the property whose size, in bytes, you wish to retrieve.

### bufferSize [out]

Type: **size_t\***

A pointer to a **size_t** value. The function dereferences the pointer and sets the value to the size, in bytes, of the output buffer that you should allocate and pass as the *propertyData* argument in your call to [GetProperty](./nf-dxcore_interface-idxcoreadapter-getproperty.md).

## Returns

Type: **[HRESULT](../../com/structure-of-com-error-codes.md)**

If the function succeeds, it returns **S_OK**. Otherwise, it returns an [**HRESULT**](../../com/structure-of-com-error-codes.md) [error code](../../com/com-error-codes-10.md).

|Return value|Description|
|-|-|
|DXGI_ERROR_INVALID_CALL|The property type specified in *property* is not recognized by this operating system (OS). Call [IsPropertySupported](./nf-dxcore_interface-idxcoreadapter-ispropertysupported.md) to confirm that the property type is available for this adapter and operating system (OS).|
|DXGI_ERROR_UNSUPPORTED|The property type specified in *property* is not supported by the adapter. Call [IsPropertySupported](./nf-dxcore_interface-idxcoreadapter-ispropertysupported.md) to confirm that the property type is available for this adapter and operating system (OS).|
|E_POINTER|`nullptr` was provided for *bufferSize*.|

## Remarks

You can call **GetPropertySize** on an adapter that's no longer valid&mdash;the function won't fail.

## See also

[IDXCoreAdapter](./nn-dxcore_interface-idxcoreadapter.md), [DXCore Reference](../dxcore-reference.md), [Using DXCore to enumerate adapters](../dxcore-enum-adapters.md)
