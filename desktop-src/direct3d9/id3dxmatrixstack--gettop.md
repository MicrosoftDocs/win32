---
description: ID3DXMATRIXStack::GetTop method (D3dx9math.h) - Retrieves the current matrix at the top of the stack.
ms.assetid: 0e20af0a-a332-4cb5-bf87-2ec75aa170ab
title: ID3DXMATRIXStack::GetTop method (D3dx9math.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- ID3DXMATRIXStack.GetTop
api_type: 
- COM
api_location: 
- d3dx9.lib
- d3dx9.dll
---

# ID3DXMATRIXStack::GetTop method (D3dx9math.h)

Retrieves the current matrix at the top of the stack.

## Syntax


```C++
D3DXMATRIX* GetTop();
```



## Parameters

This method has no parameters.

## Return value

Type: **[**D3DXMATRIX**](d3dxmatrix.md)\***

This method returns a pointer to a [**D3DXMATRIX**](d3dxmatrix.md) structure representing the current matrix.

## Remarks

The [**D3DXMATRIX**](d3dxmatrix.md) pointer returned by this method is not guaranteed to be valid after subsequent stack operations.

Note that this method does not remove the current matrix from the top of the stack; rather, it just returns the current matrix.

## Requirements



| Requirement | Value |
|--------------------|----------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>D3dx9math.h</dt> </dl> |
| Library<br/> | <dl> <dt>D3dx9.lib</dt> </dl>   |



## See also

<dl> <dt>

[ID3DXMATRIXStack](id3dxmatrixstack.md)
</dt> <dt>

[**ID3DXMATRIXStack::Pop**](id3dxmatrixstack--pop.md)
</dt> <dt>

[**ID3DXMATRIXStack::Push**](id3dxmatrixstack--push.md)
</dt> </dl>

 

 




