---
Description: 'Specifies the device conformance template for a stream in an Advanced Systems Format (ASF) file.'
ms.assetid: 'e0bfb393-c8de-47cf-b80a-b0d88722e815'
title: 'MF\_SD\_ASF\_METADATA\_DEVICE\_CONFORMANCE\_TEMPLATE attribute'
---

# MF\_SD\_ASF\_METADATA\_DEVICE\_CONFORMANCE\_TEMPLATE attribute

Specifies the device conformance template for a stream in an Advanced Systems Format (ASF) file.

## Data type

Wide-character string

## Remarks

This attribute applies to stream descriptors for ASF content. For more information about device conformance templates, see the topic "Device Conformance Template Parameters" in the Windows Media Format SDK.

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

[**IMFAttributes::GetString**](imfattributes-getstring.md)
</dt> <dt>

[**IMFAttributes::SetString**](imfattributes-setstring.md)
</dt> <dt>

[**IMFStreamDescriptor**](imfstreamdescriptor.md)
</dt> <dt>

[Stream Descriptor Attributes](stream-descriptor-attributes.md)
</dt> <dt>

[ASF Header Object](asf-file-structure.md#header-object)
</dt> </dl>

 

 




