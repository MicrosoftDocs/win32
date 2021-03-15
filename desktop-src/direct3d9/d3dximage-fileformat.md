---
description: Describes the supported image file formats. See Remarks for descriptions of these formats.
ms.assetid: 245a0052-f156-44ad-ab46-3677a818167e
title: D3DXIMAGE_FILEFORMAT enumeration (D3dx9tex.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- D3DXIMAGE_FILEFORMAT
api_type: 
- HeaderDef
api_location: 
- d3dx9tex.h
---

# D3DXIMAGE\_FILEFORMAT enumeration

Describes the supported image file formats. See Remarks for descriptions of these formats.

## Syntax


```C++
typedef enum D3DXIMAGE_FILEFORMAT { 
  D3DXIFF_BMP          = 0,
  D3DXIFF_JPG          = 1,
  D3DXIFF_TGA          = 2,
  D3DXIFF_PNG          = 3,
  D3DXIFF_DDS          = 4,
  D3DXIFF_PPM          = 5,
  D3DXIFF_DIB          = 6,
  D3DXIFF_HDR          = 7,
  D3DXIFF_PFM          = 8,
  D3DXIFF_FORCE_DWORD  = 0x7fffffff
} D3DXIMAGE_FILEFORMAT, *LPD3DXIMAGE_FILEFORMAT;
```



## Constants

<dl> <dt>

<span id="D3DXIFF_BMP"></span><span id="d3dxiff_bmp"></span>**D3DXIFF\_BMP**
</dt> <dd>

Windows bitmap (BMP) file format.

</dd> <dt>

<span id="D3DXIFF_JPG"></span><span id="d3dxiff_jpg"></span>**D3DXIFF\_JPG**
</dt> <dd>

Joint Photographics Experts Group (JPEG) compressed file format.

</dd> <dt>

<span id="D3DXIFF_TGA"></span><span id="d3dxiff_tga"></span>**D3DXIFF\_TGA**
</dt> <dd>

Truevision (Targa, or TGA) image file format.

</dd> <dt>

<span id="D3DXIFF_PNG"></span><span id="d3dxiff_png"></span>**D3DXIFF\_PNG**
</dt> <dd>

Portable Network Graphics (PNG) file format.

</dd> <dt>

<span id="D3DXIFF_DDS"></span><span id="d3dxiff_dds"></span>**D3DXIFF\_DDS**
</dt> <dd>

DirectDraw surface (DDS) file format.

</dd> <dt>

<span id="D3DXIFF_PPM"></span><span id="d3dxiff_ppm"></span>**D3DXIFF\_PPM**
</dt> <dd>

Portable pixmap (PPM) file format.

</dd> <dt>

<span id="D3DXIFF_DIB"></span><span id="d3dxiff_dib"></span>**D3DXIFF\_DIB**
</dt> <dd>

Windows device-independent bitmap (DIB) file format.

</dd> <dt>

<span id="D3DXIFF_HDR"></span><span id="d3dxiff_hdr"></span>**D3DXIFF\_HDR**
</dt> <dd>

High dynamic range (HDR) file format.

</dd> <dt>

<span id="D3DXIFF_PFM"></span><span id="d3dxiff_pfm"></span>**D3DXIFF\_PFM**
</dt> <dd>

Portable float map file format.

</dd> <dt>

<span id="D3DXIFF_FORCE_DWORD"></span><span id="d3dxiff_force_dword"></span>**D3DXIFF\_FORCE\_DWORD**
</dt> <dd>

Forces this enumeration to compile to 32 bits in size. Without this value, some compilers would allow this enumeration to compile to a size other than 32 bits. This value is not used.

</dd> </dl>

## Remarks

Functions that begin with D3DXLoadxxx support all of the formats listed. Functions that begin with D3DXSavexxx support all of the formats listed except the Truevision (.tga) and portable pixmap (.ppm) formats.

The following table lists the available input and output formats.



| File Extension | Description                                                                                                                                                                                                                                                                                                                                        |
|----------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| .bmp           | Windows bitmap format. Contains a header that describes the resolution of the device on which the rectangle of pixels was created, the dimensions of the rectangle, the size of the array of bits, a logical palette, and an array of bits that defines the relationship between pixels in the bitmapped image and entries in the logical palette. |
| .dds           | DirectDraw Surface file format. Stores textures, volume textures, and cubic environment maps, with or without mipmap levels, and with or without pixel compression. See [DDS](../direct3ddds/dx-graphics-dds.md).                                                                                                                                       |
| .dib           | Windows DIB. Contains an array of bits combined with structures that specify width and height of the bitmapped image, color format of the device where the image was created, and resolution of the device used to create that image.                                                                                                              |
| .hdr           | HDR format. Encodes each pixel as an RGBE 32-bit color, with 8 bits of mantissa for red, green, and blue, and a shared 8-bit exponent. Each channel is separately compressed with run-length encoding (RLE).                                                                                                                                       |
| .jpg           | JPEG standard. Specifies variable compression of 24-bit RGB color and 8-bit gray-scale Tagged Image File Format (TIFF) image document files.                                                                                                                                                                                                       |
| .pfm           | Portable float map format. A raw floating point image format, without any compression. The file header specifies image width, height, monochrome or color, and machine word order. Pixel data is stored as 32-bit floating point values, with 3 values per pixel for color, and one value per pixel for monochrome.                                |
| .png           | PNG format. A non-proprietary bitmap format using lossless compression.                                                                                                                                                                                                                                                                            |
| .ppm           | Portable Pixmap format. A binary or ASCII file format for color images that includes image height and width and the maximum color component value.                                                                                                                                                                                                 |
| .tga           | Targa or Truevision Graphics Adapter format. Supports depths of 8, 15, 16, 24, and 32 bits, including 8-bit gray scale, and contains optional color palette data, image (x, y) origin and size data, and pixel data.                                                                                                                               |



 

See [Types of Bitmaps](../gdiplus/-gdiplus-types-of-bitmaps-about.md) for more information on some of these formats.

## Requirements



| Requirement | Value |
|-------------------|---------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>D3dx9tex.h</dt> </dl> |



## See also

<dl> <dt>

[D3DX Enumerations](dx9-graphics-reference-d3dx-enums.md)
</dt> </dl>

 

 
