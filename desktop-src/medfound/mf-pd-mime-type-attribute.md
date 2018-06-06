---
Description: Specifies the MIME type of the content.
ms.assetid: bbcfb3e6-a86a-4621-b8d9-92ace60e8c10
title: MF\_PD\_MIME\_TYPE attribute
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# MF\_PD\_MIME\_TYPE attribute

Specifies the MIME type of the content.

## Data type

Wide-character string

## Remarks

This attribute applies to presentation descriptors.

The MIME type exposed through [System.MIMEType](https://msdn.microsoft.com/9f8f42f8-af90-4f2d-a58c-f892139e86b7) for media files may have a bias towards choosing MIME types suitable for Digital Living Network Alliance (DLNA).

MF\_PD\_MIME\_TYPE and [System.MIMEType](https://msdn.microsoft.com/9f8f42f8-af90-4f2d-a58c-f892139e86b7) may not always match.

The GUID constant for this attribute is exported from mfuuid.lib.

## Requirements



|                                     |                                                                                    |
|-------------------------------------|------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps \| UWP apps\]<br/>                              |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps \| UWP apps\]<br/>                        |
| Header<br/>                   | <dl> <dt>Mfidl.h</dt> </dl> |



## See also

<dl> <dt>

[Alphabetical List of Media Foundation Attributes](alphabetical-list-of-media-foundation-attributes.md)
</dt> <dt>

[**IMFAttributes::GetString**](/windows/desktop/api/mfobjects/nf-mfobjects-imfattributes-getstring)
</dt> <dt>

[**IMFAttributes::SetString**](/windows/desktop/api/mfobjects/nf-mfobjects-imfattributes-setstring)
</dt> <dt>

[**IMFPresentationDescriptor**](/windows/desktop/api/mfidl/nn-mfidl-imfpresentationdescriptor)
</dt> <dt>

[Presentation Descriptor Attributes](presentation-descriptor-attributes.md)
</dt> </dl>

 

 




