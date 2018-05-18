---
Description: 'Removes the current matrix from the top of the stack.'
ms.assetid: '4c542012-058a-4818-8ec4-27e7d3357ca3'
title: 'ID3DXMATRIXStack::Pop method'
---

# ID3DXMATRIXStack::Pop method

Removes the current matrix from the top of the stack.

## Syntax


```C++
HRESULT Pop();
```



## Parameters

This method has no parameters.

## Return value

Type: **[**HRESULT**](455d07e9-52c3-4efb-a9dc-2955cbfd38cc)**

If the method succeeds, the return value is D3D\_OK.

## Remarks

Note that this method decrements the count of items on the stack by 1, effectively removing the current matrix from the top of the stack and promoting a matrix to the top of the stack. If the current count of items on the stack is 0, then this method returns without performing any action. If the current count of items on the stack is 1, then this method empties the stack.

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

[**ID3DXMATRIXStack::Push**](id3dxmatrixstack--push.md)
</dt> </dl>

 

 




