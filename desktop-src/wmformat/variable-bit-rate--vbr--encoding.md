---
title: Variable Bit Rate (VBR) Encoding
description: Variable Bit Rate (VBR) Encoding
ms.assetid: d3fe0cc6-64d7-44ce-8bb4-dd2eed021345
keywords:
- Windows Media Format SDK,VBR encoding
- Windows Media Format SDK,variable bit rate (VBR)
- Windows Media Format SDK,quality-based VBR encoding
- Windows Media Format SDK,unconstrained VBR encoding
- Windows Media Format SDK,constrained VBR encoding
- codecs,VBR encoding
- codecs,variable bit rate (VBR)
- codecs,quality-based VBR encoding
- codecs,unconstrained VBR encoding
- codecs,constrained VBR encoding
- variable bit rate (VBR),about
- VBR (variable bit rate),about
- quality-based VBR encoding,about
- unconstrained VBR encoding,about
- constrained VBR encoding
ms.topic: article
ms.date: 05/31/2018
---

# Variable Bit Rate (VBR) Encoding

Variable bit rate (VBR) encoding is an alternative to constant bit rate encoding (CBR) and is supported by some codecs. Where CBR encoding strives to maintain the bit rate of the encoded media, VBR strives to achieve the best possible quality of the encoded media.

The quality of encoded content is determined by the amount of data that is lost when the content is compressed and decompressed. Many factors affect the loss of data in the compression process, but in general, the more complex the original data and the higher the compression ratio, the more detail is lost in the compression process.

There are three types of VBR encoding: quality-based, unconstrained, and constrained.

## Quality-based VBR Encoding

The first type of VBR encoding is quality-based, which uses one encoding pass. Quality-based VBR encoding enables you to specify a level of quality for a digital media stream instead of a bit rate. The codec will then encode the content so that all samples are of comparable quality.

The main advantage of quality-based VBR encoding is that quality is consistent within a file and from one file to the next. For example, you can write a program to copy songs from CD to ASF files on a computer. In this case, consistent quality is probably more important to the end-user experience than consistent file size. Using quality-based VBR encoding would ensure that all of the songs copied are of the same quality.

The disadvantage of quality-based VBR encoding is that there is really no way to know the size or bandwidth requirements of the encoded media before encoding. This can make quality-based VBR-encoded files inappropriate for circumstances where memory or bandwidth are restricted, such as portable media players, or low-bandwidth Internet connections.

In general, quality-based VBR encoding is well suited for local playback or high bandwidth network connections. In those cases, the consistent quality will provide a better user experience.

## Unconstrained VBR Encoding

Unconstrained VBR encoding uses two encoding passes. When using unconstrained VBR encoding, you specify a bit rate for the stream, as you would with CBR encoding. However, the codec uses this value only as the average bit rate for the stream and encodes so that the quality is as high as possible while maintaining the average. The actual bit rate at any point in the encoded stream can vary greatly from the average value.

You do not set a buffer window for unconstrained VBR encoding as you would for a CBR-encoded stream. Instead, the codec computes the size of the required buffer window based on the requirements of the encoded samples.

The advantage of unconstrained VBR encoding is that the compressed stream has the highest possible quality while staying within a predictable average bandwidth.

## Constrained VBR Encoding

Constrained VBR encoding is identical to unconstrained VBR encoding, except that you specify a maximum bit rate and a maximum buffer window in the profile. The codec then uses the maximum values to determine how to compress the data. If you set the maximum values high enough, constrained VBR encoding will produce the same encoded stream as unconstrained VBR encoding.

## Related topics

<dl> <dt>

[**Choosing an Encoding Method**](choosing-an-encoding-method.md)
</dt> <dt>

[**Codec Features**](codec-features.md)
</dt> <dt>

[**Configuring Streams**](configuring-streams.md)
</dt> <dt>

[**Configuring VBR Streams**](configuring-vbr-streams.md)
</dt> <dt>

[**Constant Bit Rate (CBR) Encoding**](constant-bit-rate--cbr--encoding.md)
</dt> <dt>

[**Two-Pass Encoding**](two-pass-encoding.md)
</dt> <dt>

[**Using Two-Pass Encoding**](using-two-pass-encoding.md)
</dt> </dl>

 

 




