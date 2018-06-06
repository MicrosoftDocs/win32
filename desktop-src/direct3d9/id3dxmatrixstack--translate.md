---
Description: Determines the product of the current matrix and the computed translation matrix determined by the given factors (x, y, and z).
ms.assetid: e0ac72a2-9970-433e-9026-aa79edc8261c
title: ID3DXMATRIXStack::Translate method
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
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

Type: **[**FLOAT**](https://msdn.microsoft.com/4553cafc-450e-4493-a4d4-cb6e2f274d46)**

The translation factor in the x-direction.

</dd> <dt>

*y* \[in\]
</dt> <dd>

Type: **[**FLOAT**](https://msdn.microsoft.com/4553cafc-450e-4493-a4d4-cb6e2f274d46)**

The translation factor in the y-direction.

</dd> <dt>

*z* \[in\]
</dt> <dd>

Type: **[**FLOAT**](https://msdn.microsoft.com/4553cafc-450e-4493-a4d4-cb6e2f274d46)**

The translation factor in the z-direction.

</dd> </dl>

## Return value

Type: **[**HRESULT**](https://msdn.microsoft.com/windows/desktop/455d07e9-52c3-4efb-a9dc-2955cbfd38cc)**

If the method succeeds, the return value is D3D\_OK.

## Remarks

This method right-multiplies the current matrix with the computed translation matrix (transformation is about the current world origin).


```
D3DXMATRIX tmp;
D3DXMatrixTranslation( &amp;tmp, x, y, z );
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

[**ID3DXMATRIXStack::TranslateLocal**](id3dxmatrixstack--translatelocal.md)
</dt> </dl>

 

 




