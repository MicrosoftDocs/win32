---
title: IDXCoreAdapter::SetState
description: Sets the state of the specified item on the adapter.
ms.localizationpriority: low
ms.topic: reference
ms.date: 06/20/2019
---

# IDXCoreAdapter::SetState method

> [!NOTE]
> **Some information relates to pre-released product, which may be substantially modified before it's commercially released. Microsoft makes no warranties, express or implied, with respect to the information provided here.**

> [!IMPORTANT]
> The feature described in this topic is available in pre-release versions of the [Windows 10 Insider Preview](https://www.microsoft.com/software-download/windowsinsiderpreviewSDK).

Sets the state of the specified item on the adapter. Before calling **SetState** for a property type, call [IsSetStateSupported](/windows/win32/dxcore/dxcore_interface/nf-dxcore_interface-idxcoreadapter-issetstatesupported) to confirm that setting the state kind is available for this adapter and operating system (OS).

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

Type: **[DXCoreAdapterState](/windows/win32/dxcore/dxcore_interface/ne-dxcore_interface-dxcoreadapterstate)**

The kind of state item on the adapter whose state you wish to set. See the table in [DXCoreAdapterState](/windows/win32/dxcore/dxcore_interface/ne-dxcore_interface-dxcoreadapterstate) for more info about each adapter state kind.

### inputStateDetailsSize

Type: **size_t**

The size, in bytes, of the input state details buffer that you (optionally) allocate and provide in *inputStateDetails*.

### inputStateDetails [in]

Type: **void const\***

An optional pointer to a constant input state details buffer that you allocate in your application, containing any information about your request that's required for the state kind you specify in *state*. See the table in [DXCoreAdapterState](/windows/win32/dxcore/dxcore_interface/ne-dxcore_interface-dxcoreadapterstate) for more info about any input buffer requirement for a given state kind.

### inputDataSize

Type: **size_t**

The size, in bytes, of the input buffer that you allocate and provide in *inputData*.

### inputData [in]

Type: **void\***

A pointer to an input buffer that you allocate in your application, containing the state information to set for the state item whose kind you specify in *state*. See the table in [DXCoreAdapterState](/windows/win32/dxcore/dxcore_interface/ne-dxcore_interface-dxcoreadapterstate) for more info about the input buffer requirement for a given state kind.

## Returns

Type: **[HRESULT](/windows/win32/com/structure-of-com-error-codes)**

If the function succeeds, it returns **S_OK**. Otherwise, it returns an [**HRESULT**](/windows/win32/com/structure-of-com-error-codes) [error code](/windows/win32/com/com-error-codes-10).

|Return value|Description|
|-|-|
|DXGI_ERROR_DEVICE_REMOVED|The adapter is no longer in a valid state.|
|DXGI_ERROR_INVALID_CALL|The state kind specified in *state* is not recognized by this operating system (OS). Call [IsSetStateSupported](/windows/win32/dxcore/dxcore_interface/nf-dxcore_interface-idxcoreadapter-issetstatesupported) to confirm that setting the state kind is available for this adapter and operating system (OS).|
|DXGI_ERROR_UNSUPPORTED|The state kind specified in *state* is not supported by the adapter. Call [IsSetStateSupported](/windows/win32/dxcore/dxcore_interface/nf-dxcore_interface-idxcoreadapter-issetstatesupported) to confirm that setting the state kind is available for this adapter and operating system (OS).|
|E_INVALIDARG|An insufficient buffer size is provided for *inputData* (or for *inputStateDetails* where an input state details buffer is necessary).|
|E_POINTER|`nullptr` was provided for *inputData* (or for *inputStateDetails* where an input state details buffer is necessary).|

## See also

[IDXCoreAdapter](/windows/win32/dxcore/dxcore_interface/nn-dxcore_interface-idxcoreadapter), [DXCore Reference](/windows/win32/dxcore/dxcore-reference), [Using DXCore to enumerate adapters](/windows/win32/dxcore/dxcore-enum-adapters)
