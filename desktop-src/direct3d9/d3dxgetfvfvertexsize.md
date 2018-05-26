---
Description: Returns the size of a vertex for a flexible vertex format (FVF).
ms.assetid: 9d8e2b1f-0ec8-46ab-8492-2cadd700225e
title: D3DXGetFVFVertexSize function
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# D3DXGetFVFVertexSize function

Returns the size of a vertex for a flexible vertex format (FVF).

## Syntax


```C++
UINT D3DXGetFVFVertexSize(
  _In_ DWORD FVF
);
```



## Parameters

<dl> <dt>

*FVF* \[in\]
</dt> <dd>

Type: **[**DWORD**](winprog.windows_data_types)**

FVF to be queried. A combination of [D3DFVF](d3dfvf.md).

</dd> </dl>

## Return value

Type: **[**UINT**](winprog.windows_data_types)**

The FVF vertex size, in bytes.

## Requirements



|                    |                                                                                        |
|--------------------|----------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>D3dx9mesh.h</dt> </dl> |
| Library<br/> | <dl> <dt>D3dx9.lib</dt> </dl>   |



## See also

<dl> <dt>

[Mesh Functions](dx9-graphics-reference-d3dx-functions-mesh.md)
</dt> </dl>

 

 




