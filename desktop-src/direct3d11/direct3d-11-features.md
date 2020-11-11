---
title: Direct3D 11 Features
description: The programming guide contains information about how to use the Direct3D 11 programmable pipeline to create realtime 3D graphics for games, and for scientific and desktop applications.
ms.assetid: ee4dae04-1a52-4587-87c1-006abb687a91
ms.topic: article
ms.date: 05/31/2018
---

# Direct3D 11 Features

The programming guide contains information about how to use the Direct3D 11 programmable pipeline to create realtime 3D graphics for games, and for scientific and desktop applications.

-   [Compute Shader](#compute-shader)
-   [Dynamic Shader Linking](#dynamic-shader-linking)
-   [Multithreading](#multithreading)
-   [Tessellation](#tessellation)
-   [Full Listing of Features](#full-listing-of-features)
-   [Features Added in Previous Releases](#features-added-in-previous-releases)
-   [Related topics](#related-topics)

## Compute Shader

A compute shader is a programmable shader designed for general-purpose data-parallel processing. In other words, compute shaders allow a GPU to be used as a general-purpose parallel processor. The compute shader is similar to the other programmable pipeline shaders (such as vertex, pixel, geometry) in the way that it accesses inputs and outputs. The compute shader technology is also known as the DirectCompute technology. A compute shader is integrated into Direct3D and is accessible through a Direct3D device. It can directly share memory resources with graphics shaders by using the Direct3D device. However, it is not directly connected to other shader stages.

A compute shader is designed for mass-market applications that perform computations at interactive rates, when the cost of transitioning between the API (and its associated software stack) and a CPU would consume too much overhead.

A compute shader has its own set of states. A compute shader does not necessarily have a forced 1-1 mapping to either input records (like a vertex shader does) or output records (like the pixel shader does). Some features of the graphics shader are supported, but others have been removed so that new compute shader-specific features could be added.

To support the compute shader-specific features, several new resource types are now available, such as read/write buffers, textures, and structured buffers.

See [Compute Shader Overview](direct3d-11-advanced-stages-compute-shader.md) for additional information.

## Dynamic Shader Linking

Rendering systems must deal with significant complexity when they manage shaders, while providing the opportunity to optimize shader code. This becomes an even greater challenge because shaders must support a variety of different materials in a rendered scene across various hardware configurations. To address this challenge, shader developers have often resorted to one of two general approaches. They have either created fully featured large, general-purpose shaders that can be used by a wide variety of scene items, which trade off some performance for flexibility, or created individual shaders for each geometry stream, material type, or light type combination needed.

These large, general-purpose shaders handle this challenge by recompiling the same shader with different preprocessor definitions, and the latter method uses brute-force developer power to achieve the same result. The shader permutation explosion has often been a problem for developers who must now manage thousands of different shader permutations within their game and asset pipeline.

Direct3D 11 and shader model 5 introduce object-oriented language constructs and provide runtime support of shader linking to help developers program shaders.

See [Dynamic Linking](/windows/desktop/direct3dhlsl/overviews-direct3d-11-hlsl-dynamic-linking) for additional information.

## Multithreading

Many graphics applications are CPU-bound because of costly activities such as scene graph traversal, object sorting, and physics simulations. Because multicore systems are becoming increasingly available, Direct3D 11 has improved its multithreading support to enable efficient interaction between multiple CPU threads and the D3D11 graphics APIs.

Direct3D 11 enables the following functionality to support multithreading:

-   Concurrent objects are now created in separate threads — Making entry-point functions that create objects free-threaded makes it possible for many threads to create objects simultaneously. For example, an application can now compile a shader or load a texture on one thread while rendering on another.
-   Command lists can be created on multiple threads — A command list is a recorded sequence of graphics commands. With Direct3D 11, you can create command lists on multiple CPU threads, which enables parallel traversal of the scene database or physics processing on multiple threads. This frees the main rendering thread to dispatch command buffers to the hardware.

See [MultiThreading](overviews-direct3d-11-render-multi-thread.md) for additional information.

## Tessellation

Tessellation can be used to render a single model with varying levels of detail. This approach generates a more geometrically accurate model that depends on the level of detail required for a scene. Use tessellation in a scene where the level of detail allows a lower geometry model, which reduces the demand on memory bandwidth consumed during rendering.

In Direct3D, tessellation is implemented on the GPU to calculate a smoother curved surface from a coarse (less detailed) input patch. Each (quad or triangle) patch face is subdivided into smaller triangular faces that better approximate the surface that you want.

For information about implementing tessellation in the graphics pipeline, see [Tessellation Overview](direct3d-11-advanced-stages-tessellation.md).

## Full Listing of Features

This is a complete list of the features in Direct3D 11.

-   You can run Direct3D 11 on [downlevel hardware](overviews-direct3d-11-devices-downlevel.md) by specifing a [feature level](overviews-direct3d-11-devices-downlevel-intro.md) when you create a device.
-   You can perform tessellation (see [Tessellation Overview](direct3d-11-advanced-stages-tessellation.md)) by using the following shader types:

    -   Hull Shader
    -   Domain Shader

-   Direct3D 11 supports multithreading (see [MultiThreading](overviews-direct3d-11-render-multi-thread.md))

    -   Multithread resource/shader/object creation
    -   Multithreaded Display list creation

-   Direct3D 11 expands shaders with the following features (see [Shader Model 5](/windows/desktop/direct3dhlsl/overviews-direct3d-11-hlsl))

    -   Addressable resources - textures, constant buffers, and samplers
    -   Additional resource types, such as read/write buffers and textures (see [New Resource Types](direct3d-11-advanced-stages-cs-resources.md)).
    -   Subroutines
    -   Compute shader (see [Compute Shader Overview](direct3d-11-advanced-stages-compute-shader.md)) - A shader that speeds up computations by dividing the problem space between several software threads or groups of threads, and sharing data among shader registers to significantly reduce the amount of data required to input into a shader. Algorithms that the compute shader can significantly improve include post processing, animation, physics, and artificial intelligence.
    -   Geometry shader (see [Geometry Shader Features](/windows/desktop/direct3dhlsl/overviews-direct3d-11-hlsl-gs-features))

        -   Instancing - Allows the geometry shader to output a maximum of 1024 vertices, or any combination of instances and vertices up to 1024 (maximum of 32 instances of 32 vertices each).

    -   Pixel shader

        -   Coverage as PS Input
        -   Programmable Interpolation of Inputs - The pixel shader can evaluate attributes within the pixel, anywhere on the multisample grid
        -   Centroid sampling of attributes must obey the following rules:

            -   If all samples in the primitive are covered, the attribute is evaluated at the pixel center regardless of whether the sample pattern has a sample location at the pixel center.
            -   Otherwise, the attribute is evaluated at the first covered sample, that is, the sample with the lowest index among all sample indexes. In this situation, sample coverage is determined after applying the logical AND operation to the coverage and the sample-mask rasterizer state.
            -   If no samples are covered (such as on helper pixels that are executed off the bounds of a primitive to fill out 2x2 pixel stamps), the attribute is evaluated in one of the following ways:

                -   If the sample-mask rasterizer state is a subset of the samples in the pixel, the first sample that is covered by the sample-mask rasterizer state is the evaluation point.
                -   Otherwise, in the full sample-mask condition, the pixel center is the evaluation point.

-   Direct3D 11 expands textures (see [Textures Overview](overviews-direct3d-11-resources-textures.md)) with the following features

    -   Gather4

        -   Support for multi-component textures - specify a channel to load from
        -   Support for programmable offsets

    -   Streaming

        -   Texture clamps to limit WDDM preload

    -   16K texture limits
    -   Require 8-bits of subtexel and sub-mip precision on texture filtering
    -   New texture compression formats (1 new LDR format and 1 new HDR format)

-   Direct3D 11 supports conservative oDepth - This algorithm allows a pixel shader to compare the per-pixel depth value of the pixel shader with that in the rasterizer. The result enables early depth culling operations while maintaining the ability to output oDepth from a pixel shader.
-   Direct3D 11 supports large memory

    -   Allow for resources > 4GB
    -   Keep indices of resources 32bit, but resource larger

-   Direct3D 11 supports stream output improvements

    -   Addressable Stream output
    -   Increase Stream output count to 4
    -   Change all stream output buffers to be multi-element

-   Direct3D 11 supports Shader Model 5 (see [Shader Model 5](/windows/desktop/direct3dhlsl/d3d11-graphics-reference-sm5))

    -   Doubles with denorms
    -   Count bits set instruction
    -   Find first bit set instruction
    -   Carry/Overflow handling
    -   Bit reversal instructions for FFTs
    -   Conditional Swap intrinsic
    -   Resinfo on buffers
    -   Reduced-precision reciprocal
    -   Shader conversion instructions - fp16 to fp32 and vice versa
    -   Structured buffer, which is a new type of buffer containing structured elements.

-   Direct3D 11 supports read-only depth or stencil views

    -   Disables writes to the part that is read-only, allows for using texture as input and for depth-culling

-   Direct3D 11 supports draw indirect - Direct3D 10 implements DrawAuto, which takes content (generated by the GPU) and renders it (on the GPU). Direct3D 11 generalizes DrawAuto so that it can be called by a Compute Shader using DrawInstanced and DrawIndexedInstanced.
-   Direct3D 11 supports miscellaneous features

    -   Floating-point viewports
    -   Per-resource mipmap clamping
    -   Depth Bias - This algorithm updates the behavior of depth bias, by using rasterizer state. The result eliminates the scenarios where the calculated bias could be NaN.
    -   Resource limits - Resource indices are still required to be <= 32 bits, but resources can be larger than 4 GB.
    -   Rasterizer Precision
    -   MSAA Requirements
    -   Counters Reduced
    -   1-Bit Format and Text Filter Removed

## Features Added in Previous Releases

For the list of the features added in previous releases, see the following topics:

-   [What's New in the August 2009 Windows 7/Direct3D 11 SDK](dx11-whats-new.md)
-   [What's New in the November 2008 Direct3D 11 Technical Preview](dx11-08nov-whats-new.md)

## Related topics

<dl> <dt>

[What's new in Direct3D 11](dx-graphics-overviews-introduction.md)
</dt> </dl>

 

 