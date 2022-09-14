---
title: Using shader linking
description: We show how to create precompiled HLSL functions, package them into libraries, and link them into full shaders at run-time.
ms.assetid: 3A1597FF-F848-415E-BDF8-199C69C05C3B
ms.topic: article
ms.date: 05/31/2018
---

# Using shader linking

We show how to create precompiled HLSL functions, package them into libraries, and link them into full shaders at run-time. Shader linking is supported starting with Windows 8.1.

**Objective:** Learn how to use shader linking.

## Prerequisites

We assume that you are familiar with C++. You also need basic experience with graphics programming concepts.

**Total time to complete:** 60 minutes.

## Where to go from here

Also see [HLSL compiler APIs](dx-graphics-d3dcompiler-reference.md).

We show you how to:

-   Compile your shader code
-   Load the compiled code into a shader library
-   Bind the resources from source slots to destination slots
-   Construct function-linking-graphs (FLGs) for shaders
-   Link shader graphs with a shader library to produce a shader blob that the Direct3D runtime can use

Next we make a shader library and bind resources from source slots to destination slots.

[Packaging a shader library](pachaging-a-shader-library.md)

## Related topics

<dl> <dt>

[Programming Guide for HLSL](dx-graphics-hlsl-pguide.md)
</dt> <dt>

[Direct3D 11 Graphics](/windows/desktop/direct3d11/atoc-dx-graphics-direct3d-11)
</dt> <dt>

[DXGI](/windows/desktop/direct3ddxgi/dx-graphics-dxgi)
</dt> </dl>

 

 