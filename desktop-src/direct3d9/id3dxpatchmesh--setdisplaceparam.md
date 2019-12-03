---
Description: Sets mesh geometry displacement parameters.
ms.assetid: 4c78e5b3-fb63-4341-a811-5531cf9564e7
title: ID3DXPatchMesh::SetDisplaceParam method (D3DX9Mesh.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type:
- APIRef
- kbSyntax
api_name:
- ID3DXPatchMesh.SetDisplaceParam
api_type:
- COM
api_location:
- d3dx9.lib
- d3dx9.dll
---

# ID3DXPatchMesh::SetDisplaceParam method

Sets mesh geometry displacement parameters.

## Syntax


```C++
HRESULT SetDisplaceParam(
  [in] LPDIRECT3DBASETEXTURE9 Texture,
  [in] D3DTEXTUREFILTERTYPE   MinFilter,
  [in] D3DTEXTUREFILTERTYPE   MagFilter,
  [in] D3DTEXTUREFILTERTYPE   MipFilter,
  [in] D3DTEXTUREADDRESS      Wrap,
  [in] DWORD                  dwLODBias
);
```



## Parameters

<dl> <dt>

*Texture* \[in\]
</dt> <dd>

Type: **[**LPDIRECT3DBASETEXTURE9**](https://msdn.microsoft.com/library/Bb174322(v=VS.85).aspx)**

Texture containing the displacement data.

</dd> <dt>

*MinFilter* \[in\]
</dt> <dd>

Type: **[**D3DTEXTUREFILTERTYPE**](https://msdn.microsoft.com/en-us/library/Bb172615(v=VS.85).aspx)**

Minification level. For more information, see [**D3DTEXTUREFILTERTYPE**](https://msdn.microsoft.com/en-us/library/Bb172615(v=VS.85).aspx).

</dd> <dt>

*MagFilter* \[in\]
</dt> <dd>

Type: **[**D3DTEXTUREFILTERTYPE**](https://msdn.microsoft.com/en-us/library/Bb172615(v=VS.85).aspx)**

Magnification level. For more information, see [**D3DTEXTUREFILTERTYPE**](https://msdn.microsoft.com/en-us/library/Bb172615(v=VS.85).aspx).

</dd> <dt>

*MipFilter* \[in\]
</dt> <dd>

Type: **[**D3DTEXTUREFILTERTYPE**](https://msdn.microsoft.com/en-us/library/Bb172615(v=VS.85).aspx)**

Mip filter level. For more information, see [**D3DTEXTUREFILTERTYPE**](https://msdn.microsoft.com/en-us/library/Bb172615(v=VS.85).aspx).

</dd> <dt>

*Wrap* \[in\]
</dt> <dd>

Type: **[**D3DTEXTUREADDRESS**](https://msdn.microsoft.com/en-us/library/Bb172614(v=VS.85).aspx)**

Texture address wrap mode. For more information, see [**D3DTEXTUREADDRESS**](https://msdn.microsoft.com/en-us/library/Bb172614(v=VS.85).aspx)

</dd> <dt>

*dwLODBias* \[in\]
</dt> <dd>

Type: **[**DWORD**](https://msdn.microsoft.com/en-us/library/Aa383751(v=VS.85).aspx)**

Level of detail bias value.

</dd> </dl>

## Return value

Type: **[**HRESULT**](https://msdn.microsoft.com/en-us/library/Bb401631(v=MSDN.10).aspx)**

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

 

 




