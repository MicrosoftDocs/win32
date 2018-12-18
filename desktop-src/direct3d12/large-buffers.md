---
title: Suballocation Within Buffers
description: Buffers have all the features necessary in D3D12 for applications to transfer a large range of transient data from the CPU to the GPU. This section covers four common scenarios for the use and management of resources and buffers.
ms.assetid: 359E377A-8E16-4BB5-9055-09617335AB57
ms.topic: article
ms.date: 05/31/2018
---

# Suballocation Within Buffers

Buffers have all the features necessary in D3D12 for applications to transfer a large range of transient data from the CPU to the GPU. This section covers four common scenarios for the use and management of resources and buffers.

Similar to D3D11, applications in D3D12 still need to declare the usage of memory when allocating buffers in D3D12 compared to Dynamic/Staging Resources in D3D11, but in D3D12, developers have more flexibility and tighter control over memory usage. Buffers, through suballocation, have all the features necessary for low-level memory management.

## In this section



| Topic                                                                                        | Description                                                                                                                                                                                                                                                                                                                                                                                                             |
|----------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [Uploading Different Types of Resources](uploading-resources.md)<br/>                 | Shows how to use one buffer to upload both constant buffer data and vertex buffer data to the GPU, and how to properly sub-allocate and place data within buffers. The use of one single buffer increases memory usage flexibility and provides applications with tighter control of memory usage. Also shows the differences between the D3D11 and D3D12 models for uploading different types of resources.<br/> |
| [Uploading Texture Data Through Buffers](upload-and-readback-of-texture-data.md)<br/> | Uploading 2D or 3D texture data is similar to uploading 1D data, except that applications need to pay closer attention to data alignment related to row pitch. Buffers can be used orthogonally and concurrently from multiple parts of the graphics pipeline, and are very flexible. <br/>                                                                                                                       |
| [Read back data via a buffer](readback-data-using-heaps.md)<br/>                    | Reading back data from the GPU, such as capturing a screen shot, involves the use of the Readback heap. <br/>                                                                                                                                                                                                                                                                                                     |
| [Fence-Based Resource Management](fence-based-resource-management.md)<br/>            | Shows how to manage resource data life-span by tracking GPU progress via fences. Memory can be effectively re-used with fences carefully managing the availability of free space in memory, such as in a ring buffer implementation for an Upload heap. <br/>                                                                                                                                                     |



 

## Related topics

<dl> <dt>

[Memory Management](memory-management.md)
</dt> </dl>

 

 





