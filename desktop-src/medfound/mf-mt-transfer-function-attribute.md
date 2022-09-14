---
description: Specifies the conversion function from RGB to RGB for a video media type.
ms.assetid: c64c2135-f588-4d7a-9ca8-ae4f7b290572
title: MF_MT_TRANSFER_FUNCTION attribute (Mfapi.h)
ms.topic: reference
ms.date: 05/31/2018
---

# MF\_MT\_TRANSFER\_FUNCTION attribute

Specifies the conversion function from RGB to R'G'B' for a video media type.

## Data type

**UINT32**

## Remarks

The value of this attribute is a member of the [**MFVideoTransferFunction**](/windows/desktop/api/mfobjects/ne-mfobjects-mfvideotransferfunction) enumeration.

The GUID constant for this attribute is exported from mfuuid.lib.

## Requirements



| Requirement | Value |
|-------------------------------------|------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps \| UWP apps\]<br/>                              |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps \| UWP apps\]<br/>                        |
| Header<br/>                   | <dl> <dt>Mfapi.h</dt> </dl> |



## See also

<dl> <dt>

[Alphabetical List of Media Foundation Attributes](alphabetical-list-of-media-foundation-attributes.md)
</dt> <dt>

[**IMFAttributes::GetUINT32**](/windows/desktop/api/mfobjects/nf-mfobjects-imfattributes-getuint32)
</dt> <dt>

[**IMFAttributes::SetUINT32**](/windows/desktop/api/mfobjects/nf-mfobjects-imfattributes-setuint32)
</dt> <dt>

[**IMFMediaType**](/windows/desktop/api/mfobjects/nn-mfobjects-imfmediatype)
</dt> <dt>

[Media Type Attributes](media-type-attributes.md)
</dt> <dt>

[Extended Color Information](extended-color-information.md)
</dt> </dl>

 

 




