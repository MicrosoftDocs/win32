---
Description: Given a frame hierarchy, registers all the named matrices in the animation mixer.
ms.assetid: df0560c2-4417-4d54-94c8-031521b32189
title: D3DXFrameRegisterNamedMatrices function
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# D3DXFrameRegisterNamedMatrices function

Given a frame hierarchy, registers all the named matrices in the animation mixer.

## Syntax


```C++
HRESULT D3DXFrameRegisterNamedMatrices(
  _In_ LPD3DXFRAME               pFrameRoot,
  _In_ LPD3DXANIMATIONCONTROLLER pAnimController
);
```



## Parameters

<dl> <dt>

*pFrameRoot* \[in\]
</dt> <dd>

Type: **[**LPD3DXFRAME**](d3dxframe.md)**

The top level node in the frame hierarchy.

</dd> <dt>

*pAnimController* \[in\]
</dt> <dd>

Type: **[**LPD3DXANIMATIONCONTROLLER**](id3dxanimationcontroller.md)**

Pointer to the animation controller object.

</dd> </dl>

## Return value

Type: **[**HRESULT**](https://msdn.microsoft.com/windows/desktop/455d07e9-52c3-4efb-a9dc-2955cbfd38cc)**

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

 

 




