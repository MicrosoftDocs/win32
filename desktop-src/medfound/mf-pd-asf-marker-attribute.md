---
description: Specifies the markers in an Advanced Systems Format (ASF) file. This attribute corresponds to the Marker Object in the ASF header, defined in the ASF specification.
ms.assetid: 6458eb5f-72a2-4723-b26b-b63516aa2df3
title: MF_PD_ASF_MARKER attribute (Wmcontainer.h)
ms.topic: reference
ms.date: 05/31/2018
---

# MF\_PD\_ASF\_MARKER attribute

Specifies the markers in an Advanced Systems Format (ASF) file. This attribute corresponds to the Marker Object in the ASF header, defined in the ASF specification.

## Data type

Byte array

## Remarks

This attribute applies to presentation descriptors for ASF content.

The [**IMFASFContentInfo::GeneratePresentationDescriptor**](/windows/desktop/api/wmcontainer/nf-wmcontainer-imfasfcontentinfo-generatepresentationdescriptor) method creates the presentation descriptor and generates this attribute from the Marker Object. The following table shows the format of the blob:



| Marker Object field | Data type    | Size    | Description       |
|---------------------|--------------|---------|-------------------|
| Markers Count       | **DWORD**    | 4 bytes | Number of markers |
| Markers             | **BYTE**\[\] | Varies  | Array of markers  |



 

The first **DWORD** is the number of markers, followed by an array of markers. Each marker has the following format:



| Marker Object field       | Data type     | Size    | Description                                                                       |
|---------------------------|---------------|---------|-----------------------------------------------------------------------------------|
| Marker Description Length | **DWORD**     | 4 bytes | Size of the description string, in bytes, including the NULL character.           |
| Marker Description        | **WCHAR**\[\] | Varies  | Null-terminated string that describes the marker.                                 |
| Presentation Time         | **LONGLONG**  | 8 bytes | Presentation time of the marker, in 100-nanosecond units.                         |
| Send Time                 | **LONGLONG**  | 8 bytes | Send time of the marker entry, in milliseconds.                                   |
| Offset                    | **UINT64**    | 8 bytes | Offset, in bytes, into the Data Object that specifies the position of the market. |



 

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

 

 




