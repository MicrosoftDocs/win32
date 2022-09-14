---
description: Sets an albedo value for each texel, overwriting previous albedo values.
ms.assetid: 2928c861-a07e-4099-b04f-cdfa41e70874
title: ID3DXPRTEngine::SetPerTexelAlbedo method (D3DX9Mesh.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type:
- APIRef
- kbSyntax
api_name:
- ID3DXPRTEngine.SetPerTexelAlbedo
api_type:
- COM
api_location:
- d3dx9.lib
- d3dx9.dll
---

# ID3DXPRTEngine::SetPerTexelAlbedo method

Sets an albedo value for each texel, overwriting previous albedo values.

## Syntax


```C++
HRESULT SetPerTexelAlbedo(
  [in] LPDIRECT3DTEXTURE9        pAlbedoTexture,
  [in] UINT                      NumChannels,
  [in] LPD3DXTEXTUREGUTTERHELPER pGH
);
```



## Parameters

<dl> <dt>

*pAlbedoTexture* \[in\]
</dt> <dd>

Type: **[**LPDIRECT3DTEXTURE9**](/windows/win32/api/d3d9helper/nn-d3d9helper-idirect3dtexture9)**

Pointer to an [**IDirect3DTexture9**](/windows/win32/api/d3d9helper/nn-d3d9helper-idirect3dtexture9) texture object in which to store albedo values.

</dd> <dt>

*NumChannels* \[in\]
</dt> <dd>

Type: **[**UINT**](../winprog/windows-data-types.md)**

Number of color channels to set. Set to 1 to specify gray materials (R = G = B), or 3 to enable color bleeding effects.

</dd> <dt>

*pGH* \[in\]
</dt> <dd>

Type: **[**LPD3DXTEXTUREGUTTERHELPER**](id3dxtexturegutterhelper.md)**

Optional pointer to an [**ID3DXTextureGutterHelper**](id3dxtexturegutterhelper.md) object. If not provided, a texture gutter helper object is created and destroyed internally.

</dd> </dl>

## Return value

Type: **[**HRESULT**](https://msdn.microsoft.com/library/Bb401631(v=MSDN.10).aspx)**

If the method succeeds, the return value is S\_OK. If the method fails, the return value can be one of the following: D3DERR\_INVALIDCALL, D3DERR\_NOTAVAILABLED3DERR\_OUTOFVIDEOMEMORY, D3DERR\_WASSTILLDRAWING, E\_OUTOFMEMORY.

## Requirements



| Requirement | Value |
|--------------------|----------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>D3DX9Mesh.h</dt> </dl> |
| Library<br/> | <dl> <dt>D3dx9.lib</dt> </dl>   |



## See also

<dl> <dt>

[ID3DXPRTEngine](id3dxprtengine.md)
</dt> </dl>

 

 
