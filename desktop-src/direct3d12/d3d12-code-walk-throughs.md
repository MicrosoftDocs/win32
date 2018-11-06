---
title: D3D12 Code Walk-Throughs
description: This section provides code for sample scenarios. Many of the walk-throughs provide details on what coding is required to be added to a basic sample, to avoid repeating the basic component code for each scenario.
ms.assetid: 1F37FD3A-385C-4DD5-B04C-980F078D90D0
ms.topic: article
ms.date: 05/31/2018
---

# D3D12 Code Walk-Throughs

This section provides code for sample scenarios. Many of the walk-throughs provide details on what coding is required to be added to a basic sample, to avoid repeating the basic component code for each scenario.

For the most basic component, refer to the [Creating a Basic Direct3D 12 Component](creating-a-basic-direct3d-12-component.md) section. The following walk-throughs describe more advanced scenarios.

## In this section



| Topic                                                                                           | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
|-------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [D2D using D3D11on12](d2d-using-d3d11on12.md)<br/>                                       | The **D3D1211on12** sample demonstrates how to render D2D content over D3D12 content by sharing resources between an 11 based device and a 12 based device. <br/>                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| [Multi-engine n-body gravity simulation](multi-engine-n-body-gravity-simulation.md)<br/> | The **D3D12nBodyGravity** sample demonstrates how to do compute work asynchronously. The sample spins up a number of threads each with a compute command queue and schedules compute work on the GPU that performs an n-body gravity simulation. Each thread operates on two buffers full of position and velocity data. With each iteration, the compute shader reads the current position and velocity data from one buffer and writes the next iteration into the other buffer. When the iteration completes, the compute shader swaps which buffer is the SRV for reading position/velocity data and which is the UAV for writing position/velocity updates by changing the resource state on each buffer.<br/> |
| [Predication queries](predication-queries.md)<br/>                                       | The **D3D12PredicationQueries** sample demonstrates occlusion culling using DirectX 12 query heaps and predication. The walkthrough describes the additional code needed to extend the **HelloConstBuffer** sample to handle predication queries. <br/>                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| [Dynamic Indexing using HLSL 5.1](dynamic-indexing-using-hlsl-5-1.md)<br/>               | The **D3D12DynamicIndexing** sample demonstrates some of the new HLSL features available in Shader Model 5.1 - particularly dynamic indexing and unbounded arrays - to render the same mesh multiple times, each time rendering it with a dynamically selected material. With dynamic indexing, shaders can now index into an array without knowing the value of the index at compile time. When combined with unbounded arrays, this adds another level of indirection and flexibility for shader authors and art pipelines.<br/>                                                                                                                                                                                  |
| [Indirect drawing and GPU culling](indirect-drawing-and-gpu-culling-.md)<br/>            | The D3D12ExecuteIndirect sample demonstrates how to use indirect commands to draw content. It also demonstrates how these commands can be manipulated on the GPU in a compute shader before they are issued. <br/>                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |



 

## Related topics

<dl> <dt>

[Direct3D 12 Programming Guide](directx-12-programming-guide.md)
</dt> <dt>

[DirectX advanced learning video tutorials](https://www.youtube.com/channel/UCiaX2B8XiXR70jaN7NK-FpA)
</dt> <dt>

[Example Code in the D3D12 Reference](notes-on-example-code.md)
</dt> <dt>

[Working Samples](working-samples.md)
</dt> </dl>

 

 





