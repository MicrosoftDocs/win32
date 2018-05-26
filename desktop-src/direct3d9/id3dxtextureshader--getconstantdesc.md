---
Description: Gets a pointer to the array of constants in the constant table.
ms.assetid: 2476344b-8433-46bb-9242-dff84e3168e7
title: ID3DXTextureShaderGetConstantDesc method
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# ID3DXTextureShader::GetConstantDesc method

Gets a pointer to the array of constants in the constant table.

## Syntax


```C++
HRESULT GetConstantDesc(
  [in]      D3DXHANDLE        hConstant,
  [in, out] D3DXCONSTANT_DESC *pDesc,
  [in, out] UINT              *pCount
);
```



## Parameters

<dl> <dt>

*hConstant* \[in\]
</dt> <dd>

Type: **[D3DXHANDLE](dx9-graphics-reference-effects-constants.md)**

Unique identifier to a constant. See [D3DXHANDLE](d3dxfx.md).

</dd> <dt>

*pDesc* \[in, out\]
</dt> <dd>

Type: **[**D3DXCONSTANT\_DESC**](d3dxconstant-desc.md)\***

Returns a pointer to an array of descriptions. See [**D3DXCONSTANT\_DESC**](d3dxconstant-desc.md).

</dd> <dt>

*pCount* \[in, out\]
</dt> <dd>

Type: **[**UINT**](winprog.windows_data_types)\***

The input supplied must be the maximum size of the array. The output is the number of elements that are filled in the array when the function returns.

</dd> </dl>

## Return value

Type: **[**HRESULT**](455d07e9-52c3-4efb-a9dc-2955cbfd38cc)**

If the method succeeds, the return value is D3D\_OK. If the method fails, the return value can be one of the following: D3DERR\_INVALIDCALL, D3DXERR\_INVALIDDATA.

## Remarks

Samplers can appear more than once in a constant table, therefore, this method can return an array of descriptions each with a different register index.

## Requirements



|                    |                                                                                          |
|--------------------|------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>D3DX9Shader.h</dt> </dl> |
| Library<br/> | <dl> <dt>D3dx9.lib</dt> </dl>     |



## See also

<dl> <dt>

[ID3DXTextureShader](id3dxtextureshader.md)
</dt> <dt>

[**ID3DXTextureShader::GetDesc**](id3dxtextureshader--getdesc.md)
</dt> </dl>

 

 




