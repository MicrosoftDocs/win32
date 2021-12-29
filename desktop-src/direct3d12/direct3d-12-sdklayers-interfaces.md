---
title: Debug Layer Interfaces
description: The following interfaces are declared in d3d12sdklayers.h.
ms.assetid: 9BD5910A-8FF2-4540-BB8E-8EA5C10528CE
ms.topic: article
ms.date: 05/31/2018
---

# Debug Layer interfaces

The following interfaces are defined in `d3d12sdklayers.h`.

## In this section

| Topic | Description |
|-|-|
| [**ID3D12Debug**](/windows/win32/api/d3d12sdklayers/nn-d3d12sdklayers-id3d12debug) | A debug interface controls debug settings and validates pipeline state. It can only be used if the debug layer is turned on. |
| [**ID3D12Debug1**](/windows/win32/api/d3d12sdklayers/nn-d3d12sdklayers-id3d12debug1) | Adds GPU-based validation and Dependent Command Queue Synchronization to the debug layer. |
| [**ID3D12Debug2**](/windows/win32/api/D3D12sdklayers/nn-d3d12sdklayers-id3d12debug2) | Adds configurable levels of GPU-Based Validation. |
| [**ID3D12Debug3**](/windows/win32/api/D3D12sdklayers/nn-d3d12sdklayers-id3d12debug3) | Adds to the debug layer GPU-based validation, Dependent Command Queue Synchronization, and configurable levels of GPU-based validation. |
| [**ID3D12Debug4**](/windows/win32/api/D3D12sdklayers/nn-d3d12sdklayers-id3d12debug4) | Adds the ability to disable the debug layer. |
| [**ID3D12Debug5**](/windows/win32/api/D3D12sdklayers/nn-d3d12sdklayers-id3d12debug5) | Adds to the debug layer the ability to configure the auto-naming of objects. |
| [**ID3D12DebugCommandList**](/windows/win32/api/d3d12sdklayers/nn-d3d12sdklayers-id3d12debugcommandlist) | Provides methods to monitor and debug a command list. |
| [**ID3D12DebugCommandList1**](/windows/win32/api/d3d12sdklayers/nn-d3d12sdklayers-id3d12debugcommandlist1) | This interface enables modification of additional command list debug layer settings. |
| [**ID3D12DebugCommandQueue**](/windows/win32/api/d3d12sdklayers/nn-d3d12sdklayers-id3d12debugcommandqueue) | Provides methods to monitor and debug a command queue. |
| [**ID3D12DebugDevice**](/windows/win32/api/d3d12sdklayers/nn-d3d12sdklayers-id3d12debugdevice) | This interface represents a graphics device for debugging. |
| [**ID3D12DebugDevice1**](/windows/win32/api/d3d12sdklayers/nn-d3d12sdklayers-id3d12debugdevice1) | Specifies device-wide debug layer settings. |
| [**ID3D12InfoQueue**](/windows/win32/api/d3d12sdklayers/nn-d3d12sdklayers-id3d12infoqueue) | An information-queue interface stores, retrieves, and filters debug messages. The queue consists of a message queue, an optional storage filter stack, and a optional retrieval filter stack. |
| [**ID3D12SharingContract**](/windows/win32/api/d3d12sdklayers/nn-d3d12sdklayers-id3d12sharingcontract) | Part of a contract between D3D11On12 diagnostic layers and graphics diagnostics tools. |

## Related topics

<dl> <dt>

[Direct3D 12 Programming Environment Setup](directx-12-programming-environment-set-up.md)
</dt> <dt>

[Debug Layer Reference](direct3d-12-sdklayers-reference.md)
</dt> <dt>

[Direct3D 12 Reference](direct3d-12-reference.md)
</dt> </dl>
