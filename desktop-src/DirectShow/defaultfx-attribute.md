---
description: The defaultfx attribute specifies the class identifier (CLSID) of a default effect for the timeline.
ms.assetid: 892de9fe-8fb9-419e-a18b-8f20148f4ee0
title: defaultfx Attribute
ms.topic: reference
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# defaultfx Attribute

\[The feature associated with this page, [DirectShow](/windows/win32/directshow/directshow), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer), [IMFMediaEngine](/windows/win32/api/mfmediaengine/nn-mfmediaengine-imfmediaengine), and [Audio/Video Capture in Media Foundation](/windows/win32/medfound/audio-video-capture-in-media-foundation). Those features have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer**, **IMFMediaEngine** and **Audio/Video Capture in Media Foundation** instead of **DirectShow**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

> [!Note]  
> \[Deprecated. This API may be removed from future releases of Windows.\]

 

The `defaultfx` attribute specifies the class identifier (CLSID) of a default effect for the timeline.

## Possible Values

Must be a string with the format {00000000-0000-0000-0000-000000000000}.

## Applies To

[**timeline**](timeline-element.md)

## See also

<dl> <dt>

[XTL Attributes](xtl-attributes.md)
</dt> <dt>

[**IAMTimeline::SetDefaultEffect**](iamtimeline-setdefaulteffect.md)
</dt> </dl>

 

 



