---
description: About the Audio Capture Filter
ms.assetid: ff345670-5a75-40d3-a228-8bc22aa76708
title: About the Audio Capture Filter
ms.topic: article
ms.date: 05/31/2018
---

# About the Audio Capture Filter

DirectShow enables capture from the analog inputs on a sound card through the [Audio Capture Filter](audio-capture-filter.md). This filter uses the waveIn*XXX* APIs to control any device whose driver supports these APIs. Each card on the system is represented by a separate instance of the filter.

The Audio Capture filter exposes each input on the card, such as the microphone or the MIDI input, as an input pin. The input pins represent what the driver exposes as audio source lines. No data travels through these input pins, however, and they do not connect to other DirectShow filters. They simply provide a way for an application to control the inputs. The application can use an input pin to enable or disable the input, or to set mixing properties such as bass equalization, treble equalization, pan, and so forth. The amount of control that is available depends on the driver. To fully understand and exploit the capabilities of a particular sound card, you will need the documentation from the card's manufacturer.

> [!Note]  
> You can capture from the CD-Audio input, but this audio stream has already gone through the digital-to-analog converter, so there will be a loss of sound quality from the original CD.

 

## Related topics

<dl> <dt>

[Audio Capture](audio-capture.md)
</dt> </dl>

 

 



