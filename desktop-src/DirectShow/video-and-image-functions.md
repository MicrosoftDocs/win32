---
Description: Video and Image Functions
ms.assetid: 02401edc-362b-4f6c-b10b-c46b30b3ebe7
title: Video and Image Functions
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Video and Image Functions

These functions and macros manipulate the DirectShow video format structures.



| Function                                                             | Description                                                                                                                                                       |
|----------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**BIT\_MASKS\_MATCH**](/windows/win32/Amvideo/nf-amvideo-bit_masks_match?branch=master)                         | Compares the color masks for two [**VIDEOINFO**](/windows/win32/amvideo/ns-amvideo-tagvideoinfo?branch=master) structures.                                                                                       |
| [**BITMASKS**](/windows/win32/Amvideo/nf-amvideo-bitmasks?branch=master)                                         | Retrieves the color masks from a [**VIDEOINFO**](/windows/win32/amvideo/ns-amvideo-tagvideoinfo?branch=master) structure                                                                                         |
| [**CheckVideoInfoType**](checkvideoinfotype.md)                     | Checks a media type that contains a [**VIDEOINFOHEADER**](/windows/win32/amvideo/ns-amvideo-tagvideoinfoheader?branch=master) format structure for errors that can cause buffer overruns or integer overflows.   |
| [**CheckVideoInfo2Type**](checkvideoinfo2type.md)                   | Checks a media type that contains a [**VIDEOINFOHEADER2**](/windows/win32/Dvdmedia/ns-dvdmedia-tagvideoinfoheader2?branch=master) format structure for errors that can cause buffer overruns or integer overflows. |
| [**COLORS**](/windows/win32/Amvideo/nf-amvideo-colors?branch=master)                                             | Retrieves the palette entries from a [**VIDEOINFO**](/windows/win32/amvideo/ns-amvideo-tagvideoinfo?branch=master) structure                                                                                     |
| [**ContainsPalette**](containspalette.md)                           | Determines whether a specified [**VIDEOINFOHEADER**](/windows/win32/amvideo/ns-amvideo-tagvideoinfoheader?branch=master) structure contains a palette.                                                           |
| [**ConvertVideoInfoToVideoInfo2**](convertvideoinfotovideoinfo2.md) | Converts a media type that uses [**VIDEOINFOHEADER**](/windows/win32/amvideo/ns-amvideo-tagvideoinfoheader?branch=master) to one that uses [**VIDEOINFOHEADER2**](/windows/win32/Dvdmedia/ns-dvdmedia-tagvideoinfoheader2?branch=master)                          |
| [**DIBSIZE**](/windows/win32/Amvideo/nf-amvideo-dibsize?branch=master)                                           | Calculates the number of bytes required by a device-independent bitmap (DIB).                                                                                     |
| [**GetBitCount**](getbitcount.md)                                   | Returns the number of bits per pixel used by a specified video subtype.                                                                                           |
| [**GetBitmapFormatSize**](getbitmapformatsize.md)                   | Calculates the size needed for a [**VIDEOINFO**](/windows/win32/amvideo/ns-amvideo-tagvideoinfo?branch=master) structure that can hold a specified [**BITMAPINFOHEADER**](/windows/win32/WinGDI/ns-wingdi-tagbitmapinfoheader?branch=master) structure.       |
| [**GetBitmapPalette**](getbitmappalette.md)                         | Returns the first palette entry in a [**VIDEOINFOHEADER**](/windows/win32/amvideo/ns-amvideo-tagvideoinfoheader?branch=master) structure.                                                                        |
| [**GetBitmapSize**](getbitmapsize.md)                               | Calculates the number of bytes required by a device-independent bitmap (DIB).                                                                                     |
| [**GetBitmapSubtype**](getbitmapsubtype.md)                         | Returns the media subtype **GUID** for the specified bitmap.                                                                                                      |
| [**GetSubtypeName**](getsubtypename.md)                             | Retrieves the human-readable name of a video subtype.                                                                                                             |
| [**GetTrueColorType**](gettruecolortype.md)                         | Returns the media subtype **GUID** for a 16-bit uncompressed RGB bitmap.                                                                                          |
| [**HEADER**](/windows/win32/Amvideo/nf-amvideo-header?branch=master)                                             | Returns the address of the [**BITMAPINFOHEADER**](/windows/win32/WinGDI/ns-wingdi-tagbitmapinfoheader?branch=master) within a [**VIDEOINFOHEADER**](/windows/win32/amvideo/ns-amvideo-tagvideoinfoheader?branch=master).                                      |
| [**MPEG1\_SEQUENCE\_INFO**](/windows/win32/dvdmedia/nf-dvdmedia-mpeg1_sequence_info?branch=master)                 | Returns the address of the sequence header inside an [**MPEG1VIDEOINFO**](/windows/win32/amvideo/ns-amvideo-tagmpeg1videoinfo?branch=master) structure.                                                          |
| [**PALETTISED**](/windows/win32/Amvideo/nf-amvideo-palettised?branch=master)                                     | Checks whether a bitmap has a color depth of 8 bits or less.                                                                                                      |
| [**PALETTE\_ENTRIES**](/windows/win32/Amvideo/nf-amvideo-palette_entries?branch=master)                          | Retrieves the maximum number of colors in the palette of a specified bitmap.                                                                                      |
| [**RESET\_MASKS**](/windows/win32/Amvideo/nf-amvideo-reset_masks?branch=master)                                  | Fills the color mask fields in a [**VIDEOINFO**](/windows/win32/amvideo/ns-amvideo-tagvideoinfo?branch=master) structure with zeroes.                                                                            |
| [**RESET\_HEADER**](/windows/win32/Amvideo/nf-amvideo-reset_header?branch=master)                                | Fills a [**VIDEOINFOHEADER**](/windows/win32/amvideo/ns-amvideo-tagvideoinfoheader?branch=master) with zeroes.                                                                                                   |
| [**RESET\_PALETTE**](/windows/win32/Amvideo/nf-amvideo-reset_palette?branch=master)                              | Fills the palette entries in a [**VIDEOINFO**](/windows/win32/amvideo/ns-amvideo-tagvideoinfo?branch=master) structure with zeroes.                                                                              |
| [**SIZE\_EGA\_PALETTE**](/windows/win32/Amvideo/?branch=master)                       | Calculates the size needed for the palette entries in a 4-bit RGB bitmap.                                                                                         |
| [**SIZE\_MASKS**](/windows/win32/Amvideo/?branch=master)                                    | Calculates the size of the color masks in a [**VIDEOINFO**](/windows/win32/amvideo/ns-amvideo-tagvideoinfo?branch=master) structure.                                                                             |
| [**SIZE\_MPEG1VIDEOINFO**](/windows/win32/Amvideo/nf-amvideo-size_mpeg1videoinfo?branch=master)                  | Calculates the size of an [**MPEG1VIDEOINFO**](/windows/win32/amvideo/ns-amvideo-tagmpeg1videoinfo?branch=master) structure, including the sequence header.                                                      |
| [**SIZE\_PALETTE**](/windows/win32/Amvideo/?branch=master)                                | calculates the size of the palette entries in a [**VIDEOINFO**](/windows/win32/amvideo/ns-amvideo-tagvideoinfo?branch=master) structure.                                                                         |
| [**SIZE\_PREHEADER**](/windows/win32/Amvideo/?branch=master)                            | Calculates the byte offset of the **bmiHeader** field within a [**VIDEOINFOHEADER**](/windows/win32/amvideo/ns-amvideo-tagvideoinfoheader?branch=master) structure.                                              |
| [**SIZE\_VIDEOHEADER**](/windows/win32/Amvideo/?branch=master)                        | Calculates the size of the [**VIDEOINFOHEADER**](/windows/win32/amvideo/ns-amvideo-tagvideoinfoheader?branch=master) structure.                                                                                  |
| [**TRUECOLOR**](/windows/win32/Amvideo/?branch=master)                                   | Returns the [**TRUECOLORINFO**](/windows/win32/amvideo/ns-amvideo-tag_truecolorinfo?branch=master) structure from a [**VIDEOINFO**](/windows/win32/amvideo/ns-amvideo-tagvideoinfo?branch=master) structure.                                            |
| [**ValidateBitmapInfoHeader**](validatebitmapinfoheader.md)         | Checks a [**BITMAPINFOHEADER**](/windows/win32/WinGDI/ns-wingdi-tagbitmapinfoheader?branch=master) structure for errors that can cause buffer overruns or integer overflows.                                   |



 

## Remarks

Most of the macros and functions described in the section are designed for manipulating **VIDEOINFOHEADER** and **VIDEOINFO** structures for RGB bitmaps. Use these macros with care: Most of them assume that the specified structure has been initialized properly. Many of them also assume that the **BITMAPINFOHEADER** structure is the standard size; that is, `biSize == sizeof(BITMAPINFOHEADER)`.

The DirectShow base class library also provide the following global constants, which define the standard color masks for true-color bitmaps.



| Global Data | Description                                                   |
|-------------|---------------------------------------------------------------|
| **bits555** | Array of color masks for a 16-bit RGB bitmap in 5-5-5 format. |
| **bits565** | Array of color masks for a 16-bit RGB bitmap in 5-6-5 format. |
| **bits888** | Array of color masks for a 24-bit RGB bitmap.                 |



 

Each of these constants in an array of three **DWORD**s, containing the red, green, and blue masks, in that order.

 

 



