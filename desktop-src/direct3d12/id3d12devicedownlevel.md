---
title: ID3D12DeviceDownlevel interface
description: Provides a Windows-7-specific memory statistics query.
keywords:
- ID3D12DeviceDownlevel interface
topic_type:
- apiref
api_name:
- ID3D12DeviceDownlevel
api_location:
- D3D12.dll
api_type:
- COM
ms.topic: reference
ms.date: 08/29/2019
---

# ID3D12DeviceDownlevel interface

This interface can be accessed via **QueryInterface** off of a [Direct3D 12 device](/windows/desktop/api/d3d12/nn-d3d12-id3d12device) when using [Direct3D 12 on Windows 7](https://devblogs.microsoft.com/directx/porting-directx-12-games-to-windows-7/). It provides a Windows-7-specific memory statistics query.

### Methods

The **ID3D12DeviceDownlevel** interface has these methods.

| Method | Description |
|:-------|:------------|
| [**QueryVideoMemoryInfo**](id3d12devicedownlevel-queryvideomemoryinfo.md) | Provides memory statistics on Windows 7. |

## Requirements

| Requirement | Value |
|--------|------------------|
| Header | d3d12downlevel.h |
| DLL    | D3D12.dll (Windows 7 only) |

## See also
* [Direct3D 12 On Windows 7 interfaces](direct3d-12on7-interfaces.md)
* [Direct3D 12 on Windows 7 reference (d3d12downlevel.h)](direct3d-12on7-reference.md)
* [Direct3D 12 On Windows 7](https://devblogs.microsoft.com/directx/porting-directx-12-games-to-windows-7/)
