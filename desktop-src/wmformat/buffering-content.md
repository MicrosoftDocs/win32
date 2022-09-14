---
title: Buffering Content
description: Buffering Content
ms.assetid: e14e0130-aefd-4e46-b288-4302d2333de2
keywords:
- Windows Media Format SDK,buffering content
- buffering content
ms.topic: article
ms.date: 05/31/2018
---

# Buffering Content

When the reader object opens a streaming file, it determines the size of the buffer based upon settings in the header of the file. You can think of the buffer as a bucket with a hole in the bottom that leaks at a constant rate. As long as the rate at which the bucket is filled is not, on average, greater than the rate at which it is leaking, the bucket will never overflow.

The rate at which the imaginary bucket leaks is the bit rate of the stream. The rate at which the bucket fills is the actual streaming bit rate. The data in a compressed stream varies in size from sample to sample depending on the amount of compression that was achieved. Thus, even though the bit rate of the stream is set in the profile, it represents the average bit rate, not a constant.

The other stream setting important to the buffering process is the buffer window. The buffer window is measured in time and specifies how much content can be buffered. The capacity of the imaginary bucket can be found using the buffer window. For example, if you have a stream with a bit rate of 32 Kbps and a buffer window of 3 seconds, the buffer is sized to hold 3 seconds of 32 Kbps content, or 12,000 bytes (32,000 bits per second x 3 seconds / 8 bits per byte). The codec limits the variation between the actual streaming bit rate of encoded samples so that over a period of time equal to the buffer window, the average bit rate is no greater than the bit rate of the stream.

Normally, you set the bit rate and buffer window for a stream in a profile, and the writer handles the rest. When passing compressed samples to the reader, however, you must ensure that the correct values are transferred to the new file by setting the bit rate and buffer window for the stream in the destination profile to the values from the compressed stream.

## Related topics

<dl> <dt>

[**Concepts**](concepts.md)
</dt> <dt>

[**Media Samples**](media-samples.md)
</dt> <dt>

[**Inputs, Streams and Outputs**](inputs-streams-and-outputs.md)
</dt> </dl>

 

 




