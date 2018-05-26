---
Description: Destroys the subtree of frames under the root, including the root.
ms.assetid: 0bbb529f-01d8-430b-a72b-4af5f7a71253
title: D3DXFrameDestroy function
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# D3DXFrameDestroy function

Destroys the subtree of frames under the root, including the root.

## Syntax


```C++
HRESULT D3DXFrameDestroy(
  _In_ LPD3DXFRAME             pFrameRoot,
  _In_ LPD3DXALLOCATEHIERARCHY pAlloc
);
```



## Parameters

<dl> <dt>

*pFrameRoot* \[in\]
</dt> <dd>

Type: **[**LPD3DXFRAME**](d3dxframe.md)**

Pointer to the root node.

</dd> <dt>

*pAlloc* \[in\]
</dt> <dd>

Type: **[**LPD3DXALLOCATEHIERARCHY**](id3dxallocatehierarchy.md)**

Allocation interface used to deallocate nodes of the frame hierarchy.

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

 

 




