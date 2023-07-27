---
description: The bitdepth attribute specifies the bit depth of the output video, in bits per pixel.
ms.assetid: 91a79d4e-a374-4dbc-9ec9-69cf3e1087e1
title: bitdepth Attribute
ms.topic: reference
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# bitdepth Attribute

\[The feature associated with this page, [DirectShow](/windows/win32/directshow/directshow), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer), [IMFMediaEngine](/windows/win32/api/mfmediaengine/nn-mfmediaengine-imfmediaengine), and [Audio/Video Capture in Media Foundation](/windows/win32/medfound/audio-video-capture-in-media-foundation). Those features have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer**, **IMFMediaEngine** and **Audio/Video Capture in Media Foundation** instead of **DirectShow**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

> [!Note]  
> \[Deprecated. This API may be removed from future releases of Windows.\]

 

The `bitdepth` attribute specifies the bit depth of the output video, in bits per pixel.

## Possible Values

Must be 16, 24, or 32. The default value is 16.

## Applies To

[**group**](group-element.md)

## Remarks

Set this attribute only if the type attribute is `video`.

## See also

<dl> <dt>

[XTL Attributes](xtl-attributes.md)
</dt> </dl>

 

 



