---
title: Debug Layer Interfaces
description: The following interfaces are declared in d3d12sdklayers.h.
ms.assetid: '9BD5910A-8FF2-4540-BB8E-8EA5C10528CE'
---

# Debug Layer Interfaces

The following interfaces are declared in d3d12sdklayers.h.

## In this section



| Topic                                                                 | Description                                                                                                                                                                                               |
|-----------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**ID3D12Debug**](id3d12debug.md)<br/>                         | A debug interface controls debug settings and validates pipeline state. It can only be used if the debug layer is turned on. <br/>                                                                  |
| [**ID3D12Debug1**](id3d12debug1.md)<br/>                       | Adds GPU-Based Validation and Dependent Command Queue Synchronization to the debug layer.<br/>                                                                                                      |
| [**ID3D12Debug2**](id3d12debug2.md)<br/>                       | Adds configurable levels of GPU-Based Validation to the debug layer.<br/>                                                                                                                           |
| [**ID3D12DebugCommandList**](id3d12debugcommandlist.md)<br/>   | Provides methods to monitor and debug a command list.<br/>                                                                                                                                          |
| [**ID3D12DebugCommandList1**](id3d12debugcommandlist1.md)<br/> | This interface enables modification of additional command list debug layer settings.<br/>                                                                                                           |
| [**ID3D12DebugCommandQueue**](id3d12debugcommandqueue.md)<br/> | Provides methods to monitor and debug a command queue. <br/>                                                                                                                                        |
| [**ID3D12DebugDevice**](id3d12debugdevice.md)<br/>             | This interface represents a graphics device for debugging. <br/>                                                                                                                                    |
| [**ID3D12DebugDevice1**](id3d12debugdevice1.md)<br/>           | Specifies device-wide debug layer settings.<br/>                                                                                                                                                    |
| [**ID3D12InfoQueue**](id3d12infoqueue.md)<br/>                 | An information-queue interface stores, retrieves, and filters debug messages. The queue consists of a message queue, an optional storage filter stack, and a optional retrieval filter stack. <br/> |
| [**ID3D12SharingContract**](id3d12sharingcontract.md)<br/>     | Part of a contract between D3D11On12 diagnostic layers and graphics diagnostics tools.<br/>                                                                                                         |



 

## Related topics

<dl> <dt>

[Direct3D 12 Programming Environment Setup](directx-12-programming-environment-set-up.md)
</dt> <dt>

[Debug Layer Reference](direct3d-12-sdklayers-reference.md)
</dt> <dt>

[Direct3D 12 Reference](direct3d-12-reference.md)
</dt> </dl>

 

 





