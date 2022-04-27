---
description: ID3DXMATRIXStack::Pop method (D3dx9math.h) - Removes the current matrix from the top of the stack.
ms.assetid: 4c542012-058a-4818-8ec4-27e7d3357ca3
title: ID3DXMATRIXStack::Pop method (D3dx9math.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type:
- APIRef
- kbSyntax
api_name:
- ID3DXMATRIXStack.Pop
api_type:
- COM
api_location:
- d3dx9.lib
- d3dx9.dll
---

# ID3DXMATRIXStack::Pop method (D3dx9math.h)

> [!Note]
> The math functions of the D3DX utility library are deprecated. We recommend that you use [DirectXMath](../dxmath/directxmath-portal.md) instead along with this header from [GitHub](https://github.com/microsoft/DirectXMath/tree/main/MatrixStack).

Removes the current matrix from the top of the stack.

## Syntax


```C++
HRESULT Pop();
```



## Parameters

This method has no parameters.

## Return value

Type: **[**HRESULT**](https://msdn.microsoft.com/library/Bb401631(v=MSDN.10).aspx)**

If the method succeeds, the return value is D3D\_OK.

## Remarks

Note that this method decrements the count of items on the stack by 1, effectively removing the current matrix from the top of the stack and promoting a matrix to the top of the stack. If the current count of items on the stack is 0, then this method returns without performing any action. If the current count of items on the stack is 1, then this method empties the stack.

## Requirements



| Requirement | Value |
|--------------------|----------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>D3dx9math.h</dt> </dl> |
| Library<br/> | <dl> <dt>D3dx9.lib</dt> </dl>   |



## See also

<dl> <dt>

[ID3DXMATRIXStack](id3dxmatrixstack.md)
</dt> <dt>

[**ID3DXMATRIXStack::GetTop**](id3dxmatrixstack--gettop.md)
</dt> <dt>

[**ID3DXMATRIXStack::Push**](id3dxmatrixstack--push.md)
</dt> </dl>

 

 
