---
description: Specifies whether an Advanced Systems Format (ASF) file contains any streams that are not audio or video.
ms.assetid: ccd61f50-29fb-4a50-80c9-d23d71d768f3
title: MF_PD_ASF_INFO_HAS_NON_AUDIO_VIDEO attribute (Wmcontainer.h)
ms.topic: reference
ms.date: 05/31/2018
---

# MF\_PD\_ASF\_INFO\_HAS\_NON\_AUDIO\_VIDEO attribute

Specifies whether an Advanced Systems Format (ASF) file contains any streams that are not audio or video.

## Data type

**UINT32**

Treat as a Boolean value.

## Remarks

This attribute applies to presentation descriptors for ASF content. If the value is **TRUE**, the file has at least one stream that is not audio or video. Examples include image streams, script commands, and custom arbitrary data.

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

 

 




