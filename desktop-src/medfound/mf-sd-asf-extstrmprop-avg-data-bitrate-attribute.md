---
Description: 'Specifies the average data bit rate, in bits per second, of a stream in an Advanced Systems Format (ASF) file.'
ms.assetid: '3a0b39ab-e9a9-49df-a321-a88559aec16f'
title: 'MF\_SD\_ASF\_EXTSTRMPROP\_AVG\_DATA\_BITRATE attribute'
---

# MF\_SD\_ASF\_EXTSTRMPROP\_AVG\_DATA\_BITRATE attribute

Specifies the average data bit rate, in bits per second, of a stream in an Advanced Systems Format (ASF) file.

## Data type

**UINT32**

## Remarks

This attribute applies to stream descriptors for ASF content. It corresponds to the Data Bit Rate field in the Extended Stream Properties object, and defines the leak rate used in the "leaky bucket" model. For more information, refer to the ASF specification.

The [**IMFASFContentInfo::GeneratePresentationDescriptor**](imfasfcontentinfo-generatepresentationdescriptor.md) method generates this attribute from the ASF metadata. The application can create the stream descriptor for the stream from the presentation descriptor by calling [**IMFPresentationDescriptor::GetStreamDescriptorByIndex**](imfpresentationdescriptor-getstreamdescriptorbyindex.md).

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

[**IMFStreamDescriptor**](imfstreamdescriptor.md)
</dt> <dt>

[Stream Descriptor Attributes](stream-descriptor-attributes.md)
</dt> <dt>

[ASF Header Object](asf-file-structure.md#header-object)
</dt> </dl>

 

 




