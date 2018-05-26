---
Description: Initiate the rendering of a spherical environment map.
ms.assetid: b0634120-f5ad-48b3-979a-30b0a53d22a2
title: ID3DXRenderToEnvMapBeginSphere method
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# ID3DXRenderToEnvMap::BeginSphere method

Initiate the rendering of a spherical environment map.

## Syntax


```C++
HRESULT BeginSphere(
  [in] LPDIRECT3DTEXTURE9 pTex
);
```



## Parameters

<dl> <dt>

*pTex* \[in\]
</dt> <dd>

Type: **[**LPDIRECT3DTEXTURE9**](/windows/win32/d3d9helper/nn-d3d9-idirect3dtexture9?branch=master)**

Pointer to an [**IDirect3DTexture9**](/windows/win32/d3d9helper/nn-d3d9-idirect3dtexture9?branch=master) interface that represents the texture to which to render.

</dd> </dl>

## Return value

Type: **[**HRESULT**](455d07e9-52c3-4efb-a9dc-2955cbfd38cc)**

If the method succeeds, the return value is D3D\_OK. If the method fails, the return value can be one of the following: D3DERR\_INVALIDCALL.E\_FAIL

## Remarks

See [**ID3DXRenderToEnvMap::Face**](id3dxrendertoenvmap--face.md) to draw the face.

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

 

 




