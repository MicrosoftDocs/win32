---
Description: 'Specifies the quantization parameter (QP) that was used to encode a video sample.'
ms.assetid: 'F7C4FEFC-FEE7-4614-BC90-4F9D5D878F49'
title: 'MFSampleExtension\_VideoEncodeQP attribute'
---

# MFSampleExtension\_VideoEncodeQP attribute

Specifies the quantization parameter (QP) that was used to encode a video sample.

## Data type

**UINT64**

## Get/set

To get this attribute, call [**IMFAttributes::GetUINT64**](imfattributes-getuint64.md).

To set this attribute, call [**IMFAttributes::SetUINT64**](imfattributes-setuint64.md).

## Applies to

[**IMFSample**](imfsample.md)

## Remarks

The [**H.264 Video Encoder**](h-264-video-encoder.md) sets this attribute on the output samples that it generates.

## Requirements



|                                     |                                                                                    |
|-------------------------------------|------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 8 \[desktop apps \| UWP apps\]<br/>                                  |
| Minimum supported server<br/> | None supported<br/>                                                          |
| Header<br/>                   | <dl> <dt>Mfapi.h</dt> </dl> |



## See also

<dl> <dt>

[Alphabetical List of Media Foundation Attributes](alphabetical-list-of-media-foundation-attributes.md)
</dt> <dt>

[**H.264 Video Encoder**](h-264-video-encoder.md)
</dt> <dt>

[Sample Attributes](sample-attributes.md)
</dt> <dt>

[Media Samples](media-samples.md)
</dt> </dl>

 

 




