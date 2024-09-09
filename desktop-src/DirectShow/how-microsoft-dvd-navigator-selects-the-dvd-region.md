---
description: How Microsoft DVD Navigator Selects the DVD Region
ms.assetid: 407619c6-2d4b-4f7f-a861-42ee0f462ecd
title: How Microsoft DVD Navigator Selects the DVD Region
ms.topic: article
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# How Microsoft DVD Navigator Selects the DVD Region

\[The feature associated with this page, [DirectShow](/windows/win32/directshow/directshow), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer), [IMFMediaEngine](/windows/win32/api/mfmediaengine/nn-mfmediaengine-imfmediaengine), and [Audio/Video Capture in Media Foundation](/windows/win32/medfound/audio-video-capture-in-media-foundation). Those features have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer**, **IMFMediaEngine** and **Audio/Video Capture in Media Foundation** instead of **DirectShow**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

The Microsoft DVD Navigator uses the following algorithm to determine region match while playing DVD discs on a PC:

1.  The DVD Navigator gets the disc region, drive region, and decoder region.
2.  If the disc region is "all regions," the DVD Navigator plays the disc.
3.  If the disc is not marked for all regions, the DVD Navigator checks whether the decoder has a preset region.
4.  If the decoder has a preset region and it does not match the disc region, the DVD Navigator returns an error indicating that it cannot play the disc on the current DVD configuration. (Exit)
5.  If the decoder region is not set, or is the same as the disc region, the DVD Navigator checks whether the drive region is the same as the disc region.
6.  If the drive region matches the disc region, the DVD Navigator plays the title.
7.  Otherwise, if the driver region does not match the disc region, the DVD Navigator invokes the code to change the drive's region. If the allowed number of region changes has been exhausted, the region change attempt fails and the title cannot be played on that system.

## Related topics

<dl> <dt>

[DVD Region Change Support in Windows](dvd-region-change-support-in-windows.md)
</dt> </dl>

 

 



