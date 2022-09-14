---
title: Choosing an Encoding Method
description: Choosing an Encoding Method
ms.assetid: 095245a6-39eb-4228-86ac-ade94dde3695
keywords:
- profiles,choosing encoding methods
- profiles,encoding methods
- codecs,choosing encoding methods
- codecs,encoding methods
- profiles,selecting encoding methods
- codecs,selecting encoding methods
ms.topic: article
ms.date: 05/31/2018
---

# Choosing an Encoding Method

Some codecs, like the Windows Media Video 9 codec, support multiple encoding methods. The encoding method that you choose for a stream will depend upon how the stream is to be delivered. The following table describes when to use the various encoding methods.



| Encoding method                | Description                                                                                                                                                                                       |
|--------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 1-pass Constant Bit Rate (CBR) | The only option for live streaming. Encodes to a predictable bit rate and delivers the lowest quality of all encoding methods.                                                                    |
| 2-pass CBR                     | Use for files that will be streamed over a network to a client reader, but that are not broadcast from a live source. Encodes to a predictable bit rate, but with better quality than 1-pass CBR. |
| 1-pass Variable Bit Rate (VBR) | Use when you need to specify the quality of the encoded output. Delivers the most consistent quality of all encoding methods. Use only for local files or for downloading.                        |
| 2-pass VBR – unconstrained     | Use when you need to specify a bandwidth, but fluctuations around the specified bandwidth are acceptable. For local files or downloading only.                                                    |
| 2-pass VBR – constrained       | Use under the same circumstances as unconstrained, but when you need to specify a maximum momentary bit rate. For local files or downloading only.                                                |



 

The following table lists the encoding methods that are supported by the codecs that ship with the Windows Media Format SDK.



| Codec                                  | CBR | 2-pass CBR | VBR | 2-pass VBR |
|----------------------------------------|-----|------------|-----|------------|
| Windows Media Video 9                  | X   | X          | X   | X          |
| Windows Media Audio 9 and later        | X   | X          | X   | X          |
| Windows Media Video 9 Screen           | X   |            | X   |            |
| Windows Media Audio 9 Voice            | X   |            |     |            |
| Windows Media Audio Professional       | X   | X          | X   | X          |
| Windows Media Audio Lossless           |     |            | X   |            |
| Windows Media Video 9 Image and later  | X   |            | X   |            |
| Windows Media Video 9 Advanced Profile | X   | X          | X   | X          |



 

## Related topics

<dl> <dt>

[**Designing Profiles**](designing-profiles.md)
</dt> <dt>

[**Constant Bit Rate (CBR) Encoding**](constant-bit-rate--cbr--encoding.md)
</dt> <dt>

[**Two-Pass Encoding**](two-pass-encoding.md)
</dt> <dt>

[**Variable Bit Rate (VBR) Encoding**](variable-bit-rate--vbr--encoding.md)
</dt> </dl>

 

 




