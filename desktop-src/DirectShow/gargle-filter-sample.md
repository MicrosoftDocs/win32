---
description: Gargle Filter Sample
ms.assetid: 13002a71-2da6-4713-825b-5275d41e4cb8
title: Gargle Filter Sample
ms.topic: article
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# Gargle Filter Sample

\[The feature associated with this page, [DirectShow](/windows/win32/directshow/directshow), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer), [IMFMediaEngine](/windows/win32/api/mfmediaengine/nn-mfmediaengine-imfmediaengine), and [Audio/Video Capture in Media Foundation](/windows/win32/medfound/audio-video-capture-in-media-foundation). Those features have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer**, **IMFMediaEngine** and **Audio/Video Capture in Media Foundation** instead of **DirectShow**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

## Description

The Gargle Filter is an audio effect transform filter.

The Gargle filter modulates the waveform passing through it by multiplying the waveform by another waveform that is mathematically generated within the filter. The modulating waveform is, by default, a triangular wave. The property sheet also offers the alternative of a square wave. You can set the frequency of the modulating wave through the filter's property sheet. At low modulation frequencies, the effect sounds like a tremolo. At higher modulation frequencies, it sounds like a distortion, adding extra frequencies above and below the original unmodulated sound.

## Downloading the Sample

To download the DirectShow SDK samples, install the latest version of the [Windows SDK](https://msdn.microsoft.com/windowsvista/bb980924.aspx).

This sample is installed under the following path: *\[SDK Root\]*\\Samples\\Multimedia\\DirectShow\\Filters\\Gargle.

## Related topics

<dl> <dt>

[DirectShow Samples](directshow-samples.md)
</dt> </dl>

 

 



