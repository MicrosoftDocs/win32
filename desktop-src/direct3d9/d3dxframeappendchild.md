---
Description: 'Adds a child frame to a frame.'
ms.assetid: 'a04c9bbe-8e54-467a-8e02-27c6469f4dac'
title: D3DXFrameAppendChild function
---

# D3DXFrameAppendChild function

Adds a child frame to a frame.

## Syntax


```C++
HRESULT D3DXFrameAppendChild(
  _In_       LPD3DXFRAME pFrameParent,
  _In_ const D3DXFRAME   *pFrameChild
);
```



## Parameters

<dl> <dt>

*pFrameParent* \[in\]
</dt> <dd>

Type: **[**LPD3DXFRAME**](d3dxframe.md)**

Pointer to the parent node.

</dd> <dt>

*pFrameChild* \[in\]
</dt> <dd>

Type: **const [**D3DXFRAME**](d3dxframe.md)\***

Pointer to the child node.

</dd> </dl>

## Return value

Type: **[**HRESULT**](455d07e9-52c3-4efb-a9dc-2955cbfd38cc)**

If the function succeeds, the return value is D3D\_OK. If the function fails, the return value can be one of the following values: D3DERR\_INVALIDCALL, E\_OUTOFMEMORY.

## Requirements



|                    |                                                                                        |
|--------------------|----------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>D3dx9anim.h</dt> </dl> |
| Library<br/> | <dl> <dt>D3dx9.lib</dt> </dl>   |



## See also

<dl> <dt>

[Animation Functions](dx9-graphics-reference-d3dx-functions-animation.md)
</dt> </dl>

 

 




