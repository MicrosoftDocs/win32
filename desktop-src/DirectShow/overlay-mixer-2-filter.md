---
description: Overlay Mixer 2 Filter
ms.assetid: 3d3871ac-518c-45a1-9e64-031f344f4527
title: Overlay Mixer 2 Filter
ms.topic: article
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# Overlay Mixer 2 Filter

\[The feature associated with this page, [DirectShow](/windows/win32/directshow/directshow), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer) and [IMFMediaEngine](/windows/win32/api/mfmediaengine/nn-mfmediaengine-imfmediaengine). **MediaPlayer** and **IMFMediaEngine** have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** and **IMFMediaEngine** instead of **DirectShow**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

The Overlay Mixer 2 filter is identical to the [Overlay Mixer](overlay-mixer-filter.md) filter, except:

-   It supports only media types with [**VIDEOINFOHEADER2**](/previous-versions/windows/desktop/api/dvdmedia/ns-dvdmedia-videoinfoheader2) formats.
-   It has a higher merit, which enables it to be added to a filter graph automatically.

The Overlay Mixer 2 is provided so that the Filter Graph Manager will add it to the graph when it renders non-DVD MPEG-2 video. The choice of whether to use the Overlay Mixer or the Overlay Mixer 2 is handled by the component that builds the graph, either the Filter Graph Manager, the Capture Graph Builder, or the DVD Graph Builder. From an application perspective, they are the same filter, with the same interfaces and functionality.

The following table contains information specific to the Overlay Mixer 2. For all other filter data, refer to the documentation for the Overlay Mixer.




| Label | Value |
|--------|-------|
| Input Pin Media Types | Format Type: Format_VIDEOINFO2 | 
| Filter CLSID | CLSID_OverlayMixer2 | 
| <a href="merit.md">Merit</a> | <ul><li>MERIT_UNLIKELY</li><li>Windows Vista or later: MERIT_DO_NOT_USE</li></ul> | 




 

In Windows Vista or later, the merit of the Overlay Mixer 2 filter is MERIT\_DO\_NOT\_USE, because the newer video renderers (VMR-7, VMR-9, and EVR) all support **VIDEOINFOHEADER2** formats, and therefore it is not necessary to use the Overlay Mixer.

## Related topics

<dl> <dt>

[DirectShow Filters](directshow-filters.md)
</dt> </dl>

 

 



