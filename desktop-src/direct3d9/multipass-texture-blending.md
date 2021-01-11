---
description: Direct3D applications can achieve numerous special effects by applying various textures to a primitive over the course of multiple rendering passes.
ms.assetid: 884cc928-305e-46b9-acbf-ca58dfbc05e6
title: Multipass Texture Blending (Direct3D 9)
ms.topic: article
ms.date: 05/31/2018
---

# Multipass Texture Blending (Direct3D 9)

Direct3D applications can achieve numerous special effects by applying various textures to a primitive over the course of multiple rendering passes. The common term for this is multipass texture blending. A typical use for multipass texture blending is to emulate the effects of complex lighting and shading models by applying multiple colors from several different textures. One such application is called light mapping. For more information, see [Light Mapping with Textures (Direct3D 9)](light-mapping-with-textures.md).

> [!Note]  
> Some devices are capable of applying multiple textures to primitives in a single pass. For details, see [Texture Blending (Direct3D 9)](texture-blending.md).

 

If the user's hardware does not support multiple texture blending, your application can use multipass texture blending to achieve the same visual effects. However, the application cannot sustain the frame rates that are possible when using multiple texture blending.

To perform multipass texture blending in a C/C++ application.

1.  Set a texture in texture stage 0 by calling the [**IDirect3DDevice9::SetTexture**](/windows/win32/api/d3d9helper/nf-d3d9helper-idirect3ddevice9-settexture) method.
2.  Select the desired color and alpha blending arguments and operations with the [**IDirect3DDevice9::SetTextureStageState**](/windows/win32/api/d3d9helper/nf-d3d9helper-idirect3ddevice9-settexturestagestate) method. The default settings are well-suited for multipass texture blending.
3.  Render the appropriate objects in the scene.
4.  Set the next texture in texture stage 0.
5.  Set the D3DRS\_SRCBLEND and D3DRS\_DESTBLEND render states to adjust the source and destination blending factors as needed. The system blends the new textures with the existing pixels in the render-target surface according to these parameters.
6.  Repeat Steps 3, 4, and 5 with as many textures as needed.

## Related topics

<dl> <dt>

[Texture Blending](texture-blending.md)
</dt> </dl>

 

 
