---
description: Specifies the device conformance template for a stream in an Advanced Systems Format (ASF) file.
ms.assetid: e0bfb393-c8de-47cf-b80a-b0d88722e815
title: MF_SD_ASF_METADATA_DEVICE_CONFORMANCE_TEMPLATE attribute (Wmcontainer.h)
ms.topic: reference
ms.date: 05/31/2018
---

# MF\_SD\_ASF\_METADATA\_DEVICE\_CONFORMANCE\_TEMPLATE attribute

Specifies the device conformance template for a stream in an Advanced Systems Format (ASF) file.

## Data type

Wide-character string

## Remarks

This attribute applies to stream descriptors for ASF content. For more information about device conformance templates, see the topic "Device Conformance Template Parameters" in the Windows Media Format SDK.

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

[**IMFAttributes::GetString**](/windows/desktop/api/mfobjects/nf-mfobjects-imfattributes-getstring)
</dt> <dt>

[**IMFAttributes::SetString**](/windows/desktop/api/mfobjects/nf-mfobjects-imfattributes-setstring)
</dt> <dt>

[**IMFStreamDescriptor**](/windows/desktop/api/mfidl/nn-mfidl-imfstreamdescriptor)
</dt> <dt>

[Stream Descriptor Attributes](stream-descriptor-attributes.md)
</dt> <dt>

[ASF Header Object](asf-file-structure.md)
</dt> </dl>

 

 




