---
title: Programming guide for HLSL
description: Data enters the graphics pipeline as a stream of primitives and is processed by the shader stages.
ms.assetid: 4894e085-30e7-4cc5-8ae6-a84b601e4ce3
ms.topic: article
ms.date: 02/21/2019
topic_type: 
- kbArticle
api_name: 
api_type: 
api_location: 
---

# Programming guide for HLSL

Data enters the graphics pipeline as a stream of primitives and is processed by the shader stages. The actual shader stages depend on the version of Direct3D, but certainly include the vertex, pixel and geometry stages. Other stages include the hull and domain shaders for tessellation, and the compute shader. These stages are completely programmable using the High Level Shading Language ([HLSL](dx-graphics-hlsl-reference.md)).

HLSL shaders can be compiled at author-time or at runtime, and set at runtime into the appropriate pipeline stage. Direct3D 9 shaders can be designed using [shader model 1](dx-graphics-hlsl-sm1.md), [shader model 2](dx-graphics-hlsl-sm2.md) and [shader model 3](dx-graphics-hlsl-sm3.md); Direct3D 10 shaders can only be designed on [shader model 4](dx-graphics-hlsl-sm4.md). Direct3D 11 shaders can be designed on [shader model 5](d3d11-graphics-reference-sm5.md). Direct3D 11.3 and Direct3D 12 can be designed on [shader model 5.1](shader-model-5-1.md), and Direct3D 12 can also be designed on [shader model 6](shader-model-6-0.md).

## In this section

| Topic | Description |
|-|-|
| [Using shader linking](using-shader-linking.md) | We show how to create precompiled HLSL functions, package them into libraries, and link them into full shaders at run-time. |
| [Writing HLSL Shaders in Direct3D 9](dx-graphics-hlsl-writing-shaders-9.md) | |
| [Using Shaders in Direct3D 9](dx-graphics-hlsl-using-shaders-9.md) | |
| [Using Shaders in Direct3D 10](dx-graphics-hlsl-using-shaders-10.md) | |
| [Optimizing HLSL Shaders](dx-graphics-hlsl-optimize.md) | |
| [Debugging Shaders in Visual Studio](dx-graphics-hlsl-debug-visual-studio.md) | The latest tool for debugging shaders now ships as a feature in Microsoft Visual Studio, called Visual Studio Graphics Debugger.  |
| [Compiling Shaders](dx-graphics-hlsl-part1.md) | Let's now look at various ways to compile your shader code and conventions for file extensions for shader code. |
| [Specifying Compiler Targets](specifying-compiler-targets.md) | Here we list the targets for various profiles that the **D3DCompile\*** functions and the HLSL compiler support. |
| [Unpacking and Packing DXGI\_FORMAT for In-Place Image Editing](dx-graphics-hlsl-unpacking-packing-dxgi-format.md) | |
| [Using HLSL minimum precision](using-hlsl-minimum-precision.md) | Starting with Windows 8, graphics drivers can implement minimum precision [HLSL scalar data types](dx-graphics-hlsl-scalar.md) by using any precision greater than or equal to their specified bit precision.  |
| [HLSL Shader Model 5](overviews-direct3d-11-hlsl.md) | |
| [HLSL Shader Model 5.1](hlsl-shader-model-5-1-features-for-direct3d-12.md) | This section describes the features of Shader Model 5.1 as they apply in practice to D3D12 and D3D11.3. All DirectX 12 hardware supports Shader Model 5.1. |
| [HLSL Shader Model 6.0](hlsl-shader-model-6-0-features-for-direct3d-12.md) | Describes the wave operation intrinsics added to HLSL Shader Model 6.0. |
| [HLSL Shader Model 6.4](hlsl-shader-model-6-4-features-for-direct3d-12.md) | Describes the machine learning intrinsics added to HLSL Shader Model 6.4. |

## Related topics

* [HLSL](dx-graphics-hlsl.md)
* [Reference for HLSL](dx-graphics-hlsl-reference.md)
