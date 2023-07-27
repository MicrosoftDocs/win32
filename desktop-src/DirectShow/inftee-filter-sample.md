---
description: InfTee Filter Sample
ms.assetid: ba401528-9706-41fb-99d1-2bc3ffc05f1a
title: InfTee Filter Sample
ms.topic: article
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# InfTee Filter Sample

\[The feature associated with this page, [DirectShow](/windows/win32/directshow/directshow), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer), [IMFMediaEngine](/windows/win32/api/mfmediaengine/nn-mfmediaengine-imfmediaengine), and [Audio/Video Capture in Media Foundation](/windows/win32/medfound/audio-video-capture-in-media-foundation). Those features have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer**, **IMFMediaEngine** and **Audio/Video Capture in Media Foundation** instead of **DirectShow**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

## Description

The InfTee filter provides a sample implementation of the DirectShow [Infinite Pin Tee](infinite-pin-tee-filter.md) filter. The filter has one input pin and a dynamic number of output pins. All media samples sent to the filter are delivered simultaneously from all of the output pins.

This filter appears in GraphEdit under the name "Sample Infinite Pin Tee," to distinguish it from the standard Infinite Pin Tee filter that is provided in DirectShow.

## Usage

Because this filter does not change the data that it receives, all pins must agree to the same media type. During the connection process, the filter might reconnect some pins in order to make the media types match.

Data arriving at the input pin is not copied before it is sent to the output pins. The filter also ensures that the data is delivered to the downstream filters, to guarantee that both outputs receive timely service. In particular, if one of the outputs can block in the [**COutputQueue::Receive**](coutputqueue-receive.md) member function, then the tee spins off a thread to deliver the sample. If there were no thread to deliver the sample, then the thread that delivers the sample to the tee input pin might pass the data to a downstream filter; at that point, it might block, keeping data from the other downstream filter for long periods of time.

## Downloading the Sample

To download the DirectShow SDK samples, install the latest version of the [Windows SDK](https://msdn.microsoft.com/windowsvista/bb980924.aspx).

This sample is installed under the following path: *\[SDK Root\]*\\Samples\\Multimedia\\DirectShow\\Filters\\InfTee.

## Related topics

<dl> <dt>

[DirectShow Samples](directshow-samples.md)
</dt> </dl>

 

 



