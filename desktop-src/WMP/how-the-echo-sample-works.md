---
title: How the Echo Sample Works
description: How the Echo Sample Works
ms.assetid: 554afc08-6e4f-427c-8a09-0d1ebf3ca8dc
keywords:
- Windows Media Player plug-ins,Echo sample overview
- plug-ins,Echo sample overview
- digital signal processing plug-ins,Echo sample overview
- DSP plug-ins,Echo sample overview
- Echo DSP plug-in sample,about
ms.topic: article
ms.date: 05/31/2018
---

# How the Echo Sample Works

The code creates the echo effect by allocating a buffer large enough to contain exactly the amount of audio data that can be rendered in the time frame specified by the delay time value. The size of the buffer is calculated, in bytes, by the following formula:

buffer size = delay time \* sample rate / 1000 \* block alignment

The delay time is in milliseconds. The sample rate and block alignment values are given in a WAVEFORMATEX structure. The sample rate is in samples per second; dividing by 1000 yields samples per millisecond. The block alignment is equal to the product of the number of channels (1 for mono, 2 for stereo) and the number of bits per sample (8 or 16) divided by 8 (bits per byte).

In addition to the pointer variable that points to the head of the delay buffer, the code creates a movable pointer that steps through the data in the buffer in synchronization with the processing loop in the **DoProcessOutput** function. When the movable pointer reaches the end of the delay buffer, it moves back to the head of the buffer. A buffer used in this manner is called a circular buffer.

Once the delay buffer exists, and Windows Media Player has allocated an input buffer to supply audio data and an output buffer to receive processed audio data, the echo processing proceeds like this:

1.  Enter a loop that allows processing of each audio sample in the input buffer.
2.  Retrieve a sample from the input buffer. Then, move the input buffer pointer forward to the next sample to prepare for the next loop iteration.
3.  Retrieve a sample from the delay buffer.
4.  Copy the sample from the input buffer to the same location in the delay buffer from which the last delay sample was retrieved.
5.  Move the delay buffer pointer forward to the next sample. If the pointer moves past the end of the buffer, move it to the head of the buffer.
6.  Combine the sample from the input buffer with the sample from the delay buffer.
7.  Copy the result to the output buffer. Then, move the output buffer pointer forward to the next unit to prepare for the next loop iteration.
8.  Repeat until all the samples are processed.

When an input sample retrieved in step 2 is copied to the delay buffer in step 4, it remains there until the movable pointer steps through each sample in the delay buffer and finally returns to the same position. Because the size of the delay buffer is designed to correspond to the delay time, the elapsed time between the sample being copied to the delay buffer and the sample being retrieved once again equals the specified delay (plus any latency introduced by the actual processing).

When a stream starts, no delay data is generated until the delay time has elapsed. Therefore, it is important that the delay buffer initially contains silence. If the delay buffer contains random data, the user will hear white noise until the plug-in generates enough delay data to overwrite the entire delay buffer.

## Related topics

<dl> <dt>

[**Echo Sample Overview**](echo-sample-overview.md)
</dt> </dl>

 

 




