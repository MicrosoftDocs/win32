---
Description: Determines if a parameter is used by the technique.
ms.assetid: ac50c0d3-93d9-4477-a854-d0b53df28c90
title: ID3DXEffect::IsParameterUsed method
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# ID3DXEffect::IsParameterUsed method

Determines if a parameter is used by the technique.

## Syntax


```C++
BOOL IsParameterUsed(
  [in] D3DXHANDLE hParameter,
  [in] D3DXHANDLE hTechnique
);
```



## Parameters

<dl> <dt>

*hParameter* \[in\]
</dt> <dd>

Type: **[D3DXHANDLE](dx9-graphics-reference-effects-constants.md)**

Unique identifier for the parameter. See [Handles (Direct3D 9)](handles.md).

</dd> <dt>

*hTechnique* \[in\]
</dt> <dd>

Type: **[D3DXHANDLE](dx9-graphics-reference-effects-constants.md)**

Unique identifier for the technique. See [Handles (Direct3D 9)](handles.md).

</dd> </dl>

## Return value

Type: **[**BOOL**](https://msdn.microsoft.com/4553cafc-450e-4493-a4d4-cb6e2f274d46)**

Returns **TRUE** if the parameter is being used and returns **FALSE** if the parameter is not being used.

## Requirements



|                    |                                                                                          |
|--------------------|------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>D3DX9Effect.h</dt> </dl> |
| Library<br/> | <dl> <dt>D3dx9.lib</dt> </dl>     |



## See also

<dl> <dt>

[ID3DXEffect](id3dxeffect.md)
</dt> </dl>

 

 




