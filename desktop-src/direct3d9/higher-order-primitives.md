---
description: Direct3D 9 supports points, lines, triangles, and grid primitives.
ms.assetid: 474e8bee-336d-491f-afa0-f0186a8d19c7
title: Higher-Order Primitives (Direct3D 9)
ms.topic: article
ms.date: 05/31/2018
---

# Higher-Order Primitives (Direct3D 9)

Direct3D 9 supports points, lines, triangles, and grid primitives. These have been extended to support higher-order interpolation beyond linear. While triangles and lines have spatial extent, until now they were both rendered using linear interpolation. In Direct3D 9, Direct3D supports rendering of these primitive types using higher order, up to quintic, interpolation. Furthermore, a new quad primitive type is now supported. This new type can also be rendered with higher-order interpolation. This feature is primarily driven by requirements for animation and rendering of characters. It can also be used for other surfaces such as terrain or water.

Higher-order primitives support higher-order interpolation when transmitted to the API as lists, strips, fans, or indexed meshes. This is achieved by using additional information encoded in the vertices themselves. For example, normal vectors can be used to define tangent planes at the vertices to enable cubic interpolation. Most implementations support higher-order interpolation by tessellation into planar triangles. The tessellation step is applied logically before the vertex shader stage. Because the vertex shader API does not impose semantics on its input data, a special mechanism is provided to identify the vertex stream component that represents the position, and optionally the normal vector. All other components are interpolated accordingly.

This section introduces higher-order primitives and discusses how they can be used in your applications. Information is divided into the following topics.

-   [Improved Quality through Resolution Enhancement](#improved-quality-through-resolution-enhancement)
-   [Direct Mapping from Spline-Based Tools](#direct-mapping-from-spline-based-tools)

## Improved Quality through Resolution Enhancement

Current primitives are not ideal for representing smooth surfaces. Higher-order interpolation methods, such as cubic polynomials, allow more accurate calculations in rendering curved shapes. This provides increased realism by reducing or eliminating faceting artifacts visible on silhouette edges or on specular surface lighting. Furthermore, when tessellation occurs on the chip, the tessellated triangles do not impact the bus bandwidth. In many cases, a small amount of tessellation can provide improvements in image quality with minimal performance impact.

Direct3D 9 provides a simple way to apply resolution enhancement to content created by existing polygon-oriented tools and art pipelines. The application need only provide a desired level of tessellation, and transmit the data using standard triangle syntax that includes normal vectors.

## Direct Mapping from Spline-Based Tools

Many current authoring tools support higher-order primitives to enable more powerful modeling operations than are commonly provided for with planar triangle meshes. When used efficiently, so that the number of patches generated is reasonable, such tools can produce content that can be rendered directly by the API. To meet this requirement, a new entry point has been added that interprets the incoming vertex data stream as a 2D array of control points and tessellates it to the desired resolution.

-   [Using Higher-Order Primitives (Direct3D 9)](using-higher-order-primitives.md)

## Related topics

<dl> <dt>

[Vertex Pipeline](vertex-pipeline.md)
</dt> </dl>

 

 



