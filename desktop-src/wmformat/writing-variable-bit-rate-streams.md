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
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# Writing Variable Bit Rate Streams

\[The feature associated with this page, [Windows Media Format 11 SDK](/windows/win32/wmformat/windows-media-format-11-sdk), is a legacy feature. It has been superseded by [Source Reader](/windows/win32/medfound/source-reader) and [Sink Writer](/windows/win32/medfound/sink-writer). **Source Reader** and **Sink Writer** have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **Source Reader** and **Sink Writer** instead of **Windows Media Format 11 SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

Variable bit rate (VBR) streams are written the same way as constant bit rate (CBR) streams. The only difference is in the processing performed internally by the writer and the codecs. However, bit rate based VBR (both constrained and unconstrained) requires a preprocessing pass in the writer.

You should check the return value for the first call you make to [**IWMWriter::WriteSample**](/previous-versions/windows/desktop/api/Wmsdkidl/nf-wmsdkidl-iwmwriter-writesample) for each stream. If the error code returned is NS\_E\_INVALID\_NUM\_PASSES, the stream requires a preprocessing pass.

## Related topics

<dl> <dt>

[**Using Two-Pass Encoding**](using-two-pass-encoding.md)
</dt> <dt>

[**Writing ASF Files**](writing-asf-files.md)
</dt> </dl>

 

 




