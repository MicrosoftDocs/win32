---
Description: Gets the handle of a function by looking up its name.
ms.assetid: 1e2e2dae-5084-47f3-9812-3dbf609bd70b
title: ID3DXBaseEffectGetFunctionByName method
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# ID3DXBaseEffect::GetFunctionByName method

Gets the handle of a function by looking up its name.

## Syntax


```C++
D3DXHANDLE GetFunctionByName(
  [in] LPCSTR pName
);
```



## Parameters

<dl> <dt>

*pName* \[in\]
</dt> <dd>

Type: **[**LPCSTR**](winprog.windows_data_types)**

String containing the function name.

</dd> </dl>

## Return value

Type: **[D3DXHANDLE](dx9-graphics-reference-effects-constants.md)**

Returns the handle of the specified function, or **NULL** if the name was not found. See [Handles (Direct3D 9)](handles.md).

## Requirements



|                    |                                                                                          |
|--------------------|------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>D3DX9Effect.h</dt> </dl> |
| Library<br/> | <dl> <dt>D3dx9.lib</dt> </dl>     |



## See also

<dl> <dt>

[ID3DXBaseEffect](id3dxbaseeffect.md)
</dt> </dl>

 

 




