---
description: Specifies whether metadata is written to the transcoded file.
ms.assetid: 0fbfc035-c9d1-4014-a28a-93d7e6adc718
title: MF_TRANSCODE_SKIP_METADATA_TRANSFER attribute (Mfidl.h)
ms.topic: reference
ms.date: 05/31/2018
---

# MF\_TRANSCODE\_SKIP\_METADATA\_TRANSFER attribute

Specifies whether metadata is written to the transcoded file. This container attribute is stored in the transcode profile.

## Data type

**UINT32**

Possible values for the MF\_TRANSCODE\_SKIP\_METADATA\_TRANSFER attribute are described in the following table.



| Value                                                                        | Meaning                                                                                             |
|------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------|
| <dl> <dt>0</dt> </dl> | Automatically transfers file-level metadata from the source file to the transcoded file.<br/> |
| <dl> <dt>1</dt> </dl> | The source file metadata is not written to the transcoded file.<br/>                          |



 

## Get/set

To get this attribute, call [**IMFAttributes::GetUINT32**](/windows/desktop/api/mfobjects/nf-mfobjects-imfattributes-getuint32).

To set this attribute, call [**IMFAttributes::SetUINT32**](/windows/desktop/api/mfobjects/nf-mfobjects-imfattributes-setuint32).

## Remarks

The GUID constant for this attribute is exported from mfuuid.lib.

## Requirements



| Requirement | Value |
|-------------------------------------|------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 7 \[desktop apps only\]<br/>                                         |
| Minimum supported server<br/> | Windows Server 2008 R2 \[desktop apps only\]<br/>                            |
| Header<br/>                   | <dl> <dt>Mfidl.h</dt> </dl> |



## See also

<dl> <dt>

[Alphabetical List of Media Foundation Attributes](alphabetical-list-of-media-foundation-attributes.md)
</dt> <dt>

[**IMFTranscodeProfile::GetContainerAttributes**](/windows/desktop/api/mfidl/nf-mfidl-imftranscodeprofile-getcontainerattributes)
</dt> <dt>

[**IMFTranscodeProfile::SetContainerAttributes**](/windows/desktop/api/mfidl/nf-mfidl-imftranscodeprofile-setcontainerattributes)
</dt> </dl>

 

 




