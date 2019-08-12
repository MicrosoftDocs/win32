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
ms.localizationpriority: low
ms.topic: article
ms.date: 06/20/2019
---

# DXCore adapter attribute GUIDs

> [!NOTE]
> **Some information relates to pre-released product, which may be substantially modified before it's commercially released. Microsoft makes no warranties, express or implied, with respect to the information provided here.**

> [!IMPORTANT]
> The feature described in this topic is available in pre-release versions of the [Windows 10 Insider Preview](https://www.microsoft.com/software-download/windowsinsiderpreviewSDK).

The following adapter attribute GUIDs are declared in `dxcore_interface.h`, and are used with the [IDXCoreAdapterFactory::CreateAdapterList](/windows/win32/dxcore/dxcore_interface/nf-dxcore_interface-idxcoreadapterfactory-createadapterlist) and [IDXCoreAdapter::IsAttributeSupported](/windows/win32/dxcore/dxcore_interface/nf-dxcore_interface-idxcoreadapter-isattributesupported) methods. For any given adapter, one or more of the attributes could apply.

| GUID | Value |
|-|-|
| DXCORE_ADAPTER_ATTRIBUTE_D3D11_GRAPHICS. Specifies an adapter that supports being used with the [Direct3D 11](/windows/win32/direct3d11) graphics APIs. No guarantees are made about specific features, nor is a guarantee made that the OS in its current configuration supports these APIs. | 0x8c47866b, 0x7583, 0x450d, 0xf0, 0xf0, 0x6b, 0xad, 0xa8, 0x95, 0xaf, 0x4b |
| DXCORE_ADAPTER_ATTRIBUTE_D3D12_GRAPHICS. Specifies an adapter that supports being used with the [Direct3D 12](/windows/win32/direct3d12) graphics APIs. No guarantees are made about specific features, nor is a guarantee made that the OS in its current configuration supports these APIs. | 0x0c9ece4d, 0x2f6e, 0x4f01, 0x8c, 0x96, 0xe8, 0x9e, 0x33, 0x1b, 0x47, 0xb1 |
| DXCORE_ADAPTER_ATTRIBUTE_D3D12_CORE_COMPUTE. Specifies an adapter that supports being used with the Direct3D 12 core compute APIs. No guarantees are made about specific features, nor is a guarantee made that the OS in its current configuration supports these APIs. | 0x248e2800, 0xa793, 0x4724, 0xab, 0xaa, 0x23, 0xa6, 0xde, 0x1b, 0xe0, 0x90 |

## Requirements

| | |
|-|-|
| Header | dxcore_interface.h |

## See also

* [IDXCoreAdapterFactory::CreateAdapterList](/windows/win32/dxcore/dxcore_interface/nf-dxcore_interface-idxcoreadapterfactory-createadapterlist)
* [IDXCoreAdapter::IsAttributeSupported](/windows/win32/dxcore/dxcore_interface/nf-dxcore_interface-idxcoreadapter-isattributesupported)
* [DXCore Reference](/windows/win32/dxcore/dxcore-reference)
* [Using DXCore to enumerate adapters](/windows/win32/dxcore/dxcore-enum-adapters)
* [Direct3D 12 graphics](/windows/win32/direct3d12/direct3d-12-graphics)