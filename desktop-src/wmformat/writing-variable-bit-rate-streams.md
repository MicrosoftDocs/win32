---
title: Writing Variable Bit Rate Streams
description: Writing Variable Bit Rate Streams
ms.assetid: 9eccde59-8342-44ad-90e6-032db022d7c5
keywords:
- Advanced Systems Format (ASF),writing VBR streams
- ASF (Advanced Systems Format),writing VBR streams
- variable bit rate (VBR),writing streams
- VBR (variable bit rate),writing streams
- streams,writing VBR
ms.topic: article
ms.date: 05/31/2018
---

# Writing Variable Bit Rate Streams

Variable bit rate (VBR) streams are written the same way as constant bit rate (CBR) streams. The only difference is in the processing performed internally by the writer and the codecs. However, bit rate based VBR (both constrained and unconstrained) requires a preprocessing pass in the writer.

You should check the return value for the first call you make to [**IWMWriter::WriteSample**](/previous-versions/windows/desktop/api/Wmsdkidl/nf-wmsdkidl-iwmwriter-writesample) for each stream. If the error code returned is NS\_E\_INVALID\_NUM\_PASSES, the stream requires a preprocessing pass.

## Related topics

<dl> <dt>

[**Using Two-Pass Encoding**](using-two-pass-encoding.md)
</dt> <dt>

[**Writing ASF Files**](writing-asf-files.md)
</dt> </dl>

 

 




