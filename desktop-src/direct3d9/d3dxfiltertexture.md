---
description: Filters mipmap levels of a texture.
ms.assetid: bfeae9b0-9480-4a26-a225-4a34780546ce
title: D3DXFilterTexture function (D3dx9tex.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type:
- APIRef
- kbSyntax
api_name:
- D3DXFilterTexture
api_type:
- LibDef
api_location:
- d3dx9.lib
- d3dx9.dll
---

# D3DXFilterTexture function

Filters mipmap levels of a texture.

## Syntax


```C++
HRESULT D3DXFilterTexture(
  _In_        LPDIRECT3DBASETEXTURE9 pBaseTexture,
  _Out_ const PALETTEENTRY           *pPalette,
  _In_        UINT                   SrcLevel,
  _In_        DWORD                  MipFilter
);
```



## Parameters

<dl> <dt>

*pBaseTexture* \[in\]
</dt> <dd>

Type: **[**LPDIRECT3DBASETEXTURE9**](/windows/win32/api/d3d9helper/nn-d3d9helper-idirect3dbasetexture9)**

Pointer to an [**IDirect3DBaseTexture9**](/windows/win32/api/d3d9helper/nn-d3d9helper-idirect3dbasetexture9) interface that represents the texture object to filter.

</dd> <dt>

*pPalette* \[out\]
</dt> <dd>

Type: **const [**PALETTEENTRY**](/windows/win32/api/wingdi/ns-wingdi-paletteentry)\***

Pointer to a [**PALETTEENTRY**](/windows/win32/api/wingdi/ns-wingdi-paletteentry) structure that represents a 256-color palette to fill in, or **NULL** for nonpalettized formats. If a palette is not specified, the default Direct3D palette (an all opaque white palette) is provided. See Remarks.

</dd> <dt>

*SrcLevel* \[in\]
</dt> <dd>

Type: **[**UINT**](../winprog/windows-data-types.md)**

Level whose image is used to generate the subsequent levels. Specifying D3DX\_DEFAULT for this parameter is equivalent to specifying 0.

</dd> <dt>

*MipFilter* \[in\]
</dt> <dd>

Type: **[**DWORD**](../winprog/windows-data-types.md)**

Combination of one or more [D3DX\_FILTER](d3dx-filter.md) controlling how the mipmap is filtered. Specifying D3DX\_DEFAULT for this parameter is the equivalent of specifying D3DX\_FILTER\_BOX if the texture size is a power of two, and D3DX\_FILTER\_BOX \| D3DX\_FILTER\_DITHER otherwise.

</dd> </dl>

## Return value

Type: **[**HRESULT**](https://msdn.microsoft.com/library/Bb401631(v=MSDN.10).aspx)**

If the function succeeds, the return value is D3D\_OK. If the function fails, the return value can be one of the following: D3DERR\_INVALIDCALL, D3DXERR\_INVALIDDATA.

## Remarks

A filter is recursively applied to each texture level to generate the next texture level.

Writing to a non-level-zero surface of the texture will not cause the dirty rectangle to be updated. If **D3DXFilterTexture** is called and the surface was not already dirty (this is unlikely under normal usage scenarios), the application needs to explicitly call [**AddDirtyRect**](/windows/win32/api/d3d9helper/nf-d3d9helper-idirect3dtexture9-adddirtyrect) on the texture.

Textures created in the default pool (D3DPOOL\_DEFAULT) cannot be used with **D3DXFilterTexture** (unless created with D3DUSAGE\_DYNAMIC) because a lock operation is needed on the object. Note that locks are prohibited on textures in the default pool (unless they are dynamic).

For details on [**PALETTEENTRY**](/windows/win32/api/wingdi/ns-wingdi-paletteentry), see the Platform SDK. Note that as of DirectX 8.0, the peFlags member of the **PALETTEENTRY** structure does not function as documented in the Platform SDK. The peFlags member is now the alpha channel for 8-bit palettized formats.

There is only one texture filtering function, but two macros that call this method.


```
#define D3DXFilterCubeTexture D3DXFilterTexture
#define D3DXFilterVolumeTexture D3DXFilterTexture
```



## Requirements



| Requirement | Value |
|--------------------|---------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>D3dx9tex.h</dt> </dl> |
| Library<br/> | <dl> <dt>D3dx9.lib</dt> </dl>  |



## See also

<dl> <dt>

[Texture Functions in D3DX 9](dx9-graphics-reference-d3dx-functions-texture.md)
</dt> </dl>

 

 
