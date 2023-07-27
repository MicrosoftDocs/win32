---
description: DVD Interfaces
ms.assetid: 8b0336ca-2480-4187-87f2-8b155601a77f
title: DVD Interfaces
ms.topic: article
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# DVD Interfaces

\[The feature associated with this page, [DirectShow](/windows/win32/directshow/directshow), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer), [IMFMediaEngine](/windows/win32/api/mfmediaengine/nn-mfmediaengine-imfmediaengine), and [Audio/Video Capture in Media Foundation](windows/win32/medfound/audio-video-capture-in-media-foundation). Those features have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer**, **IMFMediaEngine** and **Audio/Video Capture in Media Foundation** instead of **DirectShow**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

These interfaces support DVD playback and navigation.



| Interface                                    | Description                                                                                            |
|----------------------------------------------|--------------------------------------------------------------------------------------------------------|
| [**IAMDecoderCaps**](/windows/desktop/api/Strmif/nn-strmif-iamdecodercaps)     | Implemented by decoders to indicate various capabilities.                                              |
| [**IDvdCmd**](/windows/desktop/api/Strmif/nn-strmif-idvdcmd)                   | Block the [DVD Navigator Filter](dvd-navigator-filter.md) until a command starts or completes.        |
| [**IDvdControl2**](/windows/desktop/api/Strmif/nn-strmif-idvdcontrol2)         | Navigate and play DVD-Video titles, including karaoke titles.                                          |
| [**IDvdGraphBuilder**](/windows/desktop/api/Strmif/nn-strmif-idvdgraphbuilder) | Build a filter graph for DVD-Video playback from the available software and hardware on the system.    |
| [**IDvdInfo2**](/windows/desktop/api/Strmif/nn-strmif-idvdinfo2)               | Query for various attributes of a DVD disc or the DVD Navigator's state.                               |
| [**IDvdState**](/windows/desktop/api/Strmif/nn-strmif-idvdstate)               | Save the state of the user's session to disk, including playback location, parental level, and region. |



 

## Related topics

<dl> <dt>

[DVD Applications](dvd-applications.md)
</dt> <dt>

[Interfaces](interfaces.md)
</dt> </dl>

 

 



