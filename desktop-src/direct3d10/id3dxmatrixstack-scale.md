---
Description: 'Scale the current matrix about the world coordinate origin.'
ms.assetid: 'd0f4b341-b3b6-42e4-84df-78f203c3728e'
title: 'ID3DXMATRIXStack::Scale method'
---

# ID3DXMATRIXStack::Scale method

Scale the current matrix about the world coordinate origin.

## Syntax


```C++
HRESULT Scale(
  [in] FLOAT x,
  [in] FLOAT y,
  [in] FLOAT z
);
```



## Parameters

<dl> <dt>

*x* \[in\]
</dt> <dd>

Type: **[**FLOAT**](winprog.windows_data_types)**

The scaling component in the x-direction.

</dd> <dt>

*y* \[in\]
</dt> <dd>

Type: **[**FLOAT**](winprog.windows_data_types)**

The scaling component in the y-direction.

</dd> <dt>

*z* \[in\]
</dt> <dd>

Type: **[**FLOAT**](winprog.windows_data_types)**

The scaling component in the z-direction.

</dd> </dl>

## Return value

Type: **[**HRESULT**](455d07e9-52c3-4efb-a9dc-2955cbfd38cc)**

If the method succeeds, the return value is D3D\_OK.

## Remarks

This method right-multiplies the current matrix with the computed scale matrix. The transformation is about the current world origin.


```
D3DXMATRIX tmp;
D3DXMatrixScaling(&amp;tmp, x, y, z);
m_stack[m_currentPos] = m_stack[m_currentPos] * tmp;
```



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

 

 




