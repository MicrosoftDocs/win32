---
description: Direct3D maintains a list of up to eight current textures. It blends these textures onto all the primitive it renders. Only textures created as texture interface pointers can be used in the set of current textures.
ms.assetid: 5a58c915-7b67-45a7-9493-6657c75aaa10
title: Assigning the Current Textures (Direct3D 9)
ms.topic: article
ms.date: 05/31/2018
---

# Assigning the Current Textures (Direct3D 9)

Direct3D maintains a list of up to eight current textures. It blends these textures onto all the primitive it renders. Only textures created as texture interface pointers can be used in the set of current textures.

Applications call the [**IDirect3DDevice9::SetTexture**](/windows/win32/api/d3d9helper/nf-d3d9helper-idirect3ddevice9-settexture) method to assign textures into the set of current textures. The first parameter must be a number in the range of 0-7, inclusive. Pass the texture interface pointer as the second parameter.

The following C++ code example demonstrates how a texture can be assigned to the set of current textures.


```
// This code example assumes that the variable lpd3dDev is a
// valid pointer to an IDirect3DDevice9 interface and pTexture
// is a valid pointer to an IDirect3DBaseTexture9 interface.

// Set the third texture.
d3dDevice->SetTexture(2, pTexture);
```



> [!Note]  
> Software devices do not support assigning a texture to more than one texture stage at a time.

 

## Related topics

<dl> <dt>

[Texture Blending](texture-blending.md)
</dt> </dl>

 

 
