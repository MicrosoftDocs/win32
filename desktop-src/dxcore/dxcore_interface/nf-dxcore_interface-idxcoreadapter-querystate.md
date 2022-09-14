---
title: IDXCoreAdapter::QueryState
description: Retrieves the current state of the specified item on the adapter.
ms.topic: reference
ms.date: 06/20/2019
---

# IDXCoreAdapter::QueryState method

Retrieves the current state of the specified item on the adapter. Before calling **QueryState** for a property type, call [IsQueryStateSupported](./nf-dxcore_interface-idxcoreadapter-isquerystatesupported.md) to confirm that querying the state kind is available for this adapter and operating system (OS).

## Syntax

```cpp
virtual HRESULT STDMETHODCALLTYPE QueryState( 
  DXCoreAdapterState state,
  size_t inputStateDetailsSize,
  _In_reads_bytes_opt_(inputStateDetailsSize) const void *inputStateDetails,
  size_t outputBufferSize,
  _Out_writes_bytes_(outputBufferSize) void *outputBuffer) = 0;

template <class T1, class T2>
HRESULT QueryState( 
  DXCoreAdapterState state,
  _In_reads_bytes_opt_(sizeof(T1)) const T1 *inputStateDetails,
  _Out_writes_bytes_(sizeof(T2)) T2 *outputBuffer);

template <class T>
HRESULT QueryState( 
  DXCoreAdapterState state,
  _Out_writes_bytes_(sizeof(T)) T *outputBuffer);
```

## Parameters

### state

Type: **[DXCoreAdapterState](./ne-dxcore_interface-dxcoreadapterstate.md)**

The kind of state item on the adapter whose state you wish to retrieve. See the table in [DXCoreAdapterState](./ne-dxcore_interface-dxcoreadapterstate.md) for more info about each adapter state kind.

### inputStateDetailsSize

Type: **size_t**

The size, in bytes, of the input state details buffer that you (optionally) allocate and provide in *inputStateDetails*.

### inputStateDetails [in]

Type: **void const\***

An optional pointer to a constant input state details buffer that you allocate in your application, containing any information about your request that's required for the state kind you specify in *state*. See the table in [DXCoreAdapterState](./ne-dxcore_interface-dxcoreadapterstate.md) for more info about any input buffer requirement for a given state kind.

### outputBufferSize

Type: **size_t**

The size, in bytes, of the output buffer that you allocate and provide in *outputBuffer*.

### outputBuffer [out]

Type: **void\***

A pointer to an output buffer that you allocate in your application, and that the function fills in. See the table in [DXCoreAdapterState](./ne-dxcore_interface-dxcoreadapterstate.md) for more info about the output buffer requirement for a given state kind.

## Returns

Type: **[HRESULT](../../com/structure-of-com-error-codes.md)**

If the function succeeds, it returns **S_OK**. Otherwise, it returns an [**HRESULT**](../../com/structure-of-com-error-codes.md) [error code](../../com/com-error-codes-10.md).

|Return value|Description|
|-|-|
|DXGI_ERROR_DEVICE_REMOVED|The adapter is no longer in a valid state.|
|DXGI_ERROR_INVALID_CALL|The state kind specified in *state* is not recognized by this operating system (OS). Call [IsQueryStateSupported](./nf-dxcore_interface-idxcoreadapter-isquerystatesupported.md) to confirm that querying the state kind is available for this adapter and operating system (OS).|
|DXGI_ERROR_UNSUPPORTED|The state kind specified in *state* is not supported by the adapter. Call [IsQueryStateSupported](./nf-dxcore_interface-idxcoreadapter-isquerystatesupported.md) to confirm that querying the state kind is available for this adapter and operating system (OS).|
|E_INVALIDARG|An insufficient buffer size is provided for *outputBuffer* (or for *inputStateDetails* where an input state details buffer is necessary).|
|E_POINTER|`nullptr` was provided for *outputBuffer* (or for *inputStateDetails* where an input state details buffer is necessary).|

## Remarks

See [DXCoreAdapterState](./ne-dxcore_interface-dxcoreadapterstate.md) for more info about each adapter state kind, and what inputs and outputs are used. This function zeros out the *outputBuffer* buffer prior to filling it in.

## See also

[IDXCoreAdapter](./nn-dxcore_interface-idxcoreadapter.md), [DXCore Reference](../dxcore-reference.md), [Using DXCore to enumerate adapters](../dxcore-enum-adapters.md)
