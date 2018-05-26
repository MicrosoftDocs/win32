---
Description: Sets an array of 4D vectors.
ms.assetid: 45bc5cb1-b44a-468b-8c80-a639da8a033f
title: ID3DXTextureShaderSetVectorArray method
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# ID3DXTextureShader::SetVectorArray method

Sets an array of 4D vectors.

## Syntax


```C++
HRESULT SetVectorArray(
  [in]       D3DXHANDLE  hConstant,
  [in] const D3DXVECTOR4 *pVector,
  [in]       UINT        Count
);
```



## Parameters

<dl> <dt>

*hConstant* \[in\]
</dt> <dd>

Type: **[D3DXHANDLE](dx9-graphics-reference-effects-constants.md)**

Unique identifier to the array of vector constants. See [D3DXHANDLE](d3dxfx.md).

</dd> <dt>

*pVector* \[in\]
</dt> <dd>

Type: **const [**D3DXVECTOR4**](d3dxvector4.md)\***

Array of 4D vectors. See [**D3DXVECTOR4**](d3dxvector4.md).

</dd> <dt>

*Count* \[in\]
</dt> <dd>

Type: **[**UINT**](winprog.windows_data_types)**

Number of vectors in the array.

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

[ID3DXTextureShader](id3dxtextureshader.md)
</dt> </dl>

 

 




