---
title: Debug Layer Interfaces
description: The following interfaces are declared in d3d12sdklayers.h.
ms.assetid: 9BD5910A-8FF2-4540-BB8E-8EA5C10528CE
ms.topic: article
ms.date: 05/31/2018
---

# Debug Layer Interfaces

The following interfaces are declared in d3d12sdklayers.h.

## In this section



| Topic                                                                 | Description                                                                                                                                                                                               |
|-----------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**ID3D12Debug**](/windows/desktop/api/d3d12sdklayers/nn-d3d12sdklayers-id3d12debug)<br/>                         | A debug interface controls debug settings and validates pipeline state. It can only be used if the debug layer is turned on. <br/>                                                                  |
| [**ID3D12Debug1**](/windows/desktop/api/d3d12sdklayers/nn-d3d12sdklayers-id3d12debug1)<br/>                       | Adds GPU-Based Validation and Dependent Command Queue Synchronization to the debug layer.<br/>                                                                                                      |
| [**ID3D12Debug2**](/windows/desktop/api/D3D12sdklayers/nn-d3d12sdklayers-id3d12debug2)<br/>                       | Adds configurable levels of GPU-Based Validation to the debug layer.<br/>                                                                                                                           |
| [**ID3D12DebugCommandList**](/windows/desktop/api/d3d12sdklayers/nn-d3d12sdklayers-id3d12debugcommandlist)<br/>   | Provides methods to monitor and debug a command list.<br/>                                                                                                                                          |
| [**ID3D12DebugCommandList1**](/windows/desktop/api/d3d12sdklayers/nn-d3d12sdklayers-id3d12debugcommandlist1)<br/> | This interface enables modification of additional command list debug layer settings.<br/>                                                                                                           |
| [**ID3D12DebugCommandQueue**](/windows/desktop/api/d3d12sdklayers/nn-d3d12sdklayers-id3d12debugcommandqueue)<br/> | Provides methods to monitor and debug a command queue. <br/>                                                                                                                                        |
| [**ID3D12DebugDevice**](/windows/desktop/api/d3d12sdklayers/nn-d3d12sdklayers-id3d12debugdevice)<br/>             | This interface represents a graphics device for debugging. <br/>                                                                                                                                    |
| [**ID3D12DebugDevice1**](/windows/desktop/api/d3d12sdklayers/nn-d3d12sdklayers-id3d12debugdevice1)<br/>           | Specifies device-wide debug layer settings.<br/>                                                                                                                                                    |
| [**ID3D12InfoQueue**](/windows/desktop/api/d3d12sdklayers/nn-d3d12sdklayers-id3d12infoqueue)<br/>                 | An information-queue interface stores, retrieves, and filters debug messages. The queue consists of a message queue, an optional storage filter stack, and a optional retrieval filter stack. <br/> |
| [**ID3D12SharingContract**](/windows/desktop/api/d3d12sdklayers/nn-d3d12sdklayers-id3d12sharingcontract)<br/>     | Part of a contract between D3D11On12 diagnostic layers and graphics diagnostics tools.<br/>                                                                                                         |



 

## Related topics

<dl> <dt>

[Direct3D 12 Programming Environment Setup](directx-12-programming-environment-set-up.md)
</dt> <dt>

[Debug Layer Reference](direct3d-12-sdklayers-reference.md)
</dt> <dt>

[Direct3D 12 Reference](direct3d-12-reference.md)
</dt> </dl>

 

 





