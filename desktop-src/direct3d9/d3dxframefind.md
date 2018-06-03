---
Description: Finds the child frame of a root frame.
ms.assetid: 211e117a-9707-459a-a6a1-b3e78bdad6e2
title: D3DXFrameFind function
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# D3DXFrameFind function

Finds the child frame of a root frame.

## Syntax


```C++
LPD3DXFRAME D3DXFrameFind(
  _In_ const D3DXFRAME *pFrameRoot,
  _In_       LPCSTR    Name
);
```



## Parameters

<dl> <dt>

*pFrameRoot* \[in\]
</dt> <dd>

Type: **const [**D3DXFRAME**](d3dxframe.md)\***

Pointer to the root frame. See [**D3DXFRAME**](d3dxframe.md).

</dd> <dt>

*Name* \[in\]
</dt> <dd>

Type: **[**LPCSTR**](https://msdn.microsoft.com/windows/desktop/4553cafc-450e-4493-a4d4-cb6e2f274d46)**

Name of the child frame to find.

</dd> </dl>

## Return value

Type: **[**LPD3DXFRAME**](d3dxframe.md)**

Returns the child frame if it is found, or **NULL** otherwise. See [**D3DXFRAME**](d3dxframe.md).

## Requirements



|                    |                                                                                        |
|--------------------|----------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>D3dx9anim.h</dt> </dl> |
| Library<br/> | <dl> <dt>D3dx9.lib</dt> </dl>   |



## See also

<dl> <dt>

[Animation Functions](dx9-graphics-reference-d3dx-functions-animation.md)
</dt> </dl>

 

 




