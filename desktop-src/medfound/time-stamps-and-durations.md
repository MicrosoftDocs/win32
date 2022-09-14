---
description: This topic describes how Media Foundation Transforms should handle time stamps.
ms.assetid: 4ab576ce-becd-4736-921e-e463c0dff841
title: Time Stamps and Durations
ms.topic: article
ms.date: 05/31/2018
---

# Time Stamps and Durations

This topic describes how [Media Foundation Transforms](media-foundation-transforms.md) should handle time stamps.

An MFT must set as accurate a time stamp and duration as possible on all output samples. For a simple MFT that takes one input buffer and completely processes it into an output buffer, the MFT should just copy the time stamp and duration directly from the input sample to the output sample. However, many transforms are more complex than this and may require more complex calculations of output time. All MFTs should observe the following basic rules:

-   An MFT should try to put a time stamp and duration on all uncompressed video or audio output samples if an accurate time stamp or duration is given on the input samples or can be calculated. Interpolation may be required for some output time stamps, especially for decoders.
-   The time stamps and durations of the input samples should be preserved on the output samples as much as possible.
-   The output time stamps or durations might not match the input because the MFT is holding back data or breaking the output into different-sized pieces than the input. In that case, the MFT should calculate the output time stamp from the earliest input sample that contains data used to create the output sample. To calculate the output time stamp, add the input time stamp of the appropriate input sample to the duration of data that has already been transformed from that sample. The second example at the end of this section illustrates this idea.
-   If the input samples have duration, that duration should be preserved. If an input sample does not have duration, the MFT should calculate a duration if possible from the size of the output buffer or the data rate given by the media type.
-   Calculated durations should be truncated (rounded down), not rounded to the nearest increment. The pipeline has enough slack to handle durations that are slightly inaccurate, but it is easier for the pipeline to handle a duration that is 1% too short than a duration that is 1% too long. That said, there is no reason to deliberately shorten the durations, other than by rounding.

### Decoders

A decoder converts compressed packets into uncompressed data. Because the output is uncompressed, decoders have a special obligation to get the time stamps and durations correct. Some compressed formats, most notably MPEG-2, do not have time stamps on all input packets and often have no duration on any packet. For these formats, the decoder is responsible for putting a valid time stamp and duration on every output sample, by summing the implied durations of all the output since the last time-stamped input sample.

For video, if the duration is not available in the compressed format, the decoder should calculate the duration as the inverse of the frame rate, converted to 100-nanosecond units and rounded down.

For audio, if the duration is not available in the compressed format, the decoder should calculate the duration as the inverse of the audio sample rate multiplied by the number of samples in the output buffer, converted to 100-nanosecond units and rounded down.

The only time a transform should output a sample without a time stamp is if the MFT has never received a time stamp on an input sample, or if there is no way to calculate an accurate output time stamp from the previous input time stamp.

### Audio Decoders

For audio decoders, the duration of each output sample is calculated from the audio sampling rate and the number of PCM samples per channel in the output buffer.

The correct way to calculate output time stamps depends on whether the input samples contain time stamps.

If the input samples contain time stamps, the decoder calculates the output time stamps from the input time stamps, as follows:

-   If each input buffer contains a one or more complete compressed frames, with no partial frames, the output time stamp equals the input time stamp, minus the known latency of the decoder. For example, a Dolby Digital (AC-3) decoder has a latency of 256 PCM samples. For example, at 48-kHz sampling rate, the latency is 5.33 milliseconds (msec). Therefore, if the input time stamp is 1000 msec, the output time stamp is 1000 – 5.33 = 994.66 msec. If the input buffer includes more than one whole compressed frame, the decoder will produce one output sample for every frame in the input sample. All output samples will be time stamped correctly such that there are no gaps.
-   Depending on the transport format, an input buffer might contain partial frames. For example, a buffer might contain part of a frame from the previous input buffer, followed by one or more complete frames, followed by the start of the next frame. In this case, it is generally correct to assume that the input time stamp corresponds to the first frame that starts within the buffer. (That is, a partial frame that started in the previous buffer is not included in the time stamp for the current buffer.) Calculate the output time stamp accordingly.

If the input samples do not contain any time stamps:

-   The decoder should generate its own time stamps, setting the first output time stamp to zero.
-   The sample duration is calculated from the number of output samples in the buffer and the sample rate.
-   Subsequent time stamps are calculated from the previous time stamp and duration: Current time stamp + current duration = next time stamp. There should be no gaps in the output time stamps.

If the input stream initially contains time stamps, but for some reason switches to no time stamps, the decoder should continue to generate its own output time stamps, such that they are continuous and there is no gap.

If the input stream contains time stamps, but there are gaps in the times, the decoder will simply propagate these gaps. In other words, the decoder should not attempt to fix inconsistent time stamps in the input stream.

### Mixers

> [!Note]  
> In Windows Vista, the Media Foundation pipeline does not support MFTs with more than one input. Multiple-input MFTs are supported in Windows 7.

 

A mixer takes multiple inputs and mixes them into one output. If the input streams are not completely rate-locked, or are slightly offset in time from each other, there can be ambiguity about which time to set on the output. Here are some guidelines, depending on the media type:

-   Audio. At startup or immediately after a drain or flush, an audio mixer should wait to produce output samples until it has received an input sample on all required input streams. At that point, it should choose the earliest time stamp of the initial samples to use as a baseline for the output time stamps. The other streams should be padded with silence to make up any time discrepancy. If a sample is received on an optional input stream, it should also be factored into the calculation. From that point on, the MFT should strive to produce a continuous and unbroken chain of output time stamps. In general, the MFT should not try to account for one stream drifting relative to another. Instead, it should calculate the output time stamps from the baseline time stamp, the output rate, and the buffer sizes. When another drain or flush occurs, the MFT should reset its baseline time stamps.

-   Video. At startup or immediately after a drain or flush, a video mixer should wait to produce output samples until it has received an input sample on all required input streams. At that point, it should choose the earliest time stamp of the initial samples to use as a baseline for the output time stamps. In general, it should strive to keep continuous and regular output time stamps and fixed durations, even if the input is not as regular, if necessary by repeating input frames.

### Encoders

An encoder converts uncompressed audio or video into compressed packets. An encoder should follow these guidelines:

-   The encoder should follow the conventions of the output format. If the format does not typically time stamp every sample, as in MPEG-2, not every output sample needs to have a time stamp and a duration.

-   The input time stamps should be preserved in the output format, if the format has fields for time stamps, unless better time information is a available from another source, such as the application itself.

### Multiplexers

> [!Note]  
> In Windows Vista, the Media Foundation pipeline does not support MFTs with more than one input. Multiple-input MFTs are supported in Windows 7.

 

A multiplexer combines two different audio or video streams into one interleaved format, such as AVI or MPEG-2 Transport Stream. A multiplexer should follow these guidelines:

-   The multiplexer should follow the conventions of the output format. If the format does not typically time stamp every sample, as in MPEG-2, not every output sample needs to have a time stamp and a duration.

-   The time stamp should reflect the earliest time that would be placed on any frame that begins in that packet, or the time of the first audio sample that would be decoded from that packet. Ignore this guideline if it conflicts with the conventions of the output format.

### Demultiplexers

A demultiplexer splits an interleaved format, such as AVI or MPEG-2 Transport Stream, into the underlying audio and video streams.

If the format contains specific time stamp information that can be used to calculate accurate output time stamps based on the input time stamps, that information should be used. However, if the format contains times in a completely different base that bear no relation to the input time stamps, and an accurate offset to the input time stamp cannot be calculated, the format's own times should be ignored.

If the format does not have usable time stamp information, the demultiplexer should follow these rules:

-   Uncompressed output streams should have valid time stamps and durations if possible, calculated from the closest previous input time stamp.

-   Compressed output streams should have time stamps on only the first output sample derived from an input sample with a time stamp. If the input sample does not have a time stamp, no output samples derived from that input sample should have a time stamp. If the input sample is broken into multiple output samples, only the first output sample should have a time stamp, and the rest should have no time stamps.

### Examples

Example 1. Suppose that a video effect always takes an uncompressed input frame, applies the effect, and copies it to the output. It never holds back any frames or buffers any input. This MFT simply copies the time stamp and duration from the input sample to the output sample, if they are available, and does no time calculations at all.

Example 2. Suppose that an audio effect transforms all but 10 milliseconds (ms) of each input buffer, saving the extra 10 ms to combine with the next buffer. It gets a stream of samples that all have a duration of 50 ms. The input times are shown in the following table.



| Sample | Input time | Input duration | Output time | Output duration |
|--------|------------|----------------|-------------|-----------------|
| 1      | 20         | 50             | 20          | 40              |
| 2      | 70         | 50             | 60          | 50              |
| 3      | 121        | 50             | 110         | 50              |
| 4      | 171        | 50             | 161         | 50              |



 

Note the 1-ms discrepancy between the actual duration of sample 2 and the implied duration based on the next time stamp (121 ? 70 = 51).

Because the MFT holds back 10 ms, it outputs the first 40 ms of input sample 1 as output sample 1, with a time stamp of 20 ms and a duration of 40 ms.

Output sample 2 combines the 10 ms previously held back with 40 ms of input sample 2. This sample is given a time stamp of 60 ms (the time stamp of the previous input sample, 20ms, plus the duration of the data already processed from that sample, 40ms). It is given a duration of 50ms.

Similarly, the next sample has a time stamp of 110ms (70ms + 40ms) with a duration of 50 ms.

The next calculation is more interesting. The implied time stamp from the previous output time and duration would be 160 ms (time stamp 110 ms + duration 50 ms). However, the output time stamp is supposed to be calculated from the input time stamp of the earliest input sample that overlaps the output sample in time, plus the length of any data already processed from that sample. The closest overlapping input sample is the sample 4 (time stamp = 171), but this is not the earliest one. The earliest overlapping sample is sample 3 (time stamp = 121). Adding the 40ms that has already been processed from that sample, the result is 161.

## Related topics

<dl> <dt>

[Writing a Custom MFT](writing-a-custom-mft.md)
</dt> </dl>

 

 



