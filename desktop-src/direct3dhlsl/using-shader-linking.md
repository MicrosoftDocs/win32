---
title: Using shader linking
description: We show how to create precompiled HLSL functions, package them into libraries, and link them into full shaders at run-time.
ms.assetid: '3A1597FF-F848-415E-BDF8-199C69C05C3B'
---

# Using shader linking

We show how to create precompiled HLSL functions, package them into libraries, and link them into full shaders at run-time. Shader linking is supported starting with Windows 8.1.

**Objective:** Learn how to use shader linking.

## Prerequisites

We assume that you are familiar with C++. You also need basic experience with graphics programming concepts.

**Total time to complete:** 60 minutes.

## Where to go from here

Here we talk about how to use shader linking by referencing the [HLSL shader compiler sample](http://go.microsoft.com/fwlink/?LinkId=321937). This sample demonstrates how to use [HLSL compiler APIs](dx-graphics-d3dcompiler-reference.md) from within Windows Store apps. It also demonstrates how to use shader linking to link precompiled shader libraries and form complete shaders at runtime.

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

[Direct3D 11 Graphics](https://msdn.microsoft.com/library/windows/desktop/ff476080)
</dt> <dt>

[DXGI](https://msdn.microsoft.com/library/windows/desktop/hh404534)
</dt> </dl>

 

 




