---
description: Allows the Enhanced Video Renderer (EVR) to improve performance by using bob deinterlacing.
ms.assetid: e145e862-b987-4962-a94b-f8370bbcd5ac
title: EVRConfig_AllowDropToBob attribute (Uuids.h)
ms.topic: reference
ms.date: 05/31/2018
---

# EVRConfig\_AllowDropToBob attribute

Allows the Enhanced Video Renderer (EVR) to improve performance by using bob deinterlacing.

## Data type

**UINT32**

## Get/set

To get this attribute, call [**IMFAttributes::GetUINT32**](/windows/desktop/api/mfobjects/nf-mfobjects-imfattributes-getuint32).

To set this attribute, call [**IMFAttributes::SetUINT32**](/windows/desktop/api/mfobjects/nf-mfobjects-imfattributes-setuint32).

## Remarks

This attribute can be set on the EVRmedia sink. To set the attribute, **QueryInterface** to query the EVR media sink for the [**IMFAttributes**](/windows/desktop/api/mfobjects/nn-mfobjects-imfattributes) interface.

Setting this attribute has the same effect as setting the **MFVideoMixPrefs\_AllowDropToBob** flag on the EVR. See [**MFVideoMixPrefs**](/windows/desktop/api/evr/ne-evr-mfvideomixprefs) for a description of this flag.

The GUID constant for this attribute is exported from strmiids.lib.

## Requirements



| Requirement | Value |
|-------------------------------------|------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 7 \[desktop apps only\]<br/>                                         |
| Minimum supported server<br/> | Windows Server 2008 R2 \[desktop apps only\]<br/>                            |
| Header<br/>                   | <dl> <dt>Uuids.h</dt> </dl> |



## See also

<dl> <dt>

[Alphabetical List of Media Foundation Attributes](alphabetical-list-of-media-foundation-attributes.md)
</dt> <dt>

[EVR Attributes](enhanced-video-renderer-attributes.md)
</dt> <dt>

[Video Quality Management](video-quality-management.md)
</dt> </dl>

 

 




