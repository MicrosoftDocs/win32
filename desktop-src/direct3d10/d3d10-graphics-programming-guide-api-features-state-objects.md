---
description: In Direct3D 10, device state is grouped into state objects which greatly reduce the cost of state changes.
ms.assetid: b2839da9-60ed-4f6c-9cc7-eac53647cca7
title: State Objects (Direct3D 10)
ms.topic: article
ms.date: 05/31/2018
---

# State Objects (Direct3D 10)

In Direct3D 10, device state is grouped into state objects which greatly reduce the cost of state changes. There are several state objects, and each one is designed to initialize a set of state for a particular pipeline stage. You can create up to 4096 of each type of state object.

-   [Input-Layout State](#input-layout-state)
-   [Rasterizer State](#rasterizer-state)
-   [Depth-Stencil State](#depth-stencil-state)
-   [Blend State](#blend-state)
-   [Sampler State](#sampler-state)
-   [Performance Considerations](#performance-considerations)
-   [Related topics](#related-topics)

## Input-Layout State

This group of state (see [**D3D10\_INPUT\_ELEMENT\_DESC**](/windows/desktop/api/D3D10/ns-d3d10-d3d10_input_element_desc)) dictates how the [input-assembler stage](../direct3d11/d3d10-graphics-programming-guide-input-assembler-stage.md) reads data out of the input buffers and assembles it for use by the vertex shader. This includes state such as the number of elements in the input buffer and the signature of the input data. The input-assembler stage is a new stage in the pipeline whose job is to stream primitives from memory into the pipeline.

To create a input-layout-state object, see [**CreateInputLayout**](/windows/desktop/api/D3D10/nf-d3d10-id3d10device-createinputlayout).

## Rasterizer State

This group of state (see [**D3D10\_RASTERIZER\_DESC**](/windows/desktop/api/D3D10/ns-d3d10-d3d10_rasterizer_desc)) initializes the [rasterizer stage](../direct3d11/d3d10-graphics-programming-guide-rasterizer-stage.md). This object includes state such as fill or cull modes, enabling a scissor rectangle for clipping, and setting multisample parameters. This stage rasterizes primitives into pixels, performing operations like clipping and mapping primitives to the viewport.

To create a rasterizer-state object, see [**CreateRasterizerState**](/windows/desktop/api/D3D10/nf-d3d10-id3d10device-createrasterizerstate).

## Depth-Stencil State

This group of state (see [**D3D10\_DEPTH\_STENCIL\_DESC**](/windows/desktop/api/D3D10/ns-d3d10-d3d10_depth_stencil_desc)) initializes the depth-stencil portion of the [output-merger stage](../direct3d11/d3d10-graphics-programming-guide-output-merger-stage.md). More specifically, this object initializes depth and stencil testing.

To create a depth-stencil-state object, see [**CreateDepthStencilState**](/windows/desktop/api/D3D10/nf-d3d10-id3d10device-createdepthstencilstate).

## Blend State

This group of state (see [**D3D10\_BLEND\_DESC**](/windows/desktop/api/D3D10/ns-d3d10-d3d10_blend_desc)) initializes the blending portion of the [output-merger stage](../direct3d11/d3d10-graphics-programming-guide-output-merger-stage.md).

To create a blend-state object, see [**CreateBlendState**](/windows/desktop/api/D3D10/nf-d3d10-id3d10device-createblendstate).

## Sampler State

This group of state (see [**D3D10\_SAMPLER\_DESC**](/windows/desktop/api/D3D10/ns-d3d10-d3d10_sampler_desc)) initializes a sampler object. A sampler object is used by the shader stages to filter textures in memory.



Differences between Direct3D 9 and Direct3D 10:

- In Direct3D 10, the sampler object is no longer bound to a specific texture, it just describes how to do filtering given any attached resource.



 

To create a sampler-state object, see [**CreateSamplerState**](/windows/desktop/api/D3D10/nf-d3d10-id3d10device-createsamplerstate).

## Performance Considerations

Designing the API to use state objects creates several performance advantages. These include validating state at object creation time, enabling caching of state objects in hardware, and greatly reducing the amount of state that is passed during a state-setting API call (by passing a handle to the state object instead of the state).

To achieve these performance improvements, you should create your state objects when your application starts up, well before your render loop. State objects are immutable, that is, once they are created, you cannot change them. Instead you must destroy and recreate them. To cope with this restriction, you can create up to 4096 of each type of state objects. For example, you could create several sampler objects with various sampler-state combinations. Changing the sampler state is then accomplished by calling the appropriate Set API which passes a handle to the object (as opposed to the sampler state). This significantly reduces the amount of overhead during each render frame for changing state since the number of calls and the amount of data are greatly reduced.

Alternatively, you can choose to use the effect system which will automatically manage efficient creation and destruction of state objects for your application.

## Related topics

<dl> <dt>

[API Features (Direct3D 10)](d3d10-graphics-programming-guide-api-features.md)
</dt> </dl>

 

 
