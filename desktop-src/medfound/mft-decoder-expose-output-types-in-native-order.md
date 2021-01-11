---
description: Specifies whether a decoder exposes IYUV/I420 output types (suitable for transcoding) before other formats.
ms.assetid: 8505CFA1-210A-4DA8-B92A-FCE62F0310E5
title: MFT_DECODER_EXPOSE_OUTPUT_TYPES_IN_NATIVE_ORDER attribute (Mftransform.h)
ms.topic: reference
ms.date: 05/31/2018
---

# MFT\_DECODER\_EXPOSE\_OUTPUT\_TYPES\_IN\_NATIVE\_ORDER attribute

Specifies whether a decoder exposes IYUV/I420 output types (suitable for transcoding) before other formats.

## Data type

**UINT32**

## Remarks

This attribute is a hint for the decoder to arrange its list of output types in a particular order, depending on the intended use, either playback or transcode.

For most encoding formats (H.264, MPEG-2, WMV), the video decoders in Microsoft Media Foundation support several common YUV outputs, including NV12, YV12, YUY2, IYUV, and I420. The decoder offers an ordered list of output types through its [**IMFTransform::GetOutputAvailableType**](/windows/desktop/api/mftransform/nf-mftransform-imftransform-getoutputavailabletype) method.

For playback, NV12 is the most efficient and widely supported format. Therefore, by default, decoders typically offer NV12 as the first output type in the list. This minimizes the time needed to resolve the media type when building a playback topology. For transcoding, however, IYUV or I420 are more efficient for the CPU and are typically preferred by encoders.

If a decoder supports this attribute, the attribute has the following behavior:

-   If the attribute has a non-zero value, IYUV and I420 appear first in the list of output media types. This setting is most efficient for transcoding.
-   If the attribute is zero, NV12 appears first in the list of output media types. This setting is most efficient for playback, and is the default.

To set this attribute:

1.  Call [**IMFTransform::GetAttributes**](/windows/desktop/api/mftransform/nf-mftransform-imftransform-getattributes) on the decoder to get an [**IMFAttributes**](/windows/desktop/api/mfobjects/nn-mfobjects-imfattributes) pointer.
2.  Call [**IMFAttributes::SetUINT32**](/windows/desktop/api/mfobjects/nf-mfobjects-imfattributes-setuint32) to add the attribute.

## Requirements



| Requirement | Value |
|-------------------------------------|------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 8 \[desktop apps \| UWP apps\]<br/>                                        |
| Minimum supported server<br/> | None supported<br/>                                                                |
| Header<br/>                   | <dl> <dt>Mftransform.h</dt> </dl> |



## See also

<dl> <dt>

[Alphabetical List of Media Foundation Attributes](alphabetical-list-of-media-foundation-attributes.md)
</dt> </dl>

 

 




