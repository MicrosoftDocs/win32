---
description: ID3DXMATRIXStack::RotateYawPitchRollLocal method (D3dx9math.h) - Rotates (relative to the object's local coordinate space) around an arbitrary axis.
ms.assetid: c69f5ea7-5d14-4187-9405-1ceff8230185
title: ID3DXMATRIXStack::RotateYawPitchRollLocal method (D3dx9math.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type:
- APIRef
- kbSyntax
api_name:
- ID3DXMATRIXStack.RotateYawPitchRollLocal
api_type:
- COM
api_location:
- d3dx9.lib
- d3dx9.dll
---

# ID3DXMATRIXStack::RotateYawPitchRollLocal method (D3dx9math.h)

> [!Note]
> The math functions of the D3DX utility library are deprecated. We recommend that you use [DirectXMath](../dxmath/directxmath-portal.md) instead along with this header from [GitHub](https://github.com/microsoft/DirectXMath/tree/main/MatrixStack).

Rotates (relative to the object's local coordinate space) around an arbitrary axis.

## Syntax


```C++
HRESULT RotateYawPitchRollLocal(
  [in] FLOAT Yaw,
  [in] FLOAT Pitch,
  [in] FLOAT Roll
);
```



## Parameters

<dl> <dt>

*Yaw* \[in\]
</dt> <dd>

Type: **[**FLOAT**](../winprog/windows-data-types.md)**

The yaw around the y-axis in radians.

</dd> <dt>

*Pitch* \[in\]
</dt> <dd>

Type: **[**FLOAT**](../winprog/windows-data-types.md)**

The pitch around the x-axis in radians.

</dd> <dt>

*Roll* \[in\]
</dt> <dd>

Type: **[**FLOAT**](../winprog/windows-data-types.md)**

The roll around the z-axis in radians.

</dd> </dl>

## Return value

Type: **[**HRESULT**](https://msdn.microsoft.com/library/Bb401631(v=MSDN.10).aspx)**

If the method succeeds, the return value is D3D\_OK.

## Remarks

This method adds the rotation to the matrix stack with the computed rotation matrix similar to the following:


```
D3DXMATRIX tmp;
D3DXMatrixRotationYawPitchRoll( &tmp, yaw, pitch, roll );
m_stack[m_currentPos] = tmp * m_stack[m_currentPos];
```



Because the rotation is left-multiplied to the matrix stack, the rotation is relative to the object's local coordinate space.

## Requirements



| Requirement | Value |
|--------------------|----------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>D3dx9math.h</dt> </dl> |
| Library<br/> | <dl> <dt>D3dx9.lib</dt> </dl>   |



## See also

<dl> <dt>

[ID3DXMATRIXStack](id3dxmatrixstack.md)
</dt> <dt>

[**D3DXMatrixRotationAxis**](d3dxmatrixrotationaxis.md)
</dt> <dt>

[**ID3DXMATRIXStack::RotateAxis**](id3dxmatrixstack--rotateaxis.md)
</dt> <dt>

[**ID3DXMATRIXStack::RotateAxisLocal**](id3dxmatrixstack--rotateaxislocal.md)
</dt> <dt>

[**ID3DXMATRIXStack::RotateYawPitchRoll**](id3dxmatrixstack--rotateyawpitchroll.md)
</dt> </dl>

 

 
