---
description: XAudio2 is a low-level audio API. It provides a signal processing and mixing foundation for games that is similar to its predecessors, DirectSound and XAudio.
ms.assetid: c87be63a-58b5-9cd1-1f03-f32b5a858b2e
title: XAudio2 Introduction
ms.topic: article
ms.date: 05/31/2018
---

# XAudio2 Introduction

XAudio2 is a low-level audio API. It provides a signal processing and mixing foundation for games that is similar to its predecessors, DirectSound and XAudio.

XAudio2 is the long-awaited replacement for DirectSound. It addresses several outstanding issues and feature requests.

## XAudio2 Features

The following is a list of XAudio2 features and new functionality that enable developers to improve performance in their games.

-   DSP Effects and Per Voice Filtering

    Digital Signal Processing (DSP) effects are the pixel shaders of audio. They handle everything from transforming a sound—turning a pig squeal into a low, scary monster sound—to placing sounds in the game environment using reverb and occlusion or obstruction filtering. XAudio2 provides a flexible and powerful DSP framework. It also provides a built-in filter on every voice, for efficient low/high/band-pass filtering effects.

    See [XAudio2 Audio Effects](xaudio2-audio-effects.md) and [**IXAudio2Voice::SetFilterParameters**](/windows/win32/api/xaudio2/nf-xaudio2-ixaudio2voice-setfilterparameters) for more information about DSP effects and per voice filtering.

-   Submixing

    Submixing combines several sounds into a single audio stream—for example, an engine sound made up of composite parts, all of which are playing simultaneously. Also, you can use submixing to process and combine similar parts of a game. For example, you could combine all game sound effects to allow a user volume setting to be applied while a separate setting controls music volume. Combined with DSP, submixing provides the type of data routing and processing necessary for today's games. XAudio2 allows for arbitrary levels of submixing, enabling the creation of complex sounds and game mixes.

    See [XAudio2 Audio Graph](xaudio2-audio-graph.md) and [XAudio2 Voices](xaudio2-voices.md) for more information about submixing.

-   Compressed Audio Support

    One of the major feature requests for DirectSound has been for compressed audio support. XAudio2 supports compressed formats—ADPCM—natively with run-time decompression.

-   Enhanced Multichannel and Surround Sound Support

    Multichannel, 3D, and surround sound support is expanded. 3D and surround sound are now much more flexible and transparent. XAudio2 removes the 6-channel limit on multichannel sounds, and supports multichannel audio on any multichannel-capable audio card. The card does not need to be hardware-accelerated.

-   Multirate Processing

    To help minimize CPU usage, XAudio2 provides the technology to create multiple, low-rate audio processing graphs. This can significantly reduce CPU usage by allowing a game to process audio at the rate of the source material if the rate is less than 48 kHz.

-   Nonblocking API Model

    With few exceptions, an XAudio2 method call will not block the audio processing engine. This means that a client can safely make a set of method calls at any time without blocking on long-running calls causing delays. The exceptions are the [**IXAudio2Voice::DestroyVoice**](/windows/win32/api/xaudio2/nf-xaudio2-ixaudio2voice-destroyvoice) method (which may block the engine until the voice being destroyed is finished processing) and the methods that terminate the audio thread: [**IXAudio2::StopEngine**](/windows/win32/api/xaudio2/nf-xaudio2-ixaudio2-stopengine) and [**IXAudio2::Release**](/windows/win32/api/xaudio2/nf-xaudio2-ixaudio2-release). Note that while XAudio2 method calls will not block the audio processing engine, the XAudio2 methods contain critical sections and may themselves become blocked in some circumstances.

## When to use XAudio2

XAudio2 is primarily intended for developing high performance audio engines for games. For game developers who want to add sound effects and background music to their modern games, XAudio2 offers an audio graph and mixing engine with low-latency and support for dynamic buffers, synchronous sample-accurate playback, and implicit source rate conversion. Compared to WASAPI, XAudio2 requires only a minimum amount of code even for complex audio solutions. Compared to the Media Foundation engine, XAudio2 is a low-level, low-latency C++ API that is designed for use in games.

For applications that simply need regular music playback, the Media Foundation engine may be a better match to the application's requirements.

## Related topics

<dl> <dt>

[Programming Guide](programming-guide.md)
</dt> <dt>

[Getting Started](getting-started.md)
</dt> <dt>

[XAudio2 Programming Reference](programming-reference.md)
</dt> </dl>

 

 
