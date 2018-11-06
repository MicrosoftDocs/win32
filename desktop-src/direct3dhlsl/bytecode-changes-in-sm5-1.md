---
title: Bytecode changes in SM5.1
description: SM5.1 changes how resource registers are declared and referenced in instructions.
ms.assetid: ABECF705-67B8-4419-8D18-74B43B9DC3AF
ms.topic: article
ms.date: 05/31/2018
---

# Bytecode changes in SM5.1

SM5.1 changes how resource registers are declared and referenced in instructions.

SM5.1 moves towards declaring a register “variable”, similar to how it is done for group shared memory registers, illustrated by the following example:

``` syntax
Texture2D<float4> tex0          : register(t5,  space0);
Texture2D<float4> tex1[][5][3]  : register(t10, space0);
Texture2D<float4> tex2[8]       : register(t0,  space1);
SamplerState samp0              : register(s5, space0);

float4 main(float4 coord : COORD) : SV_TARGET
{
    float4 r = coord;
    r += tex0.Sample(samp0, r.xy);
    r += tex2[r.x].Sample(samp0, r.xy);
    r += tex1[r.x][r.y][r.z].Sample(samp0, r.xy);
    return r;
}
```

The disassembly of this example follows:

``` syntax
// Resource Bindings:
//
// Name                                 Type  Format         Dim Space Slot  Elements
// ------------------------------ ---------- ------- ----------- ----- ---- ---------
// samp0                             sampler      NA          NA     0    5         1
// tex0                              texture  float4          2d     0    5         1
// tex1[0][5][3]                     texture  float4          2d     0   10 unbounded
// tex2[8]                           texture  float4          2d     1    0         8
//
//
//
// Input signature:
//
// Name                 Index   Mask Register SysValue  Format   Used
// -------------------- ----- ------ -------- -------- ------- ------
// COORD                    0   xyzw        0     NONE   float   xyzw
//
//
// Output signature:
//
// Name                 Index   Mask Register SysValue  Format   Used
// -------------------- ----- ------ -------- -------- ------- ------
// SV_TARGET                0   xyzw        0   TARGET   float   xyzw
//
ps_5_1
dcl_globalFlags refactoringAllowed
dcl_sampler s0[5:5], mode_default, space=0
dcl_resource_texture2d (float,float,float,float) t0[5:5], space=0
dcl_resource_texture2d (float,float,float,float) t1[10:*], space=0
dcl_resource_texture2d (float,float,float,float) t2[0:7], space=1
dcl_input_ps linear v0.xyzw
dcl_output o0.xyzw
dcl_temps 2
sample r0.xyzw, v0.xyxx, t0[0].xyzw, s0[5]
add r0.xyzw, r0.xyzw, v0.xyzw
ftou r1.x, r0.x
sample r1.xyzw, r0.xyxx, t2[r1.x + 0].xyzw, s0[5]
add r0.xyzw, r0.xyzw, r1.xyzw
ftou r1.xyz, r0.zyxz
imul null, r1.yz, r1.zzyz, l(0, 15, 3, 0)
iadd r1.y, r1.z, r1.y
iadd r1.x, r1.x, r1.y
sample r1.xyzw, r0.xyxx, t1[r1.x + 10].xyzw, s0[5]
add o0.xyzw, r0.xyzw, r1.xyzw
ret
// Approximately 12 instruction slots used
```

Each shader resource range now has an ID (a name) in the shader bytecode. For example, tex1 texture array becomes ‘t1’ in the shader byte code. Giving unique IDs to each resource range allows two things:

-   Unambiguously identify which resource range (see dcl\_resource\_texture2d) is being indexed in an instruction (see sample instruction).
-   Attach set of attributes to the declaration, e.g., element type, stride size, raster operation mode, etc..

Note that the ID of the range is not related to the HLSL lower bound declaration.

The order of reflection resource bindings and shader declaration instructions is the same to aid in identifying the correspondence between HLSL variables and bytecode IDs.

Each declaration instruction in SM5.1 uses a 3D operand to define: range ID, lower and upper bounds. An additional token is emitted to specify the register space. Other tokens may be emitted as well to convey additional properties of the range, e.g., cbuffer or structured buffer declaration instruction emits the size of the cbuffer or structure. The exact details of encoding can be found in d3d12TokenizedProgramFormat.h and D3D10ShaderBinary::CShaderCodeParser.

SM5.1 instructions will not emit additional resource operand information as part of the instruction (as in SM5.0). This information is now moved to the declaration instructions. In SM5.0, instructions indexing resources required resource attributes to be described in extended opcode tokens, since indexing obfuscated the association to the declaration. In SM5.1 each ID (such as ‘t1’) is unambiguously associated with a single declaration that describes the required resource information. Therefore, the extended opcode tokens used on instructions to describe resource information are no longer emitted.

In non-declaration instructions, a resource operand for samplers, SRVs, and UAVs is a 2D operand. The first index is a literal constant that specifies the range ID. The second index represents the linearized value of the index. The value is computed relative to the beginning of the corresponding register space (not relative to the beginning of the logical range) to better correlate with the root signature and to reduce the driver compiler burden of adjusting the index.

A resource operand for CBVs is a 3D operand: literal ID of the range, index of the cbuffer, offset into the particular instance of cbuffer.

## Related topics

<dl> <dt>

[HLSL Shader Model 5.1 Features for Direct3D 12](hlsl-shader-model-5-1-features-for-direct3d-12.md)
</dt> <dt>

[Shader Model 5.1](shader-model-5-1.md)
</dt> </dl>

 

 




