---
description: Encoding Methods
ms.assetid: 17ab5ecc-0173-4c5c-9d65-40e506ab7e07
title: Encoding Methods (Microsoft Media Foundation)
ms.topic: reference
ms.date: 05/31/2018
---

# Encoding Methods (Microsoft Media Foundation)

Most of the Windows Media Audio and Video codecs support multiple encoding methods. Knowing how and when to use each method can help you create high-quality compressed content.

The encoding methods all focus on the buffer used by the decoder to manage compressed input data. This buffer is defined by the bit rate of the stream, in bits per second, and the buffer window, in milliseconds. When encoding, the codec abides by the restraints of the buffer. For more information about the buffer, see [The Leaky Bucket Buffer Model](the-leaky-bucket-buffer-model.md).

## Constant Bit Rate Encoding

The bit rate for any stream encoded by one of the Windows Media Audio and Video codecs is not constant. Constant bit rate (CBR) encoding is, therefore, a somewhat misleading term. The distinguishing feature of a CBR-encoded stream is a small buffer window, which limits the variation of sample sizes. CBR encoding is used primarily for content that is streamed over a network to its destination. In such a scenario, it is important to be able to rely on consistent bandwidth usage.

From a configuration point of view, CBR encoding differs from the other modes in that before starting to encode, you set both the average bit rate of the output content, and the buffer window that applies to that bit rate. In other modes, one or both of those values is unknown when you configure the encoder, and is computed by the codec while it encodes. CBR is the standard encoding mode used by the Windows Media Encoder DMOs.

## Two-Pass Constant Bit Rate Encoding

Standard CBR uses only a single encoding pass. You provide your content as input samples, and the codec compresses the content and returns output samples. It is also possible to process input samples twice. On the first pass, the codec performs calculations to optimize encoding for your content. On the second pass, the codec uses the data gathered during the first pass to encode the content.

Two-pass CBR encoding has many advantages. It often yields significant quality gains over standard CBR encoding without changing any of the buffering requirements. This makes this encoding mode ideal for content that is streamed over a network. The only situation where two-pass CBR is not feasible is when you encode content from a live source and cannot use a second pass.

The output media type of a two-pass CBR stream is identical to that of a standard CBR stream; you still specify the bit rate and buffer window to use. When configuring the DMO, you must set it to perform two passes. And you must notify the DMO when you are finished sending samples for the first pass.

## Quality-Based Variable Bit Rate Encoding

Because CBR encoding does not actually maintain a constant bit rate, the distinction between it and variable bit rate encoding (VBR) may seem a little hazy. The primary difference between CBR and VBR is the size of the buffer window used. VBR-encoded streams usually have large buffer windows compared to CBR-encoded streams. Quality-based VBR is no exception, in that you define neither bit rate nor buffer window for it. Instead, you set a quality value. The codec then attempts to compress the data so that the quality of the encoded media is consistent throughout its duration, regardless of the buffer requirements of the resulting stream.

Quality-based VBR uses a single encoding pass and tends to create large compressed streams. When encoding is complete, the codec sets the buffer requirements so that the decoder can decompress the data. The encoded VBR stream is not suitable for streaming over a network, so quality-based VBR should be used only for local playback scenarios (or download and play).

## Unconstrained Variable Bit Rate Encoding

Unlike quality-based VBR, unconstrained VBR does not encode to a specific quality level. Instead, it encodes the content to the highest possible quality while maintaining a specified bit rate. Unconstrained VBR uses two encoding passes and is similar to two-pass CBR, except that you do not specify a buffer window setting for the stream. This means that there is no limit to the size of individual samples in the stream, as long as the average bit rate is less than or equal to the value you set.

Unconstrained VBR is of limited use, because there are few playback scenarios that have requirements in keeping with its buffer requirements. The codec can set the buffer window to whatever value is required after encoding, giving you no control over the buffer size. In most cases, if you are not concerned about the size of the buffer or the consistency of bandwidth usage, you should use quality-based VBR.

## Peak-Constrained Variable Bit Rate Encoding

The final encoding mode is peak-constrained VBR. Like unconstrained VBR, this mode uses two encoding passes and encodes to a specified bit rate. However, with peak constrained VBR you also configure the peak value for the encoding. Peak values are similar to normal buffer configuration values: there is a peak bit rate and a peak buffer window. The file is encoded to conform to a buffer described by the peak values, with the condition that the overall average bit rate of the stream be equal to or less than the average bit rate value you specify.

Constrained VBR can be difficult to conceptualize. Here is the easiest way to think of the buffering model used. Suppose the stream is a CBR stream with the peak bit rate and peak buffer window used to define the buffer. Typically, the peak bit rate is quite high. The encoder ensures that the expected average bit rate value you indicate is maintained over the duration of the stream. At any particular point in the stream, the average bit rate is guaranteed to be greater than the total stream size in bits divided by the stream duration in seconds).

Consider the following example: You configure a stream with an average bit rate of 16,000 bits per second, a peak bit rate of 48,000 bits per second, and a peak buffer window of 3,000 (3 seconds). The size of the buffer used for the stream is 144,000 bits (48,000 bits per second x 3 seconds) as determined by the peak values. The encoder compresses the data to conform to that buffer. Additionally, the average bit rate of the stream must be 16,000 or less. If the encoder needs to make some very large samples to handle a complex segment of content, it can take advantage of the large buffer size. But other parts of the stream must be encoded at a lower bit rate to bring the average down to the specified level.

Peak-constrained VBR encoding is useful for playback devices with a finite buffer capacity and some data rate constraints. A common example of this is the encoding used for DVDs.

## Related topics

<dl> <dt>

[Using VBR Encoding](usingvbrencoding.md)
</dt> <dt>

[Windows Media Codecs](windows-media-codecs.md)
</dt> </dl>

 

 



