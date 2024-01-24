---
description: Scope Filter Sample
ms.assetid: f967d4c7-94d2-440b-9e52-423feefec66d
title: Scope Filter Sample
ms.topic: article
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# Scope Filter Sample

\[The feature associated with this page, [DirectShow](/windows/win32/directshow/directshow), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer), [IMFMediaEngine](/windows/win32/api/mfmediaengine/nn-mfmediaengine-imfmediaengine), and [Audio/Video Capture in Media Foundation](/windows/win32/medfound/audio-video-capture-in-media-foundation). Those features have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer**, **IMFMediaEngine** and **Audio/Video Capture in Media Foundation** instead of **DirectShow**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

## Description

The Scope filter is a renderer filter that displays sound data as wave forms.

## Usage

To use this filter, open GraphEdit and render an audio file (or a video file with an audio stream). Disconnect the audio renderer temporarily and insert the Infinite-Pin Tee ([InfTee Filter Sample](inftee-filter-sample.md)) sample filter. Reconnect the audio renderer. Then connect the Infinite-Pin Tee filter's second output pin to the Scope filter. Now run the graph.

The Scope window is implemented as a dialog box, not as an actual window. Developers creating control panels to alter filter parameters in real time might want to use a technique like this rather than property pages.

The Scope filter demonstrates setting up a separate thread to process data. In this case, the data is just copied to a separate buffer on the [**IMemInputPin::Receive**](/windows/desktop/api/Strmif/nf-strmif-imeminputpin-receive) method, and is then drawn on the Scope window on the separate thread.

The Scope filter also enables you to monitor audio output to determine if you are clipping, so you can adjust the gain.

This filter appears in GraphEdit as "Oscilloscope."

## Downloading the Sample

To download the DirectShow SDK samples, install the latest version of the [Windows SDK](https://msdn.microsoft.com/windowsvista/bb980924.aspx).

This sample is installed under the following path: *\[SDK Root\]*\\Samples\\Multimedia\\DirectShow\\Filters\\Scope.

## Related topics

<dl> <dt>

[DirectShow Samples](directshow-samples.md)
</dt> </dl>

 

 



