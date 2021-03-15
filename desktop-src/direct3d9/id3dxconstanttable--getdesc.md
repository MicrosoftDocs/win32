---
description: Gets a description of the constant table.
ms.assetid: 3a7396c6-3a3e-44c2-96b7-60339015b376
title: ID3DXConstantTable::GetDesc method (D3DX9Shader.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- ID3DXConstantTable.GetDesc
api_type: 
- COM
api_location: 
- d3dx9.lib
- d3dx9.dll
---

# ID3DXConstantTable::GetDesc method

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

Description of the constant table. See [**D3DXCONSTANTTABLE\_DESC**](d3dxconstanttable-desc.md).

</dd> </dl>

## Return value

Type: **[**HRESULT**](https://msdn.microsoft.com/library/Bb401631(v=MSDN.10).aspx)**

If the method succeeds, the return value is D3D\_OK. If the method fails, the return value can be one of the following: D3DERR\_INVALIDCALL, D3DXERR\_INVALIDDATA.

## Requirements



| Requirement | Value |
|--------------------|------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>D3DX9Shader.h</dt> </dl> |
| Library<br/> | <dl> <dt>D3dx9.lib</dt> </dl>     |



## See also

<dl> <dt>

[ID3DXConstantTable](id3dxconstanttable.md)
</dt> <dt>

[**ID3DXConstantTable::GetConstantDesc**](id3dxconstanttable--getconstantdesc.md)
</dt> </dl>

 

 




