---
title: Helper Functions for D3D12
description: These helper functions help particularly in handling subresources, and are declared in d3dx12.h.
ms.assetid: E40B20D9-C700-4142-BBF3-7A5086E34712
keywords:
- Helper functions
- d3dx12.h
ms.localizationpriority: low
ms.topic: article
ms.date: 05/31/2018
---

# Helper Functions for D3D12

These helper functions help particularly in handling subresources, and are declared in **d3dx12.h**.

## In this section



| Topic                                                                                             | Description                                                                                                                                                                                                                                                |
|---------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**CommandListCast**](commandlistcast.md)<br/>                                     | This function template casts a constant pointer to any command list into a const pointer to an ID3D12CommandList.<br/>                                                                                                                               |
| [**D3D12CalcSubresource**](d3d12calcsubresource.md)<br/>                                   | Calculates a subresource index for a texture. <br/>                                                                                                                                                                                                  |
| [**D3D12DecomposeSubresource**](d3d12decomposesubresource.md)<br/>                         | Outputs the mip slice, array slice, and plane slice that correspond to the specified subresource index. <br/>                                                                                                                                        |
| [**D3D12GetFormatPlaneCount**](d3d12getformatplanecount.md)<br/>                           | Gets the number of planes for the specified DXGI format for the specified virtual adapter (an **ID3D12Device**). <br/>                                                                                                                               |
| [**D3D12IsLayoutOpaque**](d3d12islayoutopaque.md)<br/>                                     | Indicates whether the layout is opaque.<br/>                                                                                                                                                                                                         |
| [**D3DX12GetBaseSubobjectType**](d3dx12getbasesubobjecttype.md)<br/>                       | Returns the subobject type that corresponds to the base class of the passed-in subobject type.<br/>                                                                                                                                                  |
| [**D3DX12ParsePipelineStateStream**](d3dx12parsepipelinestream.md)<br/>                    | Parses a pipeline state stream description, calling a user-defined callback for each subobject instance parsed.<br/>                                                                                                                                 |
| [**D3DX12SerializeVersionedRootSignature**](d3dx12serializeversionedrootsignature.md)<br/> | Helps enable root signature 1.1 features when they are available, and does not require maintaining two code paths for building root signatures. This helper method reconstructs a version 1.0 root signature when version 1.1 is not supported.<br/> |
| [**GetRequiredIntermediateSize**](getrequiredintermediatesize.md)<br/>                     | Returns the required size of a buffer to be used for data upload. <br/>                                                                                                                                                                              |
| [**Memcpysubresource**](memcpysubresource.md)<br/>                                         | Copies a subresource row by row. <br/>                                                                                                                                                                                                               |
| [**Updatesubresources**](updatesubresources1.md)<br/>                                      | Updates subresources, all the subresource arrays should be populated, typically by calling [**ID3D12Device::GetCopyableFootprints**](/windows/desktop/api/d3d12/nf-d3d12-id3d12device-getcopyablefootprints). <br/>                                                                  |
| [**Updatesubresources (heap-allocating)**](updatesubresources2.md)<br/>                    | Updates subresources with a heap-allocating implementation. <br/>                                                                                                                                                                                    |
| [**Updatesubresources (stack-allocating)**](updatesubresources3.md)<br/>                   | Updates subresources with a stack-allocating implementation. <br/>                                                                                                                                                                                   |



 

## Related topics

<dl> <dt>

[Direct3D 12 Reference](direct3d-12-reference.md)
</dt> <dt>

[Helper Structures and Functions for D3D12](helper-structures-and-functions-for-d3d12.md)
</dt> </dl>

 

 





