---
Description: Computes a coordinate-axis oriented bounding box.
ms.assetid: 1b8f328c-2fe1-462e-b464-c8dd9dc03e67
title: D3DXComputeBoundingBox function
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# D3DXComputeBoundingBox function

Computes a coordinate-axis oriented bounding box.

## Syntax


```C++
HRESULT D3DXComputeBoundingBox(
  _In_  const D3DXVECTOR3 *pFirstPosition,
  _In_        DWORD       NumVertices,
  _In_        DWORD       dwStride,
  _Out_       D3DXVECTOR3 *pMin,
  _Out_       D3DXVECTOR3 *pMax
);
```



## Parameters

<dl> <dt>

*pFirstPosition* \[in\]
</dt> <dd>

Type: **const [**D3DXVECTOR3**](https://msdn.microsoft.com/VS|directx_sdk|~\d3dxvector3.htm)\***

Pointer to the first position.

</dd> <dt>

*NumVertices* \[in\]
</dt> <dd>

Type: **[**DWORD**](https://msdn.microsoft.com/4553cafc-450e-4493-a4d4-cb6e2f274d46)**

Number of vertices.

</dd> <dt>

*dwStride* \[in\]
</dt> <dd>

Type: **[**DWORD**](https://msdn.microsoft.com/4553cafc-450e-4493-a4d4-cb6e2f274d46)**

Count or number of bytes between vertices.

</dd> <dt>

*pMin* \[out\]
</dt> <dd>

Type: **[**D3DXVECTOR3**](https://msdn.microsoft.com/VS|directx_sdk|~\d3dxvector3.htm)\***

Pointer to a [**D3DXVECTOR3**](d3d10-d3dxvector3.md) structure, describing the returned lower-left corner of the bounding box.

</dd> <dt>

*pMax* \[out\]
</dt> <dd>

Type: **[**D3DXVECTOR3**](https://msdn.microsoft.com/VS|directx_sdk|~\d3dxvector3.htm)\***

Pointer to a [**D3DXVECTOR3**](d3d10-d3dxvector3.md) structure, describing the returned upper-right corner of the bounding box.

</dd> </dl>

## Return value

Type: **[**HRESULT**](https://msdn.microsoft.com/windows/desktop/455d07e9-52c3-4efb-a9dc-2955cbfd38cc)**

If the function succeeds, the return value is D3D\_OK. If the function fails, the return value can be one of the following: D3DERR\_INVALIDCALL.

## Requirements



|                    |                                                                                         |
|--------------------|-----------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>D3DX10math.h</dt> </dl> |
| Library<br/> | <dl> <dt>D3DX10.lib</dt> </dl>   |



## See also

<dl> <dt>

[Mesh Functions](d3d10-graphics-reference-d3dx10-functions-mesh.md)
</dt> </dl>

 

 




