---
UID: NF:dxcore_interface.IDXCoreAdapter.QueryState
title: IDXCoreAdapter::QueryState
description: Retrieves the current state of the specified item on the adapter.
author: windows-sdk-content
tech.root: dxcore
ms.author: windowssdkdev
ms.date: 06/10/2019
ms.keywords: IDXCoreAdapter interface,QueryState method, IDXCoreAdapter.QueryState, IDXCoreAdapter::QueryState, QueryState, QueryState method, QueryState method,IDXCoreAdapter interface, dxcore/IDXCoreAdapter::QueryState, dxcore_interface.idxcoreadapterfactory_querystate
ms.localizationpriority: low
ms.topic: method
targetos: Windows
product: Windows
req.assembly: 
req.construct-type: method
req.ddi-compliance: 
req.dll: dxcore.dll
req.header: dxcore_interface.h
req.idl: 
req.include-header: dxcore.h
req.irql: 
req.kmdf-ver: 
req.lib: dxcore.lib
req.max-support: 
req.namespace: 
req.redist: 
req.target-min-winverclnt: Windows 10 (Build 18936)
req.target-min-winversvr: 
req.target-type: Windows
req.type-library: 
req.umdf-ver: 
req.unicode-ansi: 
topic_type:
 - apiref
 - kbsyntax
api_type:
 - COM
api_location:
 - dxcore.dll
api_name:
 - IDXCoreAdapter::QueryState
---

# IDXCoreAdapter::QueryState method

> [!NOTE]
> **Some information relates to pre-released product, which may be substantially modified before it's commercially released. Microsoft makes no warranties, express or implied, with respect to the information provided here.**

> [!IMPORTANT]
> The feature described in this topic is available in pre-release versions of the [Windows 10 Insider Preview](https://www.microsoft.com/software-download/windowsinsiderpreviewSDK).

## Description

Retrieves the current state of the specified item on the adapter. Before calling **QueryState** for a property type, call [IsQueryStateSupported](/windows/desktop/dxcore/dxcore_interface/nf-dxcore_interface-idxcoreadapter-isquerystatesupported) to confirm that querying the state kind is available for this adapter and operating system (OS).

## Parameters

### state

Type: **[DXCoreAdapterState](/windows/desktop/dxcore/dxcore_interface/ne-dxcore_interface-dxcoreadapterstate)**

The kind of state item on the adapter whose state you wish to retrieve. See the table in [DXCoreAdapterState](/windows/desktop/dxcore/dxcore_interface/ne-dxcore_interface-dxcoreadapterstate) for more info about each adapter state kind.

### inputStateDetailsSize

Type: **size_t**

The size, in bytes, of the input state details buffer that you (optionally) allocate and provide in *inputStateDetails*.

### inputStateDetails [in]

Type: **void const\***

An optional pointer to a constant input state details buffer that you allocate in your application, containing any information about your request that's required for the state kind you specify in *state*. See the table in [DXCoreAdapterState](/windows/desktop/dxcore/dxcore_interface/ne-dxcore_interface-dxcoreadapterstate) for more info about any input buffer requirement for a given state kind.

### outputBufferSize

Type: **size_t**

The size, in bytes, of the output buffer that you allocate and provide in *outputBuffer*.

### outputBuffer [out]

Type: **void\***

A pointer to an output buffer that you allocate in your application, and that the function fills in. See the table in [DXCoreAdapterState](/windows/desktop/dxcore/dxcore_interface/ne-dxcore_interface-dxcoreadapterstate) for more info about the output buffer requirement for a given state kind.

## Returns

Type: **[HRESULT](/windows/desktop/com/structure-of-com-error-codes)**

If the function succeeds, it returns **S_OK**. Otherwise, it returns an [**HRESULT**](/windows/desktop/com/structure-of-com-error-codes) [error code](/windows/desktop/com/com-error-codes-10).

|Return value|Description|
|-|-|
|DXGI_ERROR_DEVICE_REMOVED|The adapter is no longer in a valid state.|
|DXGI_ERROR_INVALID_CALL|The state kind specified in *state* is not recognized by this operating system (OS). Call [IsQueryStateSupported](/windows/desktop/dxcore/dxcore_interface/nf-dxcore_interface-idxcoreadapter-isquerystatesupported) to confirm that querying the state kind is available for this adapter and operating system (OS).|
|DXGI_ERROR_UNSUPPORTED|The state kind specified in *state* is not supported by the adapter. Call [IsQueryStateSupported](/windows/desktop/dxcore/dxcore_interface/nf-dxcore_interface-idxcoreadapter-isquerystatesupported) to confirm that querying the state kind is available for this adapter and operating system (OS).|
|E_INVALIDARG|An insufficient buffer size is provided for *outputBuffer* (or for *inputStateDetails* where an input state details buffer is necessary).|
|E_POINTER|`nullptr` was provided for *outputBuffer* (or for *inputStateDetails* where an input state details buffer is necessary).|

## Remarks

See [DXCoreAdapterState](/windows/desktop/dxcore/dxcore_interface/ne-dxcore_interface-dxcoreadapterstate) for more info about each adapter state kind, and what inputs and outputs are used. This function zeros out the *outputBuffer* buffer prior to filling it in.

## See also

[IDXCoreAdapter](/windows/desktop/dxcore/dxcore_interface/nn-dxcore_interface-idxcoreadapter), [DXCore Reference](/windows/desktop/dxcore/dxcore-reference), [Using DXCore to enumerate adapters](/windows/desktop/dxcore/dxcore-enum-adapters)
