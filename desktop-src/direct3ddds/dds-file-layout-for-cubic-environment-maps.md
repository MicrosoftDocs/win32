---
title: DDS Cube Map Example
description: For cubic environment maps, one or more faces of a cube are written to the file, using either uncompressed or compressed formats, and all faces must be the same size.
ms.assetid: a77234f6-ba10-40dd-902f-33e600384aa5
ms.topic: article
ms.date: 05/31/2018
---

# DDS Cube Map Example

For cubic environment maps, one or more faces of a cube are written to the file, using either uncompressed or compressed formats, and all faces must be the same size. Each face can have mipmaps defined, although all faces must have the same number of mipmap levels. If a file contains a cube map, DDSCAPS\_COMPLEX, DDSCAPS2\_CUBEMAP, and one or more of DSCAPS2\_CUBEMAP\_POSITIVEX/Y/Z and/or DDSCAPS2\_CUBEMAP\_NEGATIVEX/Y/Z should be set. The faces are written in the order: positive x, negative x, positive y, negative y, positive z, negative z, with any missing faces omitted. Each face is written with its main image, followed by any mipmap levels.

For example, a 256-by-256 cube map with positive x, negative y, and positive z faces, a pixel format of DXT1, and all mipmap levels would contain the following:



| DDS Components                                      | \# Bytes |
|-----------------------------------------------------|----------|
| header                                              | 128      |
| 256-by-256 positive x main image                    | 32768    |
| 128-by-128 positive x mipmap image                  | 8192     |
| 64-by-64 positive x mipmap image                    | 2048     |
| 32-by-32 positive x mipmap image                    | 512      |
| 16-by-16 positive x mipmap image                    | 128      |
| 8-by-8 positive x mipmap image                      | 32       |
| 4-by-4 positive x mipmap image                      | 8        |
| 2-by-2 positive x mipmap image                      | 8        |
| 1-by-1 positive x mipmap image                      | 8        |
| repeat the previous 9 layers for the y mipmap image | 43704    |
| repeat the previous 9 layers for the z mipmap image | 43704    |



 

Starting with DirectX 8, a cube map is stored with all faces defined.

## DXGI Cube Maps

Cubic environment maps in Direct3D 10.x and Direct3D 11 are equivalent to a 2D texture array with 6 images, and can be stored in DDS files as such. With Direct3D 10.1 and Direct3D 11, the hardware can also support arrays of cubemaps which are themselves 2D texture arrays with a multiple of 6 images (6, 12, 18, 24, etc.).

For example, here is a 256-by-256 cubemap with mipmap levels stored in a BC6H format as a 2D texture array:



| DDS Components                                                                                                                                                                                                  | \# Bytes |
|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------|
| header (FourCC of "DX10")                                                                                                                                                                                       | 128      |
| extended header (DXGI format set to 95 \[DXGI\_FORMAT\_BC6H\_UF16\], dimension value of 3 \[D3Dxx\_RESOURCE\_DIMENSION\_TEXTURE2D\], array size of 6, misc flags of 0x4 \[D3Dxx\_RESOURCE\_MISC\_TEXTURECUBE\]) | 20       |
| 256-by-256 array entry 0 (positive x) main image                                                                                                                                                                | 65536    |
| 128-by-128 array entry 0 (positive x) mipmap image                                                                                                                                                              | 16384    |
| 64-by-64 array entry 0 (positive x) mipmap image                                                                                                                                                                | 4096     |
| 32-by-32 array entry 0 (positive x) mipmap image                                                                                                                                                                | 1024     |
| 16-by-16 array entry 0 (positive x) mipmap image                                                                                                                                                                | 256      |
| 8-by-8 array entry 0 (positive x) mipmap image                                                                                                                                                                  | 64       |
| 4-by-4 array entry 0 (positive x) mipmap image                                                                                                                                                                  | 16       |
| 2-by-2 array entry 0 (positive x) mipmap image                                                                                                                                                                  | 16       |
| 1-by-1 array entry 0 (positive x) mipmap image                                                                                                                                                                  | 16       |
| repeat the previous 9 layers for array entry 1 (negative x) mipmap image                                                                                                                                        | 87408    |
| repeat the previous 9 layers for array entry 2 (positive y) mipmap image                                                                                                                                        | 87408    |
| repeat the previous 9 layers for array entry 3 (negative y) mipmap image                                                                                                                                        | 87408    |
| repeat the previous 9 layers for array entry 4 (positive z) mipmap image                                                                                                                                        | 87408    |
| repeat the previous 9 layers for array entry 5 (negative z) mipmap image                                                                                                                                        | 87408    |



 

## Related topics

<dl> <dt>

[Programming Guide for DDS](dx-graphics-dds-pguide.md)
</dt> </dl>

 

 




