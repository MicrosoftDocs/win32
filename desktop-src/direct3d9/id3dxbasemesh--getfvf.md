---
Description: Gets the fixed function vertex value.
ms.assetid: ed56ff2d-0366-426c-9f9a-7d1a7c5d1a7c
title: ID3DXBaseMesh::GetFVF method
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# ID3DXBaseMesh::GetFVF method

Gets the fixed function vertex value.

## Syntax


```C++
DWORD GetFVF();
```



## Parameters

This method has no parameters.

## Return value

Type: **[**DWORD**](https://msdn.microsoft.com/windows/desktop/4553cafc-450e-4493-a4d4-cb6e2f274d46)**

Returns the flexible vertex format (FVF) codes.

## Remarks

This method can return 0 if the vertex format cannot be mapped directly to an FVF code. This will occur for a mesh created from a vertex declaration that doesn't have the same order and elements supported by the FVF codes.

## Requirements



|                    |                                                                                        |
|--------------------|----------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>D3DX9Mesh.h</dt> </dl> |
| Library<br/> | <dl> <dt>D3dx9.lib</dt> </dl>   |



## See also

<dl> <dt>

[ID3DXBaseMesh](id3dxbasemesh.md)
</dt> </dl>

 

 




