---
description: Video and Image Functions
ms.assetid: 02401edc-362b-4f6c-b10b-c46b30b3ebe7
title: Video and Image Functions
ms.topic: article
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# Video and Image Functions

\[The feature associated with this page, [DirectShow](/windows/win32/directshow/directshow), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer), [IMFMediaEngine](/windows/win32/api/mfmediaengine/nn-mfmediaengine-imfmediaengine), and [Audio/Video Capture in Media Foundation](windows/win32/medfound/audio-video-capture-in-media-foundation). Those features have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer**, **IMFMediaEngine** and **Audio/Video Capture in Media Foundation** instead of **DirectShow**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

These functions and macros manipulate the DirectShow video format structures.



| Function                                                             | Description                                                                                                                                                       |
|----------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**BIT\_MASKS\_MATCH**](/previous-versions/windows/desktop/api/Amvideo/nf-amvideo-bit_masks_match)                         | Compares the color masks for two [**VIDEOINFO**](/previous-versions/windows/desktop/api/amvideo/ns-amvideo-videoinfo) structures.                                                                                       |
| [**BITMASKS**](/previous-versions/windows/desktop/api/Amvideo/nf-amvideo-bitmasks)                                         | Retrieves the color masks from a [**VIDEOINFO**](/previous-versions/windows/desktop/api/amvideo/ns-amvideo-videoinfo) structure                                                                                         |
| [**CheckVideoInfoType**](checkvideoinfotype.md)                     | Checks a media type that contains a [**VIDEOINFOHEADER**](/previous-versions/windows/desktop/api/amvideo/ns-amvideo-videoinfoheader) format structure for errors that can cause buffer overruns or integer overflows.   |
| [**CheckVideoInfo2Type**](checkvideoinfo2type.md)                   | Checks a media type that contains a [**VIDEOINFOHEADER2**](/previous-versions/windows/desktop/api/dvdmedia/ns-dvdmedia-videoinfoheader2) format structure for errors that can cause buffer overruns or integer overflows. |
| [**COLORS**](/previous-versions/windows/desktop/api/Amvideo/nf-amvideo-colors)                                             | Retrieves the palette entries from a [**VIDEOINFO**](/previous-versions/windows/desktop/api/amvideo/ns-amvideo-videoinfo) structure                                                                                     |
| [**ContainsPalette**](containspalette.md)                           | Determines whether a specified [**VIDEOINFOHEADER**](/previous-versions/windows/desktop/api/amvideo/ns-amvideo-videoinfoheader) structure contains a palette.                                                           |
| [**ConvertVideoInfoToVideoInfo2**](convertvideoinfotovideoinfo2.md) | Converts a media type that uses [**VIDEOINFOHEADER**](/previous-versions/windows/desktop/api/amvideo/ns-amvideo-videoinfoheader) to one that uses [**VIDEOINFOHEADER2**](/previous-versions/windows/desktop/api/dvdmedia/ns-dvdmedia-videoinfoheader2)                          |
| [**DIBSIZE**](/previous-versions/windows/desktop/api/Amvideo/nf-amvideo-dibsize)                                           | Calculates the number of bytes required by a device-independent bitmap (DIB).                                                                                     |
| [**GetBitCount**](getbitcount.md)                                   | Returns the number of bits per pixel used by a specified video subtype.                                                                                           |
| [**GetBitmapFormatSize**](getbitmapformatsize.md)                   | Calculates the size needed for a [**VIDEOINFO**](/previous-versions/windows/desktop/api/amvideo/ns-amvideo-videoinfo) structure that can hold a specified [**BITMAPINFOHEADER**](/windows/win32/api/wingdi/ns-wingdi-bitmapinfoheader) structure.       |
| [**GetBitmapPalette**](getbitmappalette.md)                         | Returns the first palette entry in a [**VIDEOINFOHEADER**](/previous-versions/windows/desktop/api/amvideo/ns-amvideo-videoinfoheader) structure.                                                                        |
| [**GetBitmapSize**](getbitmapsize.md)                               | Calculates the number of bytes required by a device-independent bitmap (DIB).                                                                                     |
| [**GetBitmapSubtype**](getbitmapsubtype.md)                         | Returns the media subtype **GUID** for the specified bitmap.                                                                                                      |
| [**GetSubtypeName**](getsubtypename.md)                             | Retrieves the human-readable name of a video subtype.                                                                                                             |
| [**GetTrueColorType**](gettruecolortype.md)                         | Returns the media subtype **GUID** for a 16-bit uncompressed RGB bitmap.                                                                                          |
| [**HEADER**](/previous-versions/windows/desktop/api/Amvideo/nf-amvideo-header)                                             | Returns the address of the [**BITMAPINFOHEADER**](/windows/win32/api/wingdi/ns-wingdi-bitmapinfoheader) within a [**VIDEOINFOHEADER**](/previous-versions/windows/desktop/api/amvideo/ns-amvideo-videoinfoheader).                                      |
| [**MPEG1\_SEQUENCE\_INFO**](/previous-versions/windows/desktop/api/amvideo/nf-amvideo-mpeg1_sequence_info)                 | Returns the address of the sequence header inside an [**MPEG1VIDEOINFO**](/previous-versions/windows/desktop/api/amvideo/ns-amvideo-mpeg1videoinfo) structure.                                                          |
| [**PALETTISED**](/previous-versions/windows/desktop/api/Amvideo/nf-amvideo-palettised)                                     | Checks whether a bitmap has a color depth of 8 bits or less.                                                                                                      |
| [**PALETTE\_ENTRIES**](/previous-versions/windows/desktop/api/Amvideo/nf-amvideo-palette_entries)                          | Retrieves the maximum number of colors in the palette of a specified bitmap.                                                                                      |
| [**RESET\_MASKS**](/previous-versions/windows/desktop/api/Amvideo/nf-amvideo-reset_masks)                                  | Fills the color mask fields in a [**VIDEOINFO**](/previous-versions/windows/desktop/api/amvideo/ns-amvideo-videoinfo) structure with zeroes.                                                                            |
| [**RESET\_HEADER**](/previous-versions/windows/desktop/api/Amvideo/nf-amvideo-reset_header)                                | Fills a [**VIDEOINFOHEADER**](/previous-versions/windows/desktop/api/amvideo/ns-amvideo-videoinfoheader) with zeroes.                                                                                                   |
| [**RESET\_PALETTE**](/previous-versions/windows/desktop/api/Amvideo/nf-amvideo-reset_palette)                              | Fills the palette entries in a [**VIDEOINFO**](/previous-versions/windows/desktop/api/amvideo/ns-amvideo-videoinfo) structure with zeroes.                                                                              |
| [**SIZE\_EGA\_PALETTE**](/previous-versions/windows/desktop/legacy/dd377602(v=vs.85))                       | Calculates the size needed for the palette entries in a 4-bit RGB bitmap.                                                                                         |
| [**SIZE\_MASKS**](/previous-versions/windows/desktop/legacy/dd377603(v=vs.85))                                    | Calculates the size of the color masks in a [**VIDEOINFO**](/previous-versions/windows/desktop/api/amvideo/ns-amvideo-videoinfo) structure.                                                                             |
| [**SIZE\_MPEG1VIDEOINFO**](/previous-versions/windows/desktop/api/Amvideo/nf-amvideo-size_mpeg1videoinfo)                  | Calculates the size of an [**MPEG1VIDEOINFO**](/previous-versions/windows/desktop/api/amvideo/ns-amvideo-mpeg1videoinfo) structure, including the sequence header.                                                      |
| [**SIZE\_PALETTE**](/previous-versions/windows/desktop/legacy/dd377605(v=vs.85))                                | calculates the size of the palette entries in a [**VIDEOINFO**](/previous-versions/windows/desktop/api/amvideo/ns-amvideo-videoinfo) structure.                                                                         |
| [**SIZE\_PREHEADER**](/previous-versions/windows/desktop/legacy/dd377606(v=vs.85))                            | Calculates the byte offset of the **bmiHeader** field within a [**VIDEOINFOHEADER**](/previous-versions/windows/desktop/api/amvideo/ns-amvideo-videoinfoheader) structure.                                              |
| [**SIZE\_VIDEOHEADER**](/previous-versions/windows/desktop/legacy/dd377607(v=vs.85))                        | Calculates the size of the [**VIDEOINFOHEADER**](/previous-versions/windows/desktop/api/amvideo/ns-amvideo-videoinfoheader) structure.                                                                                  |
| [**TRUECOLOR**](/previous-versions/windows/desktop/legacy/dd407230(v=vs.85))                                   | Returns the [**TRUECOLORINFO**](/previous-versions/windows/desktop/api/amvideo/ns-amvideo-truecolorinfo) structure from a [**VIDEOINFO**](/previous-versions/windows/desktop/api/amvideo/ns-amvideo-videoinfo) structure.                                            |
| [**ValidateBitmapInfoHeader**](validatebitmapinfoheader.md)         | Checks a [**BITMAPINFOHEADER**](/windows/win32/api/wingdi/ns-wingdi-bitmapinfoheader) structure for errors that can cause buffer overruns or integer overflows.                                   |



 

## Remarks

Most of the macros and functions described in the section are designed for manipulating **VIDEOINFOHEADER** and **VIDEOINFO** structures for RGB bitmaps. Use these macros with care: Most of them assume that the specified structure has been initialized properly. Many of them also assume that the **BITMAPINFOHEADER** structure is the standard size; that is, `biSize == sizeof(BITMAPINFOHEADER)`.

The DirectShow base class library also provide the following global constants, which define the standard color masks for true-color bitmaps.



| Global Data | Description                                                   |
|-------------|---------------------------------------------------------------|
| **bits555** | Array of color masks for a 16-bit RGB bitmap in 5-5-5 format. |
| **bits565** | Array of color masks for a 16-bit RGB bitmap in 5-6-5 format. |
| **bits888** | Array of color masks for a 24-bit RGB bitmap.                 |



 

Each of these constants in an array of three **DWORD**s, containing the red, green, and blue masks, in that order.

 

 
