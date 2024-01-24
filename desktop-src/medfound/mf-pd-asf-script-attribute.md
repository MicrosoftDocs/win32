---
description: Specifies a list of script commands and the parameters for an Advanced Systems Format (ASF) file. This attribute corresponds to the Script Command Object in the ASF header, defined in the ASF specification.
ms.assetid: c85c9da4-f0b5-4055-a645-2a71cabbe4a3
title: MF_PD_ASF_SCRIPT attribute (Wmcontainer.h)
ms.topic: reference
ms.date: 05/31/2018
---

# MF\_PD\_ASF\_SCRIPT attribute

Specifies a list of script commands and the parameters for an Advanced Systems Format (ASF) file. This attribute corresponds to the Script Command Object in the ASF header, defined in the ASF specification.

## Data type

Byte array

## Remarks

This attribute applies to presentation descriptors for ASF content.

The [**IMFASFContentInfo::GeneratePresentationDescriptor**](/windows/desktop/api/wmcontainer/nf-wmcontainer-imfasfcontentinfo-generatepresentationdescriptor) method creates the presentation descriptor and generates this attribute from the Script Command Object header. The following table shows the format of the blob:



| Script Command Object field | Data type    | Size    | Description               |
|-----------------------------|--------------|---------|---------------------------|
| Commands Count              | **DWORD**    | 4 bytes | Number of script commands |
| Command Type, Commands      | **BYTE**\[\] | Varies  | Array of script commands  |



 

The first **DWORD** is the number of script commands, followed by an array of commands. Each script command has the following format:



| Script Command Object field | Data type     | Size    | Description                                                              |
|-----------------------------|---------------|---------|--------------------------------------------------------------------------|
| Command Name Length         | **DWORD**     | 4 bytes | Size of the command string, in bytes, including the NULL character.      |
| Command Name                | **WCHAR**\[\] | Varies  | Null-terminated string that contains the script command.                 |
| Command Type Name Length    | **DWORD**     | 4 bytes | Size of the command type string, in bytes, including the NULL character. |
| Command Type Name           | **WCHAR**\[\] | Varies  | Null-terminated string that contains the command type.                   |
| Presentation Time           | **DWORD**     | 4 bytes | Presentation time of the command in milliseconds.                        |



 

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

 

 




