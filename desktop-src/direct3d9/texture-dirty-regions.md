---
Description: 'Applications can optimize which subset of a texture is copied by specifying &\#0034;dirty&\#0034; regions on textures.'
ms.assetid: '102081bc-d5d5-4ec1-b935-00d4eda8f470'
title: 'Texture Dirty Regions (Direct3D 9)'
---

# Texture Dirty Regions (Direct3D 9)

Applications can optimize which subset of a texture is copied by specifying "dirty" regions on textures. Only those regions marked as dirty are copied by a call to [**IDirect3DDevice9::UpdateTexture**](idirect3ddevice9--updatetexture.md). However, the dirty regions may be expanded to optimize alignment. When a texture is created, the entire texture is considered dirty. Only the following operations affect the dirty state of a texture:

-   Adding a dirty region to a texture.
-   Locking some buffer in the texture. This operation adds the locked region as a dirty region. The application can turn off this automatic dirty region update if it has better knowledge of the actual dirty regions.
-   Using a surface level of the texture as a destination in [**IDirect3DDevice9::UpdateSurface**](idirect3ddevice9--updatesurface.md) marks the entire texture as dirty.
-   Using the texture as a source in [**IDirect3DDevice9::UpdateTexture**](idirect3ddevice9--updatetexture.md) clears all the dirty regions on the source texture.
-   Using [**IDirect3DSurface9::GetDC**](idirect3dsurface9--getdc.md) to return a device context.
-   Calling [**IDirect3DBaseTexture9::GenerateMipSubLevels**](idirect3dbasetexture9--generatemipsublevels.md) marks the entire texture as dirty.
-   Calling [**IDirect3DBaseTexture9::SetAutoGenFilterType**](idirect3dbasetexture9--setautogenfiltertype.md) marks the entire texture as dirty.

Dirty regions are set on the top level of a mipmapped texture, and [**IDirect3DDevice9::UpdateTexture**](idirect3ddevice9--updatetexture.md) can expand the dirty region down the mip chain in order to minimize the number of bytes copied for each sublevel. Note that the sublevel dirty region coordinates are rounded outward, that is, their fractional parts are rounded toward the nearest edge of the texture.

Because each type of texture has different types of dirty regions, there are methods on each texture type. 2D textures use dirty rectangle, and volume textures use boxes.

-   [**IDirect3DCubeTexture9::AddDirtyRect**](idirect3dcubetexture9--adddirtyrect.md)
-   [**IDirect3DTexture9::AddDirtyRect**](idirect3dtexture9--adddirtyrect.md)
-   [**IDirect3DVolumeTexture9::AddDirtyBox**](idirect3dvolumetexture9--adddirtybox.md)

Passing **NULL** for the pDirtyRect or pDirtyBox parameters for the above methods expands the dirty region to cover the entire texture.

Each lock method can take D3DLOCK\_NO\_DIRTY\_UPDATE, which prevents any changes to the dirty state of the texture. For more information, see [Locking Resources (Direct3D 9)](locking-resources.md).

When more information about the true set of regions that are changed during a lock operation is available, applications should use D3DLOCK\_NO\_DIRTY\_UPDATE. Note that a lock or a copy to a texture sublevel only (that is, without locking or copying to the top level) does not update the dirty regions for that texture. Applications assume the same responsibility for updating dirty regions when they lock lower levels without locking the topmost level.

## Related topics

<dl> <dt>

[Basic Texturing Concepts](basic-texturing-concepts.md)
</dt> </dl>

 

 



