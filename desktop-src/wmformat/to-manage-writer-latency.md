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
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# To Manage Writer Latency

\[The feature associated with this page, [Windows Media Format 11 SDK](/windows/win32/wmformat/windows-media-format-11-sdk), is a legacy feature. It has been superseded by [Source Reader](/windows/win32/medfound/source-reader) and [Sink Writer](/windows/win32/medfound/sink-writer). **Source Reader** and **Sink Writer** have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **Source Reader** and **Sink Writer** instead of **Windows Media Format 11 SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

It takes time for the writer to process samples. The amount of time between passing an input sample and the writing of an output sample is called the latency of the writer. A number of factors contribute to writer latency, and you can reduce it in several ways.

The most obvious factor involved in writer latency is the time it takes to compress a sample. Under most circumstances, you will have little or no control over this. If bandwidth is not a big concern, you can reduce latency by using less compression. Of course, you can achieve the least latency by passing samples that are already compressed.

The next factor, and one over which you usually do have control, is the order in which samples are passed to the reader. You can achieve better latency by passing samples in order of presentation time, and by ensuring that the input samples are well synchronized between all input streams. The greater the discrepancy in presentation times between the samples for different streams, the more latency will result. You can set a maximum for the discrepancy between input samples by calling [**IWMWriterAdvanced::SetSyncTolerance**](/previous-versions/windows/desktop/api/Wmsdkidl/nf-wmsdkidl-iwmwriteradvanced-setsynctolerance).

## Related topics

<dl> <dt>

[**Writing ASF Files**](writing-asf-files.md)
</dt> </dl>

 

 




