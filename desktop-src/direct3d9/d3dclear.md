---
description: These flags identify a surface to reset when calling Clear.
ms.assetid: 5d76e9a3-7afc-4db7-bffe-64bc7b9f83ac
title: D3DCLEAR
ms.topic: article
ms.date: 05/31/2018
---

# D3DCLEAR

These flags identify a surface to reset when calling [**Clear**](/windows/win32/api/d3d9helper/nf-d3d9helper-idirect3ddevice9-clear).



| \#define          | Description                                                                                                                                 |
|-------------------|---------------------------------------------------------------------------------------------------------------------------------------------|
| D3DCLEAR\_STENCIL | Clear the stencil buffer.                                                                                                                   |
| D3DCLEAR\_TARGET  | Clear a render target, or all targets in a multiple render target. See [Multiple Render Targets (Direct3D 9)](multiple-render-targets.md). |
| D3DCLEAR\_ZBUFFER | Clear the depth buffer.                                                                                                                     |



 

## Constant Information



| Requirement                         |  Value           |
|--------------------------|-------------|
| Header                   | d3d9types.h |
| Minimum operating system | Windows 98  |



 

## Related topics

<dl> <dt>

[Direct3D Constants](dx9-graphics-reference-d3d-constants.md)
</dt> </dl>

 

 
