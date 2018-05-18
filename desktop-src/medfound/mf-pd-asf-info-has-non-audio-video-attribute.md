---
Description: 'Specifies whether an Advanced Systems Format (ASF) file contains any streams that are not audio or video.'
ms.assetid: 'ccd61f50-29fb-4a50-80c9-d23d71d768f3'
title: 'MF\_PD\_ASF\_INFO\_HAS\_NON\_AUDIO\_VIDEO attribute'
---

# MF\_PD\_ASF\_INFO\_HAS\_NON\_AUDIO\_VIDEO attribute

Specifies whether an Advanced Systems Format (ASF) file contains any streams that are not audio or video.

## Data type

**UINT32**

Treat as a Boolean value.

## Remarks

This attribute applies to presentation descriptors for ASF content. If the value is **TRUE**, the file has at least one stream that is not audio or video. Examples include image streams, script commands, and custom arbitrary data.

The [**IMFASFContentInfo::GeneratePresentationDescriptor**](imfasfcontentinfo-generatepresentationdescriptor.md) method generates this attribute from the ASF metadata.

## Requirements



|                                     |                                                                                          |
|-------------------------------------|------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                           |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/>                                     |
| Header<br/>                   | <dl> <dt>Wmcontainer.h</dt> </dl> |



## See also

<dl> <dt>

[Alphabetical List of Media Foundation Attributes](alphabetical-list-of-media-foundation-attributes.md)
</dt> <dt>

[**IMFAttributes::GetUINT32**](imfattributes-getuint32.md)
</dt> <dt>

[**IMFAttributes::SetUINT32**](imfattributes-setuint32.md)
</dt> <dt>

[**IMFPresentationDescriptor**](imfpresentationdescriptor.md)
</dt> <dt>

[Presentation Descriptor Attributes](presentation-descriptor-attributes.md)
</dt> <dt>

[ASF Header Object](asf-file-structure.md#header-object)
</dt> </dl>

 

 




