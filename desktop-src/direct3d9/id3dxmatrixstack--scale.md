---
Description: Scale the current matrix about the world coordinate origin.
ms.assetid: 6c4ef625-736e-41a0-8a79-4d71e8685754
title: ID3DXMATRIXStackScale method
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
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



|                    |                                                                                        |
|--------------------|----------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>D3dx9math.h</dt> </dl> |
| Library<br/> | <dl> <dt>D3dx9.lib</dt> </dl>   |



## See also

<dl> <dt>

[ID3DXMATRIXStack](id3dxmatrixstack.md)
</dt> <dt>

[**ID3DXMATRIXStack::ScaleLocal**](id3dxmatrixstack--scalelocal.md)
</dt> </dl>

 

 




