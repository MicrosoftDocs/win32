---
description: Streaming is the process of maintaining only a small portion of a playing audio file in memory. This allows large audio files such as background music to be played, and not take up a large amount of memory.
ms.assetid: 7a938ea6-15ef-66b1-0276-88eabf9a722b
title: XAudio2 Streaming Audio Data
ms.topic: article
ms.date: 05/31/2018
---

# XAudio2 Streaming Audio Data

Streaming is the process of maintaining only a small portion of a playing audio file in memory. This allows large audio files such as background music to be played, and not take up a large amount of memory.

When an audio file is streamed, its data is read from disk in chunks rather than loading the entire file at once. Streaming is accomplished by asynchronously reading audio data into a queue of disk buffers. Each buffer is filled, and then submitted to a source voice. After the voice finishes playing a buffer, the buffer becomes available for reading again. Looping through the disk buffers in this manner allows a large audio file to be played while only a portion of its data is loaded. The streaming code should be placed in a separate thread, where it can sleep while waiting for long-running disk and audio operations to finish. A callback class is used to wake the thread by triggering events when audio operations have finished.

For an example of how streaming can be accomplished with XAudio2, see [How to: Stream a Sound from Disk](how-to--stream-a-sound-from-disk.md).

## Related topics

<dl> <dt>

[Streaming Audio Data](streaming-audio-data.md)
</dt> <dt>

[XAudio2 Programming Guide](programming-guide.md)
</dt> </dl>

 

 



