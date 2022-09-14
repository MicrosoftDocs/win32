---
title: IDXCoreAdapterList::GetAdapter
description: Retrieves a specific adapter by index from a DXCore adapter list object.
ms.topic: reference
ms.date: 06/20/2019
---

# IDXCoreAdapterList::GetAdapter method

Retrieves a specific adapter by index from a DXCore adapter list object. For programming guidance, and code examples, see [Using DXCore to enumerate adapters](../dxcore-enum-adapters.md).

## Syntax

```cpp
virtual HRESULT STDMETHODCALLTYPE GetAdapter(
  uint32_t index,
  REFIID riid,
  _COM_Outptr_ void **ppvAdapter) = 0;

template<class T>
HRESULT STDMETHODCALLTYPE GetAdapter( 
  uint32_t index,
  _COM_Outptr_ T **ppvAdapter);
```

## Parameters

### index

Type: **uint32_t**

A zero-based index, identifying an adapter instance within the DXCore adapter list.

### riid

Type: **REFIID**

A reference to the globally unique identifier (GUID) of the interface that you wish to be returned in *ppvAdapter*. This is expected to be the interface identifier (IID) of [IDXCoreAdapter](./nn-dxcore_interface-idxcoreadapter.md).

### ppvAdapter [out]

Type: **void\*\***

The address of a pointer to an interface with the IID specified in the *riid* parameter. Upon successful return, *\*ppvAdapter* (the dereferenced address) contains a pointer to the DXCore adapter created.

## Returns

Type: **[HRESULT](../../com/structure-of-com-error-codes.md)**

If the function succeeds, it returns **S_OK**. Otherwise, it returns an [**HRESULT**](../../com/structure-of-com-error-codes.md) [error code](../../com/com-error-codes-10.md).

|Return value|Description|
|-|-|
|DXGI_ERROR_DEVICE_REMOVED|The *index* is valid, but the adapter is no longer in a valid state.|
|E_INVALIDARG|The provided *index* is not valid.|
|E_NOINTERFACE|An invalid value was provided for *riid*.|
|E_POINTER|`nullptr` was provided for *ppvAdapter*.|

## Remarks

Multiple calls passing an index that represents the same adapter return identical interface pointers, even across different adapter lists. As a result, it's safe to compare interface pointers to determine whether multiple pointers refer to the same adapter object.

## See also

[IDXCoreAdapterList](./nn-dxcore_interface-idxcoreadapterlist.md), [DXCore Reference](../dxcore-reference.md), [Using DXCore to enumerate adapters](../dxcore-enum-adapters.md)
