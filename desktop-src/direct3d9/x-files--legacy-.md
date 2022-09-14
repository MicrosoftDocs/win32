---
description: The X file format refers to files with the .x file name extension.
ms.assetid: 06b3dcb3-03fc-4d99-b8c3-32f56d8bf49e
title: X Files (Legacy) (Direct3D 9)
ms.topic: article
ms.date: 05/31/2018
---

# X Files (Legacy) (Direct3D 9)

The X file format refers to files with the .x file name extension. X files were introduced with DirectX 2.0. A binary version of this format was subsequently released with DirectX 3.0, which is also described in this documentation. DirectX 6.0 introduced interfaces and methods that enable reading from and writing to .x files.

X files provide a template-driven format that enables the storage of meshes, textures, animations, and user-definable objects. Support for animation sets enables you to store predefined paths for playback in real time. Instancing and hierarchies are also supported. Instancing enables multiple references to an object, such as a mesh, while storing its data only once per file. Hierarchies are used to express relationships between data records.

The .x file format provides low-level data primitives on which applications define higher-level primitives through templates.

Three-dimensional models created in Discreet's 3ds max or Alias\|Wavefront's Maya applications can be converted to .x files with the DirectX Extensions for Alias Maya.

This section describes the structure of .x files and how to use them in your applications. Information is divided into the following topics.

-   [Loading an X File (Legacy) (Direct3D 9)](loading-an-x-file--legacy-.md)
-   [Saving to an X File (Legacy) (Direct3D 9)](saving-to-an-x-file--legacy-.md)
-   [Defining a Simple Cube (Direct3D 9)](defining-a-simple-cube.md)
-   [Adding Textures (Direct3D 9)](adding-textures.md)
-   [Adding Frames and Animations (Direct3D 9)](adding-frames-and-animations.md)

For more information about the .x file format, see [X File Reference](dx9-graphics-reference-d3dx-x-file.md).

For more information about the .x file API, see [X File Reference (Legacy)](dx9-graphics-reference-x-file.md).

## Related topics

<dl> <dt>

[Getting Started](getting-started.md)
</dt> </dl>

 

 



