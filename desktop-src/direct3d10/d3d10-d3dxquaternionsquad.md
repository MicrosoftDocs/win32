---
Description: 'Interpolates between quaternions, using spherical quadrangle interpolation.'
ms.assetid: 'ba953731-4372-4b32-942b-23abfe479704'
title: D3DXQuaternionSquad function
---

# D3DXQuaternionSquad function

Interpolates between quaternions, using spherical quadrangle interpolation.

## Syntax


```C++
D3DXQUATERNION* D3DXQuaternionSquad(
  _Inout_       D3DXQUATERNION *pOut,
  _In_    const D3DXQUATERNION *pQ1,
  _In_    const D3DXQUATERNION *pA,
  _In_    const D3DXQUATERNION *pB,
  _In_    const D3DXQUATERNION *pC,
  _In_          FLOAT          t
);
```



## Parameters

<dl> <dt>

*pOut* \[in, out\]
</dt> <dd>

Type: **[**D3DXQUATERNION**](direct3d9.d3dxquaternion)\***

Pointer to the [**D3DXQUATERNION**](d3d10-d3dxquaternion.md) that is the result of the operation.

</dd> <dt>

*pQ1* \[in\]
</dt> <dd>

Type: **const [**D3DXQUATERNION**](direct3d9.d3dxquaternion)\***

Pointer to a source D3DXQUATERNION structure.

</dd> <dt>

*pA* \[in\]
</dt> <dd>

Type: **const [**D3DXQUATERNION**](direct3d9.d3dxquaternion)\***

Pointer to a source D3DXQUATERNION structure.

</dd> <dt>

*pB* \[in\]
</dt> <dd>

Type: **const [**D3DXQUATERNION**](direct3d9.d3dxquaternion)\***

Pointer to a source D3DXQUATERNION structure.

</dd> <dt>

*pC* \[in\]
</dt> <dd>

Type: **const [**D3DXQUATERNION**](direct3d9.d3dxquaternion)\***

Pointer to a source D3DXQUATERNION structure.

</dd> <dt>

*t* \[in\]
</dt> <dd>

Type: **[**FLOAT**](winprog.windows_data_types)**

Parameter that indicates how far to interpolate between the quaternions.

</dd> </dl>

## Return value

Type: **[**D3DXQUATERNION**](direct3d9.d3dxquaternion)\***

Pointer to a D3DXQUATERNION structure that is the result of the spherical quadrangle interpolation.

## Remarks

This function uses the following sequence of spherical linear interpolation operations:


```
Slerp(Slerp(pQ1, pC, t), Slerp(pA, pB, t), 2t(1 - t))
```



The return value for this function is the same value returned in the pOut parameter. In this way, the D3DXQuaternionSquad function can be used as a parameter for another function.

Use [**D3DXQuaternionNormalize**](d3d10-d3dxquaternionnormalize.md) for any quaternion input that is not already normalized.

## Requirements



|                    |                                                                                         |
|--------------------|-----------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>D3DX10Math.h</dt> </dl> |
| Library<br/> | <dl> <dt>D3DX10.lib</dt> </dl>   |



## See also

<dl> <dt>

[Math Functions](d3d10-graphics-reference-d3dx10-functions-math.md)
</dt> </dl>

 

 




