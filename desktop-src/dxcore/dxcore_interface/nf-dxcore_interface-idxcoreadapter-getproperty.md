---
title: IDXCoreAdapter::GetProperty
description: Retrieves the value of the specified adapter property.
ms.topic: reference
ms.date: 06/20/2019
---

# IDXCoreAdapter::GetProperty method

Retrieves the value of the specified adapter property. Before calling **GetProperty** for a property type, call [IsPropertySupported](./nf-dxcore_interface-idxcoreadapter-ispropertysupported.md) to confirm that the property type is available for this adapter and operating system (OS). Also before calling **GetProperty**, call [GetPropertySize](./nf-dxcore_interface-idxcoreadapter-getpropertysize.md) to determine the necessary size of the buffer in which to receive the property value.

## Syntax

```cpp
virtual HRESULT STDMETHODCALLTYPE GetProperty(
  DXCoreAdapterProperty property,
  size_t bufferSize,
  _Out_writes_bytes_(bufferSize) void *propertyData) = 0;

template <class T>
HRESULT GetProperty( 
  DXCoreAdapterProperty property,
  _Out_writes_bytes_(sizeof(T)) T *propertyData);
```

## Parameters

### property

Type: **[DXCoreAdapterProperty](./ne-dxcore_interface-dxcoreadapterproperty.md)**

The type of the property whose value you wish to retrieve. See the table in [DXCoreAdapterProperty](./ne-dxcore_interface-dxcoreadapterproperty.md) for more info about each adapter property.

### bufferSize

Type: **size_t**

The size, in bytes, of the output buffer that you allocate and provide in *propertyData*.

### propertyData [out]

Type: **void\***

A pointer to an output buffer that you allocate in your application, and that the function fills in. Call [GetPropertySize](./nf-dxcore_interface-idxcoreadapter-getpropertysize.md) to determine the size that the *propertyData* buffer should be for a given adapter property.

## Returns

Type: **[HRESULT](../../com/structure-of-com-error-codes.md)**

If the function succeeds, it returns **S_OK**. Otherwise, it returns an [**HRESULT**](../../com/structure-of-com-error-codes.md) [error code](../../com/com-error-codes-10.md).

|Return value|Description|
|-|-|
|DXGI_ERROR_INVALID_CALL|The property type specified in *property* is not recognized by this operating system (OS). Call [IsPropertySupported](./nf-dxcore_interface-idxcoreadapter-ispropertysupported.md) to confirm that the property type is available for this adapter and operating system (OS).|
|DXGI_ERROR_UNSUPPORTED|The property type specified in *property* is not supported by the adapter. Call [IsPropertySupported](./nf-dxcore_interface-idxcoreadapter-ispropertysupported.md) to confirm that the property type is available for this adapter and operating system (OS).|
|E_INVALIDARG|An insufficient buffer size is provided in *propertyData*. Call [GetPropertySize](./nf-dxcore_interface-idxcoreadapter-getpropertysize.md) to determine the size that the *propertyData* buffer should be for a given adapter property.|
|E_POINTER|`nullptr` was provided for *propertyData*.|

## Remarks

You can call **GetProperty** on an adapter that's no longer valid&mdash;the function won't fail as a result of that. This function zeros out the *propertyData* buffer prior to filling it in.

## See also

[IDXCoreAdapter](./nn-dxcore_interface-idxcoreadapter.md), [DXCore Reference](../dxcore-reference.md), [Using DXCore to enumerate adapters](../dxcore-enum-adapters.md)
