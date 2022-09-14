---
description: Specifies the language used by a stream in an Advanced Systems Format (ASF) file.
ms.assetid: 834cac0a-0c84-49aa-baf2-32bae26e215b
title: MF_SD_ASF_EXTSTRMPROP_LANGUAGE_ID_INDEX attribute (Wmcontainer.h)
ms.topic: reference
ms.date: 05/31/2018
---

# MF\_SD\_ASF\_EXTSTRMPROP\_LANGUAGE\_ID\_INDEX attribute

Specifies the language used by a stream in an Advanced Systems Format (ASF) file.

## Data type

**UINT32**

## Remarks

This attribute applies to stream descriptors for ASF content. The value is an index into the language list contained in the [**MF\_PD\_ASF\_LANGLIST**](mf-pd-asf-langlist-attribute.md) attribute.

This attribute corresponds to the Stream Language ID Index field in the Extended Stream Properties object. For more information, refer to the ASF specification.

The [**IMFASFContentInfo::GeneratePresentationDescriptor**](/windows/desktop/api/wmcontainer/nf-wmcontainer-imfasfcontentinfo-generatepresentationdescriptor) method generates this attribute from the ASF metadata. The application can create the stream descriptor for the stream from the presentation descriptor by calling [**IMFPresentationDescriptor::GetStreamDescriptorByIndex**](/windows/desktop/api/mfidl/nf-mfidl-imfpresentationdescriptor-getstreamdescriptorbyindex).

You can also get the language tag by querying the stream descriptor for the [**MF\_SD\_LANGUAGE**](mf-sd-language-attribute.md) attribute.

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

[**IMFStreamDescriptor**](/windows/desktop/api/mfidl/nn-mfidl-imfstreamdescriptor)
</dt> <dt>

[Stream Descriptor Attributes](stream-descriptor-attributes.md)
</dt> <dt>

[ASF Header Object](asf-file-structure.md)
</dt> </dl>

 

 




