---
title: Calculating Bit Rate and Buffer Window Values for Arbitrary Streams
description: Calculating Bit Rate and Buffer Window Values for Arbitrary Streams
ms.assetid: 28ba863b-9c3e-4b0e-875d-6b696600888c
keywords:
- streams,bit rates
- codecs,calculating bit rates for arbitrary streams
- bit rates,calculating for arbitrary streams
- streams,calculating bit rates for arbitrary streams
ms.topic: article
ms.date: 05/31/2018
---

# Calculating Bit Rate and Buffer Window Values for Arbitrary Streams

Calculating the proper bit rate and buffer window for an arbitrary stream type is not an exact science. One simple approach is to set the bit rate to match the size of the stream divided by its length, in seconds. For example, a stream containing a total of 68000 bits lasting 20 seconds might have a bit rate of 3400 bits per second (68000 bits / 20 seconds = 3400 bits per second).

The problem with this simple technique of assigning bit rate is that it does not take into account the distribution of data within the stream. Many arbitrary streams contain larger amounts of data at intervals along the timeline of the file. Image streams, for example, have samples that are rather large, but are usually spaced several seconds apart. The buffer window must be set to ensure that the buffer will not overflow.

To check the buffer window, multiply the bit rate (bits per second) by the buffer window (in seconds) and divide by 1000 to get the size, in bits, of the buffer for the stream. Then make sure that the buffer size is large enough to hold any combination of samples in the stream that are less than the buffer window apart in presentation time. When in doubt, set both values a little higher than you think you need them.

## Related topics

<dl> <dt>

[**Buffering Content**](buffering-content.md)
</dt> <dt>

[**Configuring Arbitrary Stream Types**](configuring-arbitrary-stream-types.md)
</dt> </dl>

 

 




