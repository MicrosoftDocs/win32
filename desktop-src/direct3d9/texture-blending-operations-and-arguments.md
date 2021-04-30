---
description: Applications associate a blending stage with each texture in the set of current textures. Direct3D evaluates each blending stage in order, beginning with the first texture in the set and ending with the eighth.
ms.assetid: 3b7faefd-30be-4f74-b0f7-621d65130286
title: Texture Blending Operations and Arguments (Direct3D 9)
ms.topic: article
ms.date: 05/31/2018
---

# Texture Blending Operations and Arguments (Direct3D 9)

Applications associate a blending stage with each texture in the set of current textures. Direct3D evaluates each blending stage in order, beginning with the first texture in the set and ending with the eighth.

Direct3D applies the information from each texture in the set of current textures to the blending stage that is associated with it. Applications control what information from a texture stage is used by calling [**IDirect3DDevice9::SetTextureStageState**](/windows/desktop/api). You can set separate operations for the color and alpha channels, and each operation uses two arguments. Specify color channel operations by using the D3DTSS\_COLOROP stage state; specify alpha operations by using D3DTSS\_ALPHAOP. Both stage states use values from the [**D3DTEXTUREOP**](./d3dtextureop.md) enumerated type.

Texture blending arguments use the D3DTSS\_COLORARG1, D3DTSS\_COLORARG2, D3DTSS\_ALPHARG1, and D3DTSS\_ALPHARG2 members of the [**D3DTEXTURESTAGESTATETYPE**](./d3dtexturestagestatetype.md) enumerated type. The corresponding argument values are identified using [D3DTA](d3dta.md).

> [!Note]  
> You can disable a texture stage - and any subsequent texture blending stages in the cascade - by setting the color operation for that stage to D3DTOP\_DISABLE. Disabling the color operation effectively disables the alpha operation as well. Alpha operations cannot be disabled when color operations are enabled. Setting the alpha operation to D3DTOP\_DISABLE when color blending is enabled causes undefined behavior.

 

To determine the supported texture blending operations of a device, query the TextureCaps member of the [**D3DCAPS9**](/windows/desktop/api/D3D9Caps/ns-d3d9caps-d3dcaps9) structure.

## Related topics

<dl> <dt>

[Texture Blending](texture-blending.md)
</dt> </dl>

 

 
