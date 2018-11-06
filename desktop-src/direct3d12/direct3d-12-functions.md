---
title: Core Functions
description: The following functions are declared in d3d12.h.
ms.assetid: C0F9A52C-483D-40B2-9E1F-CB92ADDC2856
ms.topic: article
ms.date: 05/31/2018
---

# Core Functions

The following functions are declared in d3d12.h.

## In this section



| Topic                                                                                                             | Description                                                                                                                                                                                                 |
|-------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**D3D12CreateDevice**](/windows/desktop/api/D3D12/nf-d3d12-d3d12createdevice)<br/>                                                         | Creates a device that represents the display adapter. <br/>                                                                                                                                           |
| [**D3D12CreateRootSignatureDeserializer**](/windows/desktop/api/D3D12/nf-d3d12-d3d12createrootsignaturedeserializer)<br/>                   | Deserializes a root signature so you can determine the layout definition ([**D3D12\_ROOT\_SIGNATURE\_DESC**](/windows/desktop/api/D3D12/ns-d3d12-d3d12_root_signature_desc)). <br/>                                                   |
| [**D3D12CreateVersionedRootSignatureDeserializer**](/windows/desktop/api/d3d12/nf-d3d12-d3d12createversionedrootsignaturedeserializer)<br/> | Generates an interface that can return the deserialized data structure, via [**GetUnconvertedRootSignatureDesc**](/windows/desktop/api/d3d12/nf-d3d12-id3d12versionedrootsignaturedeserializer-getunconvertedrootsignaturedesc).<br/> |
| [**D3D12EnableExperimentalFeatures**](/windows/desktop/api/D3D12/nf-d3d12-d3d12enableexperimentalfeatures)<br/>                             | Enables a list of experimental features.<br/>                                                                                                                                                         |
| [**D3D12GetDebugInterface**](/windows/desktop/api/D3D12/nf-d3d12-d3d12getdebuginterface)<br/>                                               | Gets a debug interface. <br/>                                                                                                                                                                         |
| [**D3D12SerializeRootSignature**](/windows/desktop/api/D3D12/nf-d3d12-d3d12serializerootsignature)<br/>                                     | Serializes a root signature version 1.0 that can be passed to [**ID3D12Device::CreateRootSignature**](/windows/desktop/api/D3D12/nf-d3d12-id3d12device-createrootsignature). <br/>                                                    |
| [**D3D12SerializeVersionedRootSignature**](/windows/desktop/api/d3d12/nf-d3d12-d3d12serializeversionedrootsignature)<br/>                   | Serializes a root signature of any version that can be passed to [**ID3D12Device::CreateRootSignature**](/windows/desktop/api/D3D12/nf-d3d12-id3d12device-createrootsignature). <br/>                                                 |



 

## Related topics

<dl> <dt>

[Core Reference](direct3d-12-core-reference.md)
</dt> <dt>

[Direct3D 12 Reference](direct3d-12-reference.md)
</dt> </dl>

 

 





