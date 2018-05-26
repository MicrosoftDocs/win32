---
Description: Initiate the rendering of a parabolic environment map.
ms.assetid: 80456084-f5f5-4dfe-805a-7eaaf7f7cb2a
title: ID3DXRenderToEnvMapBeginParabolic method
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# ID3DXRenderToEnvMap::BeginParabolic method

Initiate the rendering of a parabolic environment map.

## Syntax


```C++
HRESULT BeginParabolic(
  [in] LPDIRECT3DTEXTURE9 pTexZPos,
  [in] LPDIRECT3DTEXTURE9 pTexZNeg
);
```



## Parameters

<dl> <dt>

*pTexZPos* \[in\]
</dt> <dd>

Type: **[**LPDIRECT3DTEXTURE9**](/windows/win32/d3d9helper/nn-d3d9-idirect3dtexture9?branch=master)**

Pointer to an [**IDirect3DTexture9**](/windows/win32/d3d9helper/nn-d3d9-idirect3dtexture9?branch=master) interface that represents the positive render texture.

</dd> <dt>

*pTexZNeg* \[in\]
</dt> <dd>

Type: **[**LPDIRECT3DTEXTURE9**](/windows/win32/d3d9helper/nn-d3d9-idirect3dtexture9?branch=master)**

Pointer to an [**IDirect3DTexture9**](/windows/win32/d3d9helper/nn-d3d9-idirect3dtexture9?branch=master) interface that represents the negative render texture.

</dd> </dl>

## Return value

Type: **[**HRESULT**](455d07e9-52c3-4efb-a9dc-2955cbfd38cc)**

If the function succeeds, the return value is D3D\_OK. If the function fails, the return value can be one of the following: D3DERR\_INVALIDCALL.E\_FAIL

## Remarks

See [**ID3DXRenderToEnvMap::Face**](id3dxrendertoenvmap--face.md) to draw the faces.

## Requirements



|                    |                                                                                        |
|--------------------|----------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>D3dx9core.h</dt> </dl> |
| Library<br/> | <dl> <dt>D3dx9.lib</dt> </dl>   |



## See also

<dl> <dt>

[ID3DXRenderToEnvMap](id3dxrendertoenvmap.md)
</dt> <dt>

[**ID3DXRenderToEnvMap::End**](id3dxrendertoenvmap--end.md)
</dt> </dl>

 

 




