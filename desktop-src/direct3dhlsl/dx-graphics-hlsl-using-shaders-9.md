---
title: Using Shaders in Direct3D 9
description: Using Shaders in Direct3D 9
ms.assetid: 8d8f5124-fbf3-4af5-8399-43ba28aa6eb9
ms.topic: article
ms.date: 05/31/2018
topic_type: 
- kbArticle
api_name: 
api_type: 
api_location: 
---

# Using Shaders in Direct3D 9

-   [Compiling a Shader for Specific Hardware](#compiling-a-shader-for-specific-hardware)
-   [Initializing Shader Constants](#initializing-shader-constants)
-   [Binding a Shader Parameter to a Particular Register](#binding-a-shader-parameter-to-a-particular-register)
-   [Rendering a Programmable Shader](#rendering-a-programmable-shader)
-   [Debugging Shaders](#debugging-shaders)
-   [Related topics](#related-topics)

## Compiling a Shader for Specific Hardware

Shaders were first added to Microsoft DirectX in DirectX 8.0. At that time, several virtual shader machines were defined, each roughly corresponding to a particular graphics processor produced by the top 3D graphics vendors. For each of these virtual shader machines, an assembly language was designed. Programs written to the shader models (names vs\_1\_1 and ps\_1\_1 - ps\_1\_4) were relatively short and were generally written by developers directly in the appropriate assembly language. The application would pass this human-readable assembly language code to the D3DX library using [**D3DXAssembleShader**](/windows/desktop/direct3d9/d3dxassembleshader) and get back a binary representation of the shader which would in turn get passed using [**CreateVertexShader**](/windows/desktop/api/d3d9/nf-d3d9-idirect3ddevice9-createvertexshader) or [**CreatePixelShader**](/windows/desktop/api/d3d9/nf-d3d9-idirect3ddevice9-createpixelshader). For more detail, see the software development kit (SDK).

The situation in Direct3D 9 is similar. An application passes an HLSL shader to D3DX using [**D3DXCompileShader**](/windows/desktop/direct3d9/d3dxcompileshader) and gets back a binary representation of the compiled shader which in turn is passed to Microsoft Direct3D using [**CreatePixelShader**](/windows/desktop/api/d3d9/nf-d3d9-idirect3ddevice9-createpixelshader) or [**CreateVertexShader**](/windows/desktop/api/d3d9/nf-d3d9-idirect3ddevice9-createvertexshader). The runtime does not know anything about HLSL, only the binary assembly shader models. This is nice because it means that the HLSL compiler can be updated independent of the Direct3D runtime. You can also compile shaders offline using [fxc](/windows/desktop/direct3dtools/fxc).

In addition to the development of the HLSL compiler, Direct3D 9 also introduced the assembly-level shader models to expose the functionality of the latest generation of graphics hardware. Application developers can work in assembly for these new models (vs\_2\_0, vs\_3\_0, ps\_2\_0, ps\_3\_0) but we expect most developers to move to HLSL for shader development.

Of course, the ability to write an HLSL program to express a particular shading algorithm does not automatically enable it to run on any given hardware. An application calls D3DX to compile a shader into binary assembly code with [**D3DXCompileShader**](/windows/desktop/direct3d9/d3dxcompileshader). One of the limitations with this entry point is a parameter that defines which of the assembly-level models (or compilation targets) the HLSL compiler should use to express the final shader code. If an application is doing HLSL shader compilation at run time (as opposed to compile time or offline), the application could examine the capabilities of the Direct3D device and select the compilation target to match. If the algorithm expressed in the HLSL shader is too complex to execute on the selected compilation target, compilation will fail. This means that while HLSL is a huge benefit to shader development, it does not free developers from the realities of shipping games to a target audience with graphics devices of varying capabilities. As a game developer, you still have to manage a tiered approach to your visuals; this means writing better shaders for more capable graphics cards and writing more basic versions for older cards. With well written HLSL, however, this burden can be eased significantly.

Rather than compile HLSL shaders using D3DX on the customer's machine at application load time or on first use, many developers choose to compile their shader from HLSL to binary assembly code before they even ship. This keeps their HLSL source code away from prying eyes and also ensures that all the shaders their application will ever run have gone through their internal quality assurance process. A convenient utility for compiling shaders offline is [fxc](/windows/desktop/direct3dtools/fxc). This tool has a number of options that you can use to compile code for the specified compile target. Studying the disassembled output can be very educational during development if you want to optimize your shaders or just generally get to know the virtual shader machine's capabilities at a more detailed level. These options are summarized below:

## Initializing Shader Constants

Shader constants are contained in the constant table. This can be accessed with the [**ID3DXConstantTable**](/windows/desktop/direct3d9/id3dxconstanttable) interface. Global shader variables can be initialized in shader code. These are initialized at run time by calling [**SetDefaults**](/windows/desktop/direct3d9/id3dxconstanttable--setdefaults).

## Binding a Shader Parameter to a Particular Register

The compiler will automatically assign registers to global variables. The compiler would assign Environment to sampler register s0, SparkleNoise to sampler register s1, and k\_s to constant register c0 (assuming no other sampler or constant registers were already assigned) for the following three global variables:


```
sampler Environment;
sampler SparkleNoise;
float4 k_s;
```



It is also possible to bind variables to a specific register. To force the compiler to assign to a particular register, use the following syntax:


```
register(RegisterName)
```



where RegisterName is the name of the specific register. The following examples demonstrate the specific register assignment syntax, where the sampler Environment will be bound to sampler register s1, SparkleNoise will be bound to sampler register s0, and k\_s will be bound to constant register c12:


```
sampler Environment : register(s1);
sampler SparkleNoise : register(s0);
float4 k_s : register(c12);
```



## Rendering a Programmable Shader

A shader is rendered by setting the current shader in the device, initializing the shader constants, telling the device where the varying input data is coming from, and finally rendering the primitives. Each of these can be accomplished by calling the following methods respectively:

-   [**SetVertexShader**](/windows/desktop/api/d3d9helper/nf-d3d9helper-idirect3ddevice9-setvertexshader)
-   [**SetVertexShaderConstantF**](/windows/desktop/api/d3d9helper/nf-d3d9helper-idirect3ddevice9-setvertexshaderconstantf)
-   [**SetStreamSource**](/windows/desktop/api/d3d9helper/nf-d3d9helper-idirect3ddevice9-setstreamsource)
-   [**DrawPrimitive**](/windows/desktop/api/d3d9/nf-d3d9-idirect3ddevice9-drawprimitive)

## Debugging Shaders

The DirectX extension for Microsoft Visual Studio .NET is provides a fully integrated HLSL debugger within the Visual Studio .NET Integrated Development Environment (IDE). In order to prepare for shader debugging, you must install the right tools on your machine (see [Debugging Shaders in Visual Studio (Direct3D 9)](dx-graphics-hlsl-debug-visual-studio.md)).

## Related topics

<dl> <dt>

[Programming Guide for HLSL](dx-graphics-hlsl-pguide.md)
</dt> </dl>

 

 