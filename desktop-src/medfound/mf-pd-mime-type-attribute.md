---
Description: Specifies the MIME type of the content.
ms.assetid: bbcfb3e6-a86a-4621-b8d9-92ace60e8c10
title: MF\_PD\_MIME\_TYPE attribute
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# MF\_PD\_MIME\_TYPE attribute

Specifies the MIME type of the content.

## Data type

Wide-character string

## Remarks

This attribute applies to presentation descriptors.

The MIME type exposed through [System.MIMEType](properties.props_System_MIMEType) for media files may have a bias towards choosing MIME types suitable for Digital Living Network Alliance (DLNA).

MF\_PD\_MIME\_TYPE and [System.MIMEType](properties.props_System_MIMEType) may not always match.

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

[**IMFAttributes::GetString**](/windows/win32/mfobjects/nf-mfobjects-imfattributes-getstring?branch=master)
</dt> <dt>

[**IMFAttributes::SetString**](/windows/win32/mfobjects/nf-mfobjects-imfattributes-setstring?branch=master)
</dt> <dt>

[**IMFPresentationDescriptor**](/windows/win32/mfidl/nn-mfidl-imfpresentationdescriptor?branch=master)
</dt> <dt>

[Presentation Descriptor Attributes](presentation-descriptor-attributes.md)
</dt> </dl>

 

 




