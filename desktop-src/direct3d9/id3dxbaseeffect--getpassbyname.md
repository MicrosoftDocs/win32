---
Description: Gets the handle of a pass by looking up its name.
ms.assetid: 24d043a2-5c87-4a59-80d4-0c81bd7a0b3e
title: ID3DXBaseEffect::GetPassByName method
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# ID3DXBaseEffect::GetPassByName method

Gets the handle of a pass by looking up its name.

## Syntax


```C++
D3DXHANDLE GetPassByName(
  [in] D3DXHANDLE hTechnique,
  [in] LPCSTR     pName
);
```



## Parameters

<dl> <dt>

*hTechnique* \[in\]
</dt> <dd>

Type: **[D3DXHANDLE](dx9-graphics-reference-effects-constants.md)**

Handle of the parent technique. See [Handles (Direct3D 9)](handles.md).

</dd> <dt>

*pName* \[in\]
</dt> <dd>

Type: **[**LPCSTR**](https://msdn.microsoft.com/4553cafc-450e-4493-a4d4-cb6e2f274d46)**

String containing the pass name.

</dd> </dl>

## Return value

Type: **[D3DXHANDLE](dx9-graphics-reference-effects-constants.md)**

Returns the handle of the first pass inside the specified technique that has the specified name, or **NULL** if the name was not found. See [Handles (Direct3D 9)](handles.md).

## Requirements



|                    |                                                                                          |
|--------------------|------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>D3DX9Effect.h</dt> </dl> |
| Library<br/> | <dl> <dt>D3dx9.lib</dt> </dl>     |



## See also

<dl> <dt>

[ID3DXBaseEffect](id3dxbaseeffect.md)
</dt> </dl>

 

 




