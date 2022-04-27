---
description: ID3DXMATRIXStack::RotateAxisLocal method (D3DX10.h) - Rotates (relative to the object's local coordinate space) around an arbitrary axis.
ms.assetid: 90837762-9bfe-4065-94b3-1ca61184a78e
title: ID3DXMATRIXStack::RotateAxisLocal method (D3DX10.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type:
- APIRef
- kbSyntax
api_name:
- ID3DXMATRIXStack.RotateAxisLocal
api_type:
- COM
api_location:
- D3DX10.lib
- D3DX10.dll
---

# ID3DXMATRIXStack::RotateAxisLocal method (D3DX10.h)

> [!Note]
> The math functions of the D3DX utility library are deprecated. We recommend that you use [DirectXMath](../dxmath/directxmath-portal.md) instead along with this header from [GitHub](https://github.com/microsoft/DirectXMath/tree/main/MatrixStack).

Rotates (relative to the object's local coordinate space) around an arbitrary axis.

## Syntax


```C++
HRESULT RotateAxisLocal(
  [in] const D3DXVECTOR3 *pV,
  [in]       FLOAT       Angle
);
```



## Parameters

<dl> <dt>

*pV* \[in\]
</dt> <dd>

Type: **const [**D3DXVECTOR3**](../direct3d9/d3dxvector3.md)\***

Pointer to the arbitrary axis of rotation. See [**D3DXVECTOR3**](d3d10-d3dxvector3.md).

</dd> <dt>

*Angle* \[in\]
</dt> <dd>

Type: **[**FLOAT**](../winprog/windows-data-types.md)**

Rotation angle about the arbitrary axis, in radians. Angles are measured counterclockwise when looking along the arbitrary axis toward the origin.

</dd> </dl>

## Return value

Type: **[**HRESULT**](https://msdn.microsoft.com/library/Bb401631(v=MSDN.10).aspx)**

If the method succeeds, the return value is D3D\_OK. If the method fails, the return value can be D3DERR\_INVALIDCALL.

## Remarks

This method adds the rotation to the matrix stack with the computed rotation matrix similar to the following:


```
D3DXMATRIX tmp;
D3DXMatrixRotationAxis( &tmp, pV, angle );
m_stack[m_currentPos] = tmp * m_stack[m_currentPos];
```



Because the rotation is left-multiplied to the matrix stack, the rotation is relative to the object's local coordinate space.

## Requirements



| Requirement | Value |
|--------------------|---------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>D3DX10.h</dt> </dl>   |
| Library<br/> | <dl> <dt>D3DX10.lib</dt> </dl> |



## See also

<dl> <dt>

[ID3DXMatrixStack](d3d10-id3dxmatrixstack.md)
</dt> <dt>

[D3DX Interfaces](d3d10-graphics-reference-d3dx10-interfaces.md)
</dt> </dl>

 

 
