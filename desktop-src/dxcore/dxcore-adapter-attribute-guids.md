---
title: DXCore adapter attribute GUIDs
description: The following adapter attribute GUIDs are declared in `dxcore_interface.h`, and are used with the [IDXCoreAdapterFactory::CreateAdapterList](/windows/win32/dxcore/dxcore_interface/nf-dxcore_interface-idxcoreadapterfactory-createadapterlist) and [IDXCoreAdapter::IsAttributeSupported](/windows/win32/dxcore/dxcore_interface/nf-dxcore_interface-idxcoreadapter-isattributesupported) methods.
keywords:
- DXCore, adapter attribute, GUIDs
topic_type:
- apiref
api_name:
- DXCore adapter attribute GUIDs
api_location:
- dxcore_interface.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 09/19/2024
---

# DXCore adapter attribute GUIDs

The following adapter attribute GUIDs are declared in `dxcore_interface.h`, and are used with the [IDXCoreAdapterFactory::CreateAdapterList](/windows/win32/dxcore/dxcore_interface/nf-dxcore_interface-idxcoreadapterfactory-createadapterlist) and [IDXCoreAdapter::IsAttributeSupported](/windows/win32/dxcore/dxcore_interface/nf-dxcore_interface-idxcoreadapter-isattributesupported) methods. For any given adapter, one or more of the attributes could apply.

| GUID | Value |
|-|-|
| `DXCORE_ADAPTER_ATTRIBUTE_D3D11_GRAPHICS`. Specifies an adapter that supports being used with the [Direct3D 11](/windows/win32/direct3d11) graphics APIs. No guarantees are made about specific features, nor is a guarantee made that the OS in its current configuration supports these APIs. | 0x8c47866b, 0x7583, 0x450d, 0xf0, 0xf0, 0x6b, 0xad, 0xa8, 0x95, 0xaf, 0x4b |
| `DXCORE_ADAPTER_ATTRIBUTE_D3D12_GENERIC_ML`. A driver reports this attribute as a GUID in their INF if the device supports DirectX meta-commands required for ML workloads. | 0xb71b0d41, 0x1088, 0x422f, 0xa2, 0x7c, 0x2, 0x50, 0xb7, 0xd3, 0xa9, 0x88 |
| `DXCORE_ADAPTER_ATTRIBUTE_D3D12_GENERIC_MEDIA`. A driver reports this attribute as a GUID in their INF if the device supports video processing workloads. | 0x8eb2c848, 0x82f6, 0x4b49, 0xaa, 0x87, 0xae, 0xcf, 0xcf, 0x1, 0x74, 0xc6 |
| `DXCORE_ADAPTER_ATTRIBUTE_D3D12_GRAPHICS`. Specifies an adapter that supports being used with the [Direct3D 12](/windows/win32/direct3d12) graphics APIs. No guarantees are made about specific features, nor is a guarantee made that the OS in its current configuration supports these APIs. | 0x0c9ece4d, 0x2f6e, 0x4f01, 0x8c, 0x96, 0xe8, 0x9e, 0x33, 0x1b, 0x47, 0xb1 |
| `DXCORE_ADAPTER_ATTRIBUTE_D3D12_CORE_COMPUTE`. Specifies an adapter that supports being used with the [Direct3D 12 Core](../direct3d12/core-feature-levels.md) compute APIs. No guarantees are made about specific features, nor is a guarantee made that the OS in its current configuration supports these APIs. | 0x248e2800, 0xa793, 0x4724, 0xab, 0xaa, 0x23, 0xa6, 0xde, 0x1b, 0xe0, 0x90 |

## Runtime-agnostic hardware types

A class of runtime-agnostic attribute GUIDs (that indicate hardware type) can be queried from the driver. These GUIDs indicate the primary function of a device, allowing the [IDXCoreAdapterFactory1::CreateAdapterListByWorkload](/windows/win32/dxcore/dxcore_interface/nf-dxcore_interface-idxcoreadapterfactory-createadapterlist) method to reason about the hardware that the user is requesting. In addition, some NPUs implement an MCDM kernel mode driver, but don't support the Direct 3D runtime (and instead use private interfaces or other runtimes at the user-mode level). So these attribute GUIDs allow DXCore to support devices that don't have a Direct 3D user-mode driver; and enable Task Manager to accurately label adapters without needing to infer the hardware type based on Direct 3D runtime support. Exactly one of these GUIDs will be reported by a driver, or inferred by DXCore, whether or not they support Direct 3D.

| GUID | Value |
|-|-|
| `DXCORE_HARDWARE_TYPE_ATTRIBUTE_NPU`. Declared by NPUs with or without compute shader support. | 0xb69eb219, 0x3ded, 0x4464, 0x97, 0x9f, 0xa0, 0xb, 0xd4, 0x68, 0x70, 0x6 |
| `DXCORE_HARDWARE_TYPE_ATTRIBUTE_GPU`. Declared by GPUs. | 0xe0b195da, 0x58ef, 0x4a22, 0x90, 0xf1, 0x1f, 0x28, 0x16, 0x9c, 0xab, 0x8d |
| `DXCORE_HARDWARE_TYPE_ATTRIBUTE_COMPUTE_ACCELERATOR`. Declared by compute accelerators. | 0xd46140c4, 0xadd7, 0x451b, 0x9e, 0x56, 0x6, 0xfe, 0x8c, 0x3b, 0x58, 0xed |
| `DXCORE_HARDWARE_TYPE_ATTRIBUTE_MEDIA_ACCELERATOR`. Declared by media accelerators. | 0x66bdb96a, 0x50b, 0x44c7, 0xa4, 0xfd, 0xd1, 0x44, 0xce, 0xa, 0xb4, 0x43 |

## Requirements

| Requirement | Value |
|-|-|
| Header | dxcore_interface.h |

## See also

* [IDXCoreAdapterFactory::CreateAdapterList](/windows/win32/dxcore/dxcore_interface/nf-dxcore_interface-idxcoreadapterfactory-createadapterlist)
* [IDXCoreAdapter::IsAttributeSupported](/windows/win32/dxcore/dxcore_interface/nf-dxcore_interface-idxcoreadapter-isattributesupported)
* [DXCore reference](./dxcore-reference.md)
* [Using DXCore to enumerate adapters](./dxcore-enum-adapters.md)
* [Direct3D 12 graphics](../direct3d12/direct3d-12-graphics.md)
