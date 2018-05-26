---
Description: Specifies the key identifier for an encrypted Advanced Systems Format (ASF) file. This attribute corresponds to the Key ID field of the Content Encryption Header, defined in the ASF specification.
ms.assetid: ebadd156-28f4-499c-a182-f48a35ecbefb
title: MF\_PD\_ASF\_CONTENTENCRYPTION\_KEYID attribute
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# MF\_PD\_ASF\_CONTENTENCRYPTION\_KEYID attribute

Specifies the key identifier for an encrypted Advanced Systems Format (ASF) file. This attribute corresponds to the Key ID field of the Content Encryption Header, defined in the ASF specification.

## Data type

Wide-character string

## Remarks

This attribute applies to presentation descriptors for ASF content.

The [**IMFASFContentInfo::GeneratePresentationDescriptor**](/windows/win32/wmcontainer/nf-wmcontainer-imfasfcontentinfo-generatepresentationdescriptor?branch=master) method retrieves the Key ID field, converts it into a wide-character string, and then populates a null-terminated array of **WCHAR**s. The size of the array equals the Key ID Length field of the Content Encryption Header.

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

[**IMFAttributes::GetString**](/windows/win32/mfobjects/nf-mfobjects-imfattributes-getstring?branch=master)
</dt> <dt>

[**IMFAttributes::SetString**](/windows/win32/mfobjects/nf-mfobjects-imfattributes-setstring?branch=master)
</dt> <dt>

[**IMFPresentationDescriptor**](/windows/win32/mfidl/nn-mfidl-imfpresentationdescriptor?branch=master)
</dt> <dt>

[Presentation Descriptor Attributes](presentation-descriptor-attributes.md)
</dt> <dt>

[ASF Header Object](asf-file-structure.md#header-object)
</dt> <dt>

[Presentation Descriptors](presentation-descriptors.md)
</dt> </dl>

 

 




