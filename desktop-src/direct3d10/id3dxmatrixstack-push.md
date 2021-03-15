---
description: Adds a matrix to the stack.
ms.assetid: 8660047f-64bc-4b34-8270-3087412db942
title: ID3DXMATRIXStack::Push method (D3DX10.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- ID3DXMATRIXStack.Push
api_type: 
- COM
api_location: 
- D3DX10.lib
- D3DX10.dll
---

# ID3DXMATRIXStack::Push method (D3DX10.h)

Adds a matrix to the stack.

## Syntax


```C++
HRESULT Push();
```



## Parameters

This method has no parameters.

## Return value

Type: **[**HRESULT**](https://msdn.microsoft.com/library/Bb401631(v=MSDN.10).aspx)**

If the method succeeds, the return value is D3D\_OK. If the method fails, the return value can be D3DERR\_INVALIDCALL.

## Remarks

This method increments the count of items on the stack by 1, duplicating the current matrix. The stack will grow dynamically as more items are added.

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

 

 




