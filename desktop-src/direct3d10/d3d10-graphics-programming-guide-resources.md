---
description: A resource is an area in memory that can be accessed by the Direct3D pipeline.
ms.assetid: 24859fbc-b5e1-4963-baf8-4f083f41f39a
title: Resources (Direct3D 10)
ms.topic: article
ms.date: 05/31/2018
---

# Resources (Direct3D 10)

A resource is an area in memory that can be accessed by the Direct3D pipeline. In order for the pipeline to access memory efficiently, data that is provided to the pipeline (such as input geometry, shader resources, textures etc) must be stored in a resource. There are two types of resources from which all Direct3D resources derive: a buffer or a texture. Up to 128 resources can be active for each pipeline stage.

Each application will typically create many resources. Examples of resource include: vertex buffers, index buffer, constant buffer, textures, and shader resources. There are several options that determine how resources can be used. You can create resources that are strongly typed or type less; you can control whether resources have both read and write access; you can make resources accessible to only the CPU, GPU, or both. Naturally, there will be speed vs. functionality tradeoff - the more functionality you allow a resource to have, the less performance you should expect.

Since an application often uses many textures, Direct3D also introduces the concept of a texture array to simplify texture management. A texture array contains one or more textures (all of the same type and dimensions) that can be indexed from within an application or by shaders. Texture arrays allow you to use a single interface with multiple indexes to access many textures. You can create as many texture arrays to manage different texture types as you need.

Once you have created the resources that your application will use, you connect or bind each resource to the pipeline stages that will use them. This is accomplished by calling a bind API, which takes a pointer to the resource. Since more than one pipeline stage may need access to the same resource, Direct3D 10 introduces the concept of a resource view. A view identifies the portion of a resource that can be accessed. You can create m views or a resource and bind them to n pipeline stages, assuming you follow binding rules for shared resource (the runtime will generate errors at compile time if you don't).

A resource view provides a general model for access to a resource (textures, buffers, etc.). Because you can use a view to tell the runtime what data to access and how to access it, resource views allow you create type less resources. That is, you can create resources for a given size at compile time, and then declare the data type within the resource when the resource gets bound to the pipeline. Views expose many new capabilities for using resources, such as the ability to read back depth/stencil surfaces in the shader, generating dynamic cubemaps in a single pass, and rendering simultaneously to multiple slices of a volume.

To find out more about the basic resource types, texture arrays, and how to create and use resources, see these other topics:

-   [Resource Types](d3d10-graphics-programming-guide-resources-types.md)
-   [Choosing a Resource](d3d10-graphics-programming-guide-resources-choosing-basic.md)
-   [Creating Buffer Resources](d3d10-graphics-programming-guide-resources-creating.md)
-   [Creating Texture Resources](d3d10-graphics-programming-guide-resources-creating-textures.md)
-   [Copying and Accessing Resource Data](d3d10-graphics-programming-guide-resources-mapping.md)
-   [Memory Structure and Views](d3d10-graphics-programming-guide-resources-access-views.md)
-   [Block Compression](d3d10-graphics-programming-guide-resources-block-compression.md)
-   [Table of Resource Limits](d3d10-graphics-programming-guide-resources-limits.md)
-   [Coordinate Systems](d3d10-graphics-programming-guide-resources-coordinates.md)
-   [Floating-Point Rules](d3d10-graphics-programming-guide-resources-float-rules.md)
-   [Data Type Conversion Rules](d3d10-graphics-programming-guide-resources-data-conversion.md)
-   [Mapping Legacy Formats](d3d10-graphics-programming-guide-resources-legacy-formats.md)

## Related topics

<dl> <dt>

[Programming Guide for Direct3D 10](d3d10-graphics-programming-guide.md)
</dt> </dl>

 

 



