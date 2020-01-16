---
title: IHolographicQuadLayerInterop::CreateDirect3D12ContentBufferResource
description: Creates a Direct3D 12 resource for use as a content buffer for the layer.
ms.localizationpriority: low
ms.topic: reference
ms.date: 12/13/2019
---

# IHolographicQuadLayerInterop::CreateDirect3D12ContentBufferResource method

> [!NOTE]
> **Some information relates to pre-released product, which may be substantially modified before it's commercially released. Microsoft makes no warranties, express or implied, with respect to the information provided here.**

> [!IMPORTANT]
> The feature described in this topic is implemented in 
Windows 10, version 1903 (10.0; Build 18362), but the `Windows.Graphics.Holographic.Interop.h` header file is available starting in the [Windows 10 SDK Insider Preview](https://www.microsoft.com/software-download/windowsinsiderpreviewSDK).

The **CreateDirect3D12ContentBufferResource** method creates a Direct3D 12 resource for use as a back buffer for the corresponding [HolographicQuadLayer](/uwp/api/windows.graphics.holographic.holographicquadlayer) API object.

The [D3D12_RESOURCE_DESC](/windows/win32/api/d3d12/ns-d3d12-d3d12_resource_desc) structure can contain any set of valid initial values. Any values that won't work with this quad layer object will be overridden in the struct indicated by *pTexture2DDesc*, which is not an optional parameter. The resource is created so that it is already committed to a heap.

## Syntax

```cpp
HRESULT CreateDirect3D12ContentBufferResource(
  ID3D12Device *pDevice,
  D3D12_RESOURCE_DESC *pTexture2DDesc,
  ID3D12Resource **ppTexture2DResource
);
```

## Parameters

`pDevice`
Type: **[ID3D12Device](/windows/win32/api/d3d12/nn-d3d12-id3d12device)\***

A Direct3D 12 device, which will be used to create the resource.

`pTexture2DDesc`
Type: **[D3D12_RESOURCE_DESC](/windows/win32/api/d3d12/ns-d3d12-d3d12_resource_desc)\***

The Direct3D 12 resource description. This parameter is not optional.

**CreateDirect3D12ContentBufferResource** adjusts the description as needed to comply with platform requirements, such as buffer size or format restrictions, which are determined at runtime. Your application should inspect the descriptor for the texture returned in *ppCreatedTexture2DResource*, and respond appropriately to any differences from what was specified.

`ppTexture2DResource`
Type: **[ID3D12Resource](/windows/win32/api/d3d12/nn-d3d12-id3d12resource)\*\***

If successful, the Direct3D 12 2D texture resource for use as a content buffer. Otherwise, `nullptr`.

## Returns
**S_OK** if successful, otherwise returns an [HRESULT](/windows/win32/com/structure-of-com-error-codes) error code indicating the reason for failure. Also see [COM Error Codes (UI, Audio, DirectX, Codec)](/windows/win32/com/com-error-codes-10).

## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Target Platform** | Windows |
| **Header** | windows.graphics.holographic.interop.h |