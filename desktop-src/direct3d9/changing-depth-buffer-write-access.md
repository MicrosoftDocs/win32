---
description: By default, the Direct3D system is allowed to write to the depth buffer. Most applications leave writing to the depth buffer enabled, but you can achieve some special effects by not allowing the Direct3D system to write to the depth buffer.
ms.assetid: d426ebff-bfce-4e5b-a97b-7b2539b4a9de
title: Changing Depth Buffer Write Access (Direct3D 9)
ms.topic: article
ms.date: 05/31/2018
---

# Changing Depth Buffer Write Access (Direct3D 9)

By default, the Direct3D system is allowed to write to the depth buffer. Most applications leave writing to the depth buffer enabled, but you can achieve some special effects by not allowing the Direct3D system to write to the depth buffer.

You can disable depth buffer writes in C++ by calling the [**IDirect3DDevice9::SetRenderState**](/windows/win32/api/d3d9helper/nf-d3d9helper-idirect3ddevice9-setrenderstate) method with the State parameter set to D3DRS\_ZWRITEENABLE and the Value parameter set to 0.

## Related topics

<dl> <dt>

[Depth Buffers](depth-buffers.md)
</dt> </dl>

 

 
