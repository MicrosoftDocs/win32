---
title: Constant Bit Rate (CBR) Encoding
description: Constant Bit Rate (CBR) Encoding
ms.assetid: f87277a5-55f1-46c7-a6a4-5824f3904d60
keywords:
- Windows Media Format SDK,CBR encoding
- Windows Media Format SDK,constant bit rate (CBR)
- codecs,CBR encoding
- codecs,constant bit rate (CBR)
- constant bit rate (CBR)
- CBR (constant bit rate)
ms.topic: article
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# Constant Bit Rate (CBR) Encoding

\[The feature associated with this page, [Windows Media Format 11 SDK](/windows/win32/wmformat/windows-media-format-11-sdk), is a legacy feature. It has been superseded by [Source Reader](/windows/win32/medfound/source-reader) and [Sink Writer](/windows/win32/medfound/sink-writer). **Source Reader** and **Sink Writer** have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **Source Reader** and **Sink Writer** instead of **Windows Media Format 11 SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

Constant bit rate (CBR) encoding is the default method of encoding with the Windows Media Format SDK. When using CBR encoding, you specify the target bit rate for a stream, and the codec uses whatever amount of compression is necessary to achieve it.

With CBR encoding the bit rate and size of the encoded stream are known prior to encoding. For example, if you are encoding a three minute song at 32,000 bits per second, you know that the file size will be about 704 kilobytes (32,000 bps x 180 seconds / 8 bits per byte / 1,024). You also know that the bandwidth required to stream the encoded content is about 32,000 bits per second.

Constrained variable bit rate encoding (described in the following section) also enables you to know the bit rate prior to encoding, but since the rate is variable, the resulting file cannot be streamed as efficiently as a file encoded in CBR mode. With CBR, the bit rate over time always remains close to the average or target bit rate, and the amount of variation can be specified.

The disadvantage of CBR encoding is that the quality of the encoded content will not be constant. Because some content is more difficult to compress, parts of a CBR stream will be of lower quality than others. For example, a typical movie has some scenes that are fairly static and some scenes that are full of action. If you encode a movie using CBR, the scenes that are static, and therefore easy to encode efficiently, will be of higher quality than the action scenes, which are much more difficult to encode efficiently.

CBR encoding can also result in inconsistent quality from one file to another. If you use CBR to encode several songs of different genres at the same bit rate, you may notice some difference in quality between them.

In general, variations in the quality of a CBR file are more pronounced at lower bit rates. At higher bit rates, the quality of a CBR-encoded file will still vary, but the quality issues will be less noticeable to the user. When using CBR encoding, you should set the bandwidth as high as your delivery scenario allows.

## Related topics

<dl> <dt>

[**Choosing an Encoding Method**](choosing-an-encoding-method.md)
</dt> <dt>

[**Codec Features**](codec-features.md)
</dt> <dt>

[**Variable Bit Rate (VBR) Encoding**](variable-bit-rate--vbr--encoding.md)
</dt> </dl>

 

 




