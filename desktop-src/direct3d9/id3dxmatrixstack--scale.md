---
description: ID3DXMATRIXStack::Scale method (D3dx9math.h) - Scale the current matrix about the world coordinate origin.
ms.assetid: 6c4ef625-736e-41a0-8a79-4d71e8685754
title: ID3DXMATRIXStack::Scale method (D3dx9math.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type:
- APIRef
- kbSyntax
api_name:
- ID3DXMATRIXStack.Scale
api_type:
- COM
api_location:
- d3dx9.lib
- d3dx9.dll
---

# ID3DXMATRIXStack::Scale method (D3dx9math.h)

> [!Note]
> The math functions of the D3DX utility library are deprecated. We recommend that you use [DirectXMath](../dxmath/directxmath-portal.md) instead along with this header from [GitHub](https://github.com/microsoft/DirectXMath/tree/main/MatrixStack).

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

Type: **[**FLOAT**](../winprog/windows-data-types.md)**

The scaling component in the x-direction.

</dd> <dt>

*y* \[in\]
</dt> <dd>

Type: **[**FLOAT**](../winprog/windows-data-types.md)**

The scaling component in the y-direction.

</dd> <dt>

*z* \[in\]
</dt> <dd>

Type: **[**FLOAT**](../winprog/windows-data-types.md)**

The scaling component in the z-direction.

</dd> </dl>

## Return value

Type: **[**HRESULT**](https://msdn.microsoft.com/library/Bb401631(v=MSDN.10).aspx)**

If the method succeeds, the return value is D3D\_OK.

## Remarks

This method right-multiplies the current matrix with the computed scale matrix. The transformation is about the current world origin.


```
D3DXMATRIX tmp;
D3DXMatrixScaling(&tmp, x, y, z);
m_stack[m_currentPos] = m_stack[m_currentPos] * tmp;
```



## Requirements



| Requirement | Value |
|--------------------|----------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>D3dx9math.h</dt> </dl> |
| Library<br/> | <dl> <dt>D3dx9.lib</dt> </dl>   |



## See also

<dl> <dt>

[ID3DXMATRIXStack](id3dxmatrixstack.md)
</dt> <dt>

[**ID3DXMATRIXStack::ScaleLocal**](id3dxmatrixstack--scalelocal.md)
</dt> </dl>

 

 
