---
description: Ball Filter Sample
ms.assetid: 80a6db64-ef13-46a2-8f2a-e39095e874b2
title: Ball Filter Sample
ms.topic: article
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# Ball Filter Sample

\[The feature associated with this page, [DirectShow](/windows/win32/directshow/directshow), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer), [IMFMediaEngine](/windows/win32/api/mfmediaengine/nn-mfmediaengine-imfmediaengine), and [Audio/Video Capture in Media Foundation](/windows/win32/medfound/audio-video-capture-in-media-foundation). Those features have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer**, **IMFMediaEngine** and **Audio/Video Capture in Media Foundation** instead of **DirectShow**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

## Description

The Ball Filter is a video source filter that produces an image of a bouncing ball. This sample illustrates format negotiation and the use of the source filter base classes [**CSource**](csource.md) and [**CSourceStream**](csourcestream.md).

The code in Fball.h and Fball.cpp manages the filter interfaces. Those two files contain approximately the minimum code required for a source filter. The Ball.h and Ball.cpp files contain the code that bounces the ball.

This filter has a single output pin, which provides a video stream that shows a ball bouncing around in the frame. The Ball filter also accepts quality management requests from the downstream filter, which illustrates a simple quality management strategy. This filter implements the [**IQualityControl**](/windows/desktop/api/Strmif/nn-strmif-iqualitycontrol) interface for that purpose.

## Downloading the Sample

To download the DirectShow SDK samples, install the latest version of the [Windows SDK](https://msdn.microsoft.com/windowsvista/bb980924.aspx).

This sample is installed under the following path: \[*SDK Root*\]\\Samples\\Multimedia\\DirectShow\\Filters\\Ball.

## Related topics

<dl> <dt>

[DirectShow Samples](directshow-samples.md)
</dt> </dl>

 

 



