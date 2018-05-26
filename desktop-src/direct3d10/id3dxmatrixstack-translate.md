---
Description: Determines the product of the current matrix and the computed translation matrix determined by the given factors (x, y, and z).
ms.assetid: d6e347a5-bb66-451d-b66e-49ea8eff70b3
title: ID3DXMATRIXStackTranslate method
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# ID3DXMATRIXStack::Translate method

Determines the product of the current matrix and the computed translation matrix determined by the given factors (x, y, and z).

## Syntax


```C++
HRESULT Translate(
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

The translation factor in the x-direction.

</dd> <dt>

*y* \[in\]
</dt> <dd>

Type: **[**FLOAT**](winprog.windows_data_types)**

The translation factor in the y-direction.

</dd> <dt>

*z* \[in\]
</dt> <dd>

Type: **[**FLOAT**](winprog.windows_data_types)**

The translation factor in the z-direction.

</dd> </dl>

## Return value

Type: **[**HRESULT**](455d07e9-52c3-4efb-a9dc-2955cbfd38cc)**

If the method succeeds, the return value is D3D\_OK.

## Remarks

This method right-multiplies the current matrix with the computed translation matrix (transformation is about the current world origin).


```
D3DXMATRIX tmp;
D3DXMatrixTranslation( &amp;tmp, x, y, z );
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

 

 




