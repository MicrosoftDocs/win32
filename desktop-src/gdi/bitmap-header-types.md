---
description: Bitmap Header Types
ms.assetid: 6df4655a-f707-4893-b6e6-f7e4d7f67b4e
title: Bitmap Header Types
ms.topic: article
ms.date: 05/31/2018
---

# Bitmap Header Types

The bitmap has four basic header types:

-   [**BITMAPCOREHEADER**](/windows/win32/api/wingdi/ns-wingdi-bitmapcoreheader)
-   [**BITMAPINFOHEADER**](/windows/win32/api/wingdi/ns-wingdi-bitmapinfoheader)
-   [**BITMAPV4HEADER**](/windows/desktop/api/Wingdi/ns-wingdi-bitmapv4header)
-   [**BITMAPV5HEADER**](/windows/desktop/api/Wingdi/ns-wingdi-bitmapv5header)

The four types of bitmap headers are differentiated by the **Size** member, which is the first **DWORD** in each of the structures.

The [**BITMAPV5HEADER**](/windows/desktop/api/Wingdi/ns-wingdi-bitmapv5header) structure is an extended [**BITMAPV4HEADER**](/windows/desktop/api/Wingdi/ns-wingdi-bitmapv4header) structure, which is an extended [**BITMAPINFOHEADER**](/windows/win32/api/wingdi/ns-wingdi-bitmapinfoheader) structure. However, the **BITMAPINFOHEADER** and [**BITMAPCOREHEADER**](/windows/win32/api/wingdi/ns-wingdi-bitmapcoreheader) have only the **Size** member in common with other bitmap header structures.

The [**BITMAPCOREHEADER**](/windows/win32/api/wingdi/ns-wingdi-bitmapcoreheader) and [**BITMAPV4HEADER**](/windows/desktop/api/Wingdi/ns-wingdi-bitmapv4header) formats have been superseded by [**BITMAPINFOHEADER**](/windows/win32/api/wingdi/ns-wingdi-bitmapinfoheader) and [**BITMAPV5HEADER**](/windows/desktop/api/Wingdi/ns-wingdi-bitmapv5header) formats, respectively. The **BITMAPCOREHEADER** and **BITMAPV4HEADER** formats are presented for completeness and backward compatibility.

The format for a DIB is the following (for more information, see [Bitmap Storage](bitmap-storage.md) ):

-   a [**BITMAPFILEHEADER**](/windows/win32/api/wingdi/ns-wingdi-bitmapfileheader) structure
-   either a [**BITMAPCOREHEADER**](/windows/win32/api/wingdi/ns-wingdi-bitmapcoreheader), a [**BITMAPINFOHEADER**](/windows/win32/api/wingdi/ns-wingdi-bitmapinfoheader), a [**BITMAPV4HEADER**](/windows/desktop/api/Wingdi/ns-wingdi-bitmapv4header), or a [**BITMAPV5HEADER**](/windows/desktop/api/Wingdi/ns-wingdi-bitmapv5header) structure.
-   an optional color table, which is either a set of [**RGBQUAD**](/windows/win32/api/wingdi/ns-wingdi-rgbquad) structures or a set of [**RGBTRIPLE**](/windows/win32/api/wingdi/ns-wingdi-rgbtriple) structures.
-   the bitmap data
-   optional Profile data

A color table describes how pixel values correspond to RGB color values. RGB is a model for describing colors that are produced by emitting light.

*Profile data* refers to either the profile file name (linked profile) or the actual profile bits (embedded profile). The file format places the profile data at the end of the file. The profile data is placed just after the color table (if present). However, if the function receives a packed DIB, the profile data comes after the bitmap bits, like in the file format.

Profile data will only exist for [**BITMAPV5HEADER**](/windows/desktop/api/Wingdi/ns-wingdi-bitmapv5header) structures where **bV5CSType** is PROFILE\_LINKED or PROFILE\_EMBEDDED. For functions that receive packed DIBs, the profile data comes after the bitmap data.

A palettized device is any device that uses palettes to assign colors. The classic example of a palettized device is a display running in 8 bit color depth (that is, 256 colors). The display in this mode uses a small color table to assign colors to a bitmap. The colors in a bitmap are assigned to the closest color in the palette that the device is using. The palettized device does not create an optimal palette for displaying the bitmap; it simply uses whatever is in the current palette. Applications are responsible for creating a palette and selecting it into the system. In general, 16-, 24-, and 32-bits-per-pixel (bpp) bitmaps do not contain color tables (a.k.a. optimal palettes for the bitmap); the application is responsible for generating a optimal palette in this case. However, 16-, 24-, and 32-bpp bitmaps can contain such optimal color tables for displaying on palettized devices; in this case the application just needs to create a palette based off the color table present in the bitmap file.

Bitmaps that are 1, 4, or 8 bpp must have a color table with a maximum size based on the bpp. The maximum size for 1, 4, and 8 bpp bitmaps is 2 to the power of the bpp. Thus, a 1 bpp bitmap has a maximum of two colors, the 4 bpp bitmap has a maximum of 16 colors, and the 8 bpp bitmap has a maximum of 256 colors.

Bitmaps that are 16-, 24-, or 32-bpp do not require color tables, but may have them to specify colors for palettized devices. If a color table is present for 16-, 24-, or 32-bpp bitmap, the **biClrUsed** member specifies the size of the color table and the color table must have that many colors in it. If **biClrUsed** is zero, there is no color table.

The red, green, and blue bitfield masks for BI\_BITFIELD bitmaps immediately follow the [**BITMAPINFOHEADER**](/windows/win32/api/wingdi/ns-wingdi-bitmapinfoheader), [**BITMAPV4HEADER**](/windows/desktop/api/Wingdi/ns-wingdi-bitmapv4header), and [**BITMAPV5HEADER**](/windows/desktop/api/Wingdi/ns-wingdi-bitmapv5header) structures. The **BITMAPV4HEADER** and **BITMAPV5HEADER** structures contain additional members for red, green, and blue masks as follows.



| Member        | Meaning                                                                                                                        |
|---------------|--------------------------------------------------------------------------------------------------------------------------------|
| **RedMask**   | Color mask that specifies the red component of each pixel, valid only if the **Compression** member is set to BI\_BITFIELDS.   |
| **GreenMask** | Color mask that specifies the green component of each pixel, valid only if the **Compression** member is set to BI\_BITFIELDS. |
| **BlueMask**  | Color mask that specifies the blue component of each pixel, valid only if the **Compression** member is set to BI\_BITFIELDS.  |



 

When the **biCompression** member of [**BITMAPINFOHEADER**](/windows/win32/api/wingdi/ns-wingdi-bitmapinfoheader) is set to BI\_BITFIELDS and the function receives an argument of type **LPBITMAPINFO**, the color masks will immediately follow the header. The color table, if present, will follow the color masks. [**BITMAPCOREHEADER**](/windows/win32/api/wingdi/ns-wingdi-bitmapcoreheader) bitmaps do not support color masks.

By default, bitmap data is bottom-up in its format. Bottom-up means that the first scan line in the bitmap data is the last scan line to be displayed. For example, the 0<sup>th</sup> pixel of the 0<sup>th</sup> scan line of the bitmap data of a 10-pixel by 10-pixel bitmap will be the 0<sup>th</sup> pixel of the 9<sup>th</sup> scan line of the displayed or printed image. Run-length encoded (RLE) format bitmaps and [**BITMAPCOREHEADER**](/windows/win32/api/wingdi/ns-wingdi-bitmapcoreheader) bitmaps cannot be top-down bitmaps. The scan lines are **DWORD** aligned, except for RLE-compressed bitmaps. They must be padded for scan line widths, in bytes, that are not evenly divisible by four, except for RLE compressed bitmaps. For example, a 10- by 10-pixel 24-bpp bitmap will have two padding bytes at the end of each scan line.

 

 
