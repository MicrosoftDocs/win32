---
Description: Specifies the average buffer size needed for a variable bit rate (VBR) Advanced Systems Format (ASF) file.
ms.assetid: 508d8670-5f5f-422b-9fa1-150115e2dbb8
title: MF\_PD\_ASF\_METADATA\_V8\_BUFFERAVERAGE attribute
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# MF\_PD\_ASF\_METADATA\_V8\_BUFFERAVERAGE attribute

Specifies the average buffer size needed for a variable bit rate (VBR) Advanced Systems Format (ASF) file.

## Data type

**UINT32**

## Remarks

This attribute applies to presentation descriptors for ASF content.

The [**IMFASFContentInfo::GeneratePresentationDescriptor**](/windows/desktop/api/wmcontainer/nf-wmcontainer-imfasfcontentinfo-generatepresentationdescriptor) method generates this attribute that applies to the presentation descriptor for ASF content.

> [!Note]  
> This attribute applies only to files created by version 8 of the Windows Media Format SDK. It corresponds to the **BufferAverage** attribute in the Windows Media Format SDK.

 

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

[**IMFAttributes::GetUINT32**](/windows/desktop/api/mfobjects/nf-mfobjects-imfattributes-getuint32)
</dt> <dt>

[**IMFAttributes::SetUINT32**](/windows/desktop/api/mfobjects/nf-mfobjects-imfattributes-setuint32)
</dt> <dt>

[**IMFPresentationDescriptor**](/windows/desktop/api/mfidl/nn-mfidl-imfpresentationdescriptor)
</dt> <dt>

[Presentation Descriptor Attributes](presentation-descriptor-attributes.md)
</dt> <dt>

[ASF Header Object](asf-file-structure.md)
</dt> <dt>

[Presentation Descriptors](presentation-descriptors.md)
</dt> </dl>

 

 




