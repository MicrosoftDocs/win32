---
description: Using Compressed Textures (Direct3D 9)
ms.assetid: 60892a8b-93f4-43ba-87ef-d5c7cc6fb8c6
title: Using Compressed Textures (Direct3D 9)
ms.topic: article
ms.date: 05/31/2018
---

# Using Compressed Textures (Direct3D 9)

## Determining Support for Compressed Textures

To test the adapter, specify any pixel format that uses the DXT1, DXT2, DXT3, DXT4, or DXT5. If [**IDirect3D9::CheckDeviceFormat**](/windows/desktop/api) returns D3D\_OK, the device can create texture directly from a compressed texture surface that uses that format. If so, you can use compressed texture surfaces directly with Direct3D by calling the [**IDirect3DDevice9::SetTexture**](/windows/win32/api/d3d9helper/nf-d3d9helper-idirect3ddevice9-settexture) method. The following code example shows how to determine if the adapter supports a compressed texture format.


```
BOOL IsCompressedTextureFormatOk( D3DFORMAT TextureFormat, 
                                  D3DFORMAT AdapterFormat ) 
{
    HRESULT hr = pD3D->CheckDeviceFormat( D3DADAPTER_DEFAULT,
                                          D3DDEVTYPE_HAL,
                                          AdapterFormat,
                                          0,
                                          D3DRTYPE_TEXTURE,
                                          TextureFormat);

    return SUCCEEDED( hr );
}
```



If the device does not support texturing from compressed texture surfaces, you can still store texture data in a compressed format surface, but you must convert any compressed textures to a supported format before they can be used for texturing.

## Creating Compressed Textures

After creating a device that supports a compressed texture format on the adapter, you can create a compressed texture resource. Call [**IDirect3DDevice9::CreateTexture**](/windows/win32/api/d3d9helper/nf-d3d9helper-idirect3ddevice9-createtexture) and specify a compressed texture format for the Format parameter.

Before loading an image into a texture object, retrieve a pointer to the texture surface by calling the [**IDirect3DTexture9::GetSurfaceLevel**](/windows/win32/api/d3d9helper/nf-d3d9helper-idirect3dtexture9-getsurfacelevel) method.

Now you can use any D3DXLoadSurfacexxx function to load an image to the surface that was retrieved by using [**IDirect3DTexture9::GetSurfaceLevel**](/windows/win32/api/d3d9helper/nf-d3d9helper-idirect3dtexture9-getsurfacelevel). These functions handle conversion to and from compressed texture formats.

You can create and convert compressed texture (DDS) files using the DirectX Texture Editor (Dxtex.exe) supplied with the DirectX SDK. You can get Dxtex.exe and learn about it from the DirectX SDK. For info about the DirectX SDK, see [Where is the DirectX SDK?](../directx-sdk--august-2009-.md).

The advantage of this behavior is that an application can copy the contents of a compressed surface to a file without calculating how much storage is required for a surface of a particular width and height in the specific format.

The following table shows the five types of compressed textures. For more information about how the data is stored, see [Compressed Texture Formats (Direct3D 9)](compressed-texture-formats.md). You only need this information if you are writing your own compression routines.



| FOURCC | Description        | Alpha premultiplied? |
|--------|--------------------|----------------------|
| DXT1   | Opaque/1-bit alpha | N/A                  |
| DXT2   | Explicit alpha     | Yes                  |
| DXT3   | Explicit alpha     | No                   |
| DXT4   | Interpolated alpha | Yes                  |
| DXT5   | Interpolated alpha | No                   |



 

When you transfer data from a nonpremultiplied format to a premultiplied format, Direct3D scales the colors based on the alpha values. Transferring data from a premultiplied format to a nonpremultiplied format is not supported. If you try to transfer data from a premultiplied alpha source to a nonpremultiplied alpha destination, the method returns D3DERR\_INVALIDCALL. If you transfer data from a premultiplied alpha source to a destination that has no alpha, the source color components, which have been scaled by alpha, are copied as is.

## Decompressing Compressed Texture Surfaces

As with compressing a texture surface, decompressing a compressed texture is performed through Direct3D copying services.

To copy a compressed texture surface to a uncompressed texture surface, use the function [**D3DXLoadSurfaceFromSurface**](d3dxloadsurfacefromsurface.md). This functions handles compression to and from compressed and uncompressed surfaces.

## Related topics

<dl> <dt>

[Compressed Texture Resources](compressed-texture-resources.md)
</dt> </dl>

 

 
