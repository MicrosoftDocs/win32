---
Description: Builds a matrix that flattens geometry into a plane.
ms.assetid: 83c9e7d6-fc6c-48e7-bbf2-6aa10868351d
title: D3DXMatrixShadow function
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# D3DXMatrixShadow function

Builds a matrix that flattens geometry into a plane.

## Syntax


```C++
D3DXMATRIX* D3DXMatrixShadow(
  _Inout_       D3DXMATRIX  *pOut,
  _In_    const D3DXVECTOR4 *pLight,
  _In_    const D3DXPLANE   *pPlane
);
```



## Parameters

<dl> <dt>

*pOut* \[in, out\]
</dt> <dd>

Type: **[**D3DXMATRIX**](https://msdn.microsoft.com/windows/desktop/0911088b-50cf-4c4a-996e-351386fc359b)\***

Pointer to the [**D3DXMATRIX**](d3d10-d3dxmatrix.md) structure that is the result of the operation.

</dd> <dt>

*pLight* \[in\]
</dt> <dd>

Type: **const [**D3DXVECTOR4**](https://msdn.microsoft.com/windows/desktop/fbfe7851-7bec-4fa0-b4dc-52f5cb83d0a4)\***

Pointer to a [**D3DXVECTOR4**](d3d10-d3dxvector4.md) describing the light's position.

</dd> <dt>

*pPlane* \[in\]
</dt> <dd>

Type: **const [**D3DXPLANE**](https://msdn.microsoft.com/windows/desktop/ffca4650-9788-4559-8f6b-a4e5db29ce55)\***

Pointer to the source [**D3DXPLANE**](d3d10-d3dxplane.md).

</dd> </dl>

## Return value

Type: **[**D3DXMATRIX**](https://msdn.microsoft.com/windows/desktop/0911088b-50cf-4c4a-996e-351386fc359b)\***

Pointer to a D3DXMATRIX structure that flattens geometry into a plane.

## Remarks

The **D3DXMatrixShadow** function flattens geometry into a plane, as if casting a shadow from a light.

The return value for this function is the same value returned in the pOut parameter. In this way, the **D3DXMatrixShadow** function can be used as a parameter for another function.

This function uses the following formula to compute the returned matrix.


```
P = normalize(Plane);
L = Light;
d = dot(P, L)
    
P.a * L.x + d  P.a * L.y      P.a * L.z      P.a * L.w  
P.b * L.x      P.b * L.y + d  P.b * L.z      P.b * L.w  
P.c * L.x      P.c * L.y      P.c * L.z + d  P.c * L.w  
P.d * L.x      P.d * L.y      P.d * L.z      P.d * L.w + d
```



If the light's w-component is 0, the ray from the origin to the light represents a directional light. If it is 1, the light is a point light.

## Requirements



|                    |                                                                                         |
|--------------------|-----------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>D3DX10Math.h</dt> </dl> |
| Library<br/> | <dl> <dt>D3DX10.lib</dt> </dl>   |



## See also

<dl> <dt>

[Math Functions](d3d10-graphics-reference-d3dx10-functions-math.md)
</dt> </dl>

 

 




