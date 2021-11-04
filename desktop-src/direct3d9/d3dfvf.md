---
description: Flexible Vertex Format Constants, or FVF codes, are used to describe the contents of vertices interleaved in a single data stream that will be processed by the fixed-function pipeline.
ms.assetid: 85d9f5b2-8e4a-4f92-a587-eae5b293778c
title: D3DFVF
ms.topic: article
ms.date: 05/31/2018
---

# D3DFVF

Flexible Vertex Format Constants, or FVF codes, are used to describe the contents of vertices interleaved in a single data stream that will be processed by the fixed-function pipeline.

## Vertex Data Flags

The following flags describe a vertex format. For information regarding vertex formats, see [Fixed Function FVF Codes (Direct3D 9)](fixed-function-fvf-codes.md).



| \#define                            | Description                                                                                                                                                                                                                                                                                                                                                             | Data order and type                                                                                       |
|-------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------|
| D3DFVF\_DIFFUSE                     | Vertex format includes a diffuse color component.                                                                                                                                                                                                                                                                                                                       | DWORD in ARGB order. See [**D3DCOLOR\_ARGB**](d3dcolor-argb.md).                                         |
| D3DFVF\_NORMAL                      | Vertex format includes a vertex normal vector. This flag cannot be used with the D3DFVF\_XYZRHW flag.                                                                                                                                                                                                                                                                   | float, float, float                                                                                       |
| D3DFVF\_PSIZE                       | Vertex format specified in point size. This size is expressed in camera space units for vertices that are not transformed and lit, and in device-space units for transformed and lit vertices.                                                                                                                                                                          | float                                                                                                     |
| D3DFVF\_SPECULAR                    | Vertex format includes a specular color component.                                                                                                                                                                                                                                                                                                                      | DWORD in ARGB order. See [**D3DCOLOR\_ARGB**](d3dcolor-argb.md).                                         |
| D3DFVF\_XYZ                         | Vertex format includes the position of an untransformed vertex. This flag cannot be used with the D3DFVF\_XYZRHW flag.                                                                                                                                                                                                                                                  | float, float, float.                                                                                      |
| D3DFVF\_XYZRHW                      | Vertex format includes the position of a transformed vertex. This flag cannot be used with the D3DFVF\_XYZ or D3DFVF\_NORMAL flags.                                                                                                                                                                                                                                     | float, float, float, float.                                                                               |
| D3DFVF\_XYZB1 through D3DFVF\_XYZB5 | Vertex format contains position data, and a corresponding number of weighting (beta) values to use for multimatrix vertex blending operations. Currently, Direct3D can blend with up to three weighting values and four blending matrices. For more information about using blending matrices, see [Indexed Vertex Blending (Direct3D 9)](indexed-vertex-blending.md). | 1, 2, or 3 floats. When D3DFVF\_LASTBETA\_UBYTE4 is used, the last blending weight is treated as a DWORD. |
| D3DFVF\_XYZW                        | Vertex format contains transformed and clipped (x, y, z, w) data. ProcessVertices does not invoke the clipper, instead outputting data in clip coordinates. This constant is designed for, and can only be used with, the programmable vertex pipeline.                                                                                                                 | float, float, float, float                                                                                |



 

## Texture Flags

The following flags describe texture flags used by the fixed-function pipeline.



| \#define                          | Description                                                                                                                                                                                                                                                                        |
|-----------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| D3DFVF\_TEX0 - D3DFVF\_TEX8       | Number of texture coordinate sets for this vertex. The actual values for these flags are not sequential.                                                                                                                                                                           |
| D3DFVF\_TEXCOORDSIZEN(coordIndex) | Define a texture coordinate data set. n indicates the dimension of the texture coordinates. coordIndex indicates texture coordinate index number. See [**D3DFVF\_TEXCOORDSIZEN**](d3dfvf-texcoordsizen.md) and [Texture coordinates and Texture Stages](texture-coordinates.md). |



 

## Mask Flags

The following flags describe mask flags used by the fixed-function pipeline.



| \#define                             | Description                                           |
|--------------------------------------|-------------------------------------------------------|
| D3DFVF\_POSITION\_MASK               | Mask for position bits.                               |
| D3DFVF\_RESERVED0, D3DFVF\_RESERVED2 | Mask values for reserved bits in the FVF. Do not use. |
| D3DFVF\_TEXCOUNT\_MASK               | Mask value for texture flag bits.                     |



 

## Miscellaneous Flags

The following flags describe a variety of flags used by the fixed-function pipeline.



<table>
<colgroup>
<col  />
<col  />
</colgroup>
<tbody>
<tr class="odd">
<td>#define</td>
<td>Description</td>
</tr>
<tr class="even">
<td>D3DFVF_LASTBETA_D3DCOLOR</td>
<td>The last beta field in the vertex position data will be of type D3DCOLOR. The data in the beta fields are used with matrix palette skinning to specify matrix indices.</td>
</tr>
<tr class="odd">
<td>D3DFVF_LASTBETA_UBYTE4</td>
<td>The last beta field in the vertex position data will be of type UBYTE4. The data in the beta fields are used with matrix palette skinning to specify matrix indices. <span data-codelanguage=""></span>
<table>
<colgroup>
<col  />
</colgroup>
<tbody>
<tr class="odd">
<td><pre><code>// Given the following vertex data definition: 
struct VERTEXPOSITION
{
   float pos[3];
   union 
   {
      float beta[5];
      struct
      {
         float weights[4];
         DWORD MatrixIndices;  // Used as UBYTEs
      }
   }
};</code></pre></td>
</tr>
</tbody>
</table>

<p>Given the FVF is declared as: D3DFVF_XYZB5 | D3DFVF_LASTBETA_UBYTE4. Weight and MatrixIndices are included in beta[5], where D3DFVF_LASTBETA_UBYTE4 says to interpret the last DWORD in beta[5] as type UBYTE4.</p></td>
</tr>
<tr class="even">
<td>D3DFVF_TEXCOUNT_SHIFT</td>
<td>The number of bits by which to shift an integer value that identifies the number of texture coordinates for a vertex. This value might be used as shown below.
<div class="code">
<span data-codelanguage=""></span>
<table>
<colgroup>
<col  />
</colgroup>
<tbody>
<tr class="odd">
<td><pre><code>DWORD dwNumTextures = 1;  // Vertex has only one set of coordinates.

// Shift the value for use when creating a 
//   flexible vertex format (FVF) combination.
dwFVF = dwNumTextures << D3DFVF_TEXCOUNT_SHIFT;

// Now, create an FVF combination using the shifted value.</code></pre></td>
</tr>
</tbody>
</table>

</div></td>
</tr>
</tbody>
</table>



 

### Examples

The following examples show other common flag combinations.


```
// Untransformed vertex for lit, untextured, Gouraud-shaded content.
dwFVF = ( D3DFVF_XYZ | D3DFVF_DIFFUSE );
```




```
// Untransformed vertex for unlit, untextured, Gouraud-shaded 
//   content with diffuse material color specified per vertex.
dwFVF = ( D3DFVF_XYZ | D3DFVF_NORMAL | D3DFVF_DIFFUSE );
```




```
// Untransformed vertex for light-map-based lighting.
dwFVF = ( D3DFVF_XYZ | D3DFVF_TEX2 );
```




```
// Transformed vertex for light-map-based lighting with shared rhw.
dwFVF = ( D3DFVF_XYZRHW | D3DFVF_TEX2 );
```




```
// Heavyweight vertex for unlit, colored content with two 
//   sets of texture coordinates.
dwFVF = ( D3DFVF_XYZ | D3DFVF_NORMAL | D3DFVF_DIFFUSE | 
          D3DFVF_SPECULAR | D3DFVF_TEX2 );
```



## Constant Information



| Requirement                         | Value            |
|--------------------------|-------------|
| Header                   | d3d9types.h |
| Minimum operating system | Windows 98  |



 

## Related topics

<dl> <dt>

[Direct3D Constants](dx9-graphics-reference-d3d-constants.md)
</dt> <dt>

[Fixed Function FVF Codes (Direct3D 9)](fixed-function-fvf-codes.md)
</dt> <dt>

[Geometry Blending (Direct3D 9)](geometry-blending.md)
</dt> </dl>

 

 



