---
Description: Gets the handle of a function.
ms.assetid: 97c82c28-4402-4605-8247-44d6f38bfa20
title: ID3DXBaseEffectGetFunction method
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# ID3DXBaseEffect::GetFunction method

Gets the handle of a function.

## Syntax


```C++
D3DXHANDLE GetFunction(
  [in] UINT Index
);
```



## Parameters

<dl> <dt>

*Index* \[in\]
</dt> <dd>

Type: **[**UINT**](winprog.windows_data_types)**

Function index.

</dd> </dl>

## Return value

Type: **[D3DXHANDLE](dx9-graphics-reference-effects-constants.md)**

Returns the handle of the specified function, or **NULL** if the index was invalid. See [Handles (Direct3D 9)](handles.md).

## Requirements



|                    |                                                                                          |
|--------------------|------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>D3DX9Effect.h</dt> </dl> |
| Library<br/> | <dl> <dt>D3dx9.lib</dt> </dl>     |



## See also

<dl> <dt>

[ID3DXBaseEffect](id3dxbaseeffect.md)
</dt> </dl>

 

 




