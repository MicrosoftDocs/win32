---
description: Texture coordinates in Direct3D can include one, two, three, or four floating point elements to address textures with varying levels of dimension.
ms.assetid: d841af62-41b0-4b80-960b-4630b9a7210c
title: Texture Coordinate Formats (Direct3D 9)
ms.topic: article
ms.date: 05/31/2018
---

# Texture Coordinate Formats (Direct3D 9)

Texture coordinates in Direct3D can include one, two, three, or four floating point elements to address textures with varying levels of dimension. A 1D texture - a texture surface with dimensions of 1-by-n texels - is addressed by one texture coordinate. The most common case, 2D textures, are addressed with two texture coordinates commonly called u and v. Direct3D supports two types of 3D textures, cubic-environment maps and volume textures. Cubic environment maps aren't truly 3D, but they are addressed with a 3-element vector. For details, see [Cubic Environment Mapping (Direct3D 9)](cubic-environment-mapping.md).

As described in [Fixed Function FVF Codes (Direct3D 9)](fixed-function-fvf-codes.md), applications encode texture coordinates in the vertex format. The vertex format can include multiple sets of texture coordinates. Use the D3DFVF\_TEX0 through D3DFVF\_TEX8 [D3DFVF](d3dfvf.md) to describe a vertex format that includes no texture coordinates, or as many as eight sets.

Each texture coordinate set can have between one and four elements. The D3DFVF\_TEXTUREFORMAT1 through D3DFVF\_TEXTUREFORMAT4 flags describe the number of elements in a texture coordinate in a set, but these flags aren't used by themselves. Rather, the [**D3DFVF\_TEXCOORDSIZEN**](d3dfvf-texcoordsizen.md) set of macros use these flags to create bit patterns that describe the number of elements used by a particular set of texture coordinates in the vertex format. These macros accept a single parameter that identifies the index of the coordinate set whose number of elements is being defined. The following example illustrates how these macros are used.


```
// This vertex format contains two sets of texture coordinates.
// The first set (index 0) has 2 elements, and the second set 
// has 1 element. The description for this vertex format would be: 
//     dwFVF = D3DFVF_XYZ  | D3DFVF_NORMAL | D3DFVF_DIFFUSE | D3DFVF_TEX2 |
//             D3DFVF_TEXCOORDSIZE2(0) | D3DFVF_TEXCOORDSIZE1(1); 
//
typedef struct CVF
{
    D3DVECTOR position;
    D3DVECTOR normal;
    D3DCOLOR  diffuse;
    float     u, v;   // 1st set, 2D
    float     t;      // 2nd set, 1D
} CustomVertexFormat;
```



> [!Note]  
> With the exception of cubic-environment maps and volume textures, rasterizers cannot address textures by using any more than two elements. Applications can supply up to three elements for a texture coordinate, but only if the texture is a cube map, a volume texture, or the D3DTTFF\_PROJECTED texture transform flag is used. The D3DTTFF\_PROJECTED flag causes the rasterizer to divide the first two elements by the third (or n) element. For more information, see [Texture Coordinate Transformations (Direct3D 9)](texture-coordinate-transformations.md).

 

## Related topics

<dl> <dt>

[Texture Coordinates](texture-coordinates.md)
</dt> </dl>

 

 



