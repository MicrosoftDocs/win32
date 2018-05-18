---
Description: 'Specifies the language used by a stream in an Advanced Systems Format (ASF) file.'
ms.assetid: '834cac0a-0c84-49aa-baf2-32bae26e215b'
title: 'MF\_SD\_ASF\_EXTSTRMPROP\_LANGUAGE\_ID\_INDEX attribute'
---

# MF\_SD\_ASF\_EXTSTRMPROP\_LANGUAGE\_ID\_INDEX attribute

Specifies the language used by a stream in an Advanced Systems Format (ASF) file.

## Data type

**UINT32**

## Remarks

This attribute applies to stream descriptors for ASF content. The value is an index into the language list contained in the [**MF\_PD\_ASF\_LANGLIST**](mf-pd-asf-langlist-attribute.md) attribute.

This attribute corresponds to the Stream Language ID Index field in the Extended Stream Properties object. For more information, refer to the ASF specification.

The [**IMFASFContentInfo::GeneratePresentationDescriptor**](imfasfcontentinfo-generatepresentationdescriptor.md) method generates this attribute from the ASF metadata. The application can create the stream descriptor for the stream from the presentation descriptor by calling [**IMFPresentationDescriptor::GetStreamDescriptorByIndex**](imfpresentationdescriptor-getstreamdescriptorbyindex.md).

You can also get the language tag by querying the stream descriptor for the [**MF\_SD\_LANGUAGE**](mf-sd-language-attribute.md) attribute.

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

 

 




