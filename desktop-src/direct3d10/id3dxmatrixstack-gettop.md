---
description: Retrieves the current matrix at the top of the stack.
ms.assetid: cf379742-3e7d-4309-a7af-b97348428682
title: ID3DXMATRIXStack::GetTop method (D3DX10.h)
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
- D3DX10.lib
- D3DX10.dll
---

# ID3DXMATRIXStack::GetTop method (D3DX10.h)

Retrieves the current matrix at the top of the stack.

## Syntax


```C++
D3DXMATRIX* GetTop();
```



## Parameters

This method has no parameters.

## Return value

Type: **[**D3DXMATRIX**](../direct3d9/d3dxmatrix.md)\***

This method returns a pointer to a D3DXMATRIX structure representing the current matrix.

## Remarks

The D3DXMATRIX pointer returned by this method is not guaranteed to be valid after subsequent stack operations.

Note that this method does not remove the current matrix from the top of the stack; rather, it just returns the current matrix.

## Requirements



| Requirement | Value |
|--------------------|---------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>D3DX10.h</dt> </dl>   |
| Library<br/> | <dl> <dt>D3DX10.lib</dt> </dl> |



## See also

<dl> <dt>

[ID3DXMatrixStack](d3d10-id3dxmatrixstack.md)
</dt> <dt>

[D3DX Interfaces](d3d10-graphics-reference-d3dx10-interfaces.md)
</dt> </dl>

 

 
