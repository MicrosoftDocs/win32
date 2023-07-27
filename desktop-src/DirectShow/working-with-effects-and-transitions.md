---
description: Working with Effects and Transitions
ms.assetid: 00e97d02-ff43-4e1f-9806-abaeb9288058
title: Working with Effects and Transitions
ms.topic: article
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# Working with Effects and Transitions

\[The feature associated with this page, [DirectShow](/windows/win32/directshow/directshow), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer), [IMFMediaEngine](/windows/win32/api/mfmediaengine/nn-mfmediaengine-imfmediaengine), and [Audio/Video Capture in Media Foundation](/windows/win32/medfound/audio-video-capture-in-media-foundation). Those features have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer**, **IMFMediaEngine** and **Audio/Video Capture in Media Foundation** instead of **DirectShow**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

\[This API is not supported and may be altered or unavailable in the future.\]

Effects modify a single clip, track, or composition. Transitions create seques from one track or compositionsto another.

[DirectShow Editing Services](directshow-editing-services.md) uses DirectX Transform objects for its video transitions and video effects. For video transitions, use any 2-D two-input DirectX Transform object. For video effects, use any 2-D one-input DirectX Transform object. Microsoft no longer supports the development of third-party DirectX Transform objects. However, several are provided with DirectShow and others are provided with Microsoft Internet Explorer. For more information about the transitions provided with Internet Explorer, see [Visual Filters and Transitions Reference](/previous-versions/windows/internet-explorer/ie-developer/platform-apis/ms532853(v=vs.85)).

For audio effects, you can use any DirectShow audio effect filter. DES also provides a [Volume Envelope Effect](volume-envelope-effect.md) for setting the volume on a track or clip. DES does not support audio transitions.

This section contains the following topics:

-   [Adding Effect and Transition Objects](adding-effect-and-transition-objects.md)
-   [Previewing Effects and Transitions](previewing-effects-and-transitions.md)
-   [Enumerating Effects and Transitions](enumerating-effects-and-transitions.md)
-   [Setting Properties on Effects and Transitions](setting-properties-on-effects-and-transitions.md)
-   [Transition Direction](transition-direction.md)

## Related topics

<dl> <dt>

[Using DirectShow Editing Services](using-directshow-editing-services.md)
</dt> </dl>

 

 
