---
description: Specifies the final output resolution of the decoded image, after video processing.
ms.assetid: 067867D8-155C-4406-BE07-720016B2AEBC
title: MFT_DECODER_FINAL_VIDEO_RESOLUTION_HINT attribute (Mftransform.h)
ms.topic: reference
ms.date: 05/31/2018
---

# MFT\_DECODER\_FINAL\_VIDEO\_RESOLUTION\_HINT attribute

Specifies the final output resolution of the decoded image, after video processing.

## Data type

**UINT64**

## Remarks

This attribute is supported by some video decoders. An application can set this attribute to indicate the width and height of the image after video processing. The decoder can use this information to optimize the decoding process, especially if the final image size is much smaller than the native image size. For example, the decoder might skip an out-of-loop filter.

The upper 32 bits contain the width and the lower 32 bits contain the height.

To set this attribute:

1.  Call [**IMFTransform::GetAttributes**](/windows/desktop/api/mftransform/nf-mftransform-imftransform-getattributes) on the decoder to get an [**IMFAttributes**](/windows/desktop/api/mfobjects/nn-mfobjects-imfattributes) pointer.
2.  Call [**MFSetAttributeSize**](/windows/desktop/api/mfapi/nf-mfapi-mfsetattributesize) to add the attribute.

## Requirements



| Requirement | Value |
|-------------------------------------|------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 8 \[desktop apps \| UWP apps\]<br/>                                        |
| Minimum supported server<br/> | None supported<br/>                                                                |
| Header<br/>                   | <dl> <dt>Mftransform.h</dt> </dl> |



## See also

<dl> <dt>

[Alphabetical List of Media Foundation Attributes](alphabetical-list-of-media-foundation-attributes.md)
</dt> <dt>

[Transform Attributes](transform-attributes.md)
</dt> </dl>

 

 




