---
description: The Direct3D 10 graphics pipeline represents a fundamental architecture change, rebuilt from the ground-up in hardware and software to power the next-generation of games and 3D multimedia applications.
ms.assetid: 2e24de6c-4f73-4844-b87f-3487ef069db6
title: API Features (Direct3D 10)
ms.topic: article
ms.date: 05/31/2018
---

# API Features (Direct3D 10)

The Direct3D 10 graphics pipeline represents a fundamental architecture change, rebuilt from the ground-up in hardware and software to power the next-generation of games and 3D multimedia applications. It uses the Windows Display Driver Model (WDDM), which enables performance and behavioral enhancements such as virtual GPU memory.

Developers familiar with Direct3D 9 will discover a series of functional enhancements and performance improvements in Direct3D 10, including:

-   The ability to process entire primitives in the new [geometry-shader stage](/previous-versions//bb205146(v=vs.85)).
-   The ability to output pipeline-generated vertex data to memory using the [stream-output stage](../direct3d11/d3d10-graphics-programming-guide-output-stream-stage.md).
-   Organization of pipeline state into 5 immutable [state objects](d3d10-graphics-programming-guide-api-features-state-objects.md), enabling fast configuration of the pipeline.
-   Organization of shader constants into [constant buffers](d3d10-graphics-programming-guide-resources-types.md), minimizing bandwidth overhead for supplying shader-constant data.
-   The ability to perform per-primitive material swapping and setup using a geometry shader.
-   New [resource types](d3d10-graphics-programming-guide-resources-types.md) (including texture arrays that can be indexed from shaders) and resource formats.
-   Increased generalization of resource access using a [view](d3d10-graphics-programming-guide-resources-access-views.md).
-   Legacy hardware capability bits (caps) have been removed in favor of a rich set of guaranteed functionality, which targets Direct3D 10-class hardware (minimum).
-   [Layered Runtime](d3d10-graphics-programming-guide-api-features-layers.md) - The Direct3D 10 API is constructed with layers, starting with the basic functionality at the core and building optional and developer-assist functionality (debug, etc.) in outer layers.
-   Full HLSL integration - All Direct3D 10 shaders are written in HLSL and implemented with the [common-shader core](../direct3dhlsl/dx-graphics-hlsl-common-core.md).
-   An increase in the number of render targets, textures, and samplers. There is also no shader length limit.
-   Integer and bitwise shader operations.
-   Readback of a depth/stencil surface or a multisampled resource, once it is no longer bound as a render target.
-   Multisampled alpha-to-coverage support.

There are additional behavioral differences that Direct3D 9 developers should also be aware of (see [Direct3D 9 to Direct3D 10 Considerations](d3d10-graphics-programming-guide-d3d9-to-d3d10-considerations.md)).

Here is a list of Direct3D 9 features that either are no longer supported, or have been revised in Direct3D 10 (see [Deprecated Features](d3d10-graphics-programming-guide-api-features-deprecated.md)).

## Related topics

<dl> <dt>

[Programming Guide for Direct3D 10](d3d10-graphics-programming-guide.md)
</dt> </dl>

 

 
