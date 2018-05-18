---
Description: 'Contains encryption data for an Advanced Systems Format (ASF) file. This attribute corresponds to the Extended Content Encryption Object in the ASF header, defined in the ASF specification.'
ms.assetid: '8bf5e7a4-073f-4b2c-8e9c-49f6f11c9093'
title: 'MF\_PD\_ASF\_CONTENTENCRYPTIONEX\_ENCRYPTION\_DATA attribute'
---

# MF\_PD\_ASF\_CONTENTENCRYPTIONEX\_ENCRYPTION\_DATA attribute

Contains encryption data for an Advanced Systems Format (ASF) file. This attribute corresponds to the Extended Content Encryption Object in the ASF header, defined in the ASF specification.

## Data type

Byte array

## Remarks

This attribute applies to presentation descriptors for ASF content.

The [**IMFASFContentInfo::GeneratePresentationDescriptor**](imfasfcontentinfo-generatepresentationdescriptor.md) method creates the presentation descriptor and generates this attribute from the Extended Content Encryption Object header. The size of the blob equals the Data Size field. The byte array contained in the blob equals the Data field in the Extended Content Encryption object of the ASF header.

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

[**IMFAttributes::GetBlob**](imfattributes-getblob.md)
</dt> <dt>

[**IMFAttributes::SetBlob**](imfattributes-setblob.md)
</dt> <dt>

[**IMFPresentationDescriptor**](imfpresentationdescriptor.md)
</dt> <dt>

[Presentation Descriptor Attributes](presentation-descriptor-attributes.md)
</dt> <dt>

[ASF Header Object](asf-file-structure.md#header-object)
</dt> <dt>

[Presentation Descriptors](presentation-descriptors.md)
</dt> </dl>

 

 




