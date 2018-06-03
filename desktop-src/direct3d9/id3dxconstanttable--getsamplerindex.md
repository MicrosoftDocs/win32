---
Description: Returns the sampler index.
ms.assetid: c55fe0eb-a987-4d6a-91f5-3b5204b398c0
title: ID3DXConstantTable::GetSamplerIndex method
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
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

Type: **[**UINT**](https://msdn.microsoft.com/windows/desktop/4553cafc-450e-4493-a4d4-cb6e2f274d46)**

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

 

 




