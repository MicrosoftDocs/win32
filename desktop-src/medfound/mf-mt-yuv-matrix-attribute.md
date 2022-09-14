---
description: For YUV media types, defines the conversion matrix from the YCbCr color space to the RGB color space.
ms.assetid: b268d16d-b4cc-4026-9ba7-805cc5409b95
title: MF_MT_YUV_MATRIX attribute (Mfapi.h)
ms.topic: reference
ms.date: 05/31/2018
---

# MF\_MT\_YUV\_MATRIX attribute

For YUV media types, defines the conversion matrix from the Y'Cb'Cr' color space to the R'G'B' color space.

## Data type

**UINT32**

## Remarks

The value of this attribute is a member of the [**MFVideoTransferMatrix**](/windows/desktop/api/mfobjects/ne-mfobjects-mfvideotransfermatrix) enumeration.

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

 

 




