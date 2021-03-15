---
description: Resamples a texture into this gutterhelper's parameterization.
ms.assetid: a5ace0e4-2e89-471b-bdfb-67d5e85c6f46
title: ID3DXTextureGutterHelper::ResampleTex method (D3DX9Mesh.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type:
- APIRef
- kbSyntax
api_name:
- ID3DXTextureGutterHelper.ResampleTex
api_type:
- COM
api_location:
- d3dx9.lib
- d3dx9.dll
---

# ID3DXTextureGutterHelper::ResampleTex method

Resamples a texture into this gutterhelper's parameterization.

## Syntax


```C++
HRESULT ResampleTex(
  [in]  LPDIRECT3DTEXTURE9 pTextureIn,
  [in]  LPD3DXMESH         pMeshIn,
  [in]  D3DDECLUSAGE       Usage,
  [in]  UINT               UsageIndex,
  [out] LPDIRECT3DTEXTURE9 pTextureOut
);
```



## Parameters

<dl> <dt>

*pTextureIn* \[in\]
</dt> <dd>

Type: **[**LPDIRECT3DTEXTURE9**](/windows/win32/api/d3d9helper/nn-d3d9helper-idirect3dtexture9)**

Texture that corresponds to the original parameterization in pMeshIn. This texture will be used to create pTextureOut.

</dd> <dt>

*pMeshIn* \[in\]
</dt> <dd>

Type: **[**LPD3DXMESH**](id3dxmesh.md)**

Mesh containing the original and new parameterizations. It is required to store the new parameterization in D3DDECLUSAGE\_TEXCOORD index 0.

</dd> <dt>

*Usage* \[in\]
</dt> <dd>

Type: **[**D3DDECLUSAGE**](./d3ddeclusage.md)**

Vertex data usage (used in combination with UsageIndex) which identifies the component of the vertex declaration that contains the original parameterization in pMeshIn. See [**D3DDECLUSAGE**](./d3ddeclusage.md).

</dd> <dt>

*UsageIndex* \[in\]
</dt> <dd>

Type: **[**UINT**](../winprog/windows-data-types.md)**

Zero-based index (used in combination with Usage), which identifies the component of the vertex declaration that contains the original parameterization in pMeshIn. The combination of D3DDECLUSAGE\_TEXCOORD and index 0 is required for the new parameterization; any other usage/index combination may be used.

</dd> <dt>

*pTextureOut* \[out\]
</dt> <dd>

Type: **[**LPDIRECT3DTEXTURE9**](/windows/win32/api/d3d9helper/nn-d3d9helper-idirect3dtexture9)**

Resampled texture.

</dd> </dl>

## Return value

Type: **[**HRESULT**](https://msdn.microsoft.com/library/Bb401631(v=MSDN.10).aspx)**

If the method succeeds, the return value is D3D\_OK. If the method fails, the return value can be one of the following: D3DERR\_INVALIDCALL, E\_OUTOFMEMORY.

## Remarks

A parameterization in the case of this function is a set of texture coordinates that maps the triangles of a mesh to the triangles on a texture. The new parameterization is the set of texture coordinates contained in the gutter helper interface, and the original parameterization is the set of texture coordinates contained within the input mesh.

It is assumed that texture coordinates are between 0 and 1, inclusive, and the new parameterization must be declared in the vertex declaration as texture coordinate index 0. The original texture and the resampled texture must have the same width and height.

For example, to prepare for resampling a texture:

-   Create the original texture interface (pOriginalTex below) using a function like [**D3DXCreateTextureFromFile**](d3dxcreatetexturefromfile.md).
-   Create the new texture interface for the resampled texture (pResampledTex below). The size of this texture must match the size (width and height) of the gutter helper texture.
-   Call [**D3DXCreateTextureGutterHelper**](d3dxcreatetexturegutterhelper.md) to obtain the new parameterization as shown here:


```
// Given:
// pMesh points to a mesh that contains the original and new texture coordinates
ID3DXTextureGutterHelper * pGutterHelper;
    
// Mesh vertex declaration
D3DVERTEXELEMENT9 decl[] = {
    {0,  0, D3DDECLTYPE_FLOAT3, D3DDECLMETHOD_DEFAULT, D3DDECLUSAGE_POSITION, 0},
    {0, 12, D3DDECLTYPE_FLOAT3, D3DDECLMETHOD_DEFAULT, D3DDECLUSAGE_NORMAL, 0},
    // contains new set of texcoords
    {0, 24, D3DDECLTYPE_FLOAT2, D3DDECLMETHOD_DEFAULT, D3DDECLUSAGE_TEXCOORD, 0}, 
    // contains original set of texcoords
    {0, 32, D3DDECLTYPE_FLOAT2, D3DDECLMETHOD_DEFAULT, D3DDECLUSAGE_TEXCOORD, 1}, 
    D3DDECL_END()
};
    
// Create a gutter helper with the new parameterization
hr = D3DXCreateTextureGutterHelper(width, height, pMesh, 1, &pGutterHelper);  
    
// Resample the texture
hr = pGutterHelper->ResampleTex(pOriginalTex, pMesh, D3DDECLUSAGE_TEXCOORD, 
           1, pResampledTex); 
    
// Release the gutter helper interface when done with it
```



One common scenario might be to use UVAtlas to create a texture atlas and then use ResampleTex to resample the texture into the new parameterization. For more information about atlases, see [Using UVAtlas (Direct3D 9)](using-uvatlas.md).

## Requirements



| Requirement | Value |
|--------------------|----------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>D3DX9Mesh.h</dt> </dl> |
| Library<br/> | <dl> <dt>D3dx9.lib</dt> </dl>   |



## See also

<dl> <dt>

[ID3DXTextureGutterHelper](id3dxtexturegutterhelper.md)
</dt> <dt>

[**D3DXUVAtlasCreate**](d3dxuvatlascreate.md)
</dt> </dl>

 

 
