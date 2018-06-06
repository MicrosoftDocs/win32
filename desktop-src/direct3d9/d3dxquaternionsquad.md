---
Description: Interpolates between quaternions, using spherical quadrangle interpolation.
ms.assetid: afce9afb-64cc-4059-90f5-7ed1aca9b3cb
title: D3DXQuaternionSquad function
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
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

Type: **[**D3DXQUATERNION**](d3dxquaternion.md)\***

Pointer to the [**D3DXQUATERNION**](d3dxquaternion.md) structure that is the result of the operation.

</dd> <dt>

*pQ1* \[in\]
</dt> <dd>

Type: **const [**D3DXQUATERNION**](d3dxquaternion.md)\***

Pointer to a source [**D3DXQUATERNION**](d3dxquaternion.md) structure.

</dd> <dt>

*pA* \[in\]
</dt> <dd>

Type: **const [**D3DXQUATERNION**](d3dxquaternion.md)\***

Pointer to a source [**D3DXQUATERNION**](d3dxquaternion.md) structure.

</dd> <dt>

*pB* \[in\]
</dt> <dd>

Type: **const [**D3DXQUATERNION**](d3dxquaternion.md)\***

Pointer to a source [**D3DXQUATERNION**](d3dxquaternion.md) structure.

</dd> <dt>

*pC* \[in\]
</dt> <dd>

Type: **const [**D3DXQUATERNION**](d3dxquaternion.md)\***

Pointer to a source [**D3DXQUATERNION**](d3dxquaternion.md) structure.

</dd> <dt>

*t* \[in\]
</dt> <dd>

Type: **[**FLOAT**](https://msdn.microsoft.com/4553cafc-450e-4493-a4d4-cb6e2f274d46)**

Parameter that indicates how far to interpolate between the quaternions.

</dd> </dl>

## Return value

Type: **[**D3DXQUATERNION**](d3dxquaternion.md)\***

Pointer to a [**D3DXQUATERNION**](d3dxquaternion.md) structure that is the result of the spherical quadrangle interpolation.

## Remarks

This function uses the following sequence of spherical linear interpolation operations:


```
Slerp(Slerp(pQ1, pC, t), Slerp(pA, pB, t), 2t(1 - t))
```



The return value for this function is the same value returned in the *pOut* parameter. In this way, the **D3DXQuaternionSquad** function can be used as a parameter for another function.

For an example of interpolating between quaternions, see the SkinnedMesh Sample. You can get this sample and learn about it from the DirectX SDK. For info about the DirectX SDK, see [Where is the DirectX SDK?](https://msdn.microsoft.com/d8765da9-e7cf-47e8-8bc3-4b29162da41b).

Use [**D3DXQuaternionNormalize**](d3dxquaternionnormalize.md) for any quaternion input that is not already normalized.

## Requirements



|                    |                                                                                        |
|--------------------|----------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>D3dx9math.h</dt> </dl> |
| Library<br/> | <dl> <dt>D3dx9.lib</dt> </dl>   |



## See also

<dl> <dt>

[Math Functions](dx9-graphics-reference-d3dx-functions-math.md)
</dt> <dt>

[**D3DXQuaternionExp**](d3dxquaternionexp.md)
</dt> <dt>

[**D3DXQuaternionLn**](d3dxquaternionln.md)
</dt> <dt>

[**D3DXQuaternionSquadSetup**](d3dxquaternionsquadsetup.md)
</dt> </dl>

 

 




