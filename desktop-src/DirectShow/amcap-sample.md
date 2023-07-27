---
description: AmCap Sample
ms.assetid: 611b252f-1ae0-439e-ba02-8ad9bb8cec6d
title: AmCap Sample
ms.topic: article
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# AmCap Sample

\[The feature associated with this page, [DirectShow](/windows/win32/directshow/directshow), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer), [IMFMediaEngine](/windows/win32/api/mfmediaengine/nn-mfmediaengine-imfmediaengine), and [Audio/Video Capture in Media Foundation](windows/win32/medfound/audio-video-capture-in-media-foundation). Those features have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer**, **IMFMediaEngine** and **Audio/Video Capture in Media Foundation** instead of **DirectShow**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

## Description

Video capture application.

This sample application demonstrates the following tasks related to audio and video capture:

-   Capture to a file
-   Live preview
-   Allocation of the capture file
-   Display of device property pages
-   Device enumeration
-   Stream control

AMCap supports MPEG-2 program stream input, for example from analog TV Tuners that stream MPEG-2 content. A DirectShow-compatible MPEG-2 decoder is required to decode the streams.

## Downloading the Sample

To download the DirectShow SDK samples, install the latest version of the [Windows SDK](https://msdn.microsoft.com/windowsvista/bb980924.aspx).

This sample is installed under the following path: \[*SDK Root*\]\\Samples\\Multimedia\\DirectShow\\Capture\\AmCap.

## Related topics

<dl> <dt>

[DirectShow Samples](directshow-samples.md)
</dt> </dl>

 

 



