---
Description: Specifies the time, in 100-nanosecond units, needed to send an Advanced Systems Format (ASF) file. A packets send time is the time when the packet should be delivered over the network. It is not the presentation time of the packet.
ms.assetid: 2bd427e2-106d-4997-86aa-fae221e429eb
title: MF\_PD\_ASF\_FILEPROPERTIES\_SEND\_DURATION attribute
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# MF\_PD\_ASF\_FILEPROPERTIES\_SEND\_DURATION attribute

Specifies the time, in 100-nanosecond units, needed to send an Advanced Systems Format (ASF) file. A packet's *send time* is the time when the packet should be delivered over the network. It is not the presentation time of the packet.

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

[**IMFAttributes::GetUINT32**](/windows/win32/mfobjects/nf-mfobjects-imfattributes-getuint32?branch=master)
</dt> <dt>

[**IMFAttributes::SetUINT32**](/windows/win32/mfobjects/nf-mfobjects-imfattributes-setuint32?branch=master)
</dt> <dt>

[**IMFPresentationDescriptor**](/windows/win32/mfidl/nn-mfidl-imfpresentationdescriptor?branch=master)
</dt> <dt>

[Presentation Descriptor Attributes](presentation-descriptor-attributes.md)
</dt> <dt>

[ASF Header Object](asf-file-structure.md#header-object)
</dt> <dt>

[Presentation Descriptors](presentation-descriptors.md)
</dt> </dl>

 

 




