---
Description: Constructs a plane from three points.
ms.assetid: 0e77af1b-cedf-482c-8398-10becb398a2c
title: D3DXPlaneFromPoints function
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# D3DXPlaneFromPoints function

Constructs a plane from three points.

## Syntax


```C++
D3DXPLANE* D3DXPlaneFromPoints(
  _Inout_       D3DXPLANE   *pOut,
  _In_    const D3DXVECTOR3 *pV1,
  _In_    const D3DXVECTOR3 *pV2,
  _In_    const D3DXVECTOR3 *pV3
);
```



## Parameters

<dl> <dt>

*pOut* \[in, out\]
</dt> <dd>

Type: **[**D3DXPLANE**](https://msdn.microsoft.com/windows/desktop/ffca4650-9788-4559-8f6b-a4e5db29ce55)\***

Pointer to the [**D3DXPLANE**](d3d10-d3dxplane.md) that is the result of the operation.

</dd> <dt>

*pV1* \[in\]
</dt> <dd>

Type: **const [**D3DXVECTOR3**](https://msdn.microsoft.com/windows/desktop/4d73de4b-82fe-452a-8a1e-17208f172a03)\***

Pointer to a [**D3DXVECTOR3**](d3d10-d3dxvector3.md), defining one of the points used to construct the plane.

</dd> <dt>

*pV2* \[in\]
</dt> <dd>

Type: **const [**D3DXVECTOR3**](https://msdn.microsoft.com/windows/desktop/4d73de4b-82fe-452a-8a1e-17208f172a03)\***

Pointer to a D3DXVECTOR3 structure, defining one of the points used to construct the plane.

</dd> <dt>

*pV3* \[in\]
</dt> <dd>

Type: **const [**D3DXVECTOR3**](https://msdn.microsoft.com/windows/desktop/4d73de4b-82fe-452a-8a1e-17208f172a03)\***

Pointer to a D3DXVECTOR3 structure, defining one of the points used to construct the plane.

</dd> </dl>

## Return value

Type: **[**D3DXPLANE**](https://msdn.microsoft.com/windows/desktop/ffca4650-9788-4559-8f6b-a4e5db29ce55)\***

Pointer to the D3DXPLANE structure constructed from the given points.

## Remarks

The return value for this function is the same value returned in the pOut parameter. In this way, the D3DXPlaneFromPoints function can be used as a parameter for another function.

## Requirements



|                    |                                                                                         |
|--------------------|-----------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>D3DX10Math.h</dt> </dl> |
| Library<br/> | <dl> <dt>D3DX10.lib</dt> </dl>   |



## See also

<dl> <dt>

[Math Functions](d3d10-graphics-reference-d3dx10-functions-math.md)
</dt> </dl>

 

 




