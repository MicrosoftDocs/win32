---
Description: Sets mesh geometry displacement parameters.
ms.assetid: 4c78e5b3-fb63-4341-a811-5531cf9564e7
title: ID3DXPatchMesh::SetDisplaceParam method
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
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

Type: **[**LPDIRECT3DBASETEXTURE9**](/windows/desktop/api/d3d9helper/nn-d3d9-idirect3dbasetexture9)**

Texture containing the displacement data.

</dd> <dt>

*MinFilter* \[in\]
</dt> <dd>

Type: **[**D3DTEXTUREFILTERTYPE**](https://msdn.microsoft.com/VS|directx_sdk|~\d3dtexturefiltertype.htm)**

Minification level. For more information, see [**D3DTEXTUREFILTERTYPE**](https://msdn.microsoft.com/VS|directx_sdk|~\d3dtexturefiltertype.htm).

</dd> <dt>

*MagFilter* \[in\]
</dt> <dd>

Type: **[**D3DTEXTUREFILTERTYPE**](https://msdn.microsoft.com/VS|directx_sdk|~\d3dtexturefiltertype.htm)**

Magnification level. For more information, see [**D3DTEXTUREFILTERTYPE**](https://msdn.microsoft.com/VS|directx_sdk|~\d3dtexturefiltertype.htm).

</dd> <dt>

*MipFilter* \[in\]
</dt> <dd>

Type: **[**D3DTEXTUREFILTERTYPE**](https://msdn.microsoft.com/VS|directx_sdk|~\d3dtexturefiltertype.htm)**

Mip filter level. For more information, see [**D3DTEXTUREFILTERTYPE**](https://msdn.microsoft.com/VS|directx_sdk|~\d3dtexturefiltertype.htm).

</dd> <dt>

*Wrap* \[in\]
</dt> <dd>

Type: **[**D3DTEXTUREADDRESS**](https://msdn.microsoft.com/VS|directx_sdk|~\d3dtextureaddress.htm)**

Texture address wrap mode. For more information, see [**D3DTEXTUREADDRESS**](https://msdn.microsoft.com/VS|directx_sdk|~\d3dtextureaddress.htm)

</dd> <dt>

*dwLODBias* \[in\]
</dt> <dd>

Type: **[**DWORD**](https://msdn.microsoft.com/4553cafc-450e-4493-a4d4-cb6e2f274d46)**

Level of detail bias value.

</dd> </dl>

## Return value

Type: **[**HRESULT**](https://msdn.microsoft.com/windows/desktop/455d07e9-52c3-4efb-a9dc-2955cbfd38cc)**

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

 

 




