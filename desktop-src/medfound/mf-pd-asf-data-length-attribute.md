---
Description: 'Specifies the size, in bytes, of the data section of an Advanced Systems Format (ASF) file.'
ms.assetid: '93a0bf27-23db-4e8a-b471-a42122e8f9aa'
title: 'MF\_PD\_ASF\_DATA\_LENGTH attribute'
---

# MF\_PD\_ASF\_DATA\_LENGTH attribute

Specifies the size, in bytes, of the data section of an Advanced Systems Format (ASF) file.

## Data type

**UINT64**

## Remarks

This attribute applies to presentation descriptors for ASF content.

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

[**IMFAttributes::GetUINT64**](imfattributes-getuint64.md)
</dt> <dt>

[**IMFAttributes::SetUINT64**](imfattributes-setuint64.md)
</dt> <dt>

[**IMFPresentationDescriptor**](imfpresentationdescriptor.md)
</dt> <dt>

[Presentation Descriptor Attributes](presentation-descriptor-attributes.md)
</dt> <dt>

[ASF Header Object](asf-file-structure.md#header-object)
</dt> </dl>

 

 




