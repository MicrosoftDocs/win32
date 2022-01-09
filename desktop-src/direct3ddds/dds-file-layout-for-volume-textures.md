---
title: DDS Volume Texture Example
description: For a volume texture, use the DDSCAPS\_COMPLEX, DDSCAPS2\_VOLUME, DDSD\_DEPTH flags and set dwDepth. A volume texture is an extension of a standard texture for Direct3D 9 and can be defined with or without mipmaps.
ms.assetid: c1675a6d-129a-4e95-993f-e1be905781cc
ms.topic: article
ms.date: 05/31/2018
---

# DDS Volume Texture Example

For a volume texture, use the DDSCAPS\_COMPLEX, DDSCAPS2\_VOLUME, DDSD\_DEPTH flags and set dwDepth. A volume texture is an extension of a standard texture for Direct3D 9 and can be defined with or without mipmaps.

For volumes without mipmaps, each depth slice is written to the file in order. If mipmaps are included, all depth slices for a given mipmap level are written together, with each level containing half as many slices as the previous level with a minimum of 1.

For example, a 64-by-64-by-4 volume map using a pixel format of R8G8B8 (3 bytes per pixel) with all mipmap levels would contain the following:



| DDS Components                      | \# Bytes    |
|-------------------------------------|-------------|
| header                              | 128 bytes   |
| 64-by-64 slice 1 of 4 main image.   | 12288 bytes |
| 64-by-64 slice 2 of 4 main image.   | 12288 bytes |
| 64-by-64 slice 3 of 4 main image.   | 12288 bytes |
| 64-by-64 slice 4 of 4 main image.   | 12288 bytes |
| 32-by-32 slice 1 of 2 mipmap image. | 3072 bytes  |
| 32-by-32 slice 2 of 2 mipmap image. | 3072 bytes  |
| 16-by-16 slice 1 of 1 mipmap image. | 768 bytes   |
| 8-by-8 slice 1 of 1 mipmap image.   | 192 bytes   |
| 4-by-4 slice 1 of 1 mipmap image.   | 48 bytes    |
| 2-by-2 slice 1 of 1 mipmap image.   | 12 bytes    |
| 1-by-1 slice 1 of 1 mipmap image.   | 3 bytes     |



 

Note that the smallest mipmap level is only 3 bytes because the bitcount is 24 and there is no added compression at this level.

Support for volume textures was added in DirectX 8.

## Related topics

<dl> <dt>

[Programming Guide for DDS](dx-graphics-dds-pguide.md)
</dt> </dl>

 

 




