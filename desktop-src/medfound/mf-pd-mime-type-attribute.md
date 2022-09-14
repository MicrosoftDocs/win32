---
description: Specifies the MIME type of the content.
ms.assetid: bbcfb3e6-a86a-4621-b8d9-92ace60e8c10
title: MF_PD_MIME_TYPE attribute (Mfidl.h)
ms.topic: reference
ms.date: 05/31/2018
---

# MF\_PD\_MIME\_TYPE attribute

Specifies the MIME type of the content.

## Data type

Wide-character string

## Remarks

This attribute applies to presentation descriptors.

The MIME type exposed through [System.MIMEType](../properties/props-system-mimetype.md) for media files may have a bias towards choosing MIME types suitable for Digital Living Network Alliance (DLNA).

MF\_PD\_MIME\_TYPE and [System.MIMEType](../properties/props-system-mimetype.md) may not always match.

The GUID constant for this attribute is exported from mfuuid.lib.

## Requirements



| Requirement | Value |
|-------------------------------------|------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps \| UWP apps\]<br/>                              |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps \| UWP apps\]<br/>                        |
| Header<br/>                   | <dl> <dt>Mfidl.h</dt> </dl> |



## See also

<dl> <dt>

[Alphabetical List of Media Foundation Attributes](alphabetical-list-of-media-foundation-attributes.md)
</dt> <dt>

[**IMFAttributes::GetString**](/windows/desktop/api/mfobjects/nf-mfobjects-imfattributes-getstring)
</dt> <dt>

[**IMFAttributes::SetString**](/windows/desktop/api/mfobjects/nf-mfobjects-imfattributes-setstring)
</dt> <dt>

[**IMFPresentationDescriptor**](/windows/desktop/api/mfidl/nn-mfidl-imfpresentationdescriptor)
</dt> <dt>

[Presentation Descriptor Attributes](presentation-descriptor-attributes.md)
</dt> </dl>

 

 
