---
description: Returns the sampler index.
ms.assetid: 'vs|directx_sdk|~\id3dxconstanttable__getsamplerindex.htm'
title: ID3DXConstantTable::GetSamplerIndex method (D3DX9Shader.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- ID3DXConstantTable.GetSamplerIndex
api_type: 
- COM
api_location: 
- d3dx9.lib
- d3dx9.dll
---

# ID3DXConstantTable::GetSamplerIndex method

Returns the sampler index.

## Syntax


```C++
UINT GetSamplerIndex(
  [out] D3DXHANDLE hConstant
);
```



## Parameters

<dl> <dt>

*hConstant* \[out\]
</dt> <dd>

Type: **[D3DXHANDLE](dx9-graphics-reference-effects-constants.md)**

The sampler handle.

</dd> </dl>

## Return value

Type: **[**UINT**](../winprog/windows-data-types.md)**

Returns the sampler index number from the constant table.

## Requirements



| Requirement | Value |
|--------------------|------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>D3DX9Shader.h</dt> </dl> |
| Library<br/> | <dl> <dt>D3dx9.lib</dt> </dl>     |



## See also

<dl> <dt>

[ID3DXConstantTable](id3dxconstanttable.md)
</dt> </dl>

 

 
