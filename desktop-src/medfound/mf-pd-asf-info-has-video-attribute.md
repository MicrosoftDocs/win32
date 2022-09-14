---
description: Specifies whether an Advanced Systems Format (ASF) file contains at least one video stream.
ms.assetid: 98411c75-519f-4ace-999f-1ea22457ed4a
title: MF_PD_ASF_INFO_HAS_VIDEO attribute (Wmcontainer.h)
ms.topic: reference
ms.date: 05/31/2018
---

# MF\_PD\_ASF\_INFO\_HAS\_VIDEO attribute

Specifies whether an Advanced Systems Format (ASF) file contains at least one video stream.

## Data type

**UINT32**

Treat as a Boolean value.

## Remarks

This attribute applies to presentation descriptors for ASF content. If the value is **TRUE**, the file has at least one video stream. Otherwise, the file does not contain any video streams.

The [**IMFASFContentInfo::GeneratePresentationDescriptor**](/windows/desktop/api/wmcontainer/nf-wmcontainer-imfasfcontentinfo-generatepresentationdescriptor) method generates this attribute from the ASF metadata.

## Requirements



| Requirement | Value |
|-------------------------------------|------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                           |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/>                                     |
| Header<br/>                   | <dl> <dt>Wmcontainer.h</dt> </dl> |



## See also

<dl> <dt>

[Alphabetical List of Media Foundation Attributes](alphabetical-list-of-media-foundation-attributes.md)
</dt> <dt>

[**IMFAttributes::GetUINT32**](/windows/desktop/api/mfobjects/nf-mfobjects-imfattributes-getuint32)
</dt> <dt>

[**IMFAttributes::SetUINT32**](/windows/desktop/api/mfobjects/nf-mfobjects-imfattributes-setuint32)
</dt> <dt>

[**IMFPresentationDescriptor**](/windows/desktop/api/mfidl/nn-mfidl-imfpresentationdescriptor)
</dt> <dt>

[Presentation Descriptor Attributes](presentation-descriptor-attributes.md)
</dt> <dt>

[ASF Header Object](asf-file-structure.md)
</dt> </dl>

 

 




