---
title: Asm Shader Reference
description: Shaders drive the programmable graphics pipeline.
ms.assetid: 2c58815c-83b5-4ae8-a192-ba865b485bd6
ms.topic: article
ms.date: 05/31/2018
topic_type: 
- kbArticle
api_name: 
api_type: 
api_location: 
---

# Asm Shader Reference

Shaders drive the programmable graphics pipeline.

## Vertex Shader Reference

-   [vs\_1\_1](dx9-graphics-reference-asm-vs-1-1.md)
-   [vs\_2\_0](dx9-graphics-reference-asm-vs-2-0.md)
-   [vs\_2\_x](dx9-graphics-reference-asm-vs-2-x.md)
-   [vs\_3\_0](dx9-graphics-reference-asm-vs-3-0.md)

[Vertex Shader Differences](dx9-graphics-reference-asm-vs-differences.md) summarizes the differences between vertex shader versions.

## Pixel Shader Reference

-   [ps\_1\_1, ps\_1\_2, ps\_1\_3, ps\_1\_4](dx9-graphics-reference-asm-ps-1-x.md)
-   [ps\_2\_0](dx9-graphics-reference-asm-ps-2-0.md)
-   [ps\_2\_x](dx9-graphics-reference-asm-ps-2-x.md)
-   [ps\_3\_0](dx9-graphics-reference-asm-ps-3-0.md)

[Pixel Shader Differences](dx9-graphics-reference-asm-ps-differences.md) summarizes the differences between pixel shader versions.

## Shader Model 4 and 5 Reference

The [Shader Model 4 Assembly](dx-graphics-hlsl-sm4-asm.md) and [Shader Model 5 Assembly](shader-model-5-assembly--directx-hlsl-.md) sections describe the instructions that shader model 4 and 5 support.

## Behavior of Constant Registers in Assembly Shaders

There are two ways to set constant registers in an assembly shader:

-   Declare a shader constant in assembly code using one of the def\* instructions.
-   Use one of the Set\*\*\*ShaderConstant\* API methods.

### Direct3D 9 Shader Constants

In Direct3D 9 the lifetime of defined constants in a given shader is confined to the execution of that shader only (and is non-overridable). Defined constants in Direct3D 9 have no side effects outside of the shader.

Here's an example using Direct3D 9:


```
Given: 
    Create shader1 which references c4 and defines it with the def instruction

Scenario 1:
    Call Set***Shader shader1
    Call Set***ShaderConstant* to set c4
    Call Draw
    Result: The shader will see the def'd value in c4

    
Given: 
    Scenario 1 has just completed
    Create shader2 (which references c4 but does not use the def instruction
      to define it) 

Scenario 2: 
    Call Set***Shader shader2
    Call Draw
    Result: The shader will see the value last set in c4 by 
     Set***ShaderConstant* in scenario 1. This is because shader 2 
     didn't def c4.
```



In Direct3D 9, calling Get\*\*\*ShaderConstant\* will only retrieve constant values set via Set\*\*\*ShaderConstant\*.

### Direct3D 8 Shader Constants

This behavior is different in Direct3D 8.x.


```
Given:
    Create shader1 which references c4 and defines it with the def instruction

Scenario 1 (repeated with Direct3D 8):
    Call Set***Shader with shader1
    Call Set***ShaderConstant to set c4
    Call Draw
    Result: The shader will see the value in c4 from Set***ShaderConstant
```



In Direct3D 8.x Set\*\*\*ShaderConstant takes effect immediately. Consider this scenario:


```
Given:
    Create shader1 which references c4 and defines it with the def instruction
    
Scenario 3:
    Call Set***Shader with shader1
    Call Draw
    Result: The shader will see the def'd value in c4

Given:
    Scenario 3 has just completed
    Create shader2 (which references c4 but does not use the def instruction 
      to define it)     
    
Scenario 4 :    
    Call Set***Shader with shader2
    Call Draw
    Result: The shader will see the def'd value in c4 (set by def in shader 1)
```



The undesirable result is that the order in which the shaders are set could affect the observed behavior of individual shaders.

## Shader Driver Model Requirements

Direct3D 9 interfaces are restricted to device driver interface (DDI) drivers that are DirectX 7-level and above. To check the DDI level, run the [DirectX Diagnostic Tool](https://msdn.microsoft.com/library/Ee416792(v=VS.85).aspx) and examine the saved text file.

For reference, Direct3D 8 interfaces work only on DDI drivers that are DirectX 6-level and above.

## Shader Binary Format

The bitwise layout of the shader instruction stream is defined in D3d9types.h. If you want to design your own shader compiler or construction tools and you want more information about the shader token stream, refer to the Direct3D 9 Driver Development Kit (DDK).

## C-like Shader Language

See [HLSL Reference](dx-graphics-hlsl-reference.md) to experience a C-like shader language.

## Related topics

<dl> <dt>

[Reference for HLSL](dx-graphics-hlsl-reference.md)
</dt> </dl>

 

 




