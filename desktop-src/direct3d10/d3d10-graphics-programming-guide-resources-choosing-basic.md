---
description: A resource is a collection of data that is used by the 3D pipeline.
ms.assetid: 802400fa-a606-4d3d-a61d-1cdb5a9f0437
title: Choosing a Resource (Direct3D 10)
ms.topic: article
ms.date: 05/31/2018
---

# Choosing a Resource (Direct3D 10)

A resource is a collection of data that is used by the 3D pipeline. Creating resources and defining their behavior is the first step toward programming your application. This guide covers basic topics for choosing the resources required by your application.

-   [Identify Pipeline Stages That Need Resources](#identify-pipeline-stages-that-need-resources)
-   [Identify How Each Resource Will Be Used](#identify-how-each-resource-will-be-used)
-   [Binding Resources to Pipeline Stages](#binding-resources-to-pipeline-stages)
-   [Related topics](#related-topics)

## Identify Pipeline Stages That Need Resources

The first step is to choose the [pipeline stage](d3d10-graphics-programming-guide-pipeline-stages.md) (or stages) that will use a resource. That is, identify each stage that will read data from a resource as well as the stages that will write data out to a resource. Knowing the pipeline stages where the resources will be used determines the APIs that will be called to bind the resource to the stage.

This table lists the types of resources that can be bound to each pipeline stage. It includes whether the resource can be bound as an input or an output, as well as the bind API.



| Pipeline Stage  | In/Out | Resource               | Resource Type                           | Bind API                                                                                                                                                                                                |
|-----------------|--------|------------------------|-----------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Input Assembler | In     | Vertex Buffer          | Buffer                                  | [**IASetVertexBuffers**](/windows/desktop/api/D3D10/nf-d3d10-id3d10device-iasetvertexbuffers)                                                                                                                                           |
| Input Assembler | In     | Index Buffer           | Buffer                                  | [**IASetIndexBuffer**](/windows/desktop/api/D3D10/nf-d3d10-id3d10device-iasetindexbuffer)                                                                                                                                               |
| Shader Stages   | In     | Shader-ResourceView    | Buffer, Texture1D, Texture2D, Texture3D | [**VSSetShaderResources**](/windows/desktop/api/D3D10/nf-d3d10-id3d10device-vssetshaderresources), [**GSSetShaderResources**](/windows/desktop/api/D3D10/nf-d3d10-id3d10device-gssetshaderresources), [**PSSetShaderResources**](/windows/desktop/api/D3D10/nf-d3d10-id3d10device-pssetshaderresources) |
| Shader Stages   | In     | Shader-Constant Buffer | Buffer                                  | [**VSSetConstantBuffers**](/windows/desktop/api/D3D10/nf-d3d10-id3d10device-vssetconstantbuffers), [**GSSetConstantBuffers**](/windows/desktop/api/D3D10/nf-d3d10-id3d10device-gssetconstantbuffers), [**PSSetConstantBuffers**](/windows/desktop/api/D3D10/nf-d3d10-id3d10device-pssetconstantbuffers) |
| Stream Output   | Out    | Buffer                 | Buffer                                  | [**SOSetTargets**](/windows/desktop/api/D3D10/nf-d3d10-id3d10device-sosettargets)                                                                                                                                                       |
| Output Merger   | Out    | Render-target View     | Buffer, Texture1D, Texture2D, Texture3D | [**OMSetRenderTargets**](/windows/desktop/api/D3D10/nf-d3d10-id3d10device-omsetrendertargets)                                                                                                                                           |
| Output Merger   | Out    | Depth/Stencil View     | Texture1D, Texture2D                    | [**OMSetRenderTargets**](/windows/desktop/api/D3D10/nf-d3d10-id3d10device-omsetrendertargets)                                                                                                                                           |



 

## Identify How Each Resource Will Be Used

Once you have chosen the pipeline stages that your application will use (and therefore the resources that each stage will require), the next step is to determine how each resource will be used, that is, whether a resource can be accessed by the CPU or the GPU.

The hardware that your application is running on will have a minimum of at least one CPU and one GPU. To pick a usage value, consider which type of processor needs to read or write to the resource from the following options (see [**D3D10\_USAGE**](/windows/desktop/api/D3D10/ne-d3d10-d3d10_usage)).



| Resource Usage | Can be updated by                    | Frequency of Update |
|----------------|--------------------------------------|---------------------|
| Default        | GPU                                  | infrequently        |
| Dynamic        | CPU                                  | frequently          |
| Staging        | GPU                                  | n/a                 |
| Immutable      | CPU (only at resource creation time) | n/a                 |



 

Default usage should be used for a resource that is expected to be updated by the CPU infrequently (less than once per frame). Ideally, the CPU would never write directly to a resource with default usage so as to avoid potential performance penalties.

Dynamic usage should be used for a resource that the CPU updates relatively frequently (once or more per frame). A typical scenario for a dynamic resource would be to create dynamic vertex and index buffers that would be filled at runtime with data about the geometry visible from the point of view of the user for each frame. These buffers would be used to render only the geometry visible to the user for that frame.

Staging usage should be used to copy data to and from other resources. A typical scenario would be to copy data in a resource with default usage (which the CPU cannot access) to a resource with staging usage (which the CPU can access).

Immutable resources should be used when the data in the resource will never change.

Another way of looking at the same idea is to think of what an application does with a resource.



| How Application uses the Resource     | Resource Usage       |
|---------------------------------------|----------------------|
| Load once and never update            | Immutable or Default |
| Application fills resource repeatedly | Dynamic              |
| Render to texture                     | Default              |
| CPU access of GPU data                | Staging              |



 

If you are unsure what usage to choose, start with the default usage as it is expected to be the most common case. A Shader-Constant buffer is the one resource type that should always have default usage.

## Binding Resources to Pipeline Stages

A resource can be bound to more than one pipeline stage at the same time as long as the restrictions specified when the resource was created ([**usage flags**](/windows/desktop/api/D3D10/ne-d3d10-d3d10_usage), [**bind flags**](/windows/desktop/api/D3D10/ne-d3d10-d3d10_bind_flag), [**cpu access flags**](/windows/desktop/api/D3D10/ne-d3d10-d3d10_cpu_access_flag)) are met. More specifically, a resource can be bound as an input and an output simultaneously as long as reading and writing part of a resource cannot happen at the same time.

When binding a resource, think about how the GPU and the CPU will access the resource. Resources that are designed for a single purpose (do not use multiple usage, bind, and cpu access flags) will more than likely result in better performance.

For example, consider the case of a render target used as a texture multiple times. It may be faster to have two resources: a render target and a texture used as a shader resource. Each resource would use only one bind flag ([**D3D10\_BIND\_RENDER\_TARGET**](/windows/desktop/api/D3D10/ne-d3d10-d3d10_bind_flag) or **D3D10\_BIND\_SHADER\_RESOURCE**). The data would be copied from the render-target texture to the shader texture using [**CopyResource**](/windows/desktop/api/D3D10/nf-d3d10-id3d10device-copyresource) or [**CopySubresourceRegion**](/windows/desktop/api/D3D10/nf-d3d10-id3d10device-copysubresourceregion). This may improve performance by isolating the render-target write from the shader-texture read. Of course, the only way to be sure is to implement both approaches and measure the performance difference in your particular application.

## Related topics

<dl> <dt>

[Resources (Direct3D 10)](d3d10-graphics-programming-guide-resources.md)
</dt> </dl>

 

 



