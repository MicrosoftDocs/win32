---
description: Extended Color Information
ms.assetid: 05ca73c6-d105-47bc-96bc-b784f669febe
title: Extended Color Information
ms.topic: article
ms.date: 05/31/2018
---

# Extended Color Information

If you know anything about RGB color, you know that (255, 255, 255) is the 8-bit RGB triplet for the color *white*. But what is the actual *color* defined by this triplet?

The answer may be surprising: Without some additional information, this triplet does not define any particular color! The meaning of any RGB value depends on the *color space*. If we don't know the color space, then strictly speaking we don't know the color.

A color space defines how the numeric representation of a given color value should be reproduced as physical light. When video is encoded in one color space but is displayed in another, it results in distorted colors, unless the video is color-corrected. To achieve accurate color fidelity, therefore, it is crucial to know the color space of the source video. Previously, the video pipeline in Windows did not carry information about the intended color space. Starting in Windows Vista, both DirectShow and Media Foundation support extended color information in the media type. This information is also available for DirectX Video Acceleration (DXVA).

The standard way to describe a color space mathematically is to use the CIE XYZ color space, defined by the International Commission on Illumination (CIE). It is not practical to use CIE XYZ values directly in video, but the CIE XYZ color space can be used as an intermediate representation when converting between color spaces.

To reproduce colors accurately, the following information is needed:

-   Color primaries. The color primaries define how CIE XYZ tristimulus values are represented as RGB components. In effect, the color primaries define the "meaning" of a given RGB value.
-   Transfer function. The transfer function is a function that converts linear RGB values to non-linear R'G'B' values. This function is also called *gamma correction*.
-   Transfer matrix. The transfer matrix defines how R'G'B' is converted to Y'PbPr.
-   Chroma sampling. Most YUV video is transmitted with less resolution in the chroma components than the luma. Chroma sampling is indicated by the FOURCC of the video format. For example, YUY2 is a 4:2:2 format, meaning the chroma samples are sampled horizontally by a factor of 2.
-   Chroma siting. When the chroma is sampled, the position of the chroma samples relative to the luma samples determines how the missing samples should be interpolated.
-   Nominal range. The nominal range defines how Y'PbPr values are scaled to Y'CbCr.

## Color Space in Media Types

DirectShow, Media Foundation, and DirectX Video Acceleration (DXVA) all have different ways to represent video formats. Fortunately, it is easy to translate the color-space information from one to another, because the relevant enumerations are the same.

-   DXVA 1.0: Color-space information is given in the [**DXVA\_ExtendedFormat**](/windows-hardware/drivers/ddi/dxva/ns-dxva-_dxva_extendedformat) structure.
-   DXVA 2.0: Color-space information is given in the [**DXVA2\_ExtendedFormat**](/windows/desktop/api/dxva2api/ns-dxva2api-dxva2_extendedformat) structure structure. This structure is identical to the DXVA 1.0 structure, and the meaning of the fields is the same.
-   DirectShow: Color-space information is given in the [**VIDEOINFOHEADER2**](/previous-versions/windows/desktop/api/dvdmedia/ns-dvdmedia-videoinfoheader2) structure. The information is stored in the upper 24 bits of the **dwControlFlags** field. If color-space information is present, set the **AMCONTROL\_COLORINFO\_PRESENT** flag in **dwControlFlags**. When this flag is set, the **dwControlFlags** field should be interpreted as a [**DXVA\_ExtendedFormat**](/windows-hardware/drivers/ddi/dxva/ns-dxva-_dxva_extendedformat) structure, except that the lower 8 bits of the structure are reserved for **AMCONTROL\_xxx** flags.
-   Video capture drivers: Color-space information is given in the [**KS\_VIDEOINFOHEADER2**](/windows-hardware/drivers/ddi/ksmedia/ns-ksmedia-tagks_videoinfoheader2) structure. This structure is identical to the [**VIDEOINFOHEADER2**](/previous-versions/windows/desktop/api/dvdmedia/ns-dvdmedia-videoinfoheader2) structure, and the meaning of the fields is the same.
-   Media Foundation: Color-space information is stored as attributes in the media type:

    

    | Color information  | Attribute                                                                                                                                                   |
    |--------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------|
    | Color primaries    | [**MF\_MT\_VIDEO\_PRIMARIES**](mf-mt-video-primaries-attribute.md)                                                                                         |
    | Transfer function  | [**MF\_MT\_TRANSFER\_FUNCTION**](mf-mt-transfer-function-attribute.md)                                                                                     |
    | Transfer matrix    | [**MF\_MT\_YUV\_MATRIX**](mf-mt-yuv-matrix-attribute.md)                                                                                                   |
    | Chroma subsampling | [**MF\_MT\_SUBTYPE**](mf-mt-subtype-attribute.md)<br/> (Given by the FOURCC, which is stored in the first **DWORD** of the subtype GUID.)<br/> |
    | Chroma siting      | [**MF\_MT\_VIDEO\_CHROMA\_SITING**](mf-mt-video-chroma-siting-attribute.md)                                                                                |
    | Nominal range      | [**MF\_MT\_VIDEO\_NOMINAL\_RANGE**](mf-mt-video-nominal-range-attribute.md)                                                                                |

    

     

## Color Space Conversion

Conversion from one Y'CbCr space to another requires the following steps.

1.  Inverse quantization: Convert the Y'CbCr representation to a Y'PbPr representation, using the source nominal range.
2.  Upsampling: Convert the sampled chroma values to 4:4:4 by interpolating chroma values.
3.  YUV to RGB conversion: Convert from Y'PbPr to non-linear R'G'B', using the source transfer matrix.
4.  Inverse transfer function: Convert non-linear R'G'B' to linear RGB, using the inverse of the transfer function.
5.  RGB color space conversion: Use the color primaries to convert from the source RGB space to the target RGB space.
6.  Transfer function: Convert linear RGB to non-linear R'G'B, using the target transfer function.

7.  RGB to YUV conversion: Convert R'G'B' to Y'PbPr, using the target transfer matrix.
8.  Downsampling: Convert 4:4:4 to 4:2:2, 4:2:0, or 4:1:1 by filtering the chroma values.
9.  Quantization: Convert Y'PbPr to Y'CbCr, using the target nominal range.

Steps 1–4 occur in the source color space, and steps 6–9 occur in the target color space. In the actual implementation, intermediate steps can be approximated and adjacent steps can be combined. There is generally a trade-off between accuracy and computational cost.

For example, to convert from RT.601 to RT.709 requires the following stages:

-   Inverse quantization: Y'CbCr(601) to Y'PbPr(601)
-   Upsampling: Y'PbPr(601)
-   YUV to RGB: Y'PbPr(601) to R'G'B'(601)
-   Inverse transfer function: R'G'B'(601) to RGB(601)
-   RGB color space conversion: RGB(601) to RGB(709)
-   Transfer function: RGB(709) to R'G'B'(709)
-   RGB to YUV: R'G'B'(709) to Y'PbPr(709)
-   Downsampling: Y'PbPr(709)

-   Quantization: Y'PbPr(709) to Y'CbCr(709)

## Using Extended Color Information

To preserve color fidelity throughout the pipeline, color-space information must be introduced at the source or the decoder and conveyed all the way through the pipeline to the sink.

### Video Capture Devices

Most analog capture devices use a well-defined color space when capturing video. Capture drivers should offer a format with a **KS\_VIDEOINFOHEADER2** format block that contains the color information. For backward compatibility, the driver should accept formats that do not contain the color information. This will enable the driver to work with components that do not accept the extended color information.

### File-based Sources

When parsing a video file, the media source (or parser filter, in DirectShow) might be able to provide some of the color information. For example, the DVD Navigator can determine the color space based on the DVD content. Other color information might be available to the decoder. For example, an MPEG-2 elementary video stream gives the color information in the sequence\_display\_extension field. If the color information is not explicitly described in the source, it might be defined implicitly by the type of content. For example, the NTSC and PAL varieties of DV video each use different color spaces. Finally, the decoder can use whatever color information it gets from the source's media type.

### Other Components

Other components might need to use the color-space information in a media type:

-   Software color-space converters should use color-space information when selecting a conversion algorithm.
-   Video mixers, such as the enhanced video renderer (EVR) mixer, should use the color information when mixing video streams from different types of content.
-   The DXVA video processing APIs and DDIs enable the caller to specify color-space information information. The GPU should use this information when it performs hardward video mixing.

## Related topics

<dl> <dt>

[Video Media Types](video-media-types.md)
</dt> <dt>

[DirectX Video Acceleration 2.0](directx-video-acceleration-2-0.md)
</dt> </dl>

 

 
