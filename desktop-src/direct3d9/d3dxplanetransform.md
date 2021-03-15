---
description: Transforms a plane by a matrix. The input matrix is the inverse transpose of the actual transformation.
ms.assetid: 3581b397-cbd8-4aed-80dd-1841f331a367
title: D3DXPlaneTransform function (D3dx9math.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- D3DXPlaneTransform
api_type: 
- LibDef
api_location: 
- d3dx9.lib
- d3dx9.dll
---

# D3DXPlaneTransform function (D3dx9math.h)

Transforms a plane by a matrix. The input matrix is the inverse transpose of the actual transformation.

## Syntax


```C++
D3DXPLANE* D3DXPlaneTransform(
  _Inout_       D3DXPLANE  *pOut,
  _In_    const D3DXPLANE  *pP,
  _In_    const D3DXMATRIX *pM
);
```



## Parameters

<dl> <dt>

*pOut* \[in, out\]
</dt> <dd>

Type: **[**D3DXPLANE**](d3dxplane.md)\***

Pointer to the [**D3DXPLANE**](d3dxplane.md) structure that contains the resulting transformed plane. See example.

</dd> <dt>

*pP* \[in\]
</dt> <dd>

Type: **const [**D3DXPLANE**](d3dxplane.md)\***

Pointer to the input [**D3DXPLANE**](d3dxplane.md) structure, which contains the plane that will be transformed. The vector (a,b,c) that describes the plane must be normalized before this function is called. See example.

</dd> <dt>

*pM* \[in\]
</dt> <dd>

Type: **const [**D3DXMATRIX**](d3dxmatrix.md)\***

Pointer to the source [**D3DXMATRIX**](d3dxmatrix.md) structure, which contains the transformation values. This matrix must contain the inverse transpose of the transformation values.

</dd> </dl>

## Return value

Type: **[**D3DXPLANE**](d3dxplane.md)\***

Pointer to a [**D3DXPLANE**](d3dxplane.md) structure, representing the transformed plane. This is the same value returned in the pOut parameter so that this function can be used as a parameter for another function.

## Remarks

### Examples

This example transforms a plane by applying a non-uniform scale.


```
D3DXPLANE   planeNew;
D3DXPLANE   plane(0,1,1,0);
D3DXPlaneNormalize(&plane, &plane);

D3DXMATRIX  matrix;
D3DXMatrixScaling(&matrix, 1.0f,2.0f,3.0f); 
D3DXMatrixInverse(&matrix, NULL, &matrix);
D3DXMatrixTranspose(&matrix, &matrix);
D3DXPlaneTransform(&planeNew, &plane, &matrix);
```



A plane is described by ax + by + cz + dw = 0. The first plane is created with (a,b,c,d) = (0,1,1,0), which is a plane described by y + z = 0. After scaling, the new plane contains (a,b,c,d) = (0, 0.353f, 0.235f, 0), which shows the new plane to be described by 0.353y + 0.235z = 0.

The parameter pM contains the inverse transpose of the transformation matrix. The inverse transpose is required by this method so that the normal vector of the transformed plane can be correctly transformed as well.

## Requirements



| Requirement | Value |
|--------------------|----------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>D3dx9math.h</dt> </dl> |
| Library<br/> | <dl> <dt>D3dx9.lib</dt> </dl>   |



## See also

<dl> <dt>

[Math Functions](dx9-graphics-reference-d3dx-functions-math.md)
</dt> <dt>

[**D3DXPlaneNormalize**](d3dxplanenormalize.md)
</dt> <dt>

[**D3DXMatrixRotationX**](d3dxmatrixrotationx.md)
</dt> <dt>

[**D3DXMatrixRotationY**](d3dxmatrixrotationy.md)
</dt> <dt>

[**D3DXMatrixRotationZ**](d3dxmatrixrotationz.md)
</dt> <dt>

[**D3DXMatrixInverse**](d3dxmatrixinverse.md)
</dt> <dt>

[**D3DXMatrixTranspose**](d3dxmatrixtranspose.md)
</dt> </dl>

 

 




