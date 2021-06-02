---
title: ps_1_1__ps_1_2__ps_1_3__ps_1_4 Registers
description: Pixel shaders depend on registers to get vertex data, to output pixel data, to hold temporary results during calculations and to identify texture sampling stages.
ms.assetid: ca25a030-b4da-4893-b9f3-e3bb12f18d83
keywords:
- Registers - ps_1_1 to ps_1_4
ms.topic: article
ms.date: 05/31/2018
topic_type:
- kbArticle
api_name: 
api_type: 
api_location: 
---

# ps\_1\_1\_\_ps\_1\_2\_\_ps\_1\_3\_\_ps\_1\_4 Registers

Pixel shaders depend on registers to get vertex data, to output pixel data, to hold temporary results during calculations and to identify texture sampling stages. There are several types of registers, each with a unique functionality. This section contains reference information for the input and output registers implemented by pixel shader version 1\_X.

Registers hold data for use by the pixel shader. Registers are fully described in the following sections.

-   Register Types describes the four types of registers available and their purposes.
-   Read Port Limit details the restrictions on using multiple registers in a single instruction.
-   Read only Read Write describes which registers can be used for reading, writing, or both.
-   Range details the range of the component data.

## Register Types



|      |                    | Versions |      |      |              |
|------|--------------------|----------|------|------|--------------|
| Name | Type               | 1\_1     | 1\_2 | 1\_3 | 1\_4         |
| c\#  | Constant register  | 8        | 8    | 8    | 8            |
| r\#  | Temporary register | 2        | 2    | 2    | 6            |
| t\#  | Texture register   | 4        | 4    | 4    | 6            |
| v\#  | Color register     | 2        | 2    | 2    | 2 in phase 2 |



 

-   Constant registers contain constant data. Data can be loaded into a constant register using [**SetPixelShaderConstantF**](/windows/desktop/api/d3d9helper/nf-d3d9helper-idirect3ddevice9-setpixelshaderconstantf) or it can be defined using [def - ps](def---ps.md). Constant registers are not usable by texture address instructions. The only exception is the [texm3x3spec - ps](texm3x3spec---ps.md) instruction, which uses a constant register to supply an eye-ray vector.
-   Temporary registers are used to store intermediate results. r0 additionally serves as the pixel shader output. The value in r0 at the end of the shader is the pixel color for the shader.

    Shader validation will fail [**CreatePixelShader**](/windows/desktop/api/d3d9/nf-d3d9-idirect3ddevice9-createpixelshader) on any shader that attempts to read from a temporary register that has not been written by a previous instruction. [**D3DXAssembleShader**](/windows/desktop/direct3d9/d3dxassembleshader) will fail similarly, assuming validation is enabled (do not use D3DXSHADER\_SKIPVALIDATION).

-   Texture registers

    For pixel shader version 1\_1 to 1\_3, texture registers contain texture data or texture coordinates. Texture data is loaded into a texture register when a texture is sampled. Texture sampling uses texture coordinates to look up, or sample, a color value at the specified (u,v,w,q) coordinates while taking into account the texture stage state attributes. The texture coordinate data is interpolated from the vertex texture coordinate data and is associated with a specific texture stage. There is a default one-to-one association between texture stage number and texture coordinate declaration order. By default, the first set of texture coordinates defined in the vertex format is associated with texture stage 0.

    For these pixel shader versions, texture registers behave just like temporary registers when used by arithmetic instructions.

    For pixel shader version 1\_4, texture registers (t\#) contain read-only texture coordinate data. This means that the texture coordinate set and the texture stage number are independent from each other. The texture stage number (from which to sample a texture) is determined by the destination register number (r0 to r5). For the texld instruction, the texture coordinate set is determined by the source register (t0 to t5), so the texture coordinate set can be mapped to any texture stage. In addition, the source register (specifying texture coordinates) for texld can also be a temporary register (r\#), in which case the contents of the temporary register are used as texture coordinates.

-   Color registers contain per-pixel color values. The values are obtained by per-pixel iteration of the diffuse and specular color values in the vertex data. For pixel shader version 1\_4 shaders, color registers are available only during the second phase.

    If the shade mode is set to D3DSHADE\_FLAT, the iteration of both vertex colors (diffuse and specular) is disabled. Regardless of the shade mode, fog will still be iterated by the pipeline if pixel fog is enabled. Keep in mind that fog is applied later in the pipeline than the pixelshader.

    It is common to load the v0 register with the vertex diffuse color data. It is also common to load the v1 register with the vertex specular color data.

    Input color data values are clamped (saturated) to the range 0 through 1 because this is the valid input range for color registers in the pixel shader.

    Pixel shaders have read only access to color registers. The contents of these registers are iterated values, but iteration may be performed at much lower precision than texture coordinates.

## Read Port Limit

The read port limit specifies the number of different registers of each register type that can be used as a source register in a single instruction.



|      |                    | Versions |      |      |              |
|------|--------------------|----------|------|------|--------------|
| Name | Type               | 1\_1     | 1\_2 | 1\_3 | 1\_4         |
| c\#  | Constant register  | 2        | 2    | 2    | 2            |
| r\#  | Temporary register | 2        | 2    | 2    | 3            |
| t\#  | Texture register   | 2        | 3    | 3    | 1            |
| v\#  | Color register     | 2        | 2    | 2    | 2 in phase 2 |



 

For example, the color registers for almost all versions have a read port limit of two. This means that a single instruction can use a maximum of two different color registers (v0 and v1 for instance) as source registers. This example shows two color registers being used in the same instruction:


```
mad r0, v1, c2, v0
```



## Read-only, Read/Write

The register types are identified according to read-only (RO) capability or read/write (RW) capability in the following table. Read-only registers can be used only as source registers in an instruction; they can never be used as a destination register.



|      |                    | Versions |      |      |                    |
|------|--------------------|----------|------|------|--------------------|
| Name | Type               | 1\_1     | 1\_2 | 1\_3 | 1\_4               |
| c\#  | Constant register  | RO       | RO   | RO   | RO                 |
| r\#  | Temporary register | RW       | RW   | RW   | RW                 |
| t\#  | Texture register   | RW       | RW   | RW   | See following note |
| v\#  | Color register     | RO       | RO   | RO   | RO                 |



 

Registers that are RW capable can be used to store intermediate results. This includes the temporary registers and texture registers for some of the shader versions.

> [!Note]  
>
> -   For pixel shader version 1\_4, texture registers are RO for texture addressing instructions, and texture registers can be neither read from nor written to by arithmetic instructions. Also, because texture registers have become texture coordinate registers, having RO access is not a regression of previous functionality.

 

## Range

The range is the maximum and minimum register data value. The ranges vary based on the type of register. The ranges for some of the registers can be queried from the device caps using [**GetDeviceCaps**](/windows/desktop/api/d3d9/nf-d3d9-idirect3d9-getdevicecaps).



| Name | Type               | Range                                               | Versions     |
|------|--------------------|-----------------------------------------------------|--------------|
| c\#  | Constant register  | -1 to +1                                            | All versions |
| r\#  | Temporary register | \- PixelShader1xMaxValue to + PixelShader1xMaxValue | All versions |
| t\#  | Texture register   | \- MaxTextureRepeat to + MaxTextureRepeat           | All versions |
| v\#  | Color register     | 0 to 1                                              | All versions |



 

Early pixel shader hardware represents data in registers using a fixed-point number. This limits precision to a maximum of approximately eight bits for the fractional part of a number. Keep this in mind when designing a shader.

For pixel shader version 1\_1 to 1\_3, MaxTextureRepeat must be a minimum of one. For 1\_4, MaxTextureRepeat must be a minimum of eight.

See [**D3DCAPS9**](/windows/desktop/api/d3d9caps/ns-d3d9caps-d3dcaps9) for more information about PixelShader1xMaxValue.

## Related topics

<dl> <dt>

[Registers](dx9-graphics-reference-asm-ps-registers.md)
</dt> </dl>

 

 
