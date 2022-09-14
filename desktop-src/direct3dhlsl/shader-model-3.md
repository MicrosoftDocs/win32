---
title: Shader model 3 (HLSL reference)
description: Vertex shaders and pixel shaders are simplified considerably from earlier shader versions.
ms.assetid: 01ac85cb-b309-4169-acc2-320a929b65cb
ms.topic: article
ms.date: 05/31/2018
topic_type: 
- kbArticle
api_name: 
api_type: 
api_location: 
---

# Shader model 3 (HLSL reference)

Vertex shaders and pixel shaders are simplified considerably from earlier shader versions. If you are implementing shaders in hardware, you may not use vs\_3\_0 or ps\_3\_0 with any other shader versions, and you may not use either shader type with the fixed function pipeline. These changes make it possible to simplify drivers and the runtime. The only exception is that software-only vs\_3\_0 shaders may be used with any pixel shader version. In addition, if you are using a software-only vs\_3\_0 shader with a previous pixel shader version, the vertex shader can only use output semantics that are compatible with flexible vertex format (FVF) codes.

The semantics used on vertex shader outputs must be used on pixel shader inputs. The semantics are used to map the vertex shader outputs to the pixel shader inputs, similar to the way the vertex declaration is mapped to the vertex shader input registers and previous shader models. See Match Semantics on vs 3.0 and ps 3.0 Shaders.

Additional wrap mode render states have been added to cover the possibility of additional texture coordinates in this new scheme. Attributes with D3DDECLUSAGE\_TEXCOORD and usage index from 0 to 15 are interpolated in wrap mode when the corresponding [**D3DRS\_WRAP\***](/windows/desktop/direct3d9/d3drenderstatetype) is set.

-   [Vertex Shader Model 3 Features](#vertex-shader-model-3-features)
-   [Pixel Shader Model 3 Features](#pixel-shader-model-3-features)
-   [Match Semantics on vs\_3\_0 and ps\_3\_0 Shaders](/windows)
-   [Fog, Depth, and Shading Mode Changes](#fog-depth-and-shading-mode-changes)
-   [Floating Point and Integer Conversions](#floating-point-and-integer-conversions)
-   [Specifying Full or Partial Precision](#specifying-full-or-partial-precision)
-   [Software Vertex and Pixel Shaders](#software-vertex-and-pixel-shaders)

## Vertex Shader Model 3 Features

The vertex shader output register types have been collapsed into twelve registers (see [Output Registers](dx9-graphics-reference-asm-vs-registers-output.md)). Each register that is used needs to be declared using the [dcl](dcl-usage---ps.md) instruction and a semantic (for example, dcl\_color0 o0.xyzw).

The 3\_0 vertex shader model (vs\_3\_0) expands on the features of vs\_2\_0 with more powerful register indexing, a set of simplified output registers, the ability to sample a texture in a vertex shader, and the ability to control the rate at which shader inputs are initialized.

### Index Any Register

All registers( [Input Register](dx9-graphics-reference-asm-vs-registers-input.md) and [Output Registers](dx9-graphics-reference-asm-vs-registers-output.md)) can be indexed using [Loop Counter Register](dx9-graphics-reference-asm-vs-registers-loop-counter.md) (only constant registers could be indexed in earlier versions.)

You must declare input and output registers before indexing them. However, you may not index any output register that has been declared with a position or point size semantic. In fact, if indexing is used the position and psize semantics have to be declared in the o0 and o1 registers respectively.

You are only allowed to index a continuous range of registers; that is, you cannot index across registers that have not been declared. While this restriction may be inconvenient, it permits hardware optimization to take place. Attempting to index across non-contiguous registers will produce undefined results. Shader validation does not enforce this restriction.

### Simplify Output Registers

All the various types of output registers have been collapsed into twelve output registers: 1 for position, 2 for color, 8 for texture, and 1 for fog or point size. These registers will interpolate any data they contain for the pixel shader. Output register declarations are required and semantics are assigned to each register.

The registers can be broken down as follows:

-   At least one register must be declared as a four-component position register. This is the only vertex shader register that is required.
-   The first ten registers consumed by a shader may use up to four components (xyzw) maximum.
-   The last (or twelfth) register may only contain a scalar (such as point size).

For a listing of the registers, see [Registers - vs\_3\_0](dx9-graphics-reference-asm-vs-registers-vs-3-0.md).

### Texture Sample in a Vertex Shader

Vertex shader 3\_0 supports texture lookup in the vertex shader using [texldl - vs](texldl---vs.md).

## Pixel Shader Model 3 Features

The pixel shader color and texture registers have been collapsed into ten input registers (see [Input Register Types](dx9-graphics-reference-asm-ps-registers-ps-3-0.md)). The Face Register is a floating point scalar register. Only the sign of this register is valid. If the sign is negative the primitive is a back face. This can be used inside a pixel shader to achieve two-sided lighting, for instance. The Position Register references the current (x,y) pixels.

The shader constant registers can be set using:

-   [**SetPixelShaderConstantB**](/windows/desktop/api/d3d9helper/nf-d3d9helper-idirect3ddevice9-setpixelshaderconstantb)
-   [**SetPixelShaderConstantI**](/windows/desktop/api/d3d9helper/nf-d3d9helper-idirect3ddevice9-setpixelshaderconstanti)
-   [**SetPixelShaderConstantF**](/windows/desktop/api/d3d9helper/nf-d3d9helper-idirect3ddevice9-setpixelshaderconstantf)

## Match Semantics on vs\_3\_0 and ps\_3\_0 Shaders

There are some restrictions on semantic usage with vs\_3\_0 and ps\_3\_0. In general, you need to be careful when using a semantic for a shader input that matches a semantic used on a shader output.

For instance, this pixel shader packs multiple names into one register:


```
ps_3_0 
dcl_texcoord0 v0.x 
dcl_texcoord1 v0.yz // Valid to pack multiple names into one register 
dcl_texcoord2_centroid v1.w
...
```



Each register has a different semantic. Notice that you can also name v0.x and v0.yz with different (multiple) semantics because of the use of the write mask.

Given the pixel shader, the following vs\_3\_0 shader cannot be paired with it:


```
vs_3_0 
... 
dcl_texcoord0 o5.x 
dcl_texcoord1 o6.yzw 
...
```



These two shaders conflict with their use of the [**D3DDECLUSAGE\_TEXCOORD0**](/windows/desktop/direct3d9/d3ddeclusage) And **D3DDECLUSAGE\_TEXCOORD1** semantics.

Rewrite the vertex shader like this to avoid the semantic collision:


```
vs_3_0 
... 
dcl_texcoord2 o3 
dcl_texcoord3 o9 
...
```



Similarly, a semantic name declared on different input registers in the pixel shader (v0 and v1 in the pixel shader) cannot be used in a single output register in this vertex shader. For instance, this vertex shader cannot be paired with the pixel shader because D3DDECLUSAGE\_TEXCOORD1 is used for both pixel shader input registers (v0, v1) and the vertex shader output register o3.


```
vs_3_0 
... 
dcl_texcoord0 o3.x 
dcl_texcoord1 o3.yz 

dcl_texcoord2 o3.w // BAD! Would be valid if this were not o3 
dcl_texcoord3 o9 ... 
```



On the other hand, this vertex shader cannot be paired with the pixel shader because the output mask for a parameter with a given semantic does not provide the data that is requested by the pixel shader:


```
vs_3_0 
... 
dcl_texcoord0 o5.x 
dcl_texcoord1 o5.yzw 
dcl_texcoord2 o7.yz // BAD! Would be valid if w were included 
dcl_texcoord3 o9 
... 
```



This vertex shader does not provide an output with one of the semantic names requested by the pixel shader, so the shader pairing is invalid:


```
vs_3_0 
... 
dcl_texcoord0 o5.x 
dcl_texcoord1 o5.yzw 
dcl_texcoord3 o9 
// The pixel shader wants texcoord2, with a w component, 
// but it isn't output by this vertex shader at all! 
... 
```



## Fog, Depth, and Shading Mode Changes

When D3DRS\_SHADEMODE is set for flat shading during clipping and triangle rasterization, attributes with D3DDECLUSAGE\_COLOR are interpolated as flat shaded. If any components of a register are declared with a color semantic but other components of the same register are given different semantics, flat shading interpolation (linear vs. flat) will be undefined on the components in that register without a color semantic.

If fog rendering is desired, vs\_3\_0 and ps\_3\_0 shaders must implement fog. No fog calculations are done outside of the shaders. There is no fog register in vs\_3\_0, and additional semantics D3DDECLUSAGE\_FOG (for fog blend factor computed per vertex) and D3DDECLUSAGE\_DEPTH (for passing in a depth value to the pixel shader to compute the fog blend factor) have been added.

Texture stage state D3DTSS\_TEXCOORDINDEX is ignored when using pixel shader 3.0.

The following values have been added to accommodate these changes:


```
// Fog and Depth usages
D3DDECLUSAGE_FOG 
D3DDECLUSAGE_DEPTH 

// Additional wrap states for vs_3_0 attributes with D3DDECLUSAGE_TEXCOORD 
D3DRS_WRAP8 
D3DRS_WRAP9 
D3DRS_WRAP10 
D3DRS_WRAP11 
D3DRS_WRAP12 
D3DRS_WRAP13 
D3DRS_WRAP14 
D3DRS_WRAP15
```



## Floating Point and Integer Conversions

Floating point math happens at different precision and ranges (16-bit, 24-bit, and 32-bit) in different parts of the pipeline. A value greater than the dynamic range of the pipeline that enters that pipeline (for example, a 32-bit float texture map is sampled into a 24-bit float pipeline in ps\_2\_0) creates an undefined result. For predictable behavior, you should clamp such a value to the dynamic range maximum.

Conversion from a floating point value to an integer happens in several places such as:

-   When encountering a [mova - vs](mova---vs.md) instruction.
-   During texture addressing.
-   When writing out to a non-floating point render target.

## Specifying Full or Partial Precision

Both ps\_3\_0 and ps\_2\_x provide support for two levels of precision:



| ps\_3\_0 | ps\_2\_0 | Precision         | Value                |
|----------|----------|-------------------|----------------------|
| x        |          | Full              | fp32 or higher       |
| x        |          | Partial precision | fp16=s10e5           |
| x        | x        | Full              | fp24=s16e7 or higher |
| x        | x        | Partial precision | fp16=s10e5           |



 

ps\_3\_0 supports more precision than ps\_2\_0 does. By default, all operations occur at the full precision level.

Partial precision (see [Pixel Shader Register Modifiers](dx9-graphics-reference-asm-ps-registers-modifiers.md)) is requested by adding the \_pp modifier to shader code (provided that the underlying implementation supports it). Implementations are always free to ignore the modifier and perform the affected operations in full precision.

The \_pp modifier can occur in two contexts:

-   On a texture coordinate declaration to pass partial-precision texture coordinates to the pixel shader. This could be used when texture coordinates relay color data to the pixel shader, which may be faster with partial precision than with full precision in some implementations.
-   On any instruction to request the use of partial precision, including texture load instructions. This indicates that the implementation is allowed to execute the instruction with partial precision and store a partial-precision result. In the absence of an explicit modifier, the instruction must be performed at full precision (regardless of the precision of the input operands).

An application might deliberately choose to trade off precision for performance. There are several kinds of shader input data which are natural candidates for partial precision processing:

-   Color iterators are well represented by partial-precision values.
-   Texture values from most formats can be accurately represented by partial-precision values (values sampled from 32-bit, floating-point format textures are an obvious exception).
-   Constants may be represented by partial-precision representation as appropriate to the shader.

In all these cases the developer may choose to specify partial precision to process the data, knowing that no input data precision is lost. In some cases, a shader may require that the internal steps of a calculation be performed at full precision even when input and final output values do not have more than partial precision.

## Software Vertex and Pixel Shaders

Software implementations (run-time and reference for vertex shaders and reference for pixel shaders) of version 2\_0 shaders and above have some validation relaxed. This is useful for debugging and prototyping purposes. The application indicates to the runtime/assembler that it needs some of the validation relaxed using the \_sw flag in the assembler (for example, vs\_2\_sw). A software shader will not work with hardware.

vs\_2\_sw is a relaxation to the maximum caps of vs\_2\_x; similarly, ps\_2\_sw is a relaxation to the maximum caps of ps\_2\_x. Specifically, the following validations are relaxed:



| Shader model                                           |  Resource                                    |  Limit                                                                                                                                  |
|--------------------------------------------|--------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------|
| vs\_2\_sw, vs\_3\_sw, ps\_2\_sw, ps\_3\_sw | Instruction Counts                   | Unlimited                                                                                                                         |
| vs\_2\_sw, vs\_3\_sw, ps\_2\_sw, ps\_3\_sw | Float Constant Registers             | 8192                                                                                                                              |
| vs\_2\_sw, vs\_3\_sw, ps\_2\_sw, ps\_3\_sw | Integer Constant Registers           | 2048                                                                                                                              |
| vs\_2\_sw, vs\_3\_sw, ps\_2\_sw, ps\_3\_sw | Boolean Constant Registers           | 2048                                                                                                                              |
| ps\_2\_sw                                  | Dependent-read depth                 | Unlimited                                                                                                                         |
| vs\_2\_sw                                  | flow control instructions and labels | Unlimited                                                                                                                         |
| vs\_2\_sw, vs\_3\_sw, ps\_2\_sw, ps\_3\_sw | Loop start/step/counts               | Iteration start and iteration step size for rep and loop instructions are 32-bit signed integers. Count can be up to MAX\_INT/64. |
| vs\_2\_sw, vs\_3\_sw, ps\_2\_sw, ps\_3\_sw | Port limits                          | Port limits for all register files are relaxed.                                                                                   |
| vs\_3\_sw                                  | Number of interpolators              | 16 output registers in vs\_3\_sw.                                                                                                 |
| ps\_3\_sw                                  | Number of interpolators              | 14(16-2) input registers for ps\_3\_sw.                                                                                           |



 

## Related topics

<dl> <dt>

[Shader Model 3 (DirectX HLSL)](dx-graphics-hlsl-sm3.md)
</dt> </dl>

 

 
