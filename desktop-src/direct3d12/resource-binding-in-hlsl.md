---
title: Resource binding in HLSL
description: This topic describes some specific features of using High Level Shader Language (HLSL) Shader Model 5.1 with Direct3D 12.
ms.assetid: 3CD4BDAD-8AE3-4DE0-B3F8-9C9F9E83BBE9
ms.localizationpriority: high
ms.topic: article
ms.date: 08/27/2019
---

# Resource binding in HLSL

This topic describes some specific features of using High Level Shader Language (HLSL) [Shader Model 5.1](/windows/desktop/direct3dhlsl/shader-model-5-1) with Direct3D 12. All Direct3D 12 hardware supports Shader Model 5.1, so support for this model does not depend on what the hardware feature level is.

## Resource types and arrays

Shader Model 5 (SM5.0) resource syntax uses the `register` keyword to relay important information about the resource to the HLSL compiler. For example, the following statement declares an array of four textures bound at slots t3, t4, t5, and t6. t3 is the only register slot appearing in the statement, simply being the first in the array of four.

``` syntax
Texture2D<float4> tex1[4] : register(t3)
```

Shader Model 5.1 (SM5.1) resource syntax in HLSL is based on existing register resource syntax, to allow easier porting. Direct3D 12 resources in HLSL are bound to virtual registers within logical register spaces:

-   t – for shader resource views (SRV)
-   s – for samplers
-   u – for unordered access views (UAV)
-   b – for constant buffer views (CBV)

The root signature referencing the shader must be compatible with the declared register slots. For example, the following portion of a root signature would be compatible with the use of texture slots t3 through t6, as it describes a descriptor table with slots t0 through t98.

``` syntax
DescriptorTable( CBV(b1), SRV(t0,numDescriptors=99), CBV(b2) )
```

A resource declaration may be a scalar, a 1D array, or a multidimensional array:

``` syntax
Texture2D<float4> tex1 : register(t3,  space0)
Texture2D<float4> tex2[4] : register(t10)
Texture2D<float4> tex3[7][5][3] : register(t20, space1)
```

SM5.1 uses the same resource types and element types as SM5.0 does. SM5.1 declaration limits are more flexible, and constrained only by the runtime/hardware limits. The `space` keyword specifies to which logical register space the declared variable is bound. If the `space` keyword is omitted, then the default space index of 0 is implicitly assigned to the range (so the `tex2` range above resides in `space0`). `register(t3,  space0)` will never conflict with `register(t3,  space1)`, nor with any array in another space that might include t3.

An array resource may have an unbounded size, which is declared by specifying the very first dimension to be empty, or 0:

``` syntax
Texture2D<float4> tex1[] : register(t0)
```

The matching descriptor table could be:

``` syntax
DescriptorTable( CBV(b1), UAV(u0, numDescriptors = 4), SRV(t0, numDescriptors=unbounded) )
```

An unbounded array in HLSL does match a fixed number set with `numDescriptors` in the descriptor table, and a fixed size in the HLSL does match an unbounded declaration in the descriptor table.

Multi-dimensional arrays are allowed, including of an unbounded size. These multidimensional arrays are flattened out in register space.

``` syntax
Texture2D<float4> tex2[3000][10] : register(t0, space0); // t0-t29999 in space0
Texture2D<float4> tex3[0][5][3] : register(t5, space1)
```

Aliasing of resource ranges is not allowed. In other words, for each resource type (t, s, u, b), declared register ranges mustn't overlap. That includes unbounded ranges, too. Ranges declared in different register spaces never overlap. Note that unbounded `tex2` (above) resides in `space0`, while unbounded `tex3` resides in `space1`, such that they don't overlap.

Accessing resources that have been declared as arrays is as simple as indexing them.

``` syntax
Texture2D<float4> tex1[400] : register(t3);
sampler samp[7] : register(s0);
tex1[myMaterialID].Sample(samp[samplerID], texCoords);
```

There's an important default restriction on the use of the indices (`myMaterialID` and `samplerID` in the code above) in that they're not allowed to vary within a [wave](../direct3dhlsl/hlsl-shader-model-6-0-features-for-direct3d-12.md#terminology). Even changing the index based on instancing counts as varying.

If varying the index is required then specify the `NonUniformResourceIndex` qualifier on the index, for example:

``` syntax
tex1[NonUniformResourceIndex(myMaterialID)].Sample(samp[NonUniformResourceIndex(samplerID)], texCoords);
```

On some hardware the use of this qualifier generates additional code to enforce correctness (including across threads) but at a minor performance cost. If an index is changed without this qualifier and within a draw/dispatch the results are undefined.

## Descriptor arrays and texture arrays

Texture arrays have been available since DirectX 10. Texture arrays require one descriptor, however all the array slices must share the same format, width, height and mip count. Also, the array must occupy a contiguous range in virtual address space. The following code shows an example of accessing a texture array from a shader.

``` syntax
Texture2DArray<float4> myTex2DArray : register(t0); // t0
float3 myCoord(1.0f,1.4f,2.2f); // 2.2f is array index (rounded to int)
color = myTex2DArray.Sample(mySampler, myCoord);
```

In a texture array, the index can be varied freely, without any need for qualifiers such as `NonUniformResourceIndex`.

The equivalent descriptor array would be:

``` syntax
Texture2D<float4> myArrayOfTex2D[] : register(t0); // t0+
float2 myCoord(1.0f, 1.4f);
color = myArrayOfTex2D[2].Sample(mySampler,myCoord); // 2 is index
```

Note the awkward use of a float for the array index is replaced with `myArrayOfTex2D[2]`. Also descriptor arrays offer more flexibility with the dimensions. The type, `Texture2D` is this example, cannot vary, but the format, width, height, and mip count can all vary with each descriptor.

It is legitimate to have a descriptor array of texture arrays:

``` syntax
Texture2DArray<float4> myArrayOfTex2DArrays[2] : register(t0);
```

It is not legitimate to declare an array of structures, each structure containing descriptors, for example the following code is not supported.

``` syntax
struct myStruct {
    Texture2D                    a; 
    Texture2D                    b;
    ConstantBuffer<myConstants>  c;
};
myStruct foo[10000] : register(....);
```

This would have allowed the memory layout **abcabcabc....**, but is a language limitation and is not supported. One supported method of doing this would be as follows, though the memory layout in this case is **aaa...bbb...ccc...**.

``` syntax
Texture2D                     a[10000] : register(t0);
Texture2D                     b[10000] : register(t10000);
ConstantBuffer<myConstants>   c[10000] : register(b0);
```

To achieve the **abcabcabc....** memory layout, use a descriptor table without use of the `myStruct` structure.

## Resource aliasing

The resource ranges specified in the HLSL shaders are logical ranges. They are be bound to concrete heap ranges at runtime via the root signature mechanism. Normally, a logical range maps to a heap range that does not overlap with other heap ranges. However, the root signature mechanism makes it possible to alias (overlap) heap ranges of compatible types. For example, `tex2` and `tex3` ranges from the above example may be mapped to the same (or overlapping) heap range, which has the effect of aliasing textures in the HLSL program. If such aliasing is desired, the shader must be compiled with D3D10\_SHADER\_RESOURCES\_MAY\_ALIAS option, which is set by using the */res\_may\_alias* option for the [Effect-Compiler Tool](../direct3dtools/fxc.md) (FXC). The option makes the compiler produce correct code by preventing certain load/store optimizations under the assumption that resources may alias.

## Divergence and derivatives

SM5.1 does not impose limitations on the resource index; i.e.,` tex2[idx].Sample(…)` – the index idx can be a literal constant, a cbuffer constant, or an interpolated value. While the programming model provides such great flexibility, there are issues to be aware of:

-   If index diverges across a quad, the hardware-computed derivative and derived quantities such as LOD may be undefined. The HLSL compiler makes the best effort to issue a warning in this case, but will not prevent a shader from compiling. This behavior is similar to computing derivatives in divergent control flow.
-   If the resource index is divergent, the performance is diminished compared to the case of a uniform index, because the hardware needs to perform operations on several resources. Resource indexes that may be divergent must be marked with the `NonUniformResourceIndex` function in HLSL code. Otherwise results are undefined.

## UAVs in pixel shaders

SM5.1 does not impose constraints on UAV ranges in pixel shaders as was the case for SM5.0.

## Constant Buffers

SM5.1 constant buffers (cbuffer) syntax has changed from SM5.0 to enable developers to index constant buffers. To enable indexable constant buffers, SM5.1 introduces the `ConstantBuffer` “template” construct:

``` syntax
struct Foo
{
    float4 a;
    int2 b;
};
ConstantBuffer<Foo> myCB1[2][3] : register(b2, space1);
ConstantBuffer<Foo> myCB2 : register(b0, space1);
```

The preceding code declares constant buffer variable `myCB1` of type `Foo` and size 6, and a scalar, constant buffer variable `myCB2`. A constant buffer variable can now be indexed in the shader as:

``` syntax
myCB1[i][j].a.xyzw
myCB2.b.yy
```

Fields ‘a’ and ‘b’ do not become global variables, but rather must be treated as fields. For backward compatibility, SM5.1 supports the old cbuffer concept for scalar cbuffers. The following statement makes ‘a’ and ‘b’ global, read-only variables as in SM5.0. However, such an old-style cbuffer cannot be indexable.

``` syntax
cbuffer : register(b1)
{
    float4 a;
    int2 b;
};
```

Currently, the shader compiler supports the `ConstantBuffer` template for user-defined structures only.

For compatibility reasons, the HLSL compiler may automatically assign resource registers for ranges declared in `space0`. If ‘space’ is omitted in the register clause, the default `space0` is used. The compiler uses the first-hole-fits heuristic to assign the registers. The assignment can be retrieved via the reflection API, which has been extended to add the *Space* field for space, while the *BindPoint* field indicates the lower bound of the resource register range.

## Bytecode changes in SM5.1

SM5.1 changes how resource registers are declared and referenced in instructions. The syntax involves declaring a register “variable”, similar to how it is done for group shared memory registers:

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

This will disassemble to:

``` syntax
// Resource Bindings:
//
// Name                                 Type  Format         Dim    ID   HLSL Bind     Count
// ------------------------------ ---------- ------- ----------- -----   --------- ---------
// samp0                             sampler      NA          NA     S0    a5            1
// tex0                              texture  float4          2d     T0    t5            1
// tex1[0][5][3]                     texture  float4          2d     T1   t10        unbounded
// tex2[8]                           texture  float4          2d     T2    t0.space1     8
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
// Approximately 12 instruction slots are used.
```

Each shader resource range now has an ID (a name) that is unique to the shader bytecode. For example, tex1 (t10) texture array becomes ‘T1’ in the shader bytecode. Giving unique IDs to each resource range allows two things:

-   Unambiguously identify which resource range (see dcl\_resource\_texture2d) is being indexed in an instruction (see sample instruction).
-   Attaching a set of attributes to the declaration, e.g., element type, stride size, raster operation mode, etc.

Note that the ID of the range is not related to the HLSL lower bound declaration.

The order of reflection resource bindings (listing at the top) and shader declaration instructions (dcl\_\*) is the same to aid in identifying the correspondence between HLSL variables and bytecode IDs.

Each declaration instruction in SM5.1 uses a 3D operand to define: range ID, lower and upper bounds. An additional token is emitted to specify the register space. Other tokens may be emitted as well to convey additional properties of the range, e.g., cbuffer or structured buffer declaration instruction emits the size of the cbuffer or structure. The exact details of encoding can be found in d3d12TokenizedProgramFormat.h and **D3D10ShaderBinary::CShaderCodeParser**.

SM5.1 instructions will not emit additional resource operand information as part of the instruction (as in SM5.0). This information is now in the declaration instructions. In SM5.0, instructions indexing resources required resource attributes to be described in extended opcode tokens, since indexing obfuscated the association to the declaration. In SM5.1, each ID (such as ‘t1’) is unambiguously associated with a single declaration that describes the required resource information. Therefore, the extended opcode tokens used on instructions to describe resource information are no longer emitted.

In non-declaration instructions, a resource operand for samplers, SRVs, and UAVs is a 2D operand. The first index is a literal constant that specifies the range ID. The second index represents the linearized value of the index. The value is computed relative to the beginning of the corresponding register space (not relative to the beginning of the logical range) to better correlate with the root signature and to reduce the driver compiler burden of adjusting the index.

A resource operand for CBVs is a 3D operand, containing: literal ID of the range, index of the constant buffer, offset into the particular instance of constant buffer.

## Example HLSL Declarations

HLSL programs do not need to know anything about root signatures. They can assign bindings to the virtual “register” binding space, t\# for SRVs, u\# for UAVs, b\# for CBVs, s\# for samplers, or rely on the compiler to pick assignments (and query the resulting mappings using shader reflection afterwards). The root signature maps descriptor tables, root descriptors, and root constants to this virtual register space.

The following are some example declarations an HLSL shader might have. Note that there are no references to root signatures or descriptor tables.

``` syntax
Texture2D foo[5] : register(t2);
Buffer bar : register(t7);
RWBuffer dataLog : register(u1);

Sampler samp : register(s0);

struct Data
{
    UINT index;
    float4 color;
};
ConstantBuffer<Data> myData : register(b0);

Texture2D terrain[] : register(t8); // Unbounded array
Texture2D misc[] : register(t0,space1); // Another unbounded array 
                                        // space1 avoids overlap with above t#

struct MoreData
{
    float4x4 xform;
};
ConstantBuffer<MoreData> myMoreData : register(b1);

struct Stuff
{
    float2 factor;
    UINT drawID;
};
ConstantBuffer<Stuff> myStuff[][3][8]  : register(b2, space3)
```

## Related topics

* [Dynamic Indexing using HLSL 5.1](dynamic-indexing-using-hlsl-5-1.md)
* [Effect-Compiler Tool](../direct3dtools/fxc.md)
* [HLSL Shader Model 5.1 Features for Direct3D 12](../direct3dhlsl/hlsl-shader-model-5-1-features-for-direct3d-12.md)
* [Rasterizer Ordered Views](rasterizer-order-views.md)
* [Resource Binding](resource-binding.md)
* [Root Signatures](root-signatures.md)
* [Shader Model 5.1](../direct3dhlsl/shader-model-5-1.md)
* [Shader Specified Stencil Reference Value](shader-specified-stencil-reference-value.md)
* [Specifying Root Signatures in HLSL](specifying-root-signatures-in-hlsl.md)
