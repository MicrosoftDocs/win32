---
Description: Gets a vertex shader.
ms.assetid: ab58b465-7b10-46eb-88c0-c5229cb09481
title: ID3DXBaseEffectGetVertexShader method
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# ID3DXBaseEffect::GetVertexShader method

Gets a vertex shader.

## Syntax


```C++
HRESULT GetVertexShader(
  [in]  D3DXHANDLE              hParameter,
  [out] LPDIRECT3DVERTEXSHADER9 *ppVShader
);
```



## Parameters

<dl> <dt>

*hParameter* \[in\]
</dt> <dd>

Type: **[D3DXHANDLE](dx9-graphics-reference-effects-constants.md)**

Unique identifier. See [Handles (Direct3D 9)](handles.md).

</dd> <dt>

*ppVShader* \[out\]
</dt> <dd>

Type: **[**LPDIRECT3DVERTEXSHADER9**](/windows/win32/d3d9helper/nn-d3d9-idirect3dvertexshader9?branch=master)\***

Returns a vertex shader object. See [**IDirect3DVertexShader9**](/windows/win32/d3d9helper/nn-d3d9-idirect3dvertexshader9?branch=master).

</dd> </dl>

## Return value

Type: **[**HRESULT**](455d07e9-52c3-4efb-a9dc-2955cbfd38cc)**

If the method succeeds, the return value is D3D\_OK. If the method fails, the return value can be D3DERR\_INVALIDCALL.

## Requirements



|                    |                                                                                          |
|--------------------|------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>D3DX9Shader.h</dt> </dl> |
| Library<br/> | <dl> <dt>D3dx9.lib</dt> </dl>     |



## See also

<dl> <dt>

[ID3DXBaseEffect](id3dxbaseeffect.md)
</dt> </dl>

 

 




