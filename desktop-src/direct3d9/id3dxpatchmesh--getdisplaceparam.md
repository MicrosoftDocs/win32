---
description: Gets mesh geometry displacement parameters.
ms.assetid: 155724ba-71be-4e9f-8c84-bb04f8eec578
title: ID3DXPatchMesh::GetDisplaceParam method (D3DX9Mesh.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type:
- APIRef
- kbSyntax
api_name:
- ID3DXPatchMesh.GetDisplaceParam
api_type:
- COM
api_location:
- d3dx9.lib
- d3dx9.dll
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

Type: **[**LPDIRECT3DBASETEXTURE9**](/windows/win32/api/d3d9helper/nn-d3d9helper-idirect3dbasetexture9)\***

Texture containing the displacement data.

</dd> <dt>

*MinFilter* \[in\]
</dt> <dd>

Type: **[**D3DTEXTUREFILTERTYPE**](./d3dtexturefiltertype.md)\***

Minification level. For more information, see [**D3DTEXTUREFILTERTYPE**](./d3dtexturefiltertype.md).

</dd> <dt>

*MagFilter* \[in\]
</dt> <dd>

Type: **[**D3DTEXTUREFILTERTYPE**](./d3dtexturefiltertype.md)\***

Magnification level. For more information, see [**D3DTEXTUREFILTERTYPE**](./d3dtexturefiltertype.md).

</dd> <dt>

*MipFilter* \[in\]
</dt> <dd>

Type: **[**D3DTEXTUREFILTERTYPE**](./d3dtexturefiltertype.md)\***

Mip filter level. For more information, see [**D3DTEXTUREFILTERTYPE**](./d3dtexturefiltertype.md).

</dd> <dt>

*Wrap* \[in\]
</dt> <dd>

Type: **[**D3DTEXTUREADDRESS**](./d3dtextureaddress.md)\***

Texture address wrap mode. For more information, see [**D3DTEXTUREADDRESS**](./d3dtextureaddress.md).

</dd> <dt>

*dwLODBias* \[in\]
</dt> <dd>

Type: **[**DWORD**](../winprog/windows-data-types.md)\***

Level of detail bias value.

</dd> </dl>

## Return value

Type: **[**HRESULT**](https://msdn.microsoft.com/library/Bb401631(v=MSDN.10).aspx)**

If the method succeeds, the return value is D3D\_OK. If the method fails, the return value can be one of the following: D3DERR\_INVALIDCALL, E\_OUTOFMEMORY.

## Remarks

Displacement maps can only be 2D textures. Mipmapping is ignored for nonadaptive tessellation.

## Requirements



| Requirement | Value |
|--------------------|----------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>D3DX9Mesh.h</dt> </dl> |
| Library<br/> | <dl> <dt>D3dx9.lib</dt> </dl>   |



## See also

<dl> <dt>

[ID3DXPatchMesh](id3dxpatchmesh.md)
</dt> </dl>

 

 
