---
title: ID3D12CommandQueueDownlevel::Present method
description: Copies contents from a Direct3D 12 Texture2D resource into a window. | ID3D12CommandQueueDownlevel::Present method
keywords:
- Present method
- Present method, ID3D12CommandQueueDownlevel interface
- ID3D12CommandQueueDownlevel interface, Present method
topic_type:
- apiref
api_name:
- ID3D12CommandQueueDownlevel.Present
api_location:
- D3D12.dll
api_type:
- COM
ms.localizationpriority: low
ms.topic: reference
ms.date: 08/29/2019
---

# ID3D12CommandQueueDownlevel::Present method

Copies contents from a Direct3D 12 Texture2D resource into a window.

## Syntax

```cpp
HRESULT Present
    ID3D12GraphicsCommandList *pOpenCommandList,
    ID3D12Resource *pSourceTex2D,
    HWND hWindow,
    D3D12_DOWNLEVEL_PRESENT_FLAGS Flags
);
```

## Parameters

`pOpenCommandList`

Type: **[ID3D12GraphicsCommandList](/windows/win32/api/d3d12/nn-d3d12-id3d12graphicscommandlist)\***

An open command list, which Direct3D 12 enqueues a Present command onto, and then closes and submits for you.

`pSourceTex2D`

Type: **[ID3D12Resource](/windows/win32/api/d3d12/nn-d3d12-id3d12resource)\***

A resource containing your desired contents to display, with dimension [**D3D12\_RESOURCE\_DIMENSION\_TEXTURE2D**](/windows/win32/api/d3d12/ne-d3d12-d3d12_resource_dimension), and a format that is one of the following.

* DXGI_FORMAT_R16G16B16A16_FLOAT
* DXGI_FORMAT_R10G10B10A2_UNORM
* DXGI_FORMAT_R8G8B8A8_UNORM
* DXGI_FORMAT_R8G8B8A8_UNORM_SRGB
* DXGI_FORMAT_B8G8R8X8_UNORM
* DXGI_FORMAT_R10G10B10_XR_BIAS_A2_UNORM
* DXGI_FORMAT_B8G8R8A8_UNORM
* DXGI_FORMAT_B8G8R8A8_UNORM_SRGB

`hWindow`

Type: **[HWND](/windows/desktop/WinProg/windows-data-types)**

The handle to the window where the contents should be displayed.

`Flags`

Type: **[D3D12\_DOWNLEVEL\_PRESENT\_FLAGS](d3d12_downlevel_present_flags.md)**

Flags to modify the **Present** operation.

## Return value

Returns **S_OK** on success, or else a failing HRESULT.

## Requirements

|        |                  |
|--------|------------------|
| Header | d3d12downlevel.h |
| DLL    | D3D12.dll (Windows 7 only) |

## See also
* [ID3D12CommandQueueDownlevel](id3d12commandqueuedownlevel.md)
* [Direct3D 12 On Windows 7 interfaces](direct3d-12on7-interfaces.md)
* [Direct3D 12 on Windows 7 reference (d3d12downlevel.h)](direct3d-12on7-reference.md)
* [Direct3D 12 On Windows 7](https://devblogs.microsoft.com/directx/porting-directx-12-games-to-windows-7/)
