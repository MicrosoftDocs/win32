---
Description: Sets a normal vector for each texel in a texture object. This method is used to store vertex normal vectors from a mesh (or interpolated vertex normals if pixel-based precomputed radiance transfer (PRT) is being computed).
ms.assetid: 165a3ef6-c142-4988-b4fb-5aafd8ff11fe
title: ID3DXPRTEngineSetPerTexelNormal method
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# ID3DXPRTEngine::SetPerTexelNormal method

Sets a normal vector for each texel in a texture object. This method is used to store vertex normal vectors from a mesh (or interpolated vertex normals if pixel-based precomputed radiance transfer (PRT) is being computed).

## Syntax


```C++
HRESULT SetPerTexelNormal(
  [in] LPDIRECT3DTEXTURE9 pNormalTexture
);
```



## Parameters

<dl> <dt>

*pNormalTexture* \[in\]
</dt> <dd>

Type: **[**LPDIRECT3DTEXTURE9**](/windows/win32/d3d9helper/nn-d3d9-idirect3dtexture9?branch=master)**

Pointer to an [**IDirect3DTexture9**](/windows/win32/d3d9helper/nn-d3d9-idirect3dtexture9?branch=master) texture object that serves as an object space normal map in which to store normal vectors. The texture must have the same dimensions as [**ID3DXPRTBuffer**](id3dxprtbuffer.md) and must be able to store signed texture formats.

</dd> </dl>

## Return value

Type: **[**HRESULT**](455d07e9-52c3-4efb-a9dc-2955cbfd38cc)**

If the method succeeds, the return value is S\_OK. If the method fails, the return value can be one of the following: D3DERR\_INVALIDCALL, E\_OUTOFMEMORY.

## Requirements



|                    |                                                                                        |
|--------------------|----------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>D3DX9Mesh.h</dt> </dl> |
| Library<br/> | <dl> <dt>D3dx9.lib</dt> </dl>   |



## See also

<dl> <dt>

[ID3DXPRTEngine](id3dxprtengine.md)
</dt> </dl>

 

 




