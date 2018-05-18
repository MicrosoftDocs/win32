---
Description: 'Gets mesh geometry displacement parameters.'
ms.assetid: '155724ba-71be-4e9f-8c84-bb04f8eec578'
title: 'ID3DXPatchMesh::GetDisplaceParam method'
---

# ID3DXPatchMesh::GetDisplaceParam method

Gets mesh geometry displacement parameters.

## Syntax


```C++
HRESULT GetDisplaceParam(
  [in] LPDIRECT3DBASETEXTURE9 *Texture,
  [in] D3DTEXTUREFILTERTYPE   *MinFilter,
  [in] D3DTEXTUREFILTERTYPE   *MagFilter,
  [in] D3DTEXTUREFILTERTYPE   *MipFilter,
  [in] D3DTEXTUREADDRESS      *Wrap,
  [in] DWORD                  *dwLODBias
);
```



## Parameters

<dl> <dt>

*Texture* \[in\]
</dt> <dd>

Type: **[**LPDIRECT3DBASETEXTURE9**](idirect3dbasetexture9.md)\***

Texture containing the displacement data.

</dd> <dt>

*MinFilter* \[in\]
</dt> <dd>

Type: **[**D3DTEXTUREFILTERTYPE**](direct3d9.d3dtexturefiltertype)\***

Minification level. For more information, see [**D3DTEXTUREFILTERTYPE**](direct3d9.d3dtexturefiltertype).

</dd> <dt>

*MagFilter* \[in\]
</dt> <dd>

Type: **[**D3DTEXTUREFILTERTYPE**](direct3d9.d3dtexturefiltertype)\***

Magnification level. For more information, see [**D3DTEXTUREFILTERTYPE**](direct3d9.d3dtexturefiltertype).

</dd> <dt>

*MipFilter* \[in\]
</dt> <dd>

Type: **[**D3DTEXTUREFILTERTYPE**](direct3d9.d3dtexturefiltertype)\***

Mip filter level. For more information, see [**D3DTEXTUREFILTERTYPE**](direct3d9.d3dtexturefiltertype).

</dd> <dt>

*Wrap* \[in\]
</dt> <dd>

Type: **[**D3DTEXTUREADDRESS**](direct3d9.d3dtextureaddress)\***

Texture address wrap mode. For more information, see [**D3DTEXTUREADDRESS**](direct3d9.d3dtextureaddress).

</dd> <dt>

*dwLODBias* \[in\]
</dt> <dd>

Type: **[**DWORD**](winprog.windows_data_types)\***

Level of detail bias value.

</dd> </dl>

## Return value

Type: **[**HRESULT**](455d07e9-52c3-4efb-a9dc-2955cbfd38cc)**

If the method succeeds, the return value is D3D\_OK. If the method fails, the return value can be one of the following: D3DERR\_INVALIDCALL, E\_OUTOFMEMORY.

## Remarks

Displacement maps can only be 2D textures. Mipmapping is ignored for nonadaptive tessellation.

## Requirements



|                    |                                                                                        |
|--------------------|----------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>D3DX9Mesh.h</dt> </dl> |
| Library<br/> | <dl> <dt>D3dx9.lib</dt> </dl>   |



## See also

<dl> <dt>

[ID3DXPatchMesh](id3dxpatchmesh.md)
</dt> </dl>

 

 




