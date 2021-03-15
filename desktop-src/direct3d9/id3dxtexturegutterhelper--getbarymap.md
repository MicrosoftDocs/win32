---
description: Retrieves texel barycentric coordinates.
ms.assetid: f380a37f-b9c1-4433-b1d6-e9feeca79b30
title: ID3DXTextureGutterHelper::GetBaryMap method (D3DX9Mesh.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- ID3DXTextureGutterHelper.GetBaryMap
api_type: 
- COM
api_location: 
- d3dx9.lib
- d3dx9.dll
---

# ID3DXTextureGutterHelper::GetBaryMap method

Retrieves texel barycentric coordinates.

## Syntax


```C++
HRESULT GetBaryMap(
  [in, out] D3DXVECTOR2 *pBaryData
);
```



## Parameters

<dl> <dt>

*pBaryData* \[in, out\]
</dt> <dd>

Type: **[**D3DXVECTOR2**](d3dxvector2.md)\***

Pointer to a [**D3DXVECTOR2**](d3dxvector2.md) structure that contains the first two barycentric coordinates of each texel.

</dd> </dl>

## Return value

Type: **[**HRESULT**](https://msdn.microsoft.com/library/Bb401631(v=MSDN.10).aspx)**

If the method succeeds, the return value is S\_OK. If the method fails, the following value will be returned.D3DERR\_INVALIDCALL

## Remarks

The third barycentric coordinate is given by:


```
    1 - ( pBaryData.x + pBaryData.y )
```



Barycentric coordinates are always specified with respect to the triangle returned by [**ID3DXTextureGutterHelper::GetFaceMap**](id3dxtexturegutterhelper--getfacemap.md).

The barycentric coordinates returned by this method are valid only for valid (non-class 0) texels. [**ID3DXTextureGutterHelper::GetGutterMap**](id3dxtexturegutterhelper--getguttermap.md) will return nonzero values for valid texels.

[**Class 2 texels**](id3dxtexturegutterhelper.md) are mapped to the nearest point on the triangle in texel space.

The application must allocate and manage pBaryData.

Barycentric coordinates define a point inside a triangle in terms of the triangle's vertices. For a more in-depth description of barycentric coordinates, see [Mathworld's Barycentric Coordinates Description](https://mathworld.wolfram.com/BarycentricCoordinates.html).

## Requirements



| Requirement | Value |
|--------------------|----------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>D3DX9Mesh.h</dt> </dl> |
| Library<br/> | <dl> <dt>D3dx9.lib</dt> </dl>   |



## See also

<dl> <dt>

[ID3DXTextureGutterHelper](id3dxtexturegutterhelper.md)
</dt> </dl>

 

 




