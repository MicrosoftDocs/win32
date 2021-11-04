---
title: Media Samples (Windows Media Format 11 SDK)
description: Learn about media samples in the Windows Media Format 11 SDK. A media sample is an object that contains an ordered list of zero or more buffers.
ms.assetid: '5fe0d261-c4a8-4b8e-b5dd-668ce067723c'
keywords:
- Windows Media Format SDK,media samples
- Windows Media Format SDK,samples
- Advanced Systems Format (ASF),media samples
- ASF (Advanced Systems Format),media samples
- Advanced Systems Format (ASF),samples
- ASF (Advanced Systems Format),samples
ms.topic: article
ms.date: 05/31/2018
---

# Media Samples (Windows Media Format 11 SDK)

A media sample, or sample, is a block of digital media data. A sample is the basic unit that is manipulated by the reading and writing objects of the Windows Media Format SDK. The contents of an individual sample are dictated by the media type associated with the sample. For video, each sample represents a single frame. For audio, the amount of data in an individual sample is set in the profile used to create the ASF file.

Samples can contain uncompressed data, or they can contain compressed data, in which case they are called *stream samples*. When creating an ASF file, you pass samples to the writer. The writer coordinates compression of the samples with the appropriate codec and arranges the compressed data in the data section of the ASF file. On playback, the reader reads the compressed data, decompresses it, and provides the reconstructed uncompressed data as output samples.

All samples used by the Windows Media Format SDK are encapsulated in buffer object whose memory is allocated automatically by the SDK run-time components. You can also allocate your own buffers if you need to, using advanced features of the writer and reader.

**Note** The term sample is used in this SDK to refer to a media sample, not an audio sample. In audio encoding, a sample refers to a single encoded audio value. Typically, the quality of encoded audio is specified by a number of samples per second. For example, CD quality sound is recorded at 44,100 samples per second. This value is commonly abbreviated with the Hz notation, so 44,100 samples per second would be 44,100 Hz or 44.1 kHz.

## Related topics

<dl> <dt>

[**Concepts**](concepts.md)
</dt> <dt>

[**INSSBuffer Interface**](/previous-versions/windows/desktop/api/wmsbuffer/nn-wmsbuffer-inssbuffer)
</dt> <dt>

[**Inputs, Streams and Outputs**](inputs-streams-and-outputs.md)
</dt> </dl>

 

 




