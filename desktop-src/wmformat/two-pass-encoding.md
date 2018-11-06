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
ms.date: 05/31/2018
---

# Two-Pass Encoding

Two-pass encoding is an encoding method available with some codecs, like the Windows Media Video 9 codec. When you use two-pass encoding, the codec processes all of the samples for the stream twice. On the first pass, the codec gathers information about the content of the stream. On the second pass, the codec uses the information gathered on the first pass to optimize the encoding process for the stream.

In the Constant Bit Rate encoding mode, files that are encoded in two passes are generally more efficient than files encoded in a single pass. Quality-based VBR, which is one pass, produces more consistent quality than bit-rate-based VBR, which is two-pass.

You cannot use two-pass encoding on live streams.

## Related topics

<dl> <dt>

[**Codec Features**](codec-features.md)
</dt> <dt>

[**Using Two-Pass Encoding**](using-two-pass-encoding.md)
</dt> </dl>

 

 




