---
Description: 'Rotates (relative to the object''s local coordinate space) around an arbitrary axis.'
ms.assetid: 'c69f5ea7-5d14-4187-9405-1ceff8230185'
title: 'ID3DXMATRIXStack::RotateYawPitchRollLocal method'
---

# ID3DXMATRIXStack::RotateYawPitchRollLocal method

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

Type: **[**FLOAT**](winprog.windows_data_types)**

The yaw around the y-axis in radians.

</dd> <dt>

*Pitch* \[in\]
</dt> <dd>

Type: **[**FLOAT**](winprog.windows_data_types)**

The pitch around the x-axis in radians.

</dd> <dt>

*Roll* \[in\]
</dt> <dd>

Type: **[**FLOAT**](winprog.windows_data_types)**

The roll around the z-axis in radians.

</dd> </dl>

## Return value

Type: **[**HRESULT**](455d07e9-52c3-4efb-a9dc-2955cbfd38cc)**

If the method succeeds, the return value is D3D\_OK.

## Remarks

This method adds the rotation to the matrix stack with the computed rotation matrix similar to the following:


```
D3DXMATRIX tmp;
D3DXMatrixRotationYawPitchRoll( &amp;tmp, yaw, pitch, roll );
m_stack[m_currentPos] = tmp * m_stack[m_currentPos];
```



Because the rotation is left-multiplied to the matrix stack, the rotation is relative to the object's local coordinate space.

## Requirements



|                    |                                                                                        |
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

 

 




