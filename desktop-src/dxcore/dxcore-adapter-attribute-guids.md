---
title: DXCore adapter attribute GUIDs
description: The following adapter attribute GUIDs are declared in `dxcore_interface.h`, and are used with the [IDXCoreAdapterFactory::CreateAdapterList](./dxcore_interface/nf-dxcore_interface-idxcoreadapterfactory-createadapterlist.md) and [IDXCoreAdapter::IsAttributeSupported](./dxcore_interface/nf-dxcore_interface-idxcoreadapter-isattributesupported.md) methods.
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
ms.localizationpriority: low
ms.topic: reference
ms.date: 06/20/2019
---

# DXCore adapter attribute GUIDs

The following adapter attribute GUIDs are declared in `dxcore_interface.h`, and are used with the [IDXCoreAdapterFactory::CreateAdapterList](./dxcore_interface/nf-dxcore_interface-idxcoreadapterfactory-createadapterlist.md) and [IDXCoreAdapter::IsAttributeSupported](./dxcore_interface/nf-dxcore_interface-idxcoreadapter-isattributesupported.md) methods. For any given adapter, one or more of the attributes could apply.

| GUID | Value |
|-|-|
| `DXCORE_ADAPTER_ATTRIBUTE_D3D11_GRAPHICS`. Specifies an adapter that supports being used with the [Direct3D 11](/windows/win32/direct3d11) graphics APIs. No guarantees are made about specific features, nor is a guarantee made that the OS in its current configuration supports these APIs. | 0x8c47866b, 0x7583, 0x450d, 0xf0, 0xf0, 0x6b, 0xad, 0xa8, 0x95, 0xaf, 0x4b |
| `DXCORE_ADAPTER_ATTRIBUTE_D3D12_GRAPHICS`. Specifies an adapter that supports being used with the [Direct3D 12](/windows/win32/direct3d12) graphics APIs. No guarantees are made about specific features, nor is a guarantee made that the OS in its current configuration supports these APIs. | 0x0c9ece4d, 0x2f6e, 0x4f01, 0x8c, 0x96, 0xe8, 0x9e, 0x33, 0x1b, 0x47, 0xb1 |
| `DXCORE_ADAPTER_ATTRIBUTE_D3D12_CORE_COMPUTE`. Specifies an adapter that supports being used with the [Direct3D 12 Core](../direct3d12/core-feature-levels.md) compute APIs. No guarantees are made about specific features, nor is a guarantee made that the OS in its current configuration supports these APIs. | 0x248e2800, 0xa793, 0x4724, 0xab, 0xaa, 0x23, 0xa6, 0xde, 0x1b, 0xe0, 0x90 |

## Requirements

| Requirement | Value |
|-|-|
| Header | dxcore_interface.h |

## See also

* [IDXCoreAdapterFactory::CreateAdapterList](./dxcore_interface/nf-dxcore_interface-idxcoreadapterfactory-createadapterlist.md)
* [IDXCoreAdapter::IsAttributeSupported](./dxcore_interface/nf-dxcore_interface-idxcoreadapter-isattributesupported.md)
* [DXCore Reference](./dxcore-reference.md)
* [Using DXCore to enumerate adapters](./dxcore-enum-adapters.md)
* [Direct3D 12 graphics](../direct3d12/direct3d-12-graphics.md)
