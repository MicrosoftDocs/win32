---
Description: 'Specifies the type of protection mechanism used in an Advanced Systems Format (ASF) file.'
ms.assetid: '91ceb610-6ff4-4133-beab-6debb94eec2c'
title: 'MF\_PD\_ASF\_CONTENTENCRYPTION\_TYPE attribute'
---

# MF\_PD\_ASF\_CONTENTENCRYPTION\_TYPE attribute

Specifies the type of protection mechanism used in an Advanced Systems Format (ASF) file.

## Data type

Wide-character string

## Remarks

This attribute applies to presentation descriptors for ASF content.

The [**IMFASFContentInfo::GeneratePresentationDescriptor**](imfasfcontentinfo-generatepresentationdescriptor.md) method retrieves the Protection Type field, converts it into a wide-character string, and then populates a null-terminated array of **WCHAR**s. If present, the value must be "DRM". The size of the array equals the Protection Type Field Length field of the Content Encryption Header.

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

[**IMFAttributes::GetString**](imfattributes-getstring.md)
</dt> <dt>

[**IMFAttributes::SetString**](imfattributes-setstring.md)
</dt> <dt>

[**IMFPresentationDescriptor**](imfpresentationdescriptor.md)
</dt> <dt>

[Presentation Descriptor Attributes](presentation-descriptor-attributes.md)
</dt> <dt>

[ASF Header Object](asf-file-structure.md#header-object)
</dt> <dt>

[Presentation Descriptors](presentation-descriptors.md)
</dt> </dl>

 

 




