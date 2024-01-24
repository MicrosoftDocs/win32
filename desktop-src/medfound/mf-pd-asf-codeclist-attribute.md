---
description: Contains information about the codecs and formats that were used to encode the content in an Advanced Systems Format (ASF) file. This attribute corresponds to the Codec List Object in the ASF header, defined in the ASF specification.
ms.assetid: 6dde30d3-dbdc-469c-ad7e-5e670b7e0a64
title: MF_PD_ASF_CODECLIST attribute (Wmcontainer.h)
ms.topic: reference
ms.date: 05/31/2018
---

# MF\_PD\_ASF\_CODECLIST attribute

Contains information about the codecs and formats that were used to encode the content in an Advanced Systems Format (ASF) file. This attribute corresponds to the Codec List Object in the ASF header, defined in the ASF specification.

## Data type

Byte array

## Remarks

This attribute applies to presentation descriptors for ASF content.

The [**IMFASFContentInfo::GeneratePresentationDescriptor**](/windows/desktop/api/wmcontainer/nf-wmcontainer-imfasfcontentinfo-generatepresentationdescriptor) method creates the presentation descriptor and generates this attribute from the Codec List Object in the ASF header. An application that uses the [ASF Media Source](asf-media-source.md) can get this attribute by calling [**IMFMediaSource::CreatePresentationDescriptor**](/windows/desktop/api/mfidl/nf-mfidl-imfmediasource-createpresentationdescriptor) and then getting the attribute from the presentation descriptor.

The following table shows the layout of the attribute blob.



| Codec List Object field | Data type    | Size    | Description                           |
|-------------------------|--------------|---------|---------------------------------------|
| Codec Entries Count     | **DWORD**    | 4 bytes | Number of codecs                      |
| Codec Entries           | **BYTE**\[\] | Varies  | Array of codec information structures |



 

The Code Entries field is an array of structures. The following table shows the format of each entry:




| Codec List Object field | Data type | Size | Description | 
|-------------------------|-----------|------|-------------|
| Type | <strong>DWORD</strong> | 4 bytes | Codec type. This can be one of the following values:<br /><ul><li>0x0001: Audio codec</li><li>0x0002: Video codec</li><li>0xFFFF: Unknown</li></ul> | 
| Codec Name Length | <strong>DWORD</strong> | 4 bytes | Size of the Codec Name string, in bytes, including the <strong>NULL</strong> character. | 
| Codec Name | <strong>WCHAR</strong>[] | Varies | Null-terminated Unicode string that contains the name of the codec, such as "Windows Media Video 9". | 
| Codec Description Length | <strong>DWORD</strong> | 4 bytes | Size of the Codec Description string, in bytes, including the <strong>NULL</strong> character. | 
| Codec Description | <strong>WCHAR</strong>[] | Varies | A null-terminated Unicode string that contains a description of the codec. | 
| Codec Information Length | <strong>DWORD</strong> | 4 bytes | Size of the Codec Information field, in bytes. | 
| Codec Information | <strong>BYTE</strong>[] | Varies | Codec data. The meaning of this data depends on the codec. Typically, this data indicates the format. | 




 

> [!Note]  
> The layout of the attribute blob does not exactly match the layout of the Codec List Object in the ASF header. In particular, string lengths are given in bytes and include the size of the **NULL** terminator.

 

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

[**IMFAttributes::GetBlob**](/windows/desktop/api/mfobjects/nf-mfobjects-imfattributes-getblob)
</dt> <dt>

[**IMFAttributes::SetBlob**](/windows/desktop/api/mfobjects/nf-mfobjects-imfattributes-setblob)
</dt> <dt>

[**IMFPresentationDescriptor**](/windows/desktop/api/mfidl/nn-mfidl-imfpresentationdescriptor)
</dt> <dt>

[Presentation Descriptor Attributes](presentation-descriptor-attributes.md)
</dt> <dt>

[ASF Header Object](asf-file-structure.md)
</dt> <dt>

[Presentation Descriptors](presentation-descriptors.md)
</dt> </dl>

 

 




