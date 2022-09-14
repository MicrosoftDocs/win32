---
title: Helper functions for Direct3D 12
description: These helper functions help particularly in handling subresources, and are declared in `d3dx12.h`.
ms.assetid: E40B20D9-C700-4142-BBF3-7A5086E34712
keywords:
- Helper functions
- d3dx12.h
ms.topic: article
ms.date: 05/31/2018
---

# Helper functions for Direct3D 12

These helper functions help particularly in handling subresources, and are declared in `d3dx12.h`.

`d3dx12.h` is available separately from the Direct3D 12 headers. You can download `d3dx12.h` from [The D3D12 Helper Library](https://github.com/microsoft/DirectX-Headers/blob/main/include/directx/d3dx12.h).

## In this section

| Topic | Description |
|-|-|
| [**CommandListCast**](commandlistcast.md) | This function template casts a constant pointer to any command list into a const pointer to an ID3D12CommandList. |
| [**D3D12CalcSubresource**](d3d12calcsubresource.md) | Calculates a subresource index for a texture. |
| [**D3D12DecomposeSubresource**](d3d12decomposesubresource.md) | Outputs the mip slice, array slice, and plane slice that correspond to the specified subresource index. |
| [**D3D12GetFormatPlaneCount**](d3d12getformatplanecount.md) | Gets the number of planes for the specified DXGI format for the specified virtual adapter (an **ID3D12Device**). |
| [**D3D12IsLayoutOpaque**](d3d12islayoutopaque.md) | Indicates whether the layout is opaque. |
| [**D3DX12GetBaseSubobjectType**](d3dx12getbasesubobjecttype.md) | Returns the subobject type that corresponds to the base class of the passed-in subobject type. |
| [**D3DX12ParsePipelineStateStream**](d3dx12parsepipelinestream.md) | Parses a pipeline state stream description, calling a user-defined callback for each subobject instance parsed. |
| [**D3DX12SerializeVersionedRootSignature**](d3dx12serializeversionedrootsignature.md) | Helps enable root signature 1.1 features when they are available, and does not require maintaining two code paths for building root signatures. This helper method reconstructs a version 1.0 root signature when version 1.1 is not supported. |
| [**GetRequiredIntermediateSize**](getrequiredintermediatesize.md) | Returns the required size of a buffer to be used for data upload. |
| [**Memcpysubresource**](memcpysubresource.md) | Copies a subresource row by row. |
| [**Updatesubresources**](updatesubresources1.md) | Updates subresources, all the subresource arrays should be populated, typically by calling [**ID3D12Device::GetCopyableFootprints**](/windows/desktop/api/d3d12/nf-d3d12-id3d12device-getcopyablefootprints). |
| [**Updatesubresources (heap-allocating)**](updatesubresources2.md) | Updates subresources with a heap-allocating implementation. |
| [**Updatesubresources (stack-allocating)**](updatesubresources3.md) | Updates subresources with a stack-allocating implementation. |

## Related topics

* [Direct3D 12 Reference](direct3d-12-reference.md)
* [Helper Structures and Functions for D3D12](helper-structures-and-functions-for-d3d12.md)
