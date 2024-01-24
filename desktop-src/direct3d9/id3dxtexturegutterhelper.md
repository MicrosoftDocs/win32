---
description: The ID3DXTextureGutterHelper interface is used to build and manage gutter regions in a texture. Gutter regions separate textures and allow for bilinear interpolation to avoid rendering artifacts at texture boundaries.
ms.assetid: 097e27bf-a1a6-4e7e-bdad-33015b50f91f
title: ID3DXTextureGutterHelper interface (D3DX9Mesh.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type:
- APIRef
- kbSyntax
api_name:
- ID3DXTextureGutterHelper
api_type:
- COM
api_location:
- d3dx9.lib
- d3dx9.dll
---

# ID3DXTextureGutterHelper interface

The ID3DXTextureGutterHelper interface is used to build and manage gutter regions in a texture. Gutter regions separate textures and allow for bilinear interpolation to avoid rendering artifacts at texture boundaries.

The Get... methods provide access to the data structures used by the Apply... methods.

## Members

The **ID3DXTextureGutterHelper** interface inherits from the [**IUnknown**](/windows/win32/api/unknwn/nn-unknwn-iunknown) interface. **ID3DXTextureGutterHelper** also has these types of members:

-   [Methods](#methods)

### Methods

The **ID3DXTextureGutterHelper** interface has these methods.



| Method                                                                   | Description                                                                                            |
|:-------------------------------------------------------------------------|:-------------------------------------------------------------------------------------------------------|
| [**ApplyGuttersFloat**](id3dxtexturegutterhelper--applyguttersfloat.md) | Applies gutters to a FLOAT texture buffer.<br/>                                                  |
| [**ApplyGuttersPRT**](id3dxtexturegutterhelper--applyguttersprt.md)     | Applies gutters to an [**ID3DXPRTBuffer**](id3dxprtbuffer.md) buffer object.<br/>               |
| [**ApplyGuttersTex**](id3dxtexturegutterhelper--applygutterstex.md)     | Applies gutters to an [**IDirect3DTexture9**](/windows/win32/api/d3d9helper/nn-d3d9helper-idirect3dtexture9) texture object.<br/>        |
| [**GetBaryMap**](id3dxtexturegutterhelper--getbarymap.md)               | Retrieves texel barycentric coordinates.<br/>                                                    |
| [**GetFaceMap**](id3dxtexturegutterhelper--getfacemap.md)               | Retrieves the index of the mesh face to which each texel belongs.<br/>                           |
| [**GetGutterMap**](id3dxtexturegutterhelper--getguttermap.md)           | Receives a texel class value that indicates texel class according to each texel's location.<br/> |
| [**GetHeight**](id3dxtexturegutterhelper--getheight.md)                 | Retrieves the height of the texture, in pixels.<br/>                                             |
| [**GetTexelMap**](id3dxtexturegutterhelper--gettexelmap.md)             | Retrieves the (u, v) texture coordinates of each texel.<br/>                                     |
| [**GetWidth**](id3dxtexturegutterhelper--getwidth.md)                   | Retrieves the width of the texture, in pixels.<br/>                                              |
| [**ResampleTex**](id3dxtexturegutterhelper--resampletex.md)             | Resamples a texture into this gutterhelper's parameterization.<br/>                              |
| [**SetBaryMap**](id3dxtexturegutterhelper--setbarymap.md)               | Sets texel barycentric coordinates.<br/>                                                         |
| [**SetFaceMap**](id3dxtexturegutterhelper--setfacemap.md)               | Sets the index of the mesh face to which each texel belongs.<br/>                                |
| [**SetGutterMap**](id3dxtexturegutterhelper--setguttermap.md)           | Sets a texel class value that indicates texel class according to each texel's location.<br/>     |
| [**SetTexelMap**](id3dxtexturegutterhelper--settexelmap.md)             | Sets the (u, v) texture coordinates of each texel.<br/>                                          |



 

## Remarks

> [!Note]  
> When used with precomputed radiance transfer (PRT), this interface requires a unique parameterization of the model. Every texel must correspond to a single point on the surface of the model and vice-versa. If the model includes multiple textures, it must be split into separate pieces that each contain one gutter helper object per texture.

 

This interface can be used to generate a map in texture space in which each texel is in one of four classes.



| Texel Class | Texel Location                                                                                                                                                                                                                                                                                                                                                                |
|-------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0           | Invalid point; texel will not be used.                                                                                                                                                                                                                                                                                                                                        |
| 1           | Inside triangle.                                                                                                                                                                                                                                                                                                                                                              |
| 2           | Inside gutter.                                                                                                                                                                                                                                                                                                                                                                |
| 4           | Inside gutter; texel will be evaluated as a full sample in the [**ID3DXTextureGutterHelper::ApplyGuttersFloat**](id3dxtexturegutterhelper--applyguttersfloat.md), [**ID3DXTextureGutterHelper::ApplyGuttersTex**](id3dxtexturegutterhelper--applygutterstex.md), or [**ID3DXTextureGutterHelper::ApplyGuttersPRT**](id3dxtexturegutterhelper--applyguttersprt.md) methods. |



 

For classes 1 and 2, a texel is stored with the face it belongs to, along with barycentric coordinates of the first two vertices of that face. Gutter vertices are assigned to the closest edge in texture space.

There is no texel class 3.

The **ID3DXTextureGutterHelper** interface is obtained by calling the [**D3DXCreateTextureGutterHelper**](d3dxcreatetexturegutterhelper.md) function.

The LPD3DXTEXTUREGUTTERHELPER type is defined as a pointer to the **ID3DXTextureGutterHelper** interface.


```
typedef interface ID3DXTextureGutterHelper ID3DXTextureGutterHelper;
typedef interface ID3DXTextureGutterHelper *LPD3DXTEXTUREGUTTERHELPER;
```



## Requirements



| Requirement | Value |
|--------------------|----------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>D3DX9Mesh.h</dt> </dl> |
| Library<br/> | <dl> <dt>D3dx9.lib</dt> </dl>   |



## See also

<dl> <dt>

[D3DX Interfaces](dx9-graphics-reference-d3dx-interfaces.md)
</dt> </dl>

 

 
