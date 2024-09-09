---
title: Two-Pass Encoding
description: Two-Pass Encoding
ms.assetid: 354cd0a5-9a64-4171-9604-694e60b382ad
keywords:
- Windows Media Format SDK,two-pass encoding
- Windows Media Format SDK,2-pass encoding
- codecs,two-pass encoding
- codecs,2-pass encoding
- two-pass encoding,about
- 2-pass encoding,about
ms.topic: article
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# Two-Pass Encoding

\[The feature associated with this page, [Windows Media Format 11 SDK](/windows/win32/wmformat/windows-media-format-11-sdk), is a legacy feature. It has been superseded by [Source Reader](/windows/win32/medfound/source-reader) and [Sink Writer](/windows/win32/medfound/sink-writer). **Source Reader** and **Sink Writer** have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **Source Reader** and **Sink Writer** instead of **Windows Media Format 11 SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

Two-pass encoding is an encoding method available with some codecs, like the Windows Media Video 9 codec. When you use two-pass encoding, the codec processes all of the samples for the stream twice. On the first pass, the codec gathers information about the content of the stream. On the second pass, the codec uses the information gathered on the first pass to optimize the encoding process for the stream.

In the Constant Bit Rate encoding mode, files that are encoded in two passes are generally more efficient than files encoded in a single pass. Quality-based VBR, which is one pass, produces more consistent quality than bit-rate-based VBR, which is two-pass.

You cannot use two-pass encoding on live streams.

## Related topics

<dl> <dt>

[**Codec Features**](codec-features.md)
</dt> <dt>

[**Using Two-Pass Encoding**](using-two-pass-encoding.md)
</dt> </dl>

 

 




