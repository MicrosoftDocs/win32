---
title: dcl_interface (sm5 - asm)
description: Declare function table pointers (interfaces). | dcl_interface (sm5 - asm)
ms.assetid: 5A4D911E-7117-409B-8FDC-9CEC2C185C15
ms.topic: reference
ms.date: 05/31/2018
---

# dcl\_interface (sm5 - asm)

Declare function table pointers (interfaces).



| dcl\_interface fp\#\[arraySize\]\[numCallSites\] = {ft\#, ft\#, ...} |
|----------------------------------------------------------------------|



 



| Item                                                          | Description                                    |
|---------------------------------------------------------------|------------------------------------------------|
| <span id="fp_"></span><span id="FP_"></span>*fp\#*<br/> | \[in\] The function table pointers.<br/> |



 

## Remarks

Each interface needs to be bound from the API before the shader is usable. Binding gives a reference to one of the function tables so that the method slots can be filled in. The compiler will not generate pointers for unreferenced objects.

A function table pointer has a full set of method slots to avoid the extra level of indirection that a C++ pointer-to- pointer-to-vtable representation would require. That would also require that this pointers be 5-tuples. In the HLSL virtual inlining model it's always known what global variable/input is used for a call so we can set up tables per root object.

Function pointer declarations indicate which function tables are legal to use with them. This also allows derivation of method correlation information.

The first \[\] of an interface declaration is the array size. If dynamic indexing is used the declaration will indicate that as shown. An array of interface pointers can be indexed statically also, it is not required that arrays of interface pointers mean dynamic indexing.

Numbering of interface pointers starts at 0 for the first declaration and subsequently takes array size into account, so the first pointer after a four entry array fp0\[4\]\[1\] would be fp4\[\]\[\].

The second \[\] of an interface declaration is the number of call sites, which must match the number of bodies in each table referenced in the declaration.

There are no bounds to how many function table (ft\#) choices can be listed in an interface declaration.

A given function table (ft\#) can appear more than once in one or more interface declarations.

### Restrictions

-   The number of object sites in a shader, which is the sum across all *fp\#* declarations of their \[arraySize\] declarations, must be no more than 253. This number corresponds to how many **this** pointers can be present. The runtime enforces this 253 limit to keep a bound on the size of the DDI for communicating this pointer data.
-   The number of call sites in a shader, which is the sum across all fcall statements of the number of potential branch targets, must be no more than 4096.

    For example, an [fcall](fcall--sm5---asm-.md) that uses a static index for the first *fp\[\]\[\]* dimension counts as one:

    `                       fcall fp0[0][0]         // +1`

    An **fcall** that uses a dynamic index counts as the number of elements in the array (first \[\] of **dcl\_interface**):

    `                    dcl_interface_dynamicindexed fp1[2][1] = {ft2, ft3, ft4}                      ...                     `

    `fcall fp1[r0.z + 0][1]  // +2`

    This limit helps some implementations easily fit tables of function body selections in constant buffer-like storage.

This instruction applies to the following shader stages:



| Vertex | Hull | Domain | Geometry | Pixel | Compute |
|--------|------|--------|----------|-------|---------|
| X      | X    | X      | X        | X     | X       |



 

## Minimum Shader Model

This instruction is supported in the following shader models:



| Shader Model                                              | Supported |
|-----------------------------------------------------------|-----------|
| [Shader Model 5](d3d11-graphics-reference-sm5.md)        | yes       |
| [Shader Model 4.1](dx-graphics-hlsl-sm4.md)              | no        |
| [Shader Model 4](dx-graphics-hlsl-sm4.md)                | no        |
| [Shader Model 3 (DirectX HLSL)](dx-graphics-hlsl-sm3.md) | no        |
| [Shader Model 2 (DirectX HLSL)](dx-graphics-hlsl-sm2.md) | no        |
| [Shader Model 1 (DirectX HLSL)](dx-graphics-hlsl-sm1.md) | no        |



 

cs\_4\_0 and cs\_4\_1 support this instruction for UAV and SRV.

## Related topics

<dl> <dt>

[Shader Model 5 Assembly (DirectX HLSL)](shader-model-5-assembly--directx-hlsl-.md)
</dt> </dl>

 

 





