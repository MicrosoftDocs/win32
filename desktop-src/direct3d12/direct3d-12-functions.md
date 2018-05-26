---
title: Core Functions
description: The following functions are declared in d3d12.h.
ms.assetid: C0F9A52C-483D-40B2-9E1F-CB92ADDC2856
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Core Functions

The following functions are declared in d3d12.h.

## In this section



| Topic                                                                                                             | Description                                                                                                                                                                                                 |
|-------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**D3D12CreateDevice**](/windows/win32/D3D12/nf-d3d12-d3d12createdevice?branch=master)<br/>                                                         | Creates a device that represents the display adapter. <br/>                                                                                                                                           |
| [**D3D12CreateRootSignatureDeserializer**](/windows/win32/D3D12/nf-d3d12-d3d12createrootsignaturedeserializer?branch=master)<br/>                   | Deserializes a root signature so you can determine the layout definition ([**D3D12\_ROOT\_SIGNATURE\_DESC**](/windows/win32/D3D12/ns-d3d12-d3d12_root_signature_desc?branch=master)). <br/>                                                   |
| [**D3D12CreateVersionedRootSignatureDeserializer**](/windows/win32/d3d12/nf-d3d12-d3d12createversionedrootsignaturedeserializer?branch=master)<br/> | Generates an interface that can return the deserialized data structure, via [**GetUnconvertedRootSignatureDesc**](/windows/win32/d3d12/nf-d3d12-id3d12versionedrootsignaturedeserializer-getunconvertedrootsignaturedesc?branch=master).<br/> |
| [**D3D12EnableExperimentalFeatures**](/windows/win32/D3D12/nf-d3d12-d3d12enableexperimentalfeatures?branch=master)<br/>                             | Enables a list of experimental features.<br/>                                                                                                                                                         |
| [**D3D12GetDebugInterface**](/windows/win32/D3D12/nf-d3d12-d3d12getdebuginterface?branch=master)<br/>                                               | Gets a debug interface. <br/>                                                                                                                                                                         |
| [**D3D12SerializeRootSignature**](/windows/win32/D3D12/nf-d3d12-d3d12serializerootsignature?branch=master)<br/>                                     | Serializes a root signature version 1.0 that can be passed to [**ID3D12Device::CreateRootSignature**](/windows/win32/D3D12/nf-d3d12-id3d12device-createrootsignature?branch=master). <br/>                                                    |
| [**D3D12SerializeVersionedRootSignature**](/windows/win32/d3d12/nf-d3d12-d3d12serializeversionedrootsignature?branch=master)<br/>                   | Serializes a root signature of any version that can be passed to [**ID3D12Device::CreateRootSignature**](/windows/win32/D3D12/nf-d3d12-id3d12device-createrootsignature?branch=master). <br/>                                                 |



 

## Related topics

<dl> <dt>

[Core Reference](direct3d-12-core-reference.md)
</dt> <dt>

[Direct3D 12 Reference](direct3d-12-reference.md)
</dt> </dl>

 

 





