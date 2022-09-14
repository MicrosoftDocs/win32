---
description: Glitches can occur in XAudio2, this topic covers how they are reported and some approaches to fixing them.
ms.assetid: 360d1c5a-82e7-c982-82ea-5b5c7d69bc25
title: Debugging Audio Glitches in XAudio2
ms.topic: article
ms.date: 05/31/2018
---

# Debugging Audio Glitches in XAudio2

Glitches can occur in XAudio2, this topic covers how they are reported and some approaches to fixing them.

This overview covers the following topics:

-   [Causes of audio output problems or glitches](#causes-of-audio-output-problems-or-glitches)
-   [How XAudio2 reports problems](#how-xaudio2-reports-problems)
-   [Approaches to fixing problems](#approaches-to-fixing-problems)
-   [Related topics](#related-topics)

## Causes of audio output problems or glitches

Glitches can occur in XAudio2 output for several reasons.

-   An XAudio2 source voice is starved. The client is not submitting fresh audio to it fast enough. You get silence because it has no data to play.
-   XAudio2 as a whole is overburdened. It takes longer than *X* ms to produce *X* ms of audio. You get dropouts because XAudio2 can't produce data as fast as the audio device needs it. You might be running too many voices or effects at a time, doing too much work in XAudio2 callbacks, or making XAudio2 API calls too frequently.
-   The audio processing thread is stalling because the client's implementation of some XAudio2 callback is doing things that can block the thread. For example, it might be accessing the disk, synchronizing with other threads, or calling other functions that may block. Use a lower-priority background thread that the callback can signal to perform such tasks.
-   The system as a whole is overloaded. Other threads running at the same or higher priority than XAudio2 are doing too much work. They are competing with the audio thread for CPU time.

## How XAudio2 reports problems

XAudio2 can communicate glitches in the debug build in several ways.

-   If a voice is being starved, XAudio2 shows a message in this form.

    ``` syntax
    XAudio2: WARNING: Voice at 0xNNNNNNNN starved: no more source buffers are available, but no end-of-stream marker was received
    ```

-   If the audio thread runs for too long, XAudio2 shows a message in this form.

    ``` syntax
    XAudio2: WARNING: Spent Xms in audio thread; XAudio2 possibly overloaded
    ```

    Typically, this message occurs with the next message.

-   If the audio driver can't be fed new audio data on time, XAudio2 shows a message in this form.

    ``` syntax
    XAudio2: WARNING: Glitch at output sample X
    ```

-   Calling [**IXAudio2::GetPerformanceData**](/windows/win32/api/xaudio2/nf-xaudio2-ixaudio2-getperformancedata) provides XAudio2 performance data, including the total number of glitches since the XAudio2 engine started.

## Approaches to fixing problems

Possible ways to reduce audio glitches include the following.

-   In the voice starvation case: Increase the amount of audio data that is queued ahead on a voice. You can use [**IXAudio2SourceVoice::GetState**](/windows/win32/api/xaudio2/nf-xaudio2-ixaudio2sourcevoice-getstate) to discover the number of buffers queued at any moment. If you still see voice starvation errors, but can't hear any glitch, make sure you are setting [**XAUDIO2\_BUFFER**](/windows/desktop/api/xaudio2/ns-xaudio2-xaudio2_buffer).**Flags** to XAUDIO2\_END\_OF\_STREAM on the final buffer of a sound. This tells XAudio2 not to expect any more buffers necessarily to be available as soon as this one completes.

    In the other cases:

    -   Reduce the number of active voices and effects in the graph, especially expensive effects like reverb.
    -   Disable voices and effects you're not using.
    -   Use the XAUDIO2\_VOICE\_NOSRC and XAUDIO2\_VOICE\_NOPITCH flags in [**IXAudio2::CreateSourceVoice**](/windows/win32/api/xaudio2/nf-xaudio2-ixaudio2-createsourcevoice), whenever possible. Sample rate conversion is costly.
    -   Reduce the sample rate of individual voices. For example, a submix voice hosting a reverb effect can have a lower sample rate than the source voice sending to it. Sounds such as explosions and gunshots that don't need high fidelity can also be recorded at lower sample rates.
    -   Ensure that callback implementations do as little work as possible and never block.
    -   Make fewer calls to XAudio2. Audio parameters usually don't need to be updated for every video frame. Every 30 ms or so is sufficient. You should eliminate redundant calls, such as setting volume several times in quick succession.
    -   Reduce the game's overall CPU usage.

## Related topics

<dl> <dt>

[Debugging Facilities](debugging-facilities.md)
</dt> <dt>

[XAudio2 Programming Reference](programming-reference.md)
</dt> </dl>

 

 
