---
title: Presentation Time
description: Presentation Time
ms.assetid: 856e1783-85b4-4195-970f-3d7b5612672b
keywords:
- Windows Media Format SDK,presentation times
- Advanced Systems Format (ASF),presentation times
- ASF (Advanced Systems Format),presentation times
- presentation times
ms.topic: article
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# Presentation Time

\[The feature associated with this page, [Windows Media Format 11 SDK](/windows/win32/wmformat/windows-media-format-11-sdk), is a legacy feature. It has been superseded by [Source Reader](/windows/win32/medfound/source-reader) and [Sink Writer](/windows/win32/medfound/sink-writer). **Source Reader** and **Sink Writer** have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **Source Reader** and **Sink Writer** instead of **Windows Media Format 11 SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

A presentation time is a measurement of time from the first sample of the first stream in an ASF file. This measurement, as well as most other measurements of time used by the objects of this SDK, is in 100-nanosecond units. Presentation times are important because they enable the various streams in a file to be synchronized. You must supply a presentation time for each input sample you pass to the writer. Every data object in the data section of an ASF file has a presentation time associated with it. Every output sample retrieved by the reader also has a presentation time.

## Related topics

<dl> <dt>

[**Concepts**](concepts.md)
</dt> <dt>

[**Inputs, Streams and Outputs**](inputs-streams-and-outputs.md)
</dt> <dt>

[**Media Samples**](media-samples.md)
</dt> </dl>

 

 




