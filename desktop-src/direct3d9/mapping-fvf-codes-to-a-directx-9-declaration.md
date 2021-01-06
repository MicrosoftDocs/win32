---
description: This table maps FVF codes to a D3DVERTEXELEMENT9 structure.
ms.assetid: de865481-2a08-4d25-967c-8e68b7affe8d
title: Mapping FVF Codes to a Direct3D 9 Declaration (Direct3D 9)
ms.topic: article
ms.date: 05/31/2018
---

# Mapping FVF Codes to a Direct3D 9 Declaration (Direct3D 9)

This table maps FVF codes to a [**D3DVERTEXELEMENT9**](d3dvertexelement9.md) structure.



| FVF                                                   | Data type                                                           | Usage                                                                         | Usage index |
|-------------------------------------------------------|---------------------------------------------------------------------|-------------------------------------------------------------------------------|-------------|
| D3DFVF\_XYZ                                           | D3DDECLTYPE\_FLOAT3                                                 | D3DDECLUSAGE\_POSITION                                                        | 0           |
| D3DFVF\_XYZRHW                                        | D3DDECLTYPE\_FLOAT4                                                 | D3DDECLUSAGE\_POSITIONT                                                       | 0           |
| D3DFVF\_XYZW                                          | D3DDECLTYPE\_FLOAT4                                                 | D3DDECLUSAGE\_POSITION                                                        | 0           |
| D3DFVF\_XYZB5 and D3DFVF\_LASTBETA\_UBYTE4            | D3DVSDT\_FLOAT3, D3DVSDT\_FLOAT4, D3DVSDT\_UBYTE4                   | D3DDECLUSAGE\_POSITION, D3DDECLUSAGE\_BLENDWEIGHT, D3DDECLUSAGE\_BLENDINDICES | 0           |
| D3DFVF\_XYZB5 and D3DFVF\_LASTBETA\_D3DCOLOR          | D3DVSDT\_FLOAT3, D3DVSDT\_FLOAT4, D3DVSDT\_D3DCOLOR                 | D3DDECLUSAGE\_POSITION, D3DDECLUSAGE\_BLENDWEIGHT, D3DDECLUSAGE\_BLENDINDICES | 0           |
| D3DFVF\_XYZB5                                         | D3DDECLTYPE\_FLOAT3, D3DDECLTYPE\_FLOAT4, D3DDECLTYPE\_FLOAT1       | D3DDECLUSAGE\_POSITION, D3DDECLUSAGE\_BLENDWEIGHT, D3DDECLUSAGE\_BLENDINDICES | 0           |
| D3DFVF\_XYZBn (n=1..4)                                | D3DDECLTYPE\_FLOAT3, D3DDECLTYPE\_FLOATn                            | D3DDECLUSAGE\_POSITION, D3DDECLUSAGE\_BLENDWEIGHT                             | 0           |
| D3DFVF\_XYZBn (n=1..4) and D3DFVF\_LASTBETA\_UBYTE4   | D3DDECLTYPE\_FLOAT3, D3DDECLTYPE\_FLOAT(n-1), D3DDECLTYPE\_UBYTE4   | D3DDECLUSAGE\_POSITION, D3DDECLUSAGE\_BLENDWEIGHT, D3DDECLUSAGE\_BLENDINDICES | 0           |
| D3DFVF\_XYZBn (n=1..4) and D3DFVF\_LASTBETA\_D3DCOLOR | D3DDECLTYPE\_FLOAT3, D3DDECLTYPE\_FLOAT(n-1), D3DDECLTYPE\_D3DCOLOR | D3DDECLUSAGE\_POSITION, D3DDECLUSAGE\_BLENDWEIGHT, D3DDECLUSAGE\_BLENDINDICES | 0           |
| D3DFVF\_NORMAL                                        | D3DDECLTYPE\_FLOAT3                                                 | D3DDECLUSAGE\_NORMAL                                                          | 0           |
| D3DFVF\_PSIZE                                         | D3DDECLTYPE\_FLOAT1                                                 | D3DDECLUSAGE\_PSIZE                                                           | 0           |
| D3DFVF\_DIFFUSE                                       | D3DDECLTYPE\_D3DCOLOR                                               | D3DDECLUSAGE\_COLOR                                                           | 0           |
| D3DFVF\_SPECULAR                                      | D3DDECLTYPE\_D3DCOLOR                                               | D3DDECLUSAGE\_COLOR                                                           | 1           |
| D3DFVF\_TEXCOORDSIZEm(n)                              | D3DDECLTYPE\_FLOATm                                                 | D3DDECLUSAGE\_TEXCOORD                                                        | n           |



 

## Vertex Declarations with D3DDECLUSAGE\_POSITIONT

The presence of a vertex element with (D3DUSAGE\_POSITIONT, 0) is used to indicate to the device that the vertex data coming in has already been through vertex processing (like an FVF with D3DFVF\_XYZRHW bit set). At draw time, if the currently set declaration has an element with the (D3DUSAGE\_POSITIONT, 0) semantic, the entire vertex processing is skipped (just as if an FVF with D3DFVF\_XYZRHW bit has been set).

There are some restrictions on vertex declarations with (D3DDECLUSAGE\_POSITIONT, 0):

-   Only stream zero can be used in such declarations.
-   Vertex elements must be sorted by increasing stream offset.
-   The stream offset must be DWORD aligned.
-   The same (Usage, Usage Index) pair should be listed only once.
-   Only the D3DDECLMETHOD\_DEFAULT method can be used.
-   Other vertex elements cannot have the (D3DDECLUSAGE\_POSITION, 0) semantic.

In addition, there are some restrictions on such declaration related to the device driver version. These restrictions are in effect because Direct3D sends such declarations directly to the driver without doing any conversion.

## Vertex Declarations without D3DDECLUSAGE\_POSITIONT

Runtime validates the creation of declarations. Following are the general rules for what declarations are legal.

-   All vertex elements for a stream must be consecutive and sorted by offset.
-   The stream offset must be DWORD aligned.
-   The same (Usage, Usage Index) pair should be listed only once.
-   If the D3DDEVCAPS2\_VERTEXELEMENTSCANSHARESTREAMOFFSET is set then
    -   Multiple vertex elements can share the same offset in a stream.
    -   The vertex elements can all be of different types which can be of different sizes.
    -   The vertex elements can overlap arbitrarily. For example, one element can start at a location of a stream that is, at the same time, in the middle of another element.
    -   Vertex elements are allowed to have stream offset in any order.
-   The number of vertex elements cannot be greater than 64.
-   UsageIndex should be in the range \[0-15\].
-   Declaration, used with the DrawPrimitive API, should not have vertex elements other than D3DDECLMETHOD\_DEFAULT, D3DDECLMETHOD\_LOOKUPPRESAMPLED, or D3DDECLMETHOD\_LOOKUP.
-   Declaration, which contains D3DDECLMETHOD\_LOOKUP or LOOKUPPRESAMPLED, should be used only with the programmable vertex pipeline.
-   Declaration, used with the DrawRectPatch/DrawTriPatch API, cannot have vertex elements with D3DDECLMETHOD\_LOOKUPPRESAMPLED or D3DDECLMETHOD\_LOOKUP.
-   Declaration should have only one element with D3DDECLMETHOD\_LOOKUP or D3DDECLMETHOD\_LOOKUPPRESAMPLED method.
-   Declaration with D3DDECLMETHOD\_LOOKUP or D3DDECLMETHOD\_LOOKUPPRESAMPLED should not have elements other than D3DDECLMETHOD\_DEFAULT, because displacement mapping is done only for N-patches.
-   Vertex elements with D3DDECLMETHOD\_LOOKUP or D3DDECLMETHOD\_LOOKUPPRESAMPLED can only be used with the (D3DDECLUSAGE\_SAMPLE, n) semantic and vice versa.
-   If a vertex element with D3DDECLMETHOD\_LOOKUP method has a stream index and offset of an already existing vertex element, this vertex element should have the same data type.
-   A vertex element with the D3DDECLMETHOD\_LOOKUP method should have the D3DDECLTYPE\_FLOAT2/3/4 data type
-   Vertex elements with types D3DDECLMETHOD\_CROSSUV, D3DDECLMETHOD\_PARTIALU, and D3DDECLMETHOD\_PARTIALV should have an offset of a vertex element with a compatible data type.
-   A vertex element with the method D3DDECLMETHOD\_UV or D3DDECLMETHOD\_LOOKUPPRESAMPLED must have type D3DDECLTYPE\_UNUSED, stream index zero, and stream offset zero.
-   Declarations with methods D3DDECLMETHOD\_UV, D3DDECLMETHOD\_PARTIALU, and D3DDECLMETHOD\_PARTIALV can only be used with DrawRectPatch.
-   Usage D3DDECLUSAGE\_TESSFACTOR should be used only with data type D3DDECLTYPE\_FLOAT1 and usage index 0.
-   When a declaration is used for tessellation (DrawRectPatch, DrawTriPatch, N-patches), data type must be less than or equal to D3DDECLTYPE\_SHORT4.
-   Declarations that contain methods requiring certain device capabilities (for example, displacement mapping, RT-patches) can only be created if the device supports them.
-   A vertex declaration used to draw points and lines cannot have methods other than D3DDECLMETHOD\_DEFAULT.
-   The declarations that can be created also depends on the driver capabilities.

## Driver Considerations

### Pre-Direct3D 9 Drivers

-   The input declaration must be translatable to a valid FVF (have the same order of vertex elements and their data types).
-   Gaps in texture coordinates are not allowed. This means that if there is a vertex element with (D3DDECLUSAGE\_TEXCOORD, n) then there also should be a vertex element with (D3DDECLUSAGE\_TEXCOORD, n-1).

### Direct3D 9 Drivers without Pixel Shader Version 3 Support

-   The input declaration must be translatable to a valid FVF (have the same order of vertex elements and their data types).
-   Gaps in texture coordinates are allowed.

### Direct3D 9 Drivers with Pixel Shader Version 3 Support

More general declarations are allowed.

-   Vertex elements can be in arbitrary order and can have any data types.
-   Multiple vertex elements can share the same stream offset and be of a different type in the same time if D3DDEVCAPS2\_VERTEXELEMENTSCANSHARESTREAMOFFSET is set by device.

## Vertex Declaration Usage with the Programmable Vertex Pipeline

-   At draw time, Direct3D looks for the same "usage - usage index" combination in the current vertex declaration and the current vertex shader function. When the combination is found, the register from shader function DCL is used as the destination for the vertex element.
-   When a vertex element in the current vertex declaration has a usage which is not found in the current vertex shader, that vertex element is ignored.
-   When using a vertex shaders version less than 2.0, all semantics mentioned in the shader code need to be present in the declaration bound at draw time. When using vertex shaders 2.0 and above, this restriction that allows applications to use different vertex declarations with the same vertex shader does not exist. This is useful when a vertex shader reads input data based on static conditions. Vertex shader registers not initialized because of this will have undefined values.

There are additional restrictions when using with hardware vertex processing on a DirectX 8 driver:

-   Vertex elements cannot overlap or share the same offset.
-   Data types are limited to what the DirectX 8 driver can understand.

The CreateVertexDeclaration might fail if the declaration provided cannot be converted to a DirectX 8-style declaration. For a mixed mode device, this failure will happen at Draw\* time because that is the only time it can be known whether this shader is being used with hardware or software vertex processing.

## Vertex Declaration Usage with the Fixed Function Pipeline

Only declarations that adhere to the following rules can be used:

-   There should be no gaps between vertex elements (SKIP was not allowed in a DirectX 8 declaration, which is used for the fixed function pipeline).
-   Semantic (D3DDECLUSAGE\_POSITION, 0) must be specified and should have D3DDECLTYPE\_FLOAT3 data type.
-   A vertex element with method D3DDECLMETHOD\_UV must specify usage D3DDECLUSAGE\_TEXCOORD or D3DDECLUSAGE\_BLENDWEIGHT.
-   A vertex element with method D3DDECLMETHOD\_PARTIALU, \_PARTIALV, or \_CROSSUV can only be used with D3DDECLUSAGE\_POSITION, \_NORMAL, \_BLENDWEIGHT, or \_TEXCOORD, and must use input type D3DDECLTYPE\_FLOAT3.

When a declaration is used with hardware vertex processing on a DirectX 8 driver, the Direct3D runtime converts it to a DirectX 8-style declaration with the following rules:

-   Vertex elements cannot share the same offset in a stream and they cannot overlap.
-   Data type must be less or equal D3DDECLTYPE\_SHORT4.
-   Only the following methods are allowed: D3DDECLMETHOD\_DEFAULT, D3DDECLMETHOD\_CROSSUV, and D3DDECLMETHOD\_UV
-   [Mapping between a Direct3D 9 Declaration and a Direct3D 8 Declaration (Direct3D 9)](mapping-between-a-directx-9-declaration-and-directx-8.md) shows which Direct3D 9 semantics could be converted to DirectX 8-style declaration. Usage and UsageIndex are converted to a register value.
-   If there are n vertex elements in a declaration and 0 - m (m < n) maps to an FVF (elements described in the [Mapping between a Direct3D Declaration and FVF Codes (Direct3D 9)](mapping-between-a-directx-9-declaration-and-fvf-codes.md)), but m + 1 does not, then:
    -   If any of m + 2 until n - 1 vertex elements map to FVF/dx8decl, the declaration is invalid.
    -   The elements 0 to m are converted (by the runtime for DirectX 8 and older drivers, and by the Direct3D 9 drivers) using the [Mapping between a Direct3D Declaration and FVF Codes (Direct3D 9)](mapping-between-a-directx-9-declaration-and-fvf-codes.md), m + 1, m + 2 until n - 1 become mapped to contiguous texcoord(k), texcoord(k+1), starting from any texcoord in elements 0 - m.
    -   The data type at a mapped texcoord is assumed to be float\[1234\] replacing whatever data type the current element contains (but the same size). Therefore, the existing data type can be something that is not in [Mapping between a Direct3D Declaration and FVF Codes (Direct3D 9)](mapping-between-a-directx-9-declaration-and-fvf-codes.md).
    -   If k reaches 8, the declaration is invalid for FVF/dx8decl.
    -   If any mappings to texcoords have occurred, the entire declaration is required to have no elements with generation method other than DEFAULT or the declaration is invalid for FVF/dx8decl.

## Using Vertex Declarations with ProcessVertices

A vertex declaration could be used to describe the output of ProcessVertices. Such declaration should adhere to the following rules:

-   Only stream 0 must be used.
-   Only D3DDECLMETHOD\_DEFAULT methods are allowed.
-   Only D3DDECLTYPE\_FLOATn or D3DDECLTYPE\_D3DCOLOR data types can be used.
-   Vertex elements cannot share the same offset or overlap with each other.
-   Vertex elements with (D3DDECLUSAGE\_POSITION, 0) or (D3DDECLUSAGE\_POSITIONT,0) are not required.
-   Vertex elements with (D3DDECLUSAGE\_POSITION, 0) and (D3DDECLUSAGE\_POSITIONT,0) cannot be present in the same declaration.
-   The current vertex shader must be version 3.0 or higher when such declaration is used.

## Related topics

<dl> <dt>

[Vertex Declaration](vertex-declaration.md)
</dt> </dl>

 

 



