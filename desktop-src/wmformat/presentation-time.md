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
ms.date: 05/31/2018
---

# Presentation Time

A presentation time is a measurement of time from the first sample of the first stream in an ASF file. This measurement, as well as most other measurements of time used by the objects of this SDK, is in 100-nanosecond units. Presentation times are important because they enable the various streams in a file to be synchronized. You must supply a presentation time for each input sample you pass to the writer. Every data object in the data section of an ASF file has a presentation time associated with it. Every output sample retrieved by the reader also has a presentation time.

## Related topics

<dl> <dt>

[**Concepts**](concepts.md)
</dt> <dt>

[**Inputs, Streams and Outputs**](inputs-streams-and-outputs.md)
</dt> <dt>

[**Media Samples**](media-samples.md)
</dt> </dl>

 

 




