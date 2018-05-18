---
Description: 'Sets texel barycentric coordinates.'
ms.assetid: '6c7c74aa-71a3-45aa-9b18-6409fbd63bda'
title: 'ID3DXTextureGutterHelper::SetBaryMap method'
---

# ID3DXTextureGutterHelper::SetBaryMap method

Sets texel barycentric coordinates.

## Syntax


```C++
HRESULT SetBaryMap(
  [in] D3DXVECTOR2 *pBaryData
);
```



## Parameters

<dl> <dt>

*pBaryData* \[in\]
</dt> <dd>

Type: **[**D3DXVECTOR2**](d3dxvector2.md)\***

Pointer to a [**D3DXVECTOR2**](d3dxvector2.md) structure that contains the first two barycentric coordinates of each texel.

</dd> </dl>

## Return value

Type: **[**HRESULT**](455d07e9-52c3-4efb-a9dc-2955cbfd38cc)**

If the method succeeds, the return value is S\_OK. If the method fails, the following value will be returned.D3DERR\_INVALIDCALL

## Remarks

The third barycentric coordinate is given by:


```
1 - ( pBaryData.x + pBaryData.y )
```



The barycentric coordinates input to this method are valid only for valid (non-class 0) texels. [**ID3DXTextureGutterHelper::GetGutterMap**](id3dxtexturegutterhelper--getguttermap.md) will return non-zero values for valid texels.

Barycentric coordinates define a point inside a triangle in terms of the triangle's vertices. For a more in-depth description of barycentric coordinates, see [Mathworld's Barycentric Coordinates Description](http://go.microsoft.com/?linkid=9742311).

## Requirements



|                    |                                                                                        |
|--------------------|----------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>D3DX9Mesh.h</dt> </dl> |
| Library<br/> | <dl> <dt>D3dx9.lib</dt> </dl>   |



## See also

<dl> <dt>

[ID3DXTextureGutterHelper](id3dxtexturegutterhelper.md)
</dt> </dl>

 

 




