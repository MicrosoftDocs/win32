---
title: '_BITMAPINFOHEADER structure'
description: The \_BITMAPINFOHEADER structure defines the format of a video frame.
ms.assetid: 394b8ded-81db-4ad3-8cf7-086f1e832771
keywords:
- _BITMAPINFOHEADER structure windows Media Device Manager
topic_type:
- apiref
api_name:
- _BITMAPINFOHEADER
api_location:
- wmdm.idl
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# \_BITMAPINFOHEADER structure

The **\_BITMAPINFOHEADER** structure defines the format of a video frame.

## Syntax


```C++
typedef struct _tagBITMAPINFOHEADER {
  DWORD biSize;
  LONG  biWidth;
  LONG  biHeight;
  WORD  biPlanes;
  WORD  biBitCount;
  DWORD biCompression;
  DWORD biSizeImage;
  LONG  biXPelsPerMeter;
  LONG  biYPelsPerMeter;
  DWORD biClrUsed;
  DWORD biClrImportant;
} _BITMAPINFOHEADER;
```



## Members

<dl> <dt>

**biSize**
</dt> <dd>

Specifies the number of bytes required by the structure.

</dd> <dt>

**biWidth**
</dt> <dd>

Specifies the width of the bitmap, in pixels.

</dd> <dt>

**biHeight**
</dt> <dd>

Specifies the height of the bitmap, in pixels. If **biHeight** is positive, the bitmap is a bottom-up DIB and its origin is the lower-left corner. If **biHeight** is negative, the bitmap is a top-down DIB and its origin is the upper-left corner. If **biHeight** is negative, indicating a top-down DIB, **biCompression** must be either BI\_RGB or BI\_BITFIELDS. Top-down DIBs cannot be compressed.

</dd> <dt>

**biPlanes**
</dt> <dd>

Specifies the number of planes for the target device. This value must be set to 1.

</dd> <dt>

**biBitCount**
</dt> <dd>

Specifies the number of bits per pixel. The **biBitCount** member of the **BITMAPINFOHEADER** structure determines the number of bits that define each pixel and the maximum number of colors in the bitmap. This member must be one of the following values.



| Value | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
|-------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 1     | The bitmap is monochrome, and the bmiColors member contains two entries. Each bit in the bitmap array represents a pixel. If the bit is clear, the pixel is displayed with the color of the first entry in the bmiColors table; if the bit is set, the pixel has the color of the second entry in the table.                                                                                                                                                                                                                                                                                                        |
| 2     | The bitmap has four possible color values.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| 4     | The bitmap has a maximum of 16 colors, and the bmiColors member contains up to 16 entries. Each pixel in the bitmap is represented by a 4-bit index into the color table. For example, if the first byte in the bitmap is 0x1F, the byte represents two pixels. The first pixel contains the color in the second table entry, and the second pixel contains the color in the sixteenth table entry.                                                                                                                                                                                                                 |
| 8     | The bitmap has a maximum of 256 colors, and the bmiColors member contains up to 256 entries. In this case, each byte in the array represents a single pixel.                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| 16    | The bitmap has a maximum of 2^16 colors. If the biCompression member of the BITMAPINFOHEADER is BI\_RGB, the bmiColors member is **NULL**. Each WORD in the bitmap array represents a single pixel. The relative intensities of red, green, and blue are represented with 5 bits for each color component. The value for blue is in the least significant 5 bits, followed by 5 bits each for green and red. The most significant bit is not used. The bmiColors color table is used for optimizing colors used on palette-based devices, and must contain the number of entries specified by the biClrUsed member. |
| 24    | The bitmap has a maximum of 2^24 colors, and the bmiColors member is **NULL**. Each 3-byte triplet in the bitmap array represents the relative intensities of blue, green, and red, respectively, for a pixel. The bmiColors color table is used for optimizing colors used on palette-based devices, and must contain the number of entries specified by the biClrUsed member.                                                                                                                                                                                                                                     |
| 32    | The bitmap has a maximum of 2^32 colors. If the biCompression member is BI\_RGB, the bmiColors member is **NULL**. Each DWORD in the bitmap array represents the relative intensities of blue, green, and red, respectively, for a pixel. The high byte in each DWORD is not used. The bmiColors color table is used for optimizing colors used on palette-based devices, and must contain the number of entries specified by the biClrUsed member.                                                                                                                                                                 |



 

</dd> <dt>

**biCompression**
</dt> <dd>

Specifies the type of compression for a compressed bottom-up bitmap (top-down DIBs cannot be compressed). This member can be the one of the following values.



| Value         | Description                                                                                                                                                                                                                                                                                                        |
|---------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| BI\_RGB       | An uncompressed format.                                                                                                                                                                                                                                                                                            |
| BI\_BITFIELDS | Specifies that the bitmap is not compressed and that the color table consists of three DWORD color masks that specify the red, green, and blue components, respectively, of each pixel. This is valid when used with 16-bpp and 32-bpp bitmaps. This value is valid in Microsoft Windows CE version 2.0 and later. |



 

</dd> <dt>

**biSizeImage**
</dt> <dd>

Specifies the size of the image, in bytes. This may be set to zero for BI\_RGB bitmaps.

</dd> <dt>

**biXPelsPerMeter**
</dt> <dd>

Specifies the horizontal resolution, in pixels per meter, of the target device for the bitmap. An application can use this value to select a bitmap from a resource group that best matches the characteristics of the current device.

</dd> <dt>

**biYPelsPerMeter**
</dt> <dd>

Specifies the vertical resolution, in pixels per meter, of the target device for the bitmap.

</dd> <dt>

**biClrUsed**
</dt> <dd>

Specifies the number of color indexes in the color table that are actually used by the bitmap. If this value is zero, the bitmap uses the maximum number of colors corresponding to the value of the **biBitCount** member for the compression mode specified by **biCompression**.

</dd> <dt>

**biClrImportant**
</dt> <dd>

Specifies the number of color indexes required for displaying the bitmap. If this value is zero, all colors are required.

If biClrUsed is nonzero and the biBitCount member is less than 16, the biClrUsed member specifies the actual number of colors the graphics engine or device driver accesses. If biBitCount is 16 or greater, the biClrUsed member specifies the size of the color table used to optimize performance of the system color palettes. If biBitCount equals 16 or 32, the optimal color palette starts immediately following the three DWORD masks.

If the bitmap is a packed bitmap (a bitmap in which the bitmap array immediately follows the \_BITMAPINFOHEADER structure and is referenced by a single pointer), the biClrUsed member must be either zero or the actual size of the color table.

</dd> </dl>

## Remarks

This structure is contained within a **\_VIDEOINFOHEADER** structure.

## Requirements



| Requirement | Value |
|-------------------|-------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Wmdm.idl</dt> </dl> |



## See also

<dl> <dt>

[**Structures**](structures.md)
</dt> <dt>

[**\_VIDEOINFOHEADER**](-videoinfoheader.md)
</dt> </dl>

 

 





