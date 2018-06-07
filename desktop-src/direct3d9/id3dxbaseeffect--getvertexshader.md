---
Description: Gets a vertex shader.
ms.assetid: ab58b465-7b10-46eb-88c0-c5229cb09481
title: ID3DXBaseEffect::GetVertexShader method
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
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

Type: **[**LPDIRECT3DVERTEXSHADER9**](/windows/desktop/api/d3d9helper/nn-d3d9-idirect3dvertexshader9)\***

Returns a vertex shader object. See [**IDirect3DVertexShader9**](/windows/desktop/api/d3d9helper/nn-d3d9-idirect3dvertexshader9).

</dd> </dl>

## Return value

Type: **[**HRESULT**](https://msdn.microsoft.com/windows/desktop/455d07e9-52c3-4efb-a9dc-2955cbfd38cc)**

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

 

 




