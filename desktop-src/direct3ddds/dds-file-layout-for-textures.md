---
title: DDS Texture Example
description: For an uncompressed texture, use the DDSD\_PITCH and DDPF\_RGB flags; for a compressed texture, use the DDSD\_LINEARSIZE and DDPF\_FOURCC flags.
ms.assetid: 5bf54e8d-1dc5-4782-96c1-132d258fb560
ms.topic: article
ms.date: 05/31/2018
---

# DDS Texture Example

For an uncompressed texture, use the DDSD\_PITCH and DDPF\_RGB flags; for a compressed texture, use the DDSD\_LINEARSIZE and DDPF\_FOURCC flags. For a mipmapped texture, use the DDSD\_MIPMAPCOUNT, DDSCAPS\_MIPMAP, and DDSCAPS\_COMPLEX flags also as well as the mipmap count member. If mipmaps are generated, all levels down to 1-by-1 are usually written.

For a compressed texture, the size of each mipmap level image is typically one-fourth the size of the previous, with a minimum of 8 (DXT1) or 16 (DXT2-5) bytes (for square textures). Use the following formula to calculate the size of each level for a non-square texture:


```
max(1, ( (width + 3) / 4 ) ) x max(1, ( (height + 3) / 4 ) ) x 8(DXT1) or 16(DXT2-5)
```



This table lists the amount of space taken up by each layer for a 256-by-256 R8G8B8 texture, without using compression.



| DDS Components          | \# Bytes |
|-------------------------|----------|
| header                  | 128      |
| 256-by-256 main image   | 196608   |
| 128-by-128 mipmap image | 49152    |
| 64-by-64 mipmap image   | 12288    |
| 32-by-32 mipmap image   | 3072     |
| 16-by-16 mipmap image   | 768      |
| 8-by-8 mipmap image     | 192      |
| 4-by-4 mipmap image     | 48       |
| 2-by-2 mipmap image     | 12       |
| 1-by-1 mipmap image     | 3        |



 

This table lists the amount of space taken up by each layer for the same texture using compression (DXT1).



| DDS Components         | \# Bytes |
|------------------------|----------|
| header                 | 128      |
| 256-by-64 main image   | 8192     |
| 128-by-32 mipmap image | 2048     |
| 64-by-16 mipmap image  | 512      |
| 32-by-8 mipmap image   | 128      |
| 16-by-4 mipmap image   | 32       |
| 8-by-2 mipmap image    | 16       |
| 4-by-1 mipmap image    | 8        |
| 2-by-1 mipmap image    | 8        |
| 1-by-1 mipmap image    | 8        |



 

This table lists the amount of space taken up by each layer for the same texture using a DXGI compression format (in this case BC3\_UNORM) that therefore requires the extended header:



| DDS Components                                                | \# Bytes |
|---------------------------------------------------------------|----------|
| header (FourCC set to "DX10")                                 | 128      |
| extended header (DXGI format set to DXGI\_FORMAT\_BC3\_UNORM) | 20       |
| 256-by-64 main image                                          | 16384    |
| 128-by-32 mipmap image                                        | 4096     |
| 64-by-16 mipmap image                                         | 1024     |
| 32-by-8 mipmap image                                          | 256      |
| 16-by-4 mipmap image                                          | 64       |
| 8-by-2 mipmap image                                           | 32       |
| 4-by-1 mipmap image                                           | 16       |
| 2-by-1 mipmap image                                           | 16       |
| 1-by-1 mipmap image                                           | 16       |



 

## Related topics

<dl> <dt>

[Programming Guide for DDS](dx-graphics-dds-pguide.md)
</dt> </dl>

 

 




