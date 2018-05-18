---
Description: 'Specifies the maximum packet size, in bytes, of an Advanced Systems Format (ASF) file.'
ms.assetid: '8dcae150-2363-47ba-b0d3-0bc182574d81'
title: 'MF\_PD\_ASF\_FILEPROPERTIES\_MAX\_PACKET\_SIZE attribute'
---

# MF\_PD\_ASF\_FILEPROPERTIES\_MAX\_PACKET\_SIZE attribute

Specifies the maximum packet size, in bytes, of an Advanced Systems Format (ASF) file.

## Data type

**UINT32**

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

[**IMFAttributes::GetUINT32**](imfattributes-getuint32.md)
</dt> <dt>

[**IMFAttributes::SetUINT32**](imfattributes-setuint32.md)
</dt> <dt>

[**IMFPresentationDescriptor**](imfpresentationdescriptor.md)
</dt> <dt>

[Presentation Descriptor Attributes](presentation-descriptor-attributes.md)
</dt> <dt>

[ASF Header Object](asf-file-structure.md#header-object)
</dt> <dt>

[Presentation Descriptors](presentation-descriptors.md)
</dt> </dl>

 

 




