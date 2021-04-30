---
description: 'YUV formats are categorized according to the following information:'
ms.assetid: 452f017c-81ce-4be4-9962-4b9c1a9ce849
title: YUV Video Subtypes (Dshow.h)
ms.topic: reference
ms.date: 05/31/2018
---

# YUV Video Subtypes

YUV formats are categorized according to the following information:

**Packed formats versus planar formats.** In a packed format, the Y, U, and V components are stored in a single array. Pixels are organized into groups of macropixels, whose layout depends on the format. In a planar format, the Y, U, and V components are stored separately, as three planes.

**Chroma sampling.** A notation called the A:B:C notation is used to describe how often U and V are sampled relative to Y:

-   4:4:4 means no downsampling of the chroma channels.
-   4:2:2 means 2:1 horizontal downsampling, with no vertical downsampling. Every scan line contains four Y samples for every two U or V samples.
-   4:2:0 means 2:1 horizontal downsampling, with 2:1 vertical downsampling.
-   4:1:1 means 4:1 horizontal downsampling, with no vertical downsampling. Every scan line contains four Y samples for every U or V sample. 4:1:1 sampling is less common than other formats, and is not discussed in detail in this article.

**Bits per channel.** The most common sample sizes are 8, 10, or 16 bits per sample. Some YUV formats are palettized.

**Memory layout.** Two YUV format types can be otherwise identical but use different orderings for the Y, V, and U samples in memory.

**Recommended YUV Formats**



| GUID               | Format | Sampling | Packed or planar | Bits per channel |
|--------------------|--------|----------|------------------|------------------|
| MEDIASUBTYPE\_AYUV | AYUV   | 4:4:4    | Packed           | 8                |
| MEDIASUBTYPE\_YUY2 | YUY2   | 4:2:2    | Packed           | 8                |
| MEDIASUBTYPE\_UYVY | UYVY   | 4:2:2    | Packed           | 8                |
| MEDIASUBTYPE\_IMC1 | IMC1   | 4:2:0    | Planar           | 8                |
| MEDIASUBTYPE\_IMC3 | IMC2   | 4:2:0    | Planar           | 8                |
| MEDIASUBTYPE\_IMC2 | IMC3   | 4:2:0    | Planar           | 8                |
| MEDIASUBTYPE\_IMC4 | IMC4   | 4:2:0    | Planar           | 8                |
| MEDIASUBTYPE\_YV12 | YV12   | 4:2:0    | Planar           | 8                |
| MEDIASUBTYPE\_NV12 | NV12   | 4:2:0    | Planar           | 8                |



 

For a description of theses YUV formats for video rendering on Windows, see [Recommended 8-Bit YUV Formats for Video Rendering](../medfound/recommended-8-bit-yuv-formats-for-video-rendering.md) .

**Other YUV Format Types**



| GUID               | Format                                                | Sampling                                                | Packed or planar                                  | Bits per channel                             |
|--------------------|-------------------------------------------------------|---------------------------------------------------------|---------------------------------------------------|----------------------------------------------|
| MEDIASUBTYPE\_I420 | I420                                                  | 4:2:0                                                   | Planar                                            | 8                                            |
| MEDIASUBTYPE\_IF09 | No longer supported.<br/> Indeo YVU9<br/> | No longer supported.<br/> See remarks.<br/> | No longer supported.<br/> Planar<br/> | No longer supported.<br/> 8<br/> |
| MEDIASUBTYPE\_IYUV | IYUV                                                  | 4:2:0                                                   | Planar                                            | 8                                            |
| MEDIASUBTYPE\_Y211 | Y211                                                  | See remarks.                                            | Packed                                            | 8                                            |
| MEDIASUBTYPE\_Y411 | Y411                                                  | 4:1:1                                                   | Packed                                            | 8                                            |
| MEDIASUBTYPE\_Y41P | Y41P                                                  | 4:1:1                                                   | Packed                                            | 8                                            |
| MEDIASUBTYPE\_YVU9 | YVU9                                                  | See remarks.                                            | Planar                                            | 8                                            |
| MEDIASUBTYPE\_YVYU | YVYU                                                  | 4:2:2                                                   | Packed                                            | 8                                            |



 

-   I420 consists of a Y plane, followed by a U plane, followed by a V plane.
-   IYUV is identical to I420.
-   Y211 is a packed format, in which Y is sampled every 2 pixels horizontally, and U and V are sampled every 4 pixels horizontally. Each macropixel is 4 bytes and contains 4 pixels. It uses the following byte order:

    `Y0 U0 Y2 V0    Y4 U4 Y6 V4    Y8 U8 Y10 V8`

-   Y41P is a 4:1:1 packed format. It uses the following byte order:

    `U0 Y0 V0 Y1    U4 Y2 V4 Y3    Y4 Y5 Y6 Y7`

-   YVU9 is a planar format, in which U and V are sampled every 4 pixels horizontally and vertically (sometimes referred to as 16:1:1). The V plane appears before the U plane.
-   The Indeo YVU9 format (MEDIASUBTYPE\_IF09) is a variation of YVU9 with additional delta-frame information after the U plane. The Indeo codec is no longer supported in Windows.
-   YVYU is similar to UYVY with a different byte order: `Y0 V0 Y1 U0`

-   The Indeo codec is no longer supported in Windows.

## Requirements



| Requirement | Value |
|-------------------|------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Dshow.h</dt> </dl> |



## See also

<dl> <dt>

[Recommended 8-Bit YUV Formats for Video Rendering](../medfound/recommended-8-bit-yuv-formats-for-video-rendering.md)
</dt> <dt>

[Video Subtypes](video-subtypes.md)
</dt> <dt>

[Working with Video Frames](working-with-video-frames.md)
</dt> </dl>

 

 
