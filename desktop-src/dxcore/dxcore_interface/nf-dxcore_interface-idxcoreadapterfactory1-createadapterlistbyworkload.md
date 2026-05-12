---
title: IDXCoreAdapterFactory1::CreateAdapterListByWorkload
description: Generates a list of adapter objects representing the current adapter state of the system, and meeting the workload and hardware type criteria specified.
ms.topic: reference
ms.date: 09/27/2024
---

# IDXCoreAdapterFactory1::CreateAdapterListByWorkload method

Generates a list of adapter objects representing the current adapter state of the system, and meeting the workload and hardware type criteria specified. For programming guidance, and code examples, see [Using DXCore to enumerate adapters](/windows/win32/dxcore/dxcore-enum-adapters). With **CreateAdapterListByWorkload**, DXCore supports neural processing units (NPUs), which process machine-learning (ML) workloads, and media accelerators, for video encode/decode/processing workloads.

You can retrieve MCDM NPUs and media accelerators by calling [CreateAdapterList](./nf-dxcore_interface-idxcoreadapterfactory-createadapterlist.md), but the default sorting for that method is based on runtime capabilities and device performance. **CreateAdapterListByWorkload** allows DXCore to provide an adapter list sorted by what works best for a given workload, based on operating system (OS) policy, that you can easily narrow down by the type of hardware and level of Direct 3D runtime support. The default sorting in **CreateAdapterListByWorkload** can be thought of as the opposite of **CreateAdapterList**, where more specialized hardware is prioritized in the ordering that may be less generally capable than a full GPU.

## Syntax

```cpp
virtual HRESULT STDMETHODCALLTYPE CreateAdapterListByWorkload(
    DXCoreWorkload workload,
    DXCoreRuntimeFilterFlags runtimeFilter,
    DXCoreHardwareTypeFilterFlags hardwareTypeFilter,
    REFIID riid,
    _COM_Outptr_ void **ppvAdapterList) = 0;

template<class T>
HRESULT STDMETHODCALLTYPE CreateAdapterListByWorkload(
    DXCoreWorkload workload,
    DXCoreRuntimeFilterFlags runtimeFilter,
    DXCoreHardwareTypeFilterFlags hardwareTypeFilter,
    _COM_Outptr_ T **ppvAdapterList);
```

## Parameters

### workload

TBD

### runtimeFilter

TBD

### hardwareTypeFilter

TBD

### riid

Type: **REFIID**

A reference to the globally unique identifier (GUID) of the interface that you wish to be returned in *ppvAdapterList*. This is expected to be the interface identifier (IID) of [IDXCoreAdapterList](/windows/win32/dxcore/dxcore_interface/nn-dxcore_interface-idxcoreadapterlist).

### ppvAdapterList [out]

Type: **void\*\***

The address of a pointer to an interface with the IID specified in the *riid* parameter. Upon successful return, *\*ppvAdapterList* (the dereferenced address) contains a pointer to the adapter list created.

## Returns

Type: **[HRESULT](/windows/win32/com/structure-of-com-error-codes)**

If the function succeeds, it returns **S_OK**. Otherwise, it returns an [**HRESULT**](/windows/win32/com/structure-of-com-error-codes) [error code](/windows/win32/com/com-error-codes-10).

|Return value|Description|
|-|-|
|E_INVALIDARG|A value was provided outside of the range of the *workload*, *runtimeFilter*, or *hardwareTypeFilter* parameters.|
|E_NOINTERFACE|An invalid value was provided for *riid*.|
|E_POINTER|`nullptr` was provided for *ppvAdapterList*.|

## Remarks

Even if no adapters are found, as long as the arguments are valid, **CreateAdapterListByWorkload** creates a valid [IDXCoreAdapterList](/windows/win32/dxcore/dxcore_interface/nn-dxcore_interface-idxcoreadapterlist) object, and returns **S_OK**. Once generated, the adapters in this specific list won't change. But the list will be considered stale if one of the adapters later becomes invalid, or if a new adapter arrives that meets the provided filter criteria. The list returned by **CreateAdapterList** is not ordered in any particular way, and multiple calls to **CreateAdapterList** may produce differently ordered lists.

The resulting list is not ordered in any particular way, but the ordering of a list is consistent across multiple calls, and even across operating system restarts. The ordering may change upon system configuration changes, including the addition or removal of an adapter, or a driver update on an existing adapter.

## See also

[IDXCoreAdapterFactory](/windows/win32/dxcore/dxcore_interface/nn-dxcore_interface-idxcoreadapterfactory), [DXCore reference](/windows/win32/dxcore/dxcore-reference), [DXCore adapter attribute GUIDs](/windows/win32/dxcore/dxcore-adapter-attribute-guids), [Using DXCore to enumerate adapters](/windows/win32/dxcore/dxcore-enum-adapters)
