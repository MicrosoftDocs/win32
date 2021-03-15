---
description: Uses a compiled high-level shader language (HLSL) function to fill each texel of each mipmap level of a texture.
ms.assetid: a0c36967-57e6-4771-8e9f-f32949c12001
title: D3DXFillCubeTextureTX function (D3dx9tex.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type:
- APIRef
- kbSyntax
api_name:
- D3DXFillCubeTextureTX
api_type:
- LibDef
api_location:
- d3dx9.lib
- d3dx9.dll
---

# D3DXFillCubeTextureTX function

Uses a compiled high-level shader language (HLSL) function to fill each texel of each mipmap level of a texture.

## Syntax


```C++
HRESULT D3DXFillCubeTextureTX(
  _In_ LPDIRECT3DCUBETEXTURE9 pTexture,
  _In_ LPD3DXTEXTURESHADER    pTextureShader
);
```



## Parameters

<dl> <dt>

*pTexture* \[in\]
</dt> <dd>

Type: **[**LPDIRECT3DCUBETEXTURE9**](/windows/win32/api/d3d9helper/nn-d3d9helper-idirect3dcubetexture9)**

Pointer to an [**IDirect3DCubeTexture9**](/windows/win32/api/d3d9helper/nn-d3d9helper-idirect3dcubetexture9) object, representing the texture to be filled.

</dd> <dt>

*pTextureShader* \[in\]
</dt> <dd>

Type: **[**LPD3DXTEXTURESHADER**](id3dxtextureshader.md)**

Pointer to a [**ID3DXTextureShader**](id3dxtextureshader.md) texture shader object.

</dd> </dl>

## Return value

Type: **[**HRESULT**](https://msdn.microsoft.com/library/Bb401631(v=MSDN.10).aspx)**

If the function succeeds, the return value is D3D\_OK. If the function fails, the return value can be one of the following: D3DERR\_NOTAVAILABLE, D3DERR\_INVALIDCALL.

## Remarks

The texture target must be an HLSL function that takes contains the following semantics:

-   One input parameter must use a POSITION semantic.
-   One input parameter must use a PSIZE semantic.
-   The function must return a parameter that uses the COLOR semantic.

The input parameters can be in any order. For an example, see [**D3DXFillTextureTX**](d3dxfilltexturetx.md)

## Requirements



| Requirement | Value |
|--------------------|---------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>D3dx9tex.h</dt> </dl> |
| Library<br/> | <dl> <dt>D3dx9.lib</dt> </dl>  |



## See also

<dl> <dt>

[Texture Functions in D3DX 9](dx9-graphics-reference-d3dx-functions-texture.md)
</dt> <dt>

[**D3DXFillVolumeTextureTX**](d3dxfillvolumetexturetx.md)
</dt> </dl>

 

 
