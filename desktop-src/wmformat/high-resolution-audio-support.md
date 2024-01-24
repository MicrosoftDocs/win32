---
title: High-Resolution Audio Support
description: High-Resolution Audio Support
ms.assetid: 9545420f-70c4-4fd7-9033-5b5c7712c04c
keywords:
- Windows Media Format SDK,high-resolution audio support
- Windows Media Format SDK,audio support
- codecs,high-resolution audio support
- codecs,audio support
- high-resolution audio
ms.topic: article
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# High-Resolution Audio Support

\[The feature associated with this page, [Windows Media Format 11 SDK](/windows/win32/wmformat/windows-media-format-11-sdk), is a legacy feature. It has been superseded by [Source Reader](/windows/win32/medfound/source-reader) and [Sink Writer](/windows/win32/medfound/sink-writer). **Source Reader** and **Sink Writer** have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **Source Reader** and **Sink Writer** instead of **Windows Media Format 11 SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

Both the Windows Media Audio 9 Professional codec and the Windows Media Audio 9 Lossless codec support high-resolution audio. High-resolution audio is defined as an audio format with more than 16 bits per sample. The number of bits that are used for an individual audio sample affects the fidelity of the encoded sound wave.

Because PCM-encoded sound formats have been used in Windows operating systems for a long time, some of the Windows functions are old and unable to process high-resolution PCM audio. As a result, high-resolution PCM formats are represented by using different structures than standard audio. For more information, see [Working with High-Resolution PCM Audio](working-with-high-resolution-pcm-audio.md).

## Related topics

<dl> <dt>

[**Codec Features**](codec-features.md)
</dt> </dl>

 

 




