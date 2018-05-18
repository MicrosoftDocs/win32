---
Description: 'Computes a bounding sphere for the mesh.'
ms.assetid: '54f486d2-45e9-4fc1-90a3-97488ed4d900'
title: D3DXComputeBoundingSphere function
---

# D3DXComputeBoundingSphere function

Computes a bounding sphere for the mesh.

## Syntax


```C++
HRESULT D3DXComputeBoundingSphere(
  _In_ const D3DXVECTOR3 *pFirstPosition,
  _In_       DWORD       NumVertices,
  _In_       DWORD       dwStride,
  _In_       D3DXVECTOR3 *pCenter,
  _In_       FLOAT       *pRadius
);
```



## Parameters

<dl> <dt>

*pFirstPosition* \[in\]
</dt> <dd>

Type: **const [**D3DXVECTOR3**](direct3d9.d3dxvector3)\***

Pointer to first position.

</dd> <dt>

*NumVertices* \[in\]
</dt> <dd>

Type: **[**DWORD**](winprog.windows_data_types)**

Number of vertices.

</dd> <dt>

*dwStride* \[in\]
</dt> <dd>

Type: **[**DWORD**](winprog.windows_data_types)**

Number of bytes between position vectors.

</dd> <dt>

*pCenter* \[in\]
</dt> <dd>

Type: **[**D3DXVECTOR3**](direct3d9.d3dxvector3)\***

[**D3DXVECTOR3**](d3d10-d3dxvector3.md) structure, defining the coordinate center of the returned bounding sphere.

</dd> <dt>

*pRadius* \[in\]
</dt> <dd>

Type: **[**FLOAT**](winprog.windows_data_types)\***

Radius of the returned bounding sphere.

</dd> </dl>

## Return value

Type: **[**HRESULT**](455d07e9-52c3-4efb-a9dc-2955cbfd38cc)**

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

 

 




