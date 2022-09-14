---
description: Texture management is the process of determining which textures are needed for rendering at a given time and ensuring that those textures are loaded into video memory.
ms.assetid: ea6d64ee-f570-49eb-b5fd-67fcde3f8ddc
title: Automatic Texture Management (Direct3D 9)
ms.topic: article
ms.date: 05/31/2018
---

# Automatic Texture Management (Direct3D 9)

Texture management is the process of determining which textures are needed for rendering at a given time and ensuring that those textures are loaded into video memory. As with any algorithm, texture management schemes vary in complexity, but any approach to texture management involves the following key tasks.

-   Tracking the amount of available texture memory.
-   Calculating which textures are needed for rendering, and which are not.
-   Determining which existing texture resources can be reloaded with another texture image, and which surfaces should be destroyed and replaced with new texture resources.

Direct3D implements system-supported texture management to ensure that textures are loaded for optimal performance. Texture resources that Direct3D manages are referred to as managed textures.

The texture manager tracks textures with a time-stamp that identifies when the texture was last used. It then uses a least-recently-used algorithm to determine which textures should be removed. Texture priorities are used as tie breakers when two textures are targeted for removal from memory. If two textures have the same priority value, the least-recently-used texture is removed. However, if two textures have the same time-stamp, the texture that has a lower priority is removed first.

You request automatic texture management for texture surfaces when you create them. To retrieve a managed texture in a C++ application, create a texture resource by calling [**IDirect3DDevice9::CreateTexture**](/windows/win32/api/d3d9helper/nf-d3d9helper-idirect3ddevice9-createtexture) and specifying the D3DPOOL\_MANAGED for the Pool parameter. You are not allowed to specify where you want the texture created. You cannot use the D3DPOOL\_DEFAULT or D3DPOOL\_SYSTEMMEM flags when creating a managed texture. After creating the managed texture, you can call the [**IDirect3DDevice9::SetTexture**](/windows/win32/api/d3d9helper/nf-d3d9helper-idirect3ddevice9-settexture) method to set it to a stage in the rendering device's texture cascade.

You can assign a priority to managed textures by calling the [**IDirect3DResource9::SetPriority**](/windows/win32/api/d3d9helper/nf-d3d9helper-idirect3dresource9-setpriority) method for the texture surface.

Direct3D automatically downloads textures into video memory as needed. The system might cache managed textures in local or nonlocal video memory, depending on the availability of nonlocal video memory or other factors. The cache location of your managed textures is not communicated to your application, nor is this information required to use automatic texture management. If your application uses more textures than can fit in video memory, Direct3D removes older textures from video memory to make room for the new textures. If you use a removed texture again, the system uses the original system-memory texture surface to reload the texture in the video-memory cache. Although reloading the texture is necessary, it also decreases the application's performance.

You can dynamically modify the original system-memory copy of the texture by updating or locking the texture resource. When the system detects a dirty surface - after an update is completed, or when the surface is unlocked - the texture manager automatically updates the video-memory copy of the texture. The performance hit incurred is similar to reloading a removed texture.

When entering a new level in a game, your application might need to flush all managed textures from video memory (by calling [**IDirect3DDevice9::EvictManagedResources**](/windows/win32/api/d3d9helper/nf-d3d9helper-idirect3ddevice9-evictmanagedresources)).

For more information about resource management, see [Managing Resources (Direct3D 9)](managing-resources.md).

## Related topics

<dl> <dt>

[Direct3D Textures](direct3d-textures.md)
</dt> </dl>

 

 
