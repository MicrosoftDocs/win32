---
Description: Gets a description of the constant table.
ms.assetid: 91b537bb-5f7a-448b-a21f-c0ddf66d7238
title: ID3DXTextureShader::GetDesc method
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# ID3DXTextureShader::GetDesc method

Gets a description of the constant table.

## Syntax


```C++
HRESULT GetDesc(
  [in] D3DXCONSTANTTABLE_DESC *pDesc
);
```



## Parameters

<dl> <dt>

*pDesc* \[in\]
</dt> <dd>

Type: **[**D3DXCONSTANTTABLE\_DESC**](d3dxconstanttable-desc.md)\***

The attributes of the constant table. See [**D3DXCONSTANTTABLE\_DESC**](d3dxconstanttable-desc.md).

</dd> </dl>

## Return value

Type: **[**HRESULT**](https://msdn.microsoft.com/windows/desktop/455d07e9-52c3-4efb-a9dc-2955cbfd38cc)**

If the method succeeds, the return value is D3D\_OK. If the method fails, the return value can be one of the following: D3DERR\_INVALIDCALL, D3DXERR\_INVALIDDATA.

## Requirements



|                    |                                                                                          |
|--------------------|------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>D3DX9Shader.h</dt> </dl> |
| Library<br/> | <dl> <dt>D3dx9.lib</dt> </dl>     |



## See also

<dl> <dt>

[ID3DXTextureShader](id3dxtextureshader.md)
</dt> </dl>

 

 




