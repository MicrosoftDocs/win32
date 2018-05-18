---
Description: 'Rotates (relative to world coordinate space) around an arbitrary axis.'
ms.assetid: '35e237f6-40f2-4001-adb0-f489d61f64e7'
title: 'ID3DXMATRIXStack::RotateYawPitchRoll method'
---

# ID3DXMATRIXStack::RotateYawPitchRoll method

Rotates (relative to world coordinate space) around an arbitrary axis.

## Syntax


```C++
HRESULT RotateYawPitchRoll(
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
m_stack[m_currentPos] = m_stack[m_currentPos] * tmp;
```



Because the rotation is right-multiplied to the matrix stack, the rotation is relative to world coordinate space.

## Requirements



|                    |                                                                                       |
|--------------------|---------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>D3DX10.h</dt> </dl>   |
| Library<br/> | <dl> <dt>D3DX10.lib</dt> </dl> |



## See also

<dl> <dt>

[ID3DXMatrixStack](d3d10-id3dxmatrixstack.md)
</dt> <dt>

[D3DX Interfaces](d3d10-graphics-reference-d3dx10-interfaces.md)
</dt> </dl>

 

 




