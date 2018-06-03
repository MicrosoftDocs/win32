---
Description: Initiate the rendering of a cubic environment map.
ms.assetid: 0f02b2e2-8132-4994-ab07-c79a1b7821dd
title: ID3DXRenderToEnvMap::BeginCube method
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# ID3DXRenderToEnvMap::BeginCube method

Initiate the rendering of a cubic environment map.

## Syntax


```C++
HRESULT BeginCube(
  [in] LPDIRECT3DCUBETEXTURE9 pCubeTex
);
```



## Parameters

<dl> <dt>

*pCubeTex* \[in\]
</dt> <dd>

Type: **[**LPDIRECT3DCUBETEXTURE9**](/windows/desktop/api/d3d9helper/nn-d3d9-idirect3dcubetexture9)**

Pointer to an [**IDirect3DCubeTexture9**](/windows/desktop/api/d3d9helper/nn-d3d9-idirect3dcubetexture9) interface that represents the cube texture to which to render.

</dd> </dl>

## Return value

Type: **[**HRESULT**](https://msdn.microsoft.com/windows/desktop/455d07e9-52c3-4efb-a9dc-2955cbfd38cc)**

If the method succeeds, the return value is D3D\_OK. If the method fails, the return value can be D3DERR\_INVALIDCALL.

## Remarks

See [**ID3DXRenderToEnvMap::Face**](id3dxrendertoenvmap--face.md) to draw each of the 6 faces.

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

 

 




