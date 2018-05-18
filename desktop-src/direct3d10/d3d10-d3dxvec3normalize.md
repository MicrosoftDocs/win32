---
Description: 'Returns the normalized version of a 3D vector.'
ms.assetid: '420321a2-0c3b-419c-9620-acf184e7b4f0'
title: D3DXVec3Normalize function
---

# D3DXVec3Normalize function

Returns the normalized version of a 3D vector.

## Syntax


```C++
D3DXVECTOR3* D3DXVec3Normalize(
  _Inout_       D3DXVECTOR3 *pOut,
  _In_    const D3DXVECTOR3 *pV
);
```



## Parameters

<dl> <dt>

*pOut* \[in, out\]
</dt> <dd>

Type: **[**D3DXVECTOR3**](direct3d9.d3dxvector3)\***

Pointer to the [**D3DXVECTOR3**](d3d10-d3dxvector3.md) that is the result of the operation.

</dd> <dt>

*pV* \[in\]
</dt> <dd>

Type: **const [**D3DXVECTOR3**](direct3d9.d3dxvector3)\***

Pointer to the source D3DXVECTOR3 structure.

</dd> </dl>

## Return value

Type: **[**D3DXVECTOR3**](direct3d9.d3dxvector3)\***

Pointer to a D3DXVECTOR3 structure that is the normalized version of the specified vector.

## Remarks

The return value for this function is the same value returned in the pOut parameter. In this way, the D3DXVec3Normalize function can be used as a parameter for another function.

## Requirements



|                   |                                                                                         |
|-------------------|-----------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>D3DX10Math.h</dt> </dl> |



## See also

<dl> <dt>

[Math Functions](d3d10-graphics-reference-d3dx10-functions-math.md)
</dt> </dl>

 

 




