---
description: Many C++ applications clear the depth buffer before rendering each new frame.
ms.assetid: b8930211-82a1-4808-b042-1641e567cb6d
title: Clearing Depth Buffers (Direct3D 9)
ms.topic: article
ms.date: 05/31/2018
---

# Clearing Depth Buffers (Direct3D 9)

Many C++ applications clear the depth buffer before rendering each new frame. You can explicitly clear the depth buffer through Direct3D by calling [**IDirect3DDevice9::Clear**](/windows/win32/api/d3d9helper/nf-d3d9helper-idirect3ddevice9-clear) and specifying D3DCLEAR\_ZBUFFER for the Flags parameter. The **IDirect3DDevice9::Clear** method allows you to specify an arbitrary depth value in the Z parameter.

## Related topics

<dl> <dt>

[Depth Buffers](depth-buffers.md)
</dt> </dl>

 

 
