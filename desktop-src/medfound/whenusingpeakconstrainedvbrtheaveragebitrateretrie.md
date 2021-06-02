---
description: When I use peak-constrained VBR, the average bit rate retrieved from the codec object is larger than the peak bit rate.
ms.assetid: 5fc344f8-4492-4878-802a-94606c5f33e0
title: When I use peak-constrained VBR, the average bit rate retrieved from the codec object is larger than the peak bit rate. How is that possible?
ms.topic: article
ms.date: 05/31/2018
---

# When I use peak-constrained VBR, the average bit rate retrieved from the codec object is larger than the peak bit rate. How is that possible?

The relationship between the average bit rate and the peak bit rate is often misunderstood. The peak bit rate describes a buffer constraint over a period of time specified by the peak buffer window. The average bit rate for two-pass VBR (unconstrained or peak-constrained) is the average bits per second over the duration of the file.

As described in [The Leaky Bucket Buffer Model](the-leaky-bucket-buffer-model.md), the actual bit rate used over a period of time equal to the buffer window can approach twice the bit rate. This is because the buffer, defined as a number of bits equal to the bit rate times the buffer window (in seconds), is being emptied at a constant rate.

For example, in one second of a 56 Kbps stream, the encoder creates samples totaling 59 Kb. So, 56 Kb of data is removed from the buffer in that second, leaving 3 Kb in the buffer. If the stream has a buffer window of three seconds, and thus a total buffer size of 168 Kb, it would take almost 40 seconds to fill the buffer. The average bit rate for the stream (if its duration is less than the time it takes to fill the buffer) is 59 Kbps, even though the bit rate is set to 56 Kbps.

The same phenomenon applies to peak bit rate constraints. For short content, the average bit rate computed by the codec object after encoding is completed can be greater than the peak bit rate.

## Related topics

<dl> <dt>

[Frequently Asked Questions](frequentlyaskedquestions.md)
</dt> </dl>

 

 



