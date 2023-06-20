---
description: Shortcuts to C++ DVD Reference Pages
ms.assetid: b37337b7-b3be-4f49-b350-df5e3c88e3cf
title: Shortcuts to C++ DVD Reference Pages
ms.topic: article
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# Shortcuts to C++ DVD Reference Pages

\[The feature associated with this page, [DirectShow](/windows/win32/directshow/directshow), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer) and [IMFMediaEngine](/windows/win32/api/mfmediaengine/nn-mfmediaengine-imfmediaengine). **MediaPlayer** and **IMFMediaEngine** have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** and **IMFMediaEngine** instead of **DirectShow**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

The following interfaces are those typically used when writing a DVD application in C++.



| Interface                                    | Purpose                                                                                          |
|----------------------------------------------|--------------------------------------------------------------------------------------------------|
| [**IAMLine21Decoder**](/previous-versions/windows/desktop/api/il21dec/nn-il21dec-iamline21decoder) | Controls closed captioning display.                                                              |
| [**IDvdCmd**](/windows/desktop/api/Strmif/nn-strmif-idvdcmd)                   | Used in advanced command synchronization techniques to control a command object.                 |
| [**IDvdControl2**](/windows/desktop/api/Strmif/nn-strmif-idvdcontrol2)         | Issues commands to the [DVD Navigator](dvd-navigator-filter.md) filter (the "set" methods).     |
| [**IDvdGraphBuilder**](/windows/desktop/api/Strmif/nn-strmif-idvdgraphbuilder) | Creates the DVD filter graph.                                                                    |
| [**IDvdInfo2**](/windows/desktop/api/Strmif/nn-strmif-idvdinfo2)               | Queries the DVD Navigator for state information and information on the disc (the "get" methods). |
| [**IDvdState**](/windows/desktop/api/Strmif/nn-strmif-idvdstate)               | Saves information, such as bookmarks, to disc.                                                   |
| [**IVideoFrameStep**](/windows/desktop/api/Strmif/nn-strmif-ivideoframestep)   | Controls "frame stepping" if the decoder supports it.                                            |



 

## Related topics

<dl> <dt>

[DVD Applications](dvd-applications.md)
</dt> </dl>

 

 



