---
title: High-level shader language (HLSL)
description: HLSL is the C-like high-level shader language that you use with programmable shaders in DirectX.
ms.assetid: 09cdd8d6-0cf5-4f7e-b480-f748d2fa9ca9
ms.topic: article
ms.date: 01/11/2021
topic_type: 
- kbArticle
api_name: 
api_type: 
api_location: 
ms.custom: contperf-fy21q3
---

# High-level shader language (HLSL)

HLSL is the C-like high-level shader language that you use with programmable shaders in DirectX.

For example, you can use HLSL to write a [vertex shader](../direct3d11/vertex-shader-stage.md), or a [pixel shader](../direct3d11/pixel-shader-stage.md), and use those shaders in the implementation of the renderer in your [Direct3D](../direct3d12/directx-12-programming-guide.md) application.

Or you could use HLSL to write a compute shader, perhaps to implement a physics simulation. However, if for example you're inclined to write your own convolution operator (for image processing) as HLSL in a compute shader, then you'll get better performance in that scenario if you use [Direct Machine Learning (DirectML)](../direct3d12/dml.md) instead.

HLSL was created (starting with DirectX 9) to set up the programmable 3D [pipeline](../direct3d11/overviews-direct3d-11-graphics-pipeline.md). You can program the entire pipeline with HLSL instructions.

## Where to go next

* [Programming guide for HLSL](./dx-graphics-hlsl-pguide.md)
* [Reference for HLSL](./dx-graphics-hlsl-reference.md)

### Programming guide for HLSL

For a conceptual introduction to HLSL, see the [Programming guide for HLSL](./dx-graphics-hlsl-pguide.md).

The programming guide discusses the different kinds of shader stages, and how to create, compile, optimize, bind, and link shaders.

There you'll also find overviews of, and release notes about, the successive generations of shader model version that have been released, going back as far as HLSL shader model 5.

### Reference for HLSL

For HLSL reference documentation, see the [Reference for HLSL](./dx-graphics-hlsl-reference.md).

The reference section has a complete listing of the language syntax and of the intrinsic functions that are built into HLSL in order to simplify your coding requirements.

There also you'll find a discussion of shader models versus profiles, and shader model reference content going back as far as HLSL shader model 1. There's also content covering assembly instructions, the D3DCompiler tool, and info about the errors and warnings that a shader can return.