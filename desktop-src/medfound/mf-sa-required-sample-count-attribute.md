---
Description: Indicates the number of uncompressed buffers that the enhanced video renderer (EVR) media sink requires for deinterlacing.
ms.assetid: b62bff64-153f-4028-a546-250419dc4152
title: MF\_SA\_REQUIRED\_SAMPLE\_COUNT attribute
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# MF\_SA\_REQUIRED\_SAMPLE\_COUNT attribute

Indicates the number of uncompressed buffers that the enhanced video renderer (EVR) media sink requires for deinterlacing.

## Data type

**UINT32**

## Remarks

This is a stream-level attribute. To get the attribute from the EVR, do the following:

1.  Call [**IMFMediaSink::GetStreamSinkByIndex**](/windows/win32/mfidl/nf-mfidl-imfmediasink-getstreamsinkbyindex?branch=master) to get the stream sink.
2.  Query the stream sink for the [**IMFAttributes**](/windows/win32/mfobjects/nn-mfobjects-imfattributes?branch=master) interface.
3.  Call [**IMFAttributes::GetUINT32**](/windows/win32/mfobjects/nf-mfobjects-imfattributes-getuint32?branch=master).

Internally, the mixer provides this attribute to the EVR. To get the attribute from the mixer, call [**IMFTransform::GetInputStreamAttributes**](/windows/win32/mftransform/nf-mftransform-imftransform-getinputstreamattributes?branch=master).

The GUID constant for this attribute is exported from mfuuid.lib.

## Requirements



|                                     |                                                                                          |
|-------------------------------------|------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps \| UWP apps\]<br/>                                    |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps \| UWP apps\]<br/>                              |
| Header<br/>                   | <dl> <dt>Mftransform.h</dt> </dl> |



## See also

<dl> <dt>

[Alphabetical List of Media Foundation Attributes](alphabetical-list-of-media-foundation-attributes.md)
</dt> <dt>

[**IMFAttributes::GetUINT32**](/windows/win32/mfobjects/nf-mfobjects-imfattributes-getuint32?branch=master)
</dt> <dt>

[**IMFAttributes::SetUINT32**](/windows/win32/mfobjects/nf-mfobjects-imfattributes-setuint32?branch=master)
</dt> <dt>

[Media Foundation Attributes](media-foundation-attributes.md)
</dt> </dl>

 

 




