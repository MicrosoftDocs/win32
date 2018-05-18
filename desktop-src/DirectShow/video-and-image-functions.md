---
Description: Video and Image Functions
ms.assetid: '02401edc-362b-4f6c-b10b-c46b30b3ebe7'
title: Video and Image Functions
---

# Video and Image Functions

These functions and macros manipulate the DirectShow video format structures.



| Function                                                             | Description                                                                                                                                                       |
|----------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**BIT\_MASKS\_MATCH**](bit-masks-match.md)                         | Compares the color masks for two [**VIDEOINFO**](videoinfo.md) structures.                                                                                       |
| [**BITMASKS**](bitmasks.md)                                         | Retrieves the color masks from a [**VIDEOINFO**](videoinfo.md) structure                                                                                         |
| [**CheckVideoInfoType**](checkvideoinfotype.md)                     | Checks a media type that contains a [**VIDEOINFOHEADER**](videoinfoheader.md) format structure for errors that can cause buffer overruns or integer overflows.   |
| [**CheckVideoInfo2Type**](checkvideoinfo2type.md)                   | Checks a media type that contains a [**VIDEOINFOHEADER2**](videoinfoheader2.md) format structure for errors that can cause buffer overruns or integer overflows. |
| [**COLORS**](colors.md)                                             | Retrieves the palette entries from a [**VIDEOINFO**](videoinfo.md) structure                                                                                     |
| [**ContainsPalette**](containspalette.md)                           | Determines whether a specified [**VIDEOINFOHEADER**](videoinfoheader.md) structure contains a palette.                                                           |
| [**ConvertVideoInfoToVideoInfo2**](convertvideoinfotovideoinfo2.md) | Converts a media type that uses [**VIDEOINFOHEADER**](videoinfoheader.md) to one that uses [**VIDEOINFOHEADER2**](videoinfoheader2.md)                          |
| [**DIBSIZE**](dibsize.md)                                           | Calculates the number of bytes required by a device-independent bitmap (DIB).                                                                                     |
| [**GetBitCount**](getbitcount.md)                                   | Returns the number of bits per pixel used by a specified video subtype.                                                                                           |
| [**GetBitmapFormatSize**](getbitmapformatsize.md)                   | Calculates the size needed for a [**VIDEOINFO**](videoinfo.md) structure that can hold a specified [**BITMAPINFOHEADER**](bitmapinfoheader.md) structure.       |
| [**GetBitmapPalette**](getbitmappalette.md)                         | Returns the first palette entry in a [**VIDEOINFOHEADER**](videoinfoheader.md) structure.                                                                        |
| [**GetBitmapSize**](getbitmapsize.md)                               | Calculates the number of bytes required by a device-independent bitmap (DIB).                                                                                     |
| [**GetBitmapSubtype**](getbitmapsubtype.md)                         | Returns the media subtype **GUID** for the specified bitmap.                                                                                                      |
| [**GetSubtypeName**](getsubtypename.md)                             | Retrieves the human-readable name of a video subtype.                                                                                                             |
| [**GetTrueColorType**](gettruecolortype.md)                         | Returns the media subtype **GUID** for a 16-bit uncompressed RGB bitmap.                                                                                          |
| [**HEADER**](header.md)                                             | Returns the address of the [**BITMAPINFOHEADER**](bitmapinfoheader.md) within a [**VIDEOINFOHEADER**](videoinfoheader.md).                                      |
| [**MPEG1\_SEQUENCE\_INFO**](mpeg1-sequence-info.md)                 | Returns the address of the sequence header inside an [**MPEG1VIDEOINFO**](mpeg1videoinfo.md) structure.                                                          |
| [**PALETTISED**](palettised.md)                                     | Checks whether a bitmap has a color depth of 8 bits or less.                                                                                                      |
| [**PALETTE\_ENTRIES**](palette-entries.md)                          | Retrieves the maximum number of colors in the palette of a specified bitmap.                                                                                      |
| [**RESET\_MASKS**](reset-masks.md)                                  | Fills the color mask fields in a [**VIDEOINFO**](videoinfo.md) structure with zeroes.                                                                            |
| [**RESET\_HEADER**](reset-header.md)                                | Fills a [**VIDEOINFOHEADER**](videoinfoheader.md) with zeroes.                                                                                                   |
| [**RESET\_PALETTE**](reset-palette.md)                              | Fills the palette entries in a [**VIDEOINFO**](videoinfo.md) structure with zeroes.                                                                              |
| [**SIZE\_EGA\_PALETTE**](size-ega-palette.md)                       | Calculates the size needed for the palette entries in a 4-bit RGB bitmap.                                                                                         |
| [**SIZE\_MASKS**](size-masks.md)                                    | Calculates the size of the color masks in a [**VIDEOINFO**](videoinfo.md) structure.                                                                             |
| [**SIZE\_MPEG1VIDEOINFO**](size-mpeg1videoinfo.md)                  | Calculates the size of an [**MPEG1VIDEOINFO**](mpeg1videoinfo.md) structure, including the sequence header.                                                      |
| [**SIZE\_PALETTE**](size-palette.md)                                | calculates the size of the palette entries in a [**VIDEOINFO**](videoinfo.md) structure.                                                                         |
| [**SIZE\_PREHEADER**](size-preheader.md)                            | Calculates the byte offset of the **bmiHeader** field within a [**VIDEOINFOHEADER**](videoinfoheader.md) structure.                                              |
| [**SIZE\_VIDEOHEADER**](size-videoheader.md)                        | Calculates the size of the [**VIDEOINFOHEADER**](videoinfoheader.md) structure.                                                                                  |
| [**TRUECOLOR**](truecolorinfo.md)                                   | Returns the [**TRUECOLORINFO**](truecolorinfostructure.md) structure from a [**VIDEOINFO**](videoinfo.md) structure.                                            |
| [**ValidateBitmapInfoHeader**](validatebitmapinfoheader.md)         | Checks a [**BITMAPINFOHEADER**](bitmapinfoheader.md) structure for errors that can cause buffer overruns or integer overflows.                                   |



 

## Remarks

Most of the macros and functions described in the section are designed for manipulating **VIDEOINFOHEADER** and **VIDEOINFO** structures for RGB bitmaps. Use these macros with care: Most of them assume that the specified structure has been initialized properly. Many of them also assume that the **BITMAPINFOHEADER** structure is the standard size; that is, `biSize == sizeof(BITMAPINFOHEADER)`.

The DirectShow base class library also provide the following global constants, which define the standard color masks for true-color bitmaps.



| Global Data | Description                                                   |
|-------------|---------------------------------------------------------------|
| **bits555** | Array of color masks for a 16-bit RGB bitmap in 5-5-5 format. |
| **bits565** | Array of color masks for a 16-bit RGB bitmap in 5-6-5 format. |
| **bits888** | Array of color masks for a 24-bit RGB bitmap.                 |



 

Each of these constants in an array of three **DWORD**s, containing the red, green, and blue masks, in that order.

 

 



