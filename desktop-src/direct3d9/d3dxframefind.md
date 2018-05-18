---
Description: 'Finds the child frame of a root frame.'
ms.assetid: '211e117a-9707-459a-a6a1-b3e78bdad6e2'
title: D3DXFrameFind function
---

# D3DXFrameFind function

Finds the child frame of a root frame.

## Syntax


```C++
LPD3DXFRAME D3DXFrameFind(
  _In_ const D3DXFRAME *pFrameRoot,
  _In_       LPCSTR    Name
);
```



## Parameters

<dl> <dt>

*pFrameRoot* \[in\]
</dt> <dd>

Type: **const [**D3DXFRAME**](d3dxframe.md)\***

Pointer to the root frame. See [**D3DXFRAME**](d3dxframe.md).

</dd> <dt>

*Name* \[in\]
</dt> <dd>

Type: **[**LPCSTR**](winprog.windows_data_types)**

Name of the child frame to find.

</dd> </dl>

## Return value

Type: **[**LPD3DXFRAME**](d3dxframe.md)**

Returns the child frame if it is found, or **NULL** otherwise. See [**D3DXFRAME**](d3dxframe.md).

## Requirements



|                    |                                                                                        |
|--------------------|----------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>D3dx9anim.h</dt> </dl> |
| Library<br/> | <dl> <dt>D3dx9.lib</dt> </dl>   |



## See also

<dl> <dt>

[Animation Functions](dx9-graphics-reference-d3dx-functions-animation.md)
</dt> </dl>

 

 




