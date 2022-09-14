---
title: Uncompressed Media Subtypes
description: Uncompressed Media Subtypes
ms.assetid: 5586e62a-d0f5-45cc-a690-4efa244b3f32
keywords:
- Windows Media Format SDK,media types
- Advanced Systems Format (ASF),media types
- ASF (Advanced Systems Format),media types
- Windows Media Format SDK,uncompressed media subtypes
- Advanced Systems Format (ASF),uncompressed media subtypes
- ASF (Advanced Systems Format),uncompressed media subtypes
- media types,uncompressed media subtypes
- uncompressed media subtypes
ms.topic: article
ms.date: 05/31/2018
---

# Uncompressed Media Subtypes

The following table lists the uncompressed media subtypes. These are types used as input and output formats, and formats for uncompressed streams. Not all of the types in the following tables are supported in all ways. Supported input and output format types can be enumerated by codec in the writer and reader/synchronous reader, respectively. For information about the types supported for uncompressed streams, see [Using Uncompressed Audio and Video Streams](using-uncompressed-audio-and-video-streams.md).

The various RGB and palettized RGB video types listed here define colors using the RGB format, in which each color is represented by the intensity values of the red, green, and blue components of the pixel. Each intensity value can range from 0 to 255, for about 16.78 million unique colors. RGB translates easily into color values used for computer monitors, which use red, green, and blue phosphors to display color. Palettized video types must include palette information directly following the [**WMVIDEOINFOHEADER**](/previous-versions/windows/desktop/api/wmsdkidl/ns-wmsdkidl-wmvideoinfoheader) structure. Likewise, 16 bit video requires bit field information, which should be included after the WMVIDEOINFOHEADER structure.

Several of the media subtypes in the following table provide fewer colors than the RGB system is capable of, as described in the Description column. In palettized RGB types, colors in the palette represent RGB values, but are specified by a value that indicates the position of the color in the palette.



| Uncompressed media subtype | Description                                                                                                                                                                                                              |
|----------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| WMMEDIASUBTYPE\_RGB1       | Palettized RGB video with 1 color bit representing 2 colors. Usually used for monochrome images.                                                                                                                         |
| WMMEDIASUBTYPE\_RGB4       | Palettized RGB video with 4 color bits representing 16 colors.                                                                                                                                                           |
| WMMEDIASUBTYPE\_RGB8       | Palettized RGB video with 8 color bits representing 256 colors.                                                                                                                                                          |
| WMMEDIASUBTYPE\_RGB565     | RGB video with 16 color bits representing 65,536 colors. This format uses 5 bits for red, 6 bits for green, and 5 bits for blue.                                                                                         |
| WMMEDIASUBTYPE\_RGB555     | RGB video with 16 color bits representing 32,768 colors. This format uses 5 bits for each color and ignores the sixteenth bit.                                                                                           |
| WMMEDIASUBTYPE\_RGB24      | RGB video with 24 color bits representing all 16,777,216 colors available to the RGB color representation scheme. This format uses 8 bits for each color intensity value.                                                |
| WMMEDIASUBTYPE\_RGB32      | RGB video with 32 color bits representing all 16,777,216 colors available to the RGB color representation scheme. This format uses 8 bits for each color and reserves the remaining 8 bits for transparency information. |
| WMMEDIASUBTYPE\_I420       | YUV video stored in planar 4:2:0 format, with the U plane appearing first, followed by the V plane.                                                                                                                      |
| WMMEDIASUBTYPE\_IYUV       | Identical to I420.                                                                                                                                                                                                       |
| WMMEDIASUBTYPE\_YV12       | YUV video stored in planar 4:2:0 format, with the V plane appearing first, followed by the U plane. YV12 is identical to I420 except that the U and V planes are switched.                                               |
| WMMEDIASUBTYPE\_YUY2       | YUV video stored in packed 4:2:2 format.                                                                                                                                                                                 |
| WMMEDIASUBTYPE\_UYVY       | YUV video stored in packed 4:2:2 format. Similar to YUY2 but with different ordering of data.                                                                                                                            |
| WMMEDIASUBTYPE\_YVYU       | YUV video stored in packed 4:2:2 format. Similar to YUY2 but with different ordering of data.                                                                                                                            |
| WMMEDIASUBTYPE\_P422       | YUV video stored using a planar 4:2:2 format.                                                                                                                                                                            |
| WMMEDIASUBTYPE\_YVU9       | YUV video stored in planar 16:1:1 format.                                                                                                                                                                                |
| WMMEDIASUBTYPE\_PCM        | Uncompressed audio data stored using pulse code modulation.                                                                                                                                                              |
| WMMEDIASUBTYPE\_DRM        | Uncompressed but encrypted audio data used with secure audio path.                                                                                                                                                       |
| WMSCRIPTTYPE\_TwoStrings   | Script commands consisting of a string containing the command type and a string containing the command data. This is the only supported script type in the Windows Media Format SDK.                                     |
| WMMEDIASUBTYPE\_WebStream  | File transfer data containing HTML files and components for Web streaming.                                                                                                                                               |
| WMMEDIASUBTYPE\_VIDEOIMAGE | Input type for the Windows Media Video 9 Image codec. Samples are a combination of bitmap images and transformation data.                                                                                                |



 

## Related topics

<dl> <dt>

[**Assigning Output Formats**](assigning-output-formats.md)
</dt> <dt>

[**Compressed Media Subtypes**](compressed-media-subtypes.md)
</dt> <dt>

[**Media Type Identifiers**](media-type-identifiers.md)
</dt> <dt>

[**Media Types**](media-types.md)
</dt> <dt>

[**To Enumerate Input Formats**](to-enumerate-input-formats.md)
</dt> </dl>

 

 




