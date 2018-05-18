---
Description: 'Indicates the number of uncompressed buffers that the enhanced video renderer (EVR) media sink requires for deinterlacing.'
ms.assetid: 'b62bff64-153f-4028-a546-250419dc4152'
title: 'MF\_SA\_REQUIRED\_SAMPLE\_COUNT attribute'
---

# MF\_SA\_REQUIRED\_SAMPLE\_COUNT attribute

Indicates the number of uncompressed buffers that the enhanced video renderer (EVR) media sink requires for deinterlacing.

## Data type

**UINT32**

## Remarks

This is a stream-level attribute. To get the attribute from the EVR, do the following:

1.  Call [**IMFMediaSink::GetStreamSinkByIndex**](imfmediasink-getstreamsinkbyindex.md) to get the stream sink.
2.  Query the stream sink for the [**IMFAttributes**](imfattributes.md) interface.
3.  Call [**IMFAttributes::GetUINT32**](imfattributes-getuint32.md).

Internally, the mixer provides this attribute to the EVR. To get the attribute from the mixer, call [**IMFTransform::GetInputStreamAttributes**](imftransform-getinputstreamattributes.md).

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

[**IMFAttributes::GetUINT32**](imfattributes-getuint32.md)
</dt> <dt>

[**IMFAttributes::SetUINT32**](imfattributes-setuint32.md)
</dt> <dt>

[Media Foundation Attributes](media-foundation-attributes.md)
</dt> </dl>

 

 




