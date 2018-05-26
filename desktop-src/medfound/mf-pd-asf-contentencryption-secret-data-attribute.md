---
Description: Contains secret data for an encrypted Advanced Systems Format (ASF) file. This attribute corresponds to the Secret Data field of the Content Encryption Header, defined in the ASF specification.
ms.assetid: e6ce71d6-59cd-42da-906a-ab71f2bef16f
title: MF\_PD\_ASF\_CONTENTENCRYPTION\_SECRET\_DATA attribute
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# MF\_PD\_ASF\_CONTENTENCRYPTION\_SECRET\_DATA attribute

Contains secret data for an encrypted Advanced Systems Format (ASF) file. This attribute corresponds to the Secret Data field of the Content Encryption Header, defined in the ASF specification.

## Data type

Byte array

## Remarks

This attribute applies to presentation descriptors for ASF content.

The [**IMFASFContentInfo::GeneratePresentationDescriptor**](/windows/win32/wmcontainer/nf-wmcontainer-imfasfcontentinfo-generatepresentationdescriptor?branch=master) method populates a byte array with the Secret Data field. The size of the array equals the Secret Data Length field of the Content Encryption Header.

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

[**IMFAttributes::GetBlob**](/windows/win32/mfobjects/nf-mfobjects-imfattributes-getblob?branch=master)
</dt> <dt>

[**IMFAttributes::SetBlob**](/windows/win32/mfobjects/nf-mfobjects-imfattributes-setblob?branch=master)
</dt> <dt>

[**IMFPresentationDescriptor**](/windows/win32/mfidl/nn-mfidl-imfpresentationdescriptor?branch=master)
</dt> <dt>

[Presentation Descriptor Attributes](presentation-descriptor-attributes.md)
</dt> <dt>

[ASF Header Object](asf-file-structure.md#header-object)
</dt> <dt>

[Presentation Descriptors](presentation-descriptors.md)
</dt> </dl>

 

 




