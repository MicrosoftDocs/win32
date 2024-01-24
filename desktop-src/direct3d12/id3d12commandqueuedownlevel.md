---
title: ID3D12CommandQueueDownlevel interface
description: Provides a Windows-7-specific present mechanism.
keywords:
- ID3D12CommandQueueDownlevel interface
topic_type:
- apiref
api_name:
- ID3D12CommandQueueDownlevel
api_location:
- D3D12.dll
api_type:
- COM
ms.topic: reference
ms.date: 08/29/2019
---

# ID3D12CommandQueueDownlevel interface

This interface can be accessed via **QueryInterface** off of a [Direct3D 12 command queue](/windows/desktop/api/d3d12/nn-d3d12-id3d12commandqueue) when using [Direct3D 12 on Windows 7](https://devblogs.microsoft.com/directx/porting-directx-12-games-to-windows-7/). It provides a Windows-7-specific present mechanism.

### Methods

The **ID3D12CommandQueueDownlevel** interface has these methods.

| Method | Description |
|:-------|:------------|
| [**Present**](id3d12commandqueuedownlevel-present.md) | Copies contents from a D3D12 Texture2D resource into a window. |

## Requirements

| Requirement | Value |
|--------|------------------|
| Header | d3d12downlevel.h |
| DLL    | D3D12.dll (Windows 7 only) |

## See also
* [Direct3D 12 On Windows 7 interfaces](direct3d-12on7-interfaces.md)
* [Direct3D 12 on Windows 7 reference (d3d12downlevel.h)](direct3d-12on7-reference.md)
* [Direct3D 12 On Windows 7](https://devblogs.microsoft.com/directx/porting-directx-12-games-to-windows-7/)
