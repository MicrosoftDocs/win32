---
title: ID3D12DeviceDownlevel::QueryVideoMemoryInfo method
description: Copies contents from a Direct3D 12 Texture2D resource into a window. | ID3D12DeviceDownlevel::QueryVideoMemoryInfo method
keywords:
- QueryVideoMemoryInfo method
- QueryVideoMemoryInfo method, ID3D12DeviceDownlevel interface
- ID3D12DeviceDownlevel interface, QueryVideoMemoryInfo method
topic_type:
- apiref
api_name:
- ID3D12DeviceDownlevel.QueryVideoMemoryInfo
api_location:
- D3D12.dll
api_type:
- COM
ms.localizationpriority: low
ms.topic: reference
ms.date: 08/29/2019
---

# ID3D12DeviceDownlevel::QueryVideoMemoryInfo method

Provides memory statistics on Windows 7. This method is equivalent to [IDXGIAdapter3::QueryVideoMemoryInfo](/windows/win32/api/dxgi1_4/nf-dxgi1_4-idxgiadapter3-queryvideomemoryinfo), which is not available on Windows 7.

## Syntax

```cpp
HRESULT QueryVideoMemoryInfo( 
    UINT NodeIndex,
    DXGI_MEMORY_SEGMENT_GROUP MemorySegmentGroup,
    DXGI_QUERY_VIDEO_MEMORY_INFO *pVideoMemoryInfo
);
```

## Parameters

`NodeIndex`

Type: **UINT**

Specifies the device's physical adapter for which the video memory information is queried. For single-GPU operation, set this to zero. If there are multiple GPU nodes, set this to the index of the node (the device's physical adapter) for which the video memory information is queried. See [Multi-adapter systems](multi-engine.md).

`MemorySegmentGroup`

Type: **[DXGI_MEMORY_SEGMENT_GROUP](/windows/win32/api/dxgi1_4/ne-dxgi1_4-dxgi_memory_segment_group)**

Specifies a **DXGI_MEMORY_SEGMENT_GROUP** that identifies the group as local or non-local.

`pVideoMemoryInfo`

Type: **[DXGI_QUERY_VIDEO_MEMORY_INFO](/windows/win32/api/dxgi1_4/ns-dxgi1_4-dxgi_query_video_memory_info)\***

Fills in a **DXGI_QUERY_VIDEO_MEMORY_INFO** structure with the current values.

## Return value

Returns **S_OK** on success, or else a failing HRESULT.

## Requirements

|        |                  |
|--------|------------------|
| Header | d3d12downlevel.h and dxgi1_4.h |
| DLL    | D3D12.dll (Windows 7 only) |

## See also
* [ID3D12DeviceDownlevel](id3d12devicedownlevel.md)
* [Direct3D 12 On Windows 7 interfaces](direct3d-12on7-interfaces.md)
* [Direct3D 12 on Windows 7 reference (d3d12downlevel.h)](direct3d-12on7-reference.md)
* [Direct3D 12 On Windows 7](https://devblogs.microsoft.com/directx/porting-directx-12-games-to-windows-7/)
