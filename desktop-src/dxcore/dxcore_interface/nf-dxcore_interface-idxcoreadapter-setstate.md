---
title: IDXCoreAdapter::SetState
description: Sets the state of the specified item on the adapter.
ms.topic: reference
ms.date: 06/20/2019
---

# IDXCoreAdapter::SetState method

Sets the state of the specified item on the adapter. Before calling **SetState** for a property type, call [IsSetStateSupported](./nf-dxcore_interface-idxcoreadapter-issetstatesupported.md) to confirm that setting the state kind is available for this adapter and operating system (OS).

## Syntax

```cpp
virtual HRESULT STDMETHODCALLTYPE SetState( 
  DXCoreAdapterState state,
  size_t inputStateDetailsSize,
  _In_reads_bytes_opt_(inputStateDetailsSize) const void *inputStateDetails,
  size_t inputDataSize,
  _In_reads_bytes_(inputDataSize) const void *inputData) = 0;

template <class T1, class T2>
HRESULT SetState( 
  DXCoreAdapterState state,
  const T1 *inputStateDetails,
  const T2 *inputData);
```

## Parameters

### state

Type: **[DXCoreAdapterState](./ne-dxcore_interface-dxcoreadapterstate.md)**

The kind of state item on the adapter whose state you wish to set. See the table in [DXCoreAdapterState](./ne-dxcore_interface-dxcoreadapterstate.md) for more info about each adapter state kind.

### inputStateDetailsSize

Type: **size_t**

The size, in bytes, of the input state details buffer that you (optionally) allocate and provide in *inputStateDetails*.

### inputStateDetails [in]

Type: **void const\***

An optional pointer to a constant input state details buffer that you allocate in your application, containing any information about your request that's required for the state kind you specify in *state*. See the table in [DXCoreAdapterState](./ne-dxcore_interface-dxcoreadapterstate.md) for more info about any input buffer requirement for a given state kind.

### inputDataSize

Type: **size_t**

The size, in bytes, of the input buffer that you allocate and provide in *inputData*.

### inputData [in]

Type: **void\***

A pointer to an input buffer that you allocate in your application, containing the state information to set for the state item whose kind you specify in *state*. See the table in [DXCoreAdapterState](./ne-dxcore_interface-dxcoreadapterstate.md) for more info about the input buffer requirement for a given state kind.

## Returns

Type: **[HRESULT](../../com/structure-of-com-error-codes.md)**

If the function succeeds, it returns **S_OK**. Otherwise, it returns an [**HRESULT**](../../com/structure-of-com-error-codes.md) [error code](../../com/com-error-codes-10.md).

|Return value|Description|
|-|-|
|DXGI_ERROR_DEVICE_REMOVED|The adapter is no longer in a valid state.|
|DXGI_ERROR_INVALID_CALL|The state kind specified in *state* is not recognized by this operating system (OS). Call [IsSetStateSupported](./nf-dxcore_interface-idxcoreadapter-issetstatesupported.md) to confirm that setting the state kind is available for this adapter and operating system (OS).|
|DXGI_ERROR_UNSUPPORTED|The state kind specified in *state* is not supported by the adapter. Call [IsSetStateSupported](./nf-dxcore_interface-idxcoreadapter-issetstatesupported.md) to confirm that setting the state kind is available for this adapter and operating system (OS).|
|E_INVALIDARG|An insufficient buffer size is provided for *inputData* (or for *inputStateDetails* where an input state details buffer is necessary).|
|E_POINTER|`nullptr` was provided for *inputData* (or for *inputStateDetails* where an input state details buffer is necessary).|

## See also

[IDXCoreAdapter](./nn-dxcore_interface-idxcoreadapter.md), [DXCore Reference](../dxcore-reference.md), [Using DXCore to enumerate adapters](../dxcore-enum-adapters.md)
