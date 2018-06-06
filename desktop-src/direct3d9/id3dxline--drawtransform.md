---
Description: Draws a line strip in screen space with a specified input transformation matrix.
ms.assetid: 869dc705-8162-4cd9-ac6a-c0ce32f430c3
title: ID3DXLine::DrawTransform method
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# ID3DXLine::DrawTransform method

Draws a line strip in screen space with a specified input transformation matrix.

## Syntax


```C++
HRESULT DrawTransform(
  [in] const D3DXVECTOR3 *pVertexList,
  [in]       DWORD       dwVertexListCount,
  [in] const D3DXMATRIX  *pTransform,
  [in]       D3DCOLOR    Color
);
```



## Parameters

<dl> <dt>

*pVertexList* \[in\]
</dt> <dd>

Type: **const [**D3DXVECTOR3**](d3dxvector3.md)\***

Array of vertices that make up the line. See [**D3DXVECTOR3**](d3dxvector3.md).

</dd> <dt>

*dwVertexListCount* \[in\]
</dt> <dd>

Type: **[**DWORD**](https://msdn.microsoft.com/4553cafc-450e-4493-a4d4-cb6e2f274d46)**

Number of vertices in the vertex list.

</dd> <dt>

*pTransform* \[in\]
</dt> <dd>

Type: **const [**D3DXMATRIX**](d3dxmatrix.md)\***

A scale, rotate, and translate (SRT) matrix for transforming the points. See [**D3DXMATRIX**](d3dxmatrix.md). If this matrix is a projection matrix, any stippled lines will be drawn with a perspective-correct stippling pattern. Or, you can transform the vertices and use [**ID3DXLine::Draw**](id3dxline--draw.md) to draw the line with a nonperspective-correct stipple pattern.

</dd> <dt>

*Color* \[in\]
</dt> <dd>

Type: **[**D3DCOLOR**](d3dcolor.md)**

Color of the line. See [**D3DCOLOR**](d3dcolor.md).

</dd> </dl>

## Return value

Type: **[**HRESULT**](https://msdn.microsoft.com/windows/desktop/455d07e9-52c3-4efb-a9dc-2955cbfd38cc)**

If the method succeeds, the return value is D3D\_OK. If the method fails, the return value can be one of the following: D3DERR\_INVALIDCALL, D3DXERR\_INVALIDDATA.

## Requirements



|                    |                                                                                        |
|--------------------|----------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>D3dx9core.h</dt> </dl> |
| Library<br/> | <dl> <dt>D3dx9.lib</dt> </dl>   |



## See also

<dl> <dt>

[ID3DXLine](id3dxline.md)
</dt> </dl>

 

 




