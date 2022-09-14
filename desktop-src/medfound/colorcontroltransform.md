---
description: Adjusts the color characteristics of a video stream.
ms.assetid: 738c1f0c-8417-4b12-a7f1-9bbf3c7e9dd3
title: Color Control Transform DSP (Wmcodecdsp.h)
ms.topic: reference
ms.date: 05/31/2018
---

# Color Control Transform DSP

Adjusts the color characteristics of a video stream.

## CLSID

CLSID\_CColorControlDmo

## Interfaces

-   **IMediaObject**
-   **IMFTransform**
-   **IPropertyStore**

## Formats

-   RGB 24
-   RGB 32
-   RGB 555
-   RGB 565
-   AYUV
-   UYVY
-   YUY2
-   YV12

## Properties

-   [MFPKEY\_COLOR\_BRIGHTNESS](mfpkey-color-brightness.md)
-   [MFPKEY\_COLOR\_CONTRAST](mfpkey-color-contrast.md)
-   [MFPKEY\_COLOR\_HUE](mfpkey-color-hue.md)
-   [MFPKEY\_COLOR\_SATURATION](mfpkey-color-saturation.md)

## Remarks

This DSP modifies the contents of the video stream. For playback, you might be able to achieve similar effects more efficiently by using the **IMFVideoProcessor** interface, which controls video processing in the graphics card.

## Requirements



| Requirement | Value |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                          |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/>                                    |
| Header<br/>                   | <dl> <dt>Wmcodecdsp.h</dt> </dl> |
| DLL<br/>                      | <dl> <dt>Mfvdsp.dll</dt> </dl>   |



## See also

<dl> <dt>

[Digital Signal Processors](windowsmediadigitalsignalprocessors.md)
</dt> </dl>

 

 




