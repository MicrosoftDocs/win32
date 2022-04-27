---
description: ID3DXMATRIXStack interface - Applications use the methods of the ID3DXMATRIXStack interface to manipulate a matrix stack.
ms.assetid: 4d382d39-a9da-4a3b-b7b6-d6890357d467
title: ID3DXMATRIXStack interface (D3dx9math.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type:
- APIRef
- kbSyntax
api_name:
- ID3DXMATRIXStack
api_type:
- COM
api_location:
- d3dx9.lib
- d3dx9.dll
---

# ID3DXMATRIXStack interface

> [!Note]
> The math functions of the D3DX utility library are deprecated. We recommend that you use [DirectXMath](../dxmath/directxmath-portal.md) instead along with this header from [GitHub](https://github.com/microsoft/DirectXMath/tree/main/MatrixStack).

Applications use the methods of the ID3DXMATRIXStack interface to manipulate a matrix stack.

## Members

The **ID3DXMATRIXStack** interface inherits from the [**IUnknown**](/windows/win32/api/unknwn/nn-unknwn-iunknown) interface. **ID3DXMATRIXStack** also has these types of members:

-   [Methods](#methods)

### Methods

The **ID3DXMATRIXStack** interface has these methods.



| Method                                                                       | Description                                                                                                                                |
|:-----------------------------------------------------------------------------|:-------------------------------------------------------------------------------------------------------------------------------------------|
| [**GetTop**](id3dxmatrixstack--gettop.md)                                   | Retrieves the current matrix at the top of the stack.<br/>                                                                           |
| [**LoadIdentity**](id3dxmatrixstack--loadidentity.md)                       | Loads identity in the current matrix.<br/>                                                                                           |
| [**LoadMatrix**](id3dxmatrixstack--loadmatrix.md)                           | Loads the given matrix into the current matrix.<br/>                                                                                 |
| [**MultMatrix**](id3dxmatrixstack--multmatrix.md)                           | Determines the product of the current matrix and the given matrix.<br/>                                                              |
| [**MultMatrixLocal**](id3dxmatrixstack--multmatrixlocal.md)                 | Determines the product of the given matrix and the current matrix.<br/>                                                              |
| [**Pop**](id3dxmatrixstack--pop.md)                                         | Removes the current matrix from the top of the stack.<br/>                                                                           |
| [**Push**](id3dxmatrixstack--push.md)                                       | Adds a matrix to the stack.<br/>                                                                                                     |
| [**RotateAxis**](id3dxmatrixstack--rotateaxis.md)                           | Rotates (relative to world coordinate space) around an arbitrary axis.<br/>                                                          |
| [**RotateAxisLocal**](id3dxmatrixstack--rotateaxislocal.md)                 | Rotates (relative to the object's local coordinate space) around an arbitrary axis.<br/>                                             |
| [**RotateYawPitchRoll**](id3dxmatrixstack--rotateyawpitchroll.md)           | Rotates (relative to world coordinate space) around an arbitrary axis.<br/>                                                          |
| [**RotateYawPitchRollLocal**](id3dxmatrixstack--rotateyawpitchrolllocal.md) | Rotates (relative to the object's local coordinate space) around an arbitrary axis.<br/>                                             |
| [**Scale**](id3dxmatrixstack--scale.md)                                     | Scale the current matrix about the world coordinate origin.<br/>                                                                     |
| [**ScaleLocal**](id3dxmatrixstack--scalelocal.md)                           | Scale the current matrix about the object origin.<br/>                                                                               |
| [**Translate**](id3dxmatrixstack--translate.md)                             | Determines the product of the current matrix and the computed translation matrix determined by the given factors (x, y, and z).<br/> |
| [**TranslateLocal**](id3dxmatrixstack--translatelocal.md)                   | Determines the product of the computed translation matrix determined by the given factors (x, y, and z) and the current matrix.<br/> |



 

## Remarks

The **ID3DXMATRIXStack** interface is obtained by calling the [**D3DXCreateMatrixStack**](d3dxcreatematrixstack.md) function.

The LPD3DXMATRIXSTACK type is defined as a pointer to the **ID3DXMATRIXStack** interface.


```
typedef interface ID3DXMATRIXStack ID3DXMATRIXStack;
typedef interface ID3DXMATRIXStack *LPD3DXMATRIXSTACK;
```



## Requirements



| Requirement | Value |
|--------------------|----------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>D3dx9math.h</dt> </dl> |
| Library<br/> | <dl> <dt>D3dx9.lib</dt> </dl>   |



## See also

<dl> <dt>

[D3DX Interfaces](dx9-graphics-reference-d3dx-interfaces.md)
</dt> </dl>

 

 
