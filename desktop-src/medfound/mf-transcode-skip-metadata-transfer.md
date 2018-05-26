---
Description: Specifies whether metadata is written to the transcoded file.
ms.assetid: 0fbfc035-c9d1-4014-a28a-93d7e6adc718
title: MF\_TRANSCODE\_SKIP\_METADATA\_TRANSFER attribute
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
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

To get this attribute, call [**IMFAttributes::GetUINT32**](/windows/win32/mfobjects/nf-mfobjects-imfattributes-getuint32?branch=master).

To set this attribute, call [**IMFAttributes::SetUINT32**](/windows/win32/mfobjects/nf-mfobjects-imfattributes-setuint32?branch=master).

## Remarks

The GUID constant for this attribute is exported from mfuuid.lib.

## Requirements



|                                     |                                                                                    |
|-------------------------------------|------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 7 \[desktop apps only\]<br/>                                         |
| Minimum supported server<br/> | Windows Server 2008 R2 \[desktop apps only\]<br/>                            |
| Header<br/>                   | <dl> <dt>Mfidl.h</dt> </dl> |



## See also

<dl> <dt>

[Alphabetical List of Media Foundation Attributes](alphabetical-list-of-media-foundation-attributes.md)
</dt> <dt>

[**IMFTranscodeProfile::GetContainerAttributes**](/windows/win32/mfidl/nf-mfidl-imftranscodeprofile-getcontainerattributes?branch=master)
</dt> <dt>

[**IMFTranscodeProfile::SetContainerAttributes**](/windows/win32/mfidl/nf-mfidl-imftranscodeprofile-setcontainerattributes?branch=master)
</dt> </dl>

 

 




