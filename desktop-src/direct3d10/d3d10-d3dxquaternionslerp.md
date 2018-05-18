---
Description: 'Interpolates between two quaternions, using spherical linear interpolation.'
ms.assetid: '487e1df1-bf20-49cb-ad14-61fcf1300904'
title: D3DXQuaternionSlerp function
---

# D3DXQuaternionSlerp function

Interpolates between two quaternions, using spherical linear interpolation.

## Syntax


```C++
D3DXQUATERNION* D3DXQuaternionSlerp(
  _Inout_       D3DXQUATERNION *pOut,
  _In_    const D3DXQUATERNION *pQ1,
  _In_    const D3DXQUATERNION *pQ2,
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

*pQ2* \[in\]
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

Pointer to a D3DXQUATERNION structure that is the result of the interpolation.

## Remarks

The return value for this function is the same value returned in the pOut parameter. In this way, the D3DXQuaternionSlerp function can be used as a parameter for another function.

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

 

 




