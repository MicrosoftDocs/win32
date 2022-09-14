---
description: The following video subtype GUIDs are defined in the header file mfapi.h. To specify the subtype, set the MF\_MT\_SUBTYPE attribute on the media type.
ms.assetid: 7dfd85e6-936e-4b78-a2cb-a5d59153e1c4
title: Video Subtype GUIDs
ms.topic: article
ms.date: 05/31/2018
---

# Video Subtype GUIDs

The following video subtype GUIDs are defined in the header file mfapi.h. To specify the subtype, set the [**MF\_MT\_SUBTYPE**](mf-mt-subtype-attribute.md) attribute on the media type.

When these subtypes are used, set the [MF\_MT\_MAJOR\_TYPE](mf-mt-major-type-attribute.md) attribute to **MFMediaType\_Video**.

-   [Uncompressed RGB Formats](#uncompressed-rgb-formats)
-   [YUV Formats: 8-Bit and Palettized](#yuv-formats-8-bit-and-palettized)
-   [YUV Formats: 10-Bit and 16-Bit](#yuv-formats-10-bit-and-16-bit)
-   [Luminance and Depth Formats](#luminance-and-depth-formats)
-   [Encoded Video Types](#encoded-video-types)
-   [Creating Subtype GUIDs from FOURCCs and D3DFORMAT Values](#creating-subtype-guids-from-fourccs-and-d3dformat-values)
-   [Related topics](#related-topics)

## Uncompressed RGB Formats



| GUID                             | Description                                                                                     |
|----------------------------------|-------------------------------------------------------------------------------------------------|
| **MFVideoFormat\_RGB8**          | RGB, 8 bits per pixel (bpp). (Same memory layout as **D3DFMT\_P8**.)                            |
| **MFVideoFormat\_RGB555**        | RGB 555, 16 bpp. (Same memory layout as **D3DFMT\_X1R5G5B5**.)                                  |
| **MFVideoFormat\_RGB565**        | RGB 565, 16 bpp. (Same memory layout as **D3DFMT\_R5G6B5**.)                                    |
| **MFVideoFormat\_RGB24**         | RGB, 24 bpp.                                                                                    |
| **MFVideoFormat\_RGB32**         | RGB, 32 bpp.                                                                                    |
| **MFVideoFormat\_ARGB32**        | RGB, 32 bpp with alpha channel.                                                                 |
| **MFVideoFormat\_A2R10G10B10**   | RGB, 10 bpp for each color and 2 bpp for alpha. (Same memory layout as **D3DFMT\_A2B10G10R10**) |
| **MFVideoFormat\_A16B16G16R16F** | RGB, 16 bpp with alpha channel. (Same memory layout as **D3DFMT\_A16B16G16R16F**)               |



 

> [!Note]  
> These subtypes do not match the RGB subtype GUIDs used in previous SDKs, such as DirectShow.

 

## YUV Formats: 8-Bit and Palettized



| GUID                    | Format | Sampling | Packed or planar | Bits per channel |
|-------------------------|--------|----------|------------------|------------------|
| **MFVideoFormat\_AI44** | AI44   | 4:4:4    | Packed           | Palettized       |
| **MFVideoFormat\_AYUV** | AYUV   | 4:4:4    | Packed           | 8                |
| **MFVideoFormat\_I420** | I420   | 4:2:0    | Planar           | 8                |
| **MFVideoFormat\_IYUV** | IYUV   | 4:2:0    | Planar           | 8                |
| **MFVideoFormat\_NV11** | NV11   | 4:1:1    | Planar           | 8                |
| **MFVideoFormat\_NV12** | NV12   | 4:2:0    | Planar           | 8                |
| **MFVideoFormat\_NV21** | NV21   | 4:2:0    | Planar           | 8                |
| **MFVideoFormat\_UYVY** | UYVY   | 4:2:2    | Packed           | 8                |
| **MFVideoFormat\_Y41P** | Y41P   | 4:1:1    | Packed           | 8                |
| **MFVideoFormat\_Y41T** | Y41T   | 4:1:1    | Packed           | 8                |
| **MFVideoFormat\_Y42T** | Y42T   | 4:2:2    | Packed           | 8                |
| **MFVideoFormat\_YUY2** | YUY2   | 4:2:2    | Packed           | 8                |
| **MFVideoFormat\_YVU9** | YVU9   | 8:4:4    | Planar           | 9                |
| **MFVideoFormat\_YV12** | YV12   | 4:2:0    | Planar           | 8                |
| **MFVideoFormat\_YVYU** | YVYU   | 4:2:2    | Packed           | 8                |



 

The recommended YUV formats are described in detail in the topic [Recommended 8-Bit YUV Formats for Video Rendering](recommended-8-bit-yuv-formats-for-video-rendering.md).

> [!Note]  
> I420 and IYUV have the same layout in memory, but are assigned distinct subtype GUIDs. The subtype GUIDs correspond to the FOURCC codes 'I420' and 'IYUV'; see [Video FOURCCs](video-fourccs.md) for more information.

 

## YUV Formats: 10-Bit and 16-Bit



| GUID                    | Format | Sampling | Packed or planar | Bits per channel |
|-------------------------|--------|----------|------------------|------------------|
| **MFVideoFormat\_P010** | P010   | 4:2:0    | Planar           | 10               |
| **MFVideoFormat\_P016** | P016   | 4:2:0    | Planar           | 16               |
| **MFVideoFormat\_P210** | P210   | 4:2:2    | Planar           | 10               |
| **MFVideoFormat\_P216** | P216   | 4:2:2    | Planar           | 16               |
| **MFVideoFormat\_v210** | v210   | 4:2:2    | Packed           | 10               |
| **MFVideoFormat\_v216** | v216   | 4:2:2    | Packed           | 16               |
| **MFVideoFormat\_v410** | v40    | 4:4:4    | Packed           | 10               |
| **MFVideoFormat\_Y210** | Y210   | 4:2:2    | Packed           | 10               |
| **MFVideoFormat\_Y216** | Y216   | 4:2:2    | Packed           | 16               |
| **MFVideoFormat\_Y410** | Y40    | 4:4:4    | Packed           | 10               |
| **MFVideoFormat\_Y416** | Y416   | 4:4:4    | Packed           | 16               |



 

For more information about these formats, see [10-bit and 16-bit YUV Video Formats](10-bit-and-16-bit-yuv-video-formats.md).

## Luminance and Depth Formats



| GUID                   | Description                                                          |
|------------------------|----------------------------------------------------------------------|
| **MFVideoFormat\_L8**  | 8-bit luminance only. (bpp). (Same memory layout as **D3DFMT\_L8**.) |
| **MFVideoFormat\_L16** | 16-bit luminance only. (Same memory layout as **D3DFMT\_L16**.)      |
| **MFVideoFormat\_D16** | 16-bit z-buffer depth. (Same memory layout as **D3DFMT\_D16**.)      |



 

## Encoded Video Types



| GUID                        | FOURCC         | Description                                                                                                                                                                                                                                                                                                 |
|-----------------------------|----------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **MFVideoFormat\_DV25**     | 'dv25'         | DVCPRO 25 (525-60 or 625-50).                                                                                                                                                                                                                                                                               |
| **MFVideoFormat\_DV50**     | 'dv50'         | DVCPRO 50 (525-60 or 625-50).                                                                                                                                                                                                                                                                               |
| **MFVideoFormat\_DVC**      | 'dvc '         | DVC/DV Video.                                                                                                                                                                                                                                                                                               |
| **MFVideoFormat\_DVH1**     | 'dvh1'         | DVCPRO 100 (1080/60i, 1080/50i, or 720/60P).                                                                                                                                                                                                                                                                |
| **MFVideoFormat\_DVHD**     | 'dvhd'         | HD-DVCR (1125-60 or 1250-50).                                                                                                                                                                                                                                                                               |
| **MFVideoFormat\_DVSD**     | 'dvsd'         | SDL-DVCR (525-60 or 625-50).                                                                                                                                                                                                                                                                                |
| **MFVideoFormat\_DVSL**     | 'dvsl'         | SD-DVCR (525-60 or 625-50).                                                                                                                                                                                                                                                                                 |
| **MFVideoFormat\_H263**     | 'H263'         | H.263 video.                                                                                                                                                                                                                                                                                                |
| **MFVideoFormat\_H264**     | 'H264'         | H.264 video.<br/> Media samples contain H.264 bitstream data with start codes and has interleaved SPS/PPS. Each sample contains one complete picture, either one field or one frame.<br/>                                                                                                       |
| **MFVideoFormat\_H265**     | 'H265'         | H.265 video.                                                                                                                                                                                                                                                                                                |
| **MFVideoFormat\_H264\_ES** | Not applicable | H.264 elementary stream.<br/> This media type is the same as **MFVideoFormat\_H264**, except media samples contain a fragmented H.264 bitstream. Each sample may contain a partial picture; multiple complete pictures; or one or more complete pictures plus a partial picture.<br/>           |
| **MFVideoFormat\_HEVC**     | 'HEVC'         | The HEVC Main profile and Main Still Picture profile.<br/> Each sample contains one complete picture.<br/> Supported in Windows 8.1 and later. The HEVC Main profile and Main Still Picture profile elementary stream. <br/>                                                              |
| **MFVideoFormat\_HEVC\_ES** | 'HEVS'         | This media type is the same as **MFVideoFormat\_HEVC**, except media samples contain a fragmented HEVC bitstream. Each sample may contain a partial picture; multiple complete pictures; or one or more complete pictures plus a partial picture.<br/> Supported in Windows 8.1 and later.<br/> |
| **MFVideoFormat\_M4S2**     | 'M4S2'         | MPEG-4 part 2 video.                                                                                                                                                                                                                                                                                        |
| **MFVideoFormat\_MJPG**     | 'MJPG'         | Motion JPEG.                                                                                                                                                                                                                                                                                                |
| **MFVideoFormat\_MP43**     | 'MP43'         | Microsoft MPEG 4 codec version 3. This codec is no longer supported.                                                                                                                                                                                                                                        |
| **MFVideoFormat\_MP4S**     | 'MP4S'         | ISO MPEG 4 codec version 1.                                                                                                                                                                                                                                                                                 |
| **MFVideoFormat\_MP4V**     | 'MP4V'         | MPEG-4 part 2 video.                                                                                                                                                                                                                                                                                        |
| **MFVideoFormat\_MPEG2**    | Not applicable | MPEG-2 video. (Equivalent to **MEDIASUBTYPE\_MPEG2\_VIDEO** in DirectShow.)                                                                                                                                                                                                                                 |
| **MFVideoFormat\_VP80**     | 'MPG1'         | VP8 video.                                                                                                                                                                                                                                                                                                  |
| **MFVideoFormat\_VP90**     | 'MPG1'         | VP9 video.                                                                                                                                                                                                                                                                                                  |
| **MFVideoFormat\_MPG1**     | 'MPG1'         | MPEG-1 video.                                                                                                                                                                                                                                                                                               |
| **MFVideoFormat\_MSS1**     | 'MSS1'         | Windows Media Screen codec version 1.                                                                                                                                                                                                                                                                       |
| **MFVideoFormat\_MSS2**     | 'MSS2'         | Windows Media Video 9 Screen codec.                                                                                                                                                                                                                                                                         |
| **MFVideoFormat\_WMV1**     | 'WMV1'         | Windows Media Video codec version 7.                                                                                                                                                                                                                                                                        |
| **MFVideoFormat\_WMV2**     | 'WMV2'         | Windows Media Video 8 codec.                                                                                                                                                                                                                                                                                |
| **MFVideoFormat\_WMV3**     | 'WMV3'         | Windows Media Video 9 codec.                                                                                                                                                                                                                                                                                |
| **MFVideoFormat\_WVC1**     | 'WVC1'         | SMPTE 421M ("VC-1").                                                                                                                                                                                                                                                                                        |
| **MFVideoFormat\_420O**     | '420O'         | 8-bit per channel planar YUV 4:2:0 video.                                                                                                                                                                                                                                                                   |
| **MFVideoFormat\_AV1**     | 'AV01'         | AV1 video.                                                                                                                                                                                                                                                                                                |



 

## Creating Subtype GUIDs from FOURCCs and D3DFORMAT Values

Video formats are often represented by FOURCCs or **D3DFORMAT** values. A range of GUIDs is reserved for representing these values as subtypes. These GUIDs have the form `XXXXXXXX-0000-0010-8000-00AA00389B71`, where `XXXXXXXX` is the 4-byte FOURCC code or **D3DFORMAT** value.

If a video format has an associated FOURCC or **D3DFORMAT** value, you can create the corresponding subtype GUID as follows: Start with the constant **MFVideoFormat\_Base** and replace the first **DWORD** of the GUID with the video FOURCC or the **D3DFORMAT** value. You can use the [**DEFINE\_MEDIATYPE\_GUID**](/windows/desktop/api/mfapi/nf-mfapi-define_mediatype_guid) macro for this purpose.

> [!Note]  
> DirectShow also uses this system for most video subtypes, but not for uncompressed RGB formats. Therefore, the RGB subtypes in DirectShow do not match the RGB subtypes in Media Foundation.

 

The **D3DFORMAT** enumeration is defined in the header file d3d9types.h. The following table shows the most common uncompressed RGB formats and the corresponding **D3DFORMAT** value.



| RGB format                                                              | **D3DFORMAT** value     |
|-------------------------------------------------------------------------|-------------------------|
| 32-bit RGB                                                              | **D3DFMT\_X8R8G8B8**    |
| 32-bit RGB with alpha channel                                           | **D3DFMT\_A8R8G8B8**    |
| 24-bit RGB                                                              | **D3DFMT\_R8G8B8**      |
| RGB 555 (16-bit RGB)                                                    | **D3DFMT\_X1R5G5B5**    |
| RGB 555 with alpha channel                                              | **D3DFMT\_A1R5G5B5**    |
| RGB 565 (16-bit RGB)                                                    | **D3DFMT\_R5G6B5**      |
| 8-bit palettized RGB                                                    | **D3DFMT\_P8**          |
| A2 R10 G10 B10 (32-bit RGB with alpha channel; 10 bits per RGB channel) | **D3DFMT\_A2R10G10B10** |
| A2 B10 G10 R10 (32-bit RGB with alpha channel; 10 bits per RGB channel) | **D3DFMT\_A2B10G10R10** |
| 8-bit luminance only.                                                   | **D3DFMT\_L8**          |
| 16-bit luminance only.                                                  | **D3DFMT\_L16**         |
| 16-bit z-buffer depth                                                   | **D3DFMT\_D16**         |



 

For more information about FOURCCs, see [Video FOURCCs](video-fourccs.md).

## Related topics

<dl> <dt>

[**IMFMediaType**](/windows/desktop/api/mfobjects/nn-mfobjects-imfmediatype)
</dt> <dt>

[Media Type GUIDs](media-type-guids.md)
</dt> <dt>

[**MF\_MT\_SUBTYPE**](mf-mt-subtype-attribute.md)
</dt> <dt>

[Media Types](media-types.md)
</dt> <dt>

[Video Media Types](video-media-types.md)
</dt> </dl>

 

 




