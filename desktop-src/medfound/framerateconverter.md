---
description: Changes the frame rate of a video stream.
ms.assetid: a66b9c52-a015-41d2-b27a-3ce6a4d95be9
title: Frame Rate Converter DSP (Wmcodecdsp.h)
ms.topic: reference
ms.date: 05/31/2018
---

# Frame Rate Converter DSP

Changes the frame rate of a video stream.

## CLSID

CLSID\_CFrameRateConvertDmo

## Interfaces

-   **IMediaObject**
-   **IMFTransform**
-   **IPropertyStore**

## Formats

-   ARGB 32
-   RGB 24
-   RGB 32
-   RGB 555
-   RGB 565
-   AYUV
-   IYUV
-   UYVY
-   Y211
-   Y411
-   Y41P
-   YUY2
-   YUYV
-   YV12
-   YVYU

## Properties

-   [MFPKEY\_CONV\_INPUTFRAMERATE](mfpkey-conv-inputframerate.md)
-   [MFPKEY\_CONV\_OUTPUTFRAMERATE](mfpkey-conv-outputframerate.md)

## Remarks

This DSP changes the frame rate by repeating or dropping frames.

By default, the DSP gets the frame rates from the media types. Optionally, you can specify the frame rates by setting the MFPKEY\_CONV\_INPUTFRAMERATE and MFPKEY\_CONV\_OUTPUTFRAMERATE properties. These values override the frame rate given in the media type. However, if you are using this DSP within the Media Foundation pipeline, you should not set these properties.

## Requirements



| Requirement | Value |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                          |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/>                                    |
| Header<br/>                   | <dl> <dt>Wmcodecdsp.h</dt> </dl> |
| DLL<br/>                      | <dl> <dt>Mfvdsp.dll</dt> </dl>   |



## See also

<dl> <dt>

[Digital Signal Processors](windowsmediadigitalsignalprocessors.md)
</dt> </dl>

 

 




