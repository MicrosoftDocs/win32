---
description: Alpha Setter Effect
ms.assetid: dd3ab119-328b-4782-811a-f06909c17dec
title: Alpha Setter Effect
ms.topic: article
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# Alpha Setter Effect

\[The feature associated with this page, [DirectShow](/windows/win32/directshow/directshow), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer), [IMFMediaEngine](/windows/win32/api/mfmediaengine/nn-mfmediaengine-imfmediaengine), and [Audio/Video Capture in Media Foundation](windows/win32/medfound/audio-video-capture-in-media-foundation). Those features have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer**, **IMFMediaEngine** and **Audio/Video Capture in Media Foundation** instead of **DirectShow**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

> [!Note]  
> \[Deprecated. This API may be removed from future releases of Windows.\]

 

The Alpha Setter effect sets the alpha bits on a video image.

Class ID (CLSID): {506D89AE-909A-44f7-9444-ABD575896E35}

CLSID Variable Name: CLSID\_DxtAlphaSetter

Friendly Name: "DxtAlphaSetter"

### Properties



| Property  | Type   | Default | Description                                                 |
|-----------|--------|---------|-------------------------------------------------------------|
| Alpha     | BYTE   | -1      | Sets the alpha for the entire image.                        |
| AlphaRamp | double | -1.0    | Sets the alpha as a percentage of the original alpha value. |



 

## Remarks

A property with a negative value is ignored. Only one property can have a non-negative value. The Alpha property specifies a constant alpha value for every pixel in the image. This property overwrites the alpha values from the original image. The AlphaRamp property specifies each pixel's alpha value as a percentage of the pixel's original value, from 0.0 to 1.0.

## Related topics

<dl> <dt>

[Alpha Blending](alpha-blending.md)
</dt> </dl>

 

 



