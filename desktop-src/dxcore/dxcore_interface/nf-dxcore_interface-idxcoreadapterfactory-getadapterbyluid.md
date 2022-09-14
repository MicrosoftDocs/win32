---
title: IDXCoreAdapterFactory::GetAdapterByLuid
description: Retrieves the DXCore adapter object ([IDXCoreAdapter](./nn-dxcore_interface-idxcoreadapter.md)) for a specified LUID, if available.
ms.topic: reference
ms.date: 06/20/2019
---

# IDXCoreAdapterFactory::GetAdapterByLuid method

Retrieves the DXCore adapter object ([IDXCoreAdapter](./nn-dxcore_interface-idxcoreadapter.md)) for a specified LUID, if available. For programming guidance, and code examples, see [Using DXCore to enumerate adapters](../dxcore-enum-adapters.md).

## Syntax

```cpp
virtual HRESULT STDMETHODCALLTYPE GetAdapterByLuid( 
  const LUID &adapterLUID,
   REFIID riid,
  _COM_Outptr_ void **ppvAdapter) = 0;

template<class T>
HRESULT STDMETHODCALLTYPE GetAdapterByLuid( 
  const LUID &adapterLUID,
  _COM_Outptr_ T **ppvAdapter);
```

## Parameters

### adapterLUID

Type: **[LUID](/windows/win32/api/winnt/ns-winnt-luid) const\&**

The locally unique value that identifies the adapter instance.

### riid [in]

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
|DXGI_ERROR_DEVICE_REMOVED|The adapter LUID passed in *adapterLUID* is recognized, but the adapter is no longer in a valid state.|
|E_INVALIDARG|No such adapter LUID as the value passed in *adapterLUID* is available through DXCore.|
|E_NOINTERFACE|An invalid value was provided for *riid*.|
|E_POINTER|`nullptr` was provided for *ppvAdapter*.|

## Remarks

Multiple calls passing the same [LUID](/windows/win32/api/winnt/ns-winnt-luid) return identical interface pointers. As a result, it's safe to compare interface pointers to determine whether multiple pointers refer to the same adapter object.

## See also

[IDXCoreAdapterFactory](./nn-dxcore_interface-idxcoreadapterfactory.md), [DXCore Reference](../dxcore-reference.md), [Using DXCore to enumerate adapters](../dxcore-enum-adapters.md)
