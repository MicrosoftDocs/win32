---
description: Defines the vertex declaration method which is a predefined operation performed by the tessellator (or any procedural geometry routine on the vertex data during tessellation).
ms.assetid: 030e04a6-4e2d-4756-80ef-e4a6a0103fd1
title: D3DDECLMETHOD enumeration (D3D9Types.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- D3DDECLMETHOD
api_type: 
- HeaderDef
api_location: 
- D3D9Types.h
---

# D3DDECLMETHOD enumeration

Defines the vertex declaration method which is a predefined operation performed by the tessellator (or any procedural geometry routine on the vertex data during tessellation).

## Syntax


```C++
typedef enum D3DDECLMETHOD { 
  D3DDECLMETHOD_DEFAULT           = 0,
  D3DDECLMETHOD_PARTIALU          = 1,
  D3DDECLMETHOD_PARTIALV          = 2,
  D3DDECLMETHOD_CROSSUV           = 3,
  D3DDECLMETHOD_UV                = 4,
  D3DDECLMETHOD_LOOKUP            = 5,
  D3DDECLMETHOD_LOOKUPPRESAMPLED  = 6
} D3DDECLMETHOD, *LPD3DDECLMETHOD;
```



## Constants

<dl> <dt>

<span id="D3DDECLMETHOD_DEFAULT"></span><span id="d3ddeclmethod_default"></span>**D3DDECLMETHOD\_DEFAULT**
</dt> <dd>

Default value. The tessellator copies the vertex data (spline data for patches) as is, with no additional calculations. When the tessellator is used, this element is interpolated. Otherwise vertex data is copied into the input register. The input and output type can be any value, but are always the same type.

</dd> <dt>

<span id="D3DDECLMETHOD_PARTIALU"></span><span id="d3ddeclmethod_partialu"></span>**D3DDECLMETHOD\_PARTIALU**
</dt> <dd>

Computes the tangent at a point on the rectangle or triangle patch in the U direction. The input type can be one of the following:

-   D3DDECLTYPE\_D3DCOLOR
-   D3DDECLTYPE\_FLOAT3
-   D3DDECLTYPE\_FLOAT4
-   D3DDECLTYPE\_SHORT4
-   D3DDECLTYPE\_UBYTE4

The output type is always D3DDECLTYPE\_FLOAT3.

</dd> <dt>

<span id="D3DDECLMETHOD_PARTIALV"></span><span id="d3ddeclmethod_partialv"></span>**D3DDECLMETHOD\_PARTIALV**
</dt> <dd>

Computes the tangent at a point on the rectangle or triangle patch in the V direction. The input type can be one of the following:

-   D3DDECLTYPE\_D3DCOLOR
-   D3DDECLTYPE\_FLOAT3
-   D3DDECLTYPE\_FLOAT4
-   D3DDECLTYPE\_SHORT4
-   D3DDECLTYPE\_UBYTE4

The output type is always D3DDECLTYPE\_FLOAT3.

</dd> <dt>

<span id="D3DDECLMETHOD_CROSSUV"></span><span id="d3ddeclmethod_crossuv"></span>**D3DDECLMETHOD\_CROSSUV**
</dt> <dd>

Computes the normal at a point on the rectangle or triangle patch by taking the cross product of two tangents. The input type can be one of the following:

-   D3DDECLTYPE\_D3DCOLOR
-   D3DDECLTYPE\_FLOAT3
-   D3DDECLTYPE\_FLOAT4
-   D3DDECLTYPE\_SHORT4
-   D3DDECLTYPE\_UBYTE4

The output type is always D3DDECLTYPE\_FLOAT3.

</dd> <dt>

<span id="D3DDECLMETHOD_UV"></span><span id="d3ddeclmethod_uv"></span>**D3DDECLMETHOD\_UV**
</dt> <dd>

Copy out the U, V values at a point on the rectangle or triangle patch. This results in a 2D float. The input type must be set to D3DDECLTYPE\_UNUSED. The output data type is always D3DDECLTYPE\_FLOAT2. The input stream and offset are also unused (but must be set to 0).

</dd> <dt>

<span id="D3DDECLMETHOD_LOOKUP"></span><span id="d3ddeclmethod_lookup"></span>**D3DDECLMETHOD\_LOOKUP**
</dt> <dd>

Look up a displacement map. The input type can be one of the following:

-   D3DDECLTYPE\_FLOAT2
-   D3DDECLTYPE\_FLOAT3
-   D3DDECLTYPE\_FLOAT4

Only the .x and .y components are used for the texture map lookup. The output type is always D3DDECLTYPE\_FLOAT1. The device must support displacement mapping. For more information about displacement mapping, see [Displacement Mapping (Direct3D 9)](displacement-mapping.md). This constant is supported only by the programmable pipeline on N-patch data, if N-patches are enabled.

</dd> <dt>

<span id="D3DDECLMETHOD_LOOKUPPRESAMPLED"></span><span id="d3ddeclmethod_lookuppresampled"></span>**D3DDECLMETHOD\_LOOKUPPRESAMPLED**
</dt> <dd>

Look up a presampled displacement map. The input type must be set to D3DDECLTYPE\_UNUSED; the stream index and the stream offset must be set to 0. The output type for this operation is always D3DDECLTYPE\_FLOAT1. The device must support displacement mapping. For more information about displacement mapping, see [Displacement Mapping (Direct3D 9)](displacement-mapping.md). This constant is supported only by the programmable pipeline on N-patch data, if N-patches are enabled. This method can be used only with D3DDECLUSAGE\_SAMPLE.

</dd> </dl>

## Remarks

The tessellator looks at the method to determine what data to calculate from the vertex data during tessellation. Mesh data should use the default value. Patches can use any of the other implemented types.

Vertex data is declared with an array of [**D3DVERTEXELEMENT9**](d3dvertexelement9.md) structures. Each element in the array contains a vertex declaration method.

In addition to using D3DDECLMETHOD\_DEFAULT, a normal mesh can use D3DDECLMETHOD\_LOOKUP and D3DDECLMETHOD\_LOOKUPPRESAMPLED methods when N-patches are enabled.

## Requirements



| Requirement | Value |
|-------------------|----------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>D3D9Types.h</dt> </dl> |



## See also

<dl> <dt>

[Direct3D Enumerations](dx9-graphics-reference-d3d-enums.md)
</dt> </dl>

 

 




