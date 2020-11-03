---
title: Programming Guide for DDS
description: Direct3D implements the DDS file format for storing uncompressed or compressed (DXTn) textures.
ms.assetid: 39f9847e-3b1c-4401-a253-74c183ffcc83
ms.topic: article
ms.date: 05/31/2018
---

# Programming Guide for DDS

Direct3D implements the DDS file format for storing uncompressed or compressed (DXTn) textures. The file format implements several slightly different types designed for storing different types of data, and supports single layer textures, textures with mipmaps, cube maps, volume maps and texture arrays (in Direct3D 10/11). This section describes the layout of a DDS file.

For help creating a texture in Direct3D 11, see [How to: Create a Texture](/windows/desktop/direct3d11/overviews-direct3d-11-resources-textures-create). For help in Direct3D 9, see [Texture Support in D3DX (Direct3D 9)](/windows/desktop/direct3d9/texture-support-in-d3dx).

-   [DDS File Layout](#dds-file-layout)
-   [DDS Variants](#dds-variants)
-   [Using Texture Arrays in Direct3D 10/11](#using-texture-arrays-in-direct3d-1011)
-   [Common DDS File Resource Formats and Associated Header Content](#common-dds-file-resource-formats-and-associated-header-content)
-   [Related topics](#related-topics)

## DDS File Layout

A DDS file is a binary file that contains the following information:

-   A DWORD (magic number) containing the four character code value 'DDS ' (0x20534444).

-   A description of the data in the file.

    The data is described with a header description using [**DDS\_HEADER**](dds-header.md); the pixel format is defined using [**DDS\_PIXELFORMAT**](dds-pixelformat.md). Note that the **DDS\_HEADER** and **DDS\_PIXELFORMAT** structures replace the deprecated DDSURFACEDESC2, DDSCAPS2 and DDPIXELFORMAT DirectDraw 7 structures. **DDS\_HEADER** is the binary equivalent of DDSURFACEDESC2 and DDSCAPS2. **DDS\_PIXELFORMAT** is the binary equivalent of DDPIXELFORMAT.

    ```
    DWORD               dwMagic;
    DDS_HEADER          header;
            
    ```

    

    If the DDS\_PIXELFORMAT dwFlags is set to DDPF\_FOURCC and dwFourCC is set to "DX10" an additional [**DDS\_HEADER\_DXT10**](dds-header-dxt10.md) structure will be present to accommodate texture arrays or DXGI formats that cannot be expressed as an RGB pixel format such as floating point formats, sRGB formats etc. When the **DDS\_HEADER\_DXT10** structure is present the entire data description will looks like this.

    ```
    DWORD               dwMagic;
    DDS_HEADER          header;
    DDS_HEADER_DXT10    header10;
    ```

    

-   A pointer to an array of bytes that contains the main surface data.
    ```
    BYTE bdata[]
    ```

    

-   A pointer to an array of bytes that contains the remaining surfaces such as; mipmap levels, faces in a cube map, depths in a volume texture. Follow these links for more information about the DDS file layout for a: [texture](dds-file-layout-for-textures.md), a [cube map](dds-file-layout-for-cubic-environment-maps.md), or a [volume texture](dds-file-layout-for-volume-textures.md).

    ```
    BYTE bdata2[]
    ```

    

For broad hardware support, we recommend that you use the [**DXGI\_FORMAT\_R8G8B8A8\_UNORM**](/windows/desktop/api/dxgiformat/ne-dxgiformat-dxgi_format), [**DXGI\_FORMAT\_R8G8B8A8\_UNORM\_SRGB**](/windows/desktop/api/dxgiformat/ne-dxgiformat-dxgi_format), [**DXGI\_FORMAT\_R8G8B8A8\_SNORM**](/windows/desktop/api/dxgiformat/ne-dxgiformat-dxgi_format), [**DXGI\_FORMAT\_B8G8R8A8\_UNORM**](/windows/desktop/api/dxgiformat/ne-dxgiformat-dxgi_format), [**DXGI\_FORMAT\_R16G16\_SNORM**](/windows/desktop/api/dxgiformat/ne-dxgiformat-dxgi_format), [**DXGI\_FORMAT\_R8G8\_SNORM**](/windows/desktop/api/dxgiformat/ne-dxgiformat-dxgi_format), [**DXGI\_FORMAT\_R8\_UNORM**](/windows/desktop/api/dxgiformat/ne-dxgiformat-dxgi_format), [**DXGI\_FORMAT\_BC1\_UNORM**](/windows/desktop/api/dxgiformat/ne-dxgiformat-dxgi_format), [**DXGI\_FORMAT\_BC1\_UNORM\_SRGB**](/windows/desktop/api/dxgiformat/ne-dxgiformat-dxgi_format), [**DXGI\_FORMAT\_BC2\_UNORM**](/windows/desktop/api/dxgiformat/ne-dxgiformat-dxgi_format), [**DXGI\_FORMAT\_BC2\_UNORM\_SRGB**](/windows/desktop/api/dxgiformat/ne-dxgiformat-dxgi_format), [**DXGI\_FORMAT\_BC3\_UNORM**](/windows/desktop/api/dxgiformat/ne-dxgiformat-dxgi_format), or [**DXGI\_FORMAT\_BC3\_UNORM\_SRGB**](/windows/desktop/api/dxgiformat/ne-dxgiformat-dxgi_format) format.

For more info about compressed texture formats, see [Texture Block Compression in Direct3D 11](/windows/desktop/direct3d11/texture-block-compression-in-direct3d-11) and [Block Compression (Direct3D 10)](/windows/desktop/direct3d10/d3d10-graphics-programming-guide-resources-block-compression).

The D3DX library (for example, D3DX11.lib) and other similar libraries unreliably or inconsistently provide the pitch value in the **dwPitchOrLinearSize** member of the [**DDS\_HEADER**](dds-header.md) structure. Therefore, when you read and write to DDS files, we recommend that you compute the pitch in one of the following ways for the indicated formats:

-   For block-compressed formats, compute the pitch as:

    max( 1, ((width+3)/4) ) \* block-size

    The block-size is 8 bytes for DXT1, BC1, and BC4 formats, and 16 bytes for other block-compressed formats.

-   For R8G8\_B8G8, G8R8\_G8B8, legacy UYVY-packed, and legacy YUY2-packed formats, compute the pitch as:

    ((width+1) >> 1) \* 4

-   For other formats, compute the pitch as:

    ( width \* bits-per-pixel + 7 ) / 8

    You divide by 8 for byte alignment.

> [!Note]  
> The pitch value that you calculate does not always equal the pitch that the runtime supplies, which is DWORD-aligned in some situations and byte-aligned in other situations. Therefore, we recommend that you copy a scan line at a time rather than try to copy the whole image in one copy.

 

## DDS Variants

There are many tools that create and consume DDS files, but they can vary in the details of what they require in the header. Writers should populate the headers as fully as possible, and readers should check the minimal values for maximum compatibility. To validate a DDS file, a reader should ensure the file is at least 128 bytes long to accommodate the magic value and basic header, the magic value is 0x20534444 ("DDS "), the DDS\_HEADER size is 124, and the DDS\_PIXELFORMAT in the header size is 32. If the DDS\_PIXELFORMAT dwFlags is set to DDPF\_FOURCC and a dwFourCC is set to "DX10", then the total file size needs to be at least 148 bytes.

There are some common variants in use where the pixel format is set to a DDPF\_FOURCC code where dwFourCC is set to a D3DFORMAT or DXGI\_FORMAT enumeration value. There is no way to tell if an enumeration value is a D3DFORMAT or a DXGI\_FORMAT, so it is highly recommended that the "DX10" extension and DDS\_HEADER\_DXT10 header is used instead to store the dxgiFormat when the basic DDS\_PIXELFORMAT cannot express the format.

The standard DDS\_PIXELFORMAT should be preferred for maximum compatibility to store RGB uncompressed data and DXT1-5 data as not all DDS tools support the DX10 extension.

## Using Texture Arrays in Direct3D 10/11

The new DDS structures ([**DDS\_HEADER**](dds-header.md) and [**DDS\_HEADER\_DXT10**](dds-header-dxt10.md)) in Direct3D 10/11 extend the DDS file format to support an array of textures, which is a new resource type in Direct3D 10/11. Here is some sample code that shows how to access the different mipmap levels in an array of textures, using the new headers.


```
DWORD               dwMagic;
DDS_HEADER          header;
DDS_HEADER_DXT10    header10;
   
for (int iArrayElement = 0; iArrayElement < header10.arraySize; iArrayElement++)
{
   for (int iMipLevel = 0; iMipLevel < header.dwMipMapCount; iMipLevel++)
   {
     ...
   }
}       
```



## Common DDS File Resource Formats and Associated Header Content



| Resource Format                                                                            | dwFlags        | dwRGBBitCount | dwRBitMask | dwGBitMask | dwBBitMask | dwABitMask |
|--------------------------------------------------------------------------------------------|----------------|---------------|------------|------------|------------|------------|
| DXGI\_FORMAT\_R8G8B8A8\_UNORM<br/> D3DFMT\_A8B8G8R8<br/>                       | DDS\_RGBA      | 32            | 0xff       | 0xff00     | 0xff0000   | 0xff000000 |
| DXGI\_FORMAT\_R16G16\_UNORM<br/> D3DFMT\_G16R16<br/>                           | DDS\_RGBA      | 32            | 0xffff     | 0xffff0000 |            |            |
| \*\*<br/> DXGI\_FORMAT\_R10G10B10A2\_UNORM<br/> D3DFMT\_A2B10G10R10<br/> | DDS\_RGBA      | 32            | 0x3ff      | 0xffc00    | 0x3ff00000 |            |
| DXGI\_FORMAT\_R16G16\_UNORM<br/> D3DFMT\_G16R16<br/>                           | DDS\_RGB       | 32            | 0xffff     | 0xffff0000 |            |            |
| DXGI\_FORMAT\_B5G5R5A1\_UNORM<br/> D3DFMT\_A1R5G5B5<br/>                       | DDS\_RGBA      | 16            | 0x7c00     | 0x3e0      | 0x1f       | 0x8000     |
| DXGI\_FORMAT\_B5G6R5\_UNORM<br/> D3FMT\_R5G6B5<br/>                            | DDS\_RGB       | 16            | 0xf800     | 0x7e0      | 0x1f       |            |
| DXGI\_A8\_UNORM<br/> D3DFMT\_A8<br/>                                           | DDS\_ALPHA     | 8             |            |            |            | 0xff       |
| D3DFMT\_A8R8G8B8<br/>                                                                | DDS\_RGBA      | 32            | 0xff0000   | 0xff00     | 0xff       | 0xff000000 |
| D3DFMT\_X8R8G8B8<br/>                                                                | DDS\_RGB       | 32            | 0xff0000   | 0xff00     | 0xff       |            |
| D3DFMT\_X8B8G8R8<br/>                                                                | DDS\_RGB       | 32            | 0xff       | 0xff00     | 0xff0000   |            |
| \*\*<br/> D3DFMT\_A2R10G10B10<br/>                                             | DDS\_RGBA      | 32            | 0x3ff00000 | 0xffc00    | 0x3ff      | 0xc0000000 |
| D3DFMT\_R8G8B8<br/>                                                                  | DDS\_RGB       | 24            | 0xff0000   | 0xff00     | 0xff       |            |
| D3DFMT\_X1R5G5B5<br/>                                                                | DDS\_RGB       | 16            | 0x7c00     | 0x3e0      | 0x1f       |            |
| D3DFMT\_A4R4G4B4<br/>                                                                | DDS\_RGBA      | 16            | 0xf00      | 0xf0       | 0xf        | 0xf000     |
| D3DFMT\_X4R4G4B4<br/>                                                                | DDS\_RGB       | 16            | 0xf00      | 0xf0       | 0xf        |            |
| D3DFMT\_A8R3G3B2<br/>                                                                | DDS\_RGBA      | 16            | 0xe0       | 0x1c       | 0x3        | 0xff00     |
| D3DFMT\_A8L8<br/>                                                                    | DDS\_LUMINANCE | 16            | 0xff       |            |            | 0xff00     |
| D3DFMT\_L16<br/>                                                                     | DDS\_LUMINANCE | 16            | 0xffff     |            |            |            |
| D3DFMT\_L8<br/>                                                                      | DDS\_LUMINANCE | 8             | 0xff       |            |            |            |
| D3DFMT\_A4L4<br/>                                                                    | DDS\_LUMINANCE | 8             | 0xf        |            |            | 0xf0       |



 



| Resource Format                                                                             | dwFlags     | dwFourCC |
|---------------------------------------------------------------------------------------------|-------------|----------|
| DXGI\_FORMAT\_BC1\_UNORM<br/> D3DFMT\_DXT1<br/>                                 | DDS\_FOURCC | "DXT1"   |
| DXGI\_FORMAT\_BC2\_UNORM<br/> D3DFMT\_DXT3<br/>                                 | DDS\_FOURCC | "DXT3"   |
| DXGI\_FORMAT\_BC3\_UNORM<br/> D3DFMT\_DXT5<br/>                                 | DDS\_FOURCC | "DXT5"   |
| \*<br/> DXGI\_FORMAT\_BC4\_UNORM<br/>                                           | DDS\_FOURCC | "BC4U"   |
| \*<br/> DXGI\_FORMAT\_BC4\_SNORM<br/>                                           | DDS\_FOURCC | "BC4S"   |
| \*<br/> DXGI\_FORMAT\_BC5\_UNORM<br/>                                           | DDS\_FOURCC | "ATI2"   |
| \*<br/> DXGI\_FORMAT\_BC5\_SNORM<br/>                                           | DDS\_FOURCC | "BC5S"   |
| DXGI\_FORMAT\_R8G8\_B8G8\_UNORM<br/> D3DFMT\_R8G8\_B8G8<br/>                    | DDS\_FOURCC | "RGBG"   |
| DXGI\_FORMAT\_G8R8\_G8B8\_UNORM<br/> D3DFMT\_G8R8\_G8B8<br/>                    | DDS\_FOURCC | "GRGB"   |
| \*<br/> DXGI\_FORMAT\_R16G16B16A16\_UNORM<br/> D3DFMT\_A16B16G16R16<br/>  | DDS\_FOURCC | 36       |
| \*<br/> DXGI\_FORMAT\_R16G16B16A16\_SNORM<br/> D3DFMT\_Q16W16V16U16<br/>  | DDS\_FOURCC | 110      |
| \*<br/> DXGI\_FORMAT\_R16\_FLOAT<br/> D3DFMT\_R16F<br/>                   | DDS\_FOURCC | 111      |
| \*<br/> DXGI\_FORMAT\_R16G16\_FLOAT<br/> D3DFMT\_G16R16F<br/>             | DDS\_FOURCC | 112      |
| \*<br/> DXGI\_FORMAT\_R16G16B16A16\_FLOAT<br/> D3DFMT\_A16B16G16R16F<br/> | DDS\_FOURCC | 113      |
| \*<br/> DXGI\_FORMAT\_R32\_FLOAT<br/> D3DFMT\_R32F<br/>                   | DDS\_FOURCC | 114      |
| \*<br/> DXGI\_FORMAT\_R32G32\_FLOAT<br/> D3DFMT\_G32R32F<br/>             | DDS\_FOURCC | 115      |
| \*<br/> DXGI\_FORMAT\_R32G32B32A32\_FLOAT<br/> D3DFMT\_A32B32G32R32F<br/> | DDS\_FOURCC | 116      |
| D3DFMT\_DXT2<br/>                                                                     | DDS\_FOURCC | "DXT2"   |
| D3DFMT\_DXT4<br/>                                                                     | DDS\_FOURCC | "DXT4"   |
| D3DFMT\_UYVY<br/>                                                                     | DDS\_FOURCC | "UYVY"   |
| D3DFMT\_YUY2<br/>                                                                     | DDS\_FOURCC | "YUY2"   |
| D3DFMT\_CxV8U8<br/>                                                                   | DDS\_FOURCC | 117      |
| Any DXGI format                                                                             | DDS\_FOURCC | "DX10"   |



 

\* = A robust DDS reader must be able to handle these legacy format codes. However, such a DDS reader should prefer to use the "DX10" header extension when it writes these format codes to avoid ambiguity.

\*\* = Because of some long-standing issues in common implementations of DDS readers and writers, the most robust way to write out 10:10:10:2-type data is to use the "DX10" header extension with the [**DXGI\_FORMAT**](/windows/desktop/api/dxgiformat/ne-dxgiformat-dxgi_format) code "24" (that is, the DXGI\_FORMAT\_R10G10B10A2\_UNORM value). D3DFMT\_A2R10G10B10 data should be converted to 10:10:10:2-type data before being written out as a DXGI\_FORMAT\_R10G10B10A2\_UNORM format DDS file.

## Related topics

<dl> <dt>

[DDS](dx-graphics-dds.md)
</dt> </dl>

 

