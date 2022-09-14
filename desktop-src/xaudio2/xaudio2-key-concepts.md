---
description: This overview introduces some key concepts for using XAudio2.
ms.assetid: 103e939f-7815-51c5-159a-c607da1e99ba
title: XAudio2 Key Concepts
ms.topic: article
ms.date: 05/31/2018
---

# XAudio2 Key Concepts

This overview introduces some key concepts for using XAudio2.

-   [XAudio2 Engine](#xaudio2-engine)
-   [Voices](#voices)
-   [Audio Graph](#audio-graph)
-   [Callbacks](#callbacks)
-   [Related Topics](#related-topics)

## XAudio2 Engine

The [**IXAudio2**](/windows/desktop/api/xaudio2/nn-xaudio2-ixaudio2) interface is the core of the XAudio2 engine. Creating an instance of the **IXAudio2** interface allows the client to enumerate the available audio devices, to configure global API properties, to create voices, and to monitor performance. The [**XAudio2Create**](/windows/desktop/api/xaudio2/nf-xaudio2-xaudio2create) helper function performs instantiation and initialization tasks for XAudio2.

You can create instances of XAudio2 multiple times within a single process. Each XAudio2 object operates independently, and has its own audio processing thread. Only the debug settings are shared. This is important on Windows where several different components may be loaded in a single process. For example, Internet Explorer might use multiple XAudio2 components simultaneously. Although it is possible to create multiple XAudio2 engine objects within a single client application, you should not pass information between their respective graphs.

For an example of initializing the XAudio2 engine, see [How to: Initialize XAudio2](how-to--initialize-xaudio2.md).

## Voices

Voices are the objects XAudio2 use to process, to manipulate, and to play audio data. There are three types of voices in XAudio2.

-   [**Source Voices**](/windows/desktop/api/xaudio2/nn-xaudio2-ixaudio2sourcevoice)

    Source voices represent a stream of audio data. Source voices send their data to other types of voices.

-   [**Submix Voices**](/windows/desktop/api/xaudio2/nn-xaudio2-ixaudio2submixvoice)

    Submix voices perform some manipulation of audio data they receive. One example of audio data manipulation might be sample rate conversion. After a submix voice processes data, it passes that data to another submix voice or to a master voice.

-   [**Mastering Voices**](/windows/desktop/api/xaudio2/nn-xaudio2-ixaudio2masteringvoice)

    Mastering voices receive data from source voices and submix voices, and sends that data to the audio hardware.

See [XAudio2 Voices](voices.md) for an overview of XAudio2 voices.

## Audio Graph

An audio graph is a collection of XAudio2 voices. Audio starts at one side of an audio graph in source voices, optionally passes through one or more submix voices, and ends at a mastering voice. An audio graph will contain a source voice for each sound currently playing, zero or more submix voices, and one mastering voice. The simplest audio graph, and the minimum needed to make a noise in XAudio2, is a single source voice outputting directly to a mastering voice. See [How to: Play a Sound with XAudio2](how-to--play-a-sound-with-xaudio2.md) for an example of the minimum steps need to play a sound with XAudio2.

See [XAudio2 Audio Graph](audio-graphs.md) for an overview of XAudio2 audio graphs.

## Callbacks

Callbacks are the mechanism XAudio2 uses to signal client code that some event has occurred in a voice or in the engine object. Because audio playback is asynchronous in the XAudio2 engine, callbacks provide the only way to determine when a sound is finished playing.

See [XAudio2 Callbacks](callbacks.md) for an overview of XAudio2 callbacks.

## Related topics

<dl> <dt>

[Getting Started](getting-started.md)
</dt> <dt>

[XAudio2 Versions](xaudio2-versions.md)
</dt> <dt>

[How to: Initialize XAudio2](how-to--initialize-xaudio2.md)
</dt> <dt>

[How to: Play a sound with XAudio2](how-to--play-a-sound-with-xaudio2.md)
</dt> </dl>

 

 



