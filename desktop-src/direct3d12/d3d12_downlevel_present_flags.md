---
title: D3D12_DOWNLEVEL_PRESENT_FLAGS enumeration
description: Flags passed to the ID3D12CommandQueueDownlevel::Present method.
ms.localizationpriority: low
ms.topic: reference
ms.date: 08/29/2019
topic_type: 
- APIRef
api_name: 
- D3D12_DOWNLEVEL_PRESENT_FLAGS
api_type: 
- HeaderDef
---

# D3D12\_DOWNLEVEL\_PRESENT\_FLAGS enumeration

Flags passed to the [**ID3D12CommandQueueDownlevel::Present**](id3d12commandqueuedownlevel-present.md) function to modify behavior.

## Syntax

```cpp
enum D3D12_DOWNLEVEL_PRESENT_FLAGS
{
    D3D12_DOWNLEVEL_PRESENT_FLAG_NONE = 0,
    D3D12_DOWNLEVEL_PRESENT_FLAG_WAIT_FOR_VBLANK = 1
};
```

## Constants

**D3D12\_DOWNLEVEL\_PRESENT\_FLAG\_NONE**

No options selected.

**D3D12\_DOWNLEVEL\_PRESENT\_FLAG\_WAIT\_FOR\_VBLANK**

The **Present** operation won't be done until a VSync has occurred since the last time you **Present**ed.

## Requirements

| Requirement | Value |
|--------|------------------|
| Header | d3d12downlevel.h |
| DLL    | D3D12.dll (Windows 7 only) |

## See also
* [ID3D12CommandQueueDownlevel](id3d12commandqueuedownlevel.md)
* [Direct3D 12 On Windows 7 enumerations](direct3d-12on7-enumerations.md)
* [Direct3D 12 on Windows 7 reference (d3d12downlevel.h)](direct3d-12on7-reference.md)
* [Direct3D 12 On Windows 7](https://devblogs.microsoft.com/directx/porting-directx-12-games-to-windows-7/)
