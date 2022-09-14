---
title: To Manage Writer Latency
description: To Manage Writer Latency
ms.assetid: 62ec3f25-5cd9-499e-9579-00e00086df7f
keywords:
- Advanced Systems Format (ASF),managing writer latency
- ASF (Advanced Systems Format),managing writer latency
- Advanced Systems Format (ASF),writer latency
- ASF (Advanced Systems Format),writer latency
- writer latency
- latency
ms.topic: article
ms.date: 05/31/2018
---

# To Manage Writer Latency

It takes time for the writer to process samples. The amount of time between passing an input sample and the writing of an output sample is called the latency of the writer. A number of factors contribute to writer latency, and you can reduce it in several ways.

The most obvious factor involved in writer latency is the time it takes to compress a sample. Under most circumstances, you will have little or no control over this. If bandwidth is not a big concern, you can reduce latency by using less compression. Of course, you can achieve the least latency by passing samples that are already compressed.

The next factor, and one over which you usually do have control, is the order in which samples are passed to the reader. You can achieve better latency by passing samples in order of presentation time, and by ensuring that the input samples are well synchronized between all input streams. The greater the discrepancy in presentation times between the samples for different streams, the more latency will result. You can set a maximum for the discrepancy between input samples by calling [**IWMWriterAdvanced::SetSyncTolerance**](/previous-versions/windows/desktop/api/Wmsdkidl/nf-wmsdkidl-iwmwriteradvanced-setsynctolerance).

## Related topics

<dl> <dt>

[**Writing ASF Files**](writing-asf-files.md)
</dt> </dl>

 

 




