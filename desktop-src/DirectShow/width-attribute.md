---
description: The width attribute specifies the width of the output video, in pixels.
ms.assetid: 3fcc28d8-b7ef-474b-8594-b31422974998
title: width Attribute
ms.topic: reference
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# width Attribute

\[The feature associated with this page, [DirectShow](/windows/win32/directshow/directshow), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer), [IMFMediaEngine](/windows/win32/api/mfmediaengine/nn-mfmediaengine-imfmediaengine), and [Audio/Video Capture in Media Foundation](windows/win32/medfound/audio-video-capture-in-media-foundation). Those features have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer**, **IMFMediaEngine** and **Audio/Video Capture in Media Foundation** instead of **DirectShow**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

> [!Note]  
> \[Deprecated. This API may be removed from future releases of Windows.\]

 

The `width` attribute specifies the width of the output video, in pixels.

## Possible Values

Floating-point value. The value must include the leading zero before the decimal place. For example, 0.3, not .3. Do not use more than seven decimal digits.

## Applies To

[**group**](group-element.md)

## Remarks

Set this attribute only if the **type** attribute is `video`.

## See also

<dl> <dt>

[XTL Attributes](xtl-attributes.md)
</dt> </dl>

 

 



