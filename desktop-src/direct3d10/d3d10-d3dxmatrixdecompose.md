---
Description: 'Breaks down a general 3D transformation matrix into its scalar, rotational, and translational components.'
ms.assetid: '3694769f-56e7-4983-924e-021c129462a2'
title: D3DXMatrixDecompose function
---

# D3DXMatrixDecompose function

Breaks down a general 3D transformation matrix into its scalar, rotational, and translational components.

## Syntax


```C++
HRESULT D3DXMatrixDecompose(
  _In_       D3DXVECTOR3    *pOutScale,
  _In_       D3DXQUATERNION *pOutRotation,
  _In_       D3DXVECTOR3    *pOutTranslation,
  _In_ const D3DXMATRIX     *pM
);
```



## Parameters

<dl> <dt>

*pOutScale* \[in\]
</dt> <dd>

Type: **[**D3DXVECTOR3**](direct3d9.d3dxvector3)\***

Pointer to the output [**D3DXVECTOR3**](d3d10-d3dxvector3.md) that contains scaling factors applied along the x, y, and z-axes.

</dd> <dt>

*pOutRotation* \[in\]
</dt> <dd>

Type: **[**D3DXQUATERNION**](direct3d9.d3dxquaternion)\***

Pointer to the [**D3DXQUATERNION**](d3d10-d3dxquaternion.md) that describes the rotation.

</dd> <dt>

*pOutTranslation* \[in\]
</dt> <dd>

Type: **[**D3DXVECTOR3**](direct3d9.d3dxvector3)\***

Pointer to the D3DXVECTOR3 vector that describes the translation.

</dd> <dt>

*pM* \[in\]
</dt> <dd>

Type: **const [**D3DXMATRIX**](direct3d9.d3dxmatrix)\***

Pointer to an input [**D3DXMATRIX**](d3d10-d3dxmatrix.md) matrix to decompose.

</dd> </dl>

## Return value

Type: **[**HRESULT**](455d07e9-52c3-4efb-a9dc-2955cbfd38cc)**

If the function succeeds, the return value is S\_OK. If the function fails, the return value can be the following: D3DERR\_INVALIDCALL.

## Requirements



|                    |                                                                                         |
|--------------------|-----------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>D3DX10Math.h</dt> </dl> |
| Library<br/> | <dl> <dt>D3DX10.lib</dt> </dl>   |



## See also

<dl> <dt>

[Math Functions](d3d10-graphics-reference-d3dx10-functions-math.md)
</dt> </dl>

 

 




