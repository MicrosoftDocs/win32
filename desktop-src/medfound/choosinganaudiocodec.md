---
description: Choosing an Audio Codec
ms.assetid: 37f3582c-c718-42ae-b887-d7d31ee853e9
title: Choosing an Audio Codec (Microsoft Media Foundation)
ms.topic: article
ms.date: 05/31/2018
---

# Choosing an Audio Codec (Microsoft Media Foundation)

The [**Windows Media Audio Encoder**](windowsmediaaudioencoder.md) provides three categories of audio encoding as shown in the following table.



| Category                         | Purpose                                                    |
|----------------------------------|------------------------------------------------------------|
| Windows Media Audio Standard     | General-purpose compression of audio.                      |
| Windows Media Audio Professional | Compressing multi-channel and high-definition audio.       |
| Windows Media Audio Lossless     | Compressing audio without losing any of the original data. |



 

The Standard category provides general-purpose audio encoding suitable for a variety of playback scenarios. For example, it can compress audio to a low bit rate for streaming over a network with limited bandwidth, or for rendering on portable devices. On the other end of the scale, it can produce compressed audio content for high-quality playback. The emphasis of the Standard encoding algorithms is on music, but they are suitable for other complex audio content as well. The Standard category should be your default for audio content. The Professional and Lossless categories should be used to meet specific needs.

A separate encoder, the [**Windows Media Voice Encoder**](windowsmediaaudiovoiceencoder.md), provides compression of speech.

## Related topics

<dl> <dt>

[Working with Audio](workingwithaudio.md)
</dt> </dl>

 

 



