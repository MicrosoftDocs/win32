---
Description: Adds a matrix to the stack.
ms.assetid: 99bc636d-f1fd-4ace-a649-6a1a952927e0
title: ID3DXMATRIXStackPush method
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# ID3DXMATRIXStack::Push method

Adds a matrix to the stack.

## Syntax


```C++
HRESULT Push();
```



## Parameters

This method has no parameters.

## Return value

Type: **[**HRESULT**](455d07e9-52c3-4efb-a9dc-2955cbfd38cc)**

If the method succeeds, the return value is D3D\_OK. If the method fails, the return value can be D3DERR\_INVALIDCALL.

## Remarks

This method increments the count of items on the stack by 1, duplicating the current matrix. The stack will grow dynamically as more items are added.

## Requirements



|                    |                                                                                        |
|--------------------|----------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>D3dx9math.h</dt> </dl> |
| Library<br/> | <dl> <dt>D3dx9.lib</dt> </dl>   |



## See also

<dl> <dt>

[ID3DXMATRIXStack](id3dxmatrixstack.md)
</dt> <dt>

[**ID3DXMATRIXStack::GetTop**](id3dxmatrixstack--gettop.md)
</dt> <dt>

[**ID3DXMATRIXStack::Pop**](id3dxmatrixstack--pop.md)
</dt> </dl>

 

 




