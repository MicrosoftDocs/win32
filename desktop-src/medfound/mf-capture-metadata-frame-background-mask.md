---
description: Reports the metadata and mask buffer for a background segmentation mask that distinguishes between the background and foreground of a video frame.
title: MF_CAPTURE_METADATA_FRAME_BACKGROUND_MASK attribute (Mfapi.h)
ms.topic: reference
ms.date: 06/01/2021
---

# MF\_CAPTURE\_METADATA\_FRAME\_BACKGROUND\_MASK attribute

Reports the metadata and mask buffer for a background segmentation mask that distinguishes between the background and foreground of a video frame.

## Data type

**BLOB**

## Remarks

The data carried by this attribute is a [KSCAMERA_METADATA_BACKGROUNDSEGMENTATIONMASK](/windows-hardware/drivers/ddi/ksmedia/ns-ksmedia-tagkscamera_metadata_backgroundsegmentationmask) structure that contains information about the dimensions of the background mask as well as its coverage of the frame it is inferred from, which is the frame that is outputted by the stream. It also carries a contiguous buffer representing the mask to be leveraged by the consuming app to define which pixels are considered part of the foreground or background. The scaling and image coordinate correlation of the mask regarding the frame is handled by the consuming app. 

## Requirements



| Requirement | Value |
|-------------------------------------|------------------------------------------------------------------------------------|
| Minimum supported client<br/> | TBD release cobalt<br/>                          |
| Minimum supported server<br/> | TBD release cobalt<br/>                      |
| Header<br/>                   | <dl> <dt>Mfapi.h</dt> </dl> |



## See also

<dl> <dt>

[Alphabetical List of Media Foundation Attributes](alphabetical-list-of-media-foundation-attributes.md)
</dt> <dt>

[**IMFAttributes::GetBlob**](/windows/desktop/api/mfobjects/nf-mfobjects-imfattributes-getblob)
</dt> <dt>

[**IMFAttributes::SetBlob**](/windows/desktop/api/mfobjects/nf-mfobjects-imfattributes-setblob)
</dt> <dt>

[**IMFMediaType**](/windows/desktop/api/mfobjects/nn-mfobjects-imfmediatype)
</dt> <dt>

[Media Type Attributes](media-type-attributes.md)
</dt> </dl>

 




