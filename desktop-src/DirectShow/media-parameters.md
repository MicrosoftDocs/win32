---
description: Media Parameters
ms.assetid: 48b2bc2e-897d-4aa9-8a50-c2855a17dca5
title: Media Parameters
ms.topic: article
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# Media Parameters

\[The feature associated with this page, [DirectShow](/windows/win32/directshow/directshow), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer), [IMFMediaEngine](/windows/win32/api/mfmediaengine/nn-mfmediaengine-imfmediaengine), and [Audio/Video Capture in Media Foundation](/windows/win32/medfound/audio-video-capture-in-media-foundation). Those features have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer**, **IMFMediaEngine** and **Audio/Video Capture in Media Foundation** instead of **DirectShow**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

Media parameters enable an application to configure an object's properties so that they change over time in a mathematically deterministic way.

For example, suppose that a sound engineer is mixing a digital master tape and wants to apply a slight delay to a vocal section, to fill out the sound. The effect will be jarring if the delay cuts in abruptly. Instead, the effect should begin 100 percent dry (no delay), and the wet/dry mix should increase gradually until it reaches the desired level. Moreover, this transition should follow a smooth curve or linear progression. To support this scenario, a DMO can expose the following interfaces:

-   [**IMediaParamInfo**](/previous-versions/windows/desktop/api/Medparam/nn-medparam-imediaparaminfo) contains methods for discovering information about the supported properties. Typically, the client will call these methods before it begins to stream data.
-   [**IMediaParams**](/previous-versions/windows/desktop/api/Medparam/nn-medparam-imediaparams) contain methods for setting the curves that a parameter will follow during streaming.

These interfaces are designed primarily for DMOs, but any object can support them. Within this section, the term *parameter* refers to any property that supports these two interfaces.

This section contains the following topics:

-   [Parameter Curves](parameter-curves.md)
-   [Parameter Information](parameter-information.md)
-   [Envelope Segments](envelope-segments.md)
-   [Calculating Parameter Values](calculating-parameter-values.md)

## Related topics

<dl> <dt>

[DirectX Media Objects](directx-media-objects.md)
</dt> </dl>

 

 



