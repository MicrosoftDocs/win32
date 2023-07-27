---
description: About the Audio Capture Filter
ms.assetid: ff345670-5a75-40d3-a228-8bc22aa76708
title: About the Audio Capture Filter
ms.topic: article
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# About the Audio Capture Filter

\[The feature associated with this page, [DirectShow](/windows/win32/directshow/directshow), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer), [IMFMediaEngine](/windows/win32/api/mfmediaengine/nn-mfmediaengine-imfmediaengine), and [Audio/Video Capture in Media Foundation](windows/win32/medfound/audio-video-capture-in-media-foundation). Those features have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer**, **IMFMediaEngine** and **Audio/Video Capture in Media Foundation** instead of **DirectShow**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

DirectShow enables capture from the analog inputs on a sound card through the [Audio Capture Filter](audio-capture-filter.md). This filter uses the waveIn*XXX* APIs to control any device whose driver supports these APIs. Each card on the system is represented by a separate instance of the filter.

The Audio Capture filter exposes each input on the card, such as the microphone or the MIDI input, as an input pin. The input pins represent what the driver exposes as audio source lines. No data travels through these input pins, however, and they do not connect to other DirectShow filters. They simply provide a way for an application to control the inputs. The application can use an input pin to enable or disable the input, or to set mixing properties such as bass equalization, treble equalization, pan, and so forth. The amount of control that is available depends on the driver. To fully understand and exploit the capabilities of a particular sound card, you will need the documentation from the card's manufacturer.

> [!Note]  
> You can capture from the CD-Audio input, but this audio stream has already gone through the digital-to-analog converter, so there will be a loss of sound quality from the original CD.

 

## Related topics

<dl> <dt>

[Audio Capture](audio-capture.md)
</dt> </dl>

 

 



