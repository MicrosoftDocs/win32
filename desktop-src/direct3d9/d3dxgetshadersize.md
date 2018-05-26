---
Description: Returns the size of the shader byte code, in bytes.
ms.assetid: 7dd091f7-fda9-49e1-982d-2eb57d9ecb23
title: D3DXGetShaderSize function
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# D3DXGetShaderSize function

Returns the size of the shader byte code, in bytes.

## Syntax


```C++
UINT D3DXGetShaderSize(
  _In_ const DWORD *pFunction
);
```



## Parameters

<dl> <dt>

*pFunction* \[in\]
</dt> <dd>

Type: **const [**DWORD**](winprog.windows_data_types)\***

Pointer to the function DWORD stream.

</dd> </dl>

## Return value

Type: **[**UINT**](winprog.windows_data_types)**

Returns the size of the shader byte code, in bytes.

## Requirements



|                    |                                                                                          |
|--------------------|------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>D3DX9Shader.h</dt> </dl> |
| Library<br/> | <dl> <dt>D3dx9.lib</dt> </dl>     |



## See also

<dl> <dt>

[Shader Functions](dx9-graphics-reference-d3dx-functions-shader.md)
</dt> </dl>

 

 




