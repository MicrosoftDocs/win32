---
Description: Specifies the offset, in bytes, from the start of an Advanced Systems Format (ASF) file to the start of the first data packet.
ms.assetid: 5145d952-19d9-4bf8-9046-0b5d28f5e641
title: MF\_PD\_ASF\_DATA\_START\_OFFSET attribute
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# MF\_PD\_ASF\_DATA\_START\_OFFSET attribute

Specifies the offset, in bytes, from the start of an Advanced Systems Format (ASF) file to the start of the first data packet.

## Data type

**UINT64**

## Remarks

This attribute applies to presentation descriptors for ASF content.

The [**IMFASFContentInfo::GeneratePresentationDescriptor**](/windows/win32/wmcontainer/nf-wmcontainer-imfasfcontentinfo-generatepresentationdescriptor?branch=master) method generates this attribute from the ASF metadata.

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

[**IMFAttributes::GetUINT64**](/windows/win32/mfobjects/nf-mfobjects-imfattributes-getuint64?branch=master)
</dt> <dt>

[**IMFAttributes::SetUINT64**](/windows/win32/mfobjects/nf-mfobjects-imfattributes-setuint64?branch=master)
</dt> <dt>

[**IMFPresentationDescriptor**](/windows/win32/mfidl/nn-mfidl-imfpresentationdescriptor?branch=master)
</dt> <dt>

[Presentation Descriptor Attributes](presentation-descriptor-attributes.md)
</dt> <dt>

[ASF Header Object](asf-file-structure.md#header-object)
</dt> </dl>

 

 




