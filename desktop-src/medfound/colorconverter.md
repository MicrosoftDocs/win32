---
description: Converts a video stream between color formats.
ms.assetid: 1c15dc2b-0e69-4d16-af02-8056a1eb2c5c
title: Color Converter DSP (Wmcodecdsp.h)
ms.topic: reference
ms.date: 05/31/2018
---

# Color Converter DSP

Converts a video stream between color formats.

## CLSID

CLSID\_CColorConvertDMO

## Interfaces

-   [**IMediaObject**](/previous-versions/windows/desktop/api/mediaobj/nn-mediaobj-imediaobject)
-   [**IMFRealTimeClient**](/windows/desktop/api/mfidl/nn-mfidl-imfrealtimeclient)
-   [**IMFTransform**](/windows/desktop/api/mftransform/nn-mftransform-imftransform)
-   [**IPropertyStore**](/windows/win32/api/propsys/nn-propsys-ipropertystore)
-   [IWMColorConvProps](/windows/desktop/api/wmcodecdsp/nn-wmcodecdsp-iwmcolorconvprops)

## Input Formats

-   RGB 24
-   RGB 32
-   RGB 555
-   RGB 565
-   RGB 8
-   AYUV
-   I420
-   IYUV
-   NV11
-   NV12
-   UYVY
-   V216
-   V410
-   Y41P
-   Y41T
-   Y42T
-   YUY2
-   YV12
-   YVU9
-   YVYU

## Output Formats

-   RGB 24
-   RGB 32
-   RGB 555
-   RGB 565
-   RGB 8
-   AYUV
-   I420
-   IYUV
-   NV11
-   NV12
-   UYVY
-   V216
-   V410
-   YUY2
-   YV12
-   YVYU

## Properties

-   [MFPKEY\_COLORCONV\_SRCLEFT](mfpkey-colorconv-srcleft.md)
-   [MFPKEY\_COLORCONV\_SRCTOP](mfpkey-colorconv-srctop.md)
-   [MFPKEY\_COLORCONV\_DSTLEFT](mfpkey-colorconv-dstleft.md)
-   [MFPKEY\_COLORCONV\_DSTTOP](mfpkey-colorconv-dsttop.md)
-   [MFPKEY\_COLORCONV\_WIDTH](mfpkey-colorconv-width.md)
-   [MFPKEY\_COLORCONV\_HEIGHT](mfpkey-colorconv-height.md)
-   [MFPKEY\_COLORCONV\_MODE](mfpkey-colorconv-mode.md)

## Remarks

The Color Converter DSP is implemented as a COM object that can act as a DirectXMedia Object (DMO) or a Media Foundation Transform (MFT). The object has a single class identifier (CLSID) regardless of whether it acts as a DMO or an MFT. For information about when a DSP acts as a DMO or an MFT, see [Digital Signal Processors](windowsmediadigitalsignalprocessors.md).

The globally unique identifiers (GUIDs) for RGB media subtypes differ depending on whether a DSP is acting as a DMO or an MFT. The GUIDs for non-RGB media subtypes are the same, regardless of whether a DSP is acting as a DMO or an MFT. For information about the GUIDs that represent media subtypes, see [Video Subtype GUIDs](video-subtype-guids.md).

By default, this DSP copies the entire source image to the output buffer. Optionally, you can specify source and destination rectangles. The DSP copies the portion of the source image defined by source rectangle, and writes it into the destination rectangle on the output buffer. The DSP does not perform any scaling; the source and destination rectangles must be the same size. The source and destination rectangles cannot exceed the boundaries of the video frame.

All of the properties except [**MFPKEY\_COLORCONV\_MODE**](mfpkey-colorconv-mode.md) must be set in a group. If you set any of these properties, you must set all of the others. Otherwise, the source and destination rectangles might be invalid, in which case both the [**IMFTransform::ProcessOutput**](/windows/desktop/api/mftransform/nf-mftransform-imftransform-processoutput) and [**IMediaObject::ProcessOutput**](/previous-versions/windows/desktop/api/mediaobj/nf-mediaobj-imediaobject-processoutput) methods will return **E\_INVALIDARG**.

The color converter does not support every combination of input format and output format. Usually, you should set the media format that you know, either input or output, and then enumerate the available formats on the opposite stream.

## Requirements



| Requirement | Value |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                          |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/>                                    |
| Header<br/>                   | <dl> <dt>Wmcodecdsp.h</dt> </dl> |
| DLL<br/>                      | <dl> <dt>Colorcnv.dll</dt> </dl> |



## See also

<dl> <dt>

[Digital Signal Processors](windowsmediadigitalsignalprocessors.md)
</dt> </dl>

 

 
