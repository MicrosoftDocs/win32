---
Description: Returns the sampler index.
ms.assetid: c55fe0eb-a987-4d6a-91f5-3b5204b398c0
title: ID3DXConstantTableGetSamplerIndex method
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
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

Type: **[**UINT**](winprog.windows_data_types)**

Returns the sampler index number from the constant table.

## Requirements



|                    |                                                                                          |
|--------------------|------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>D3DX9Shader.h</dt> </dl> |
| Library<br/> | <dl> <dt>D3dx9.lib</dt> </dl>     |



## See also

<dl> <dt>

[ID3DXConstantTable](id3dxconstanttable.md)
</dt> </dl>

 

 




