---
Description: 'Specifies whether the Source Reader shuts down the media source.'
ms.assetid: 'c85f5994-8005-48c9-8a05-0316f48f4142'
title: 'MF\_SOURCE\_READER\_DISCONNECT\_MEDIASOURCE\_ON\_SHUTDOWN attribute'
---

# MF\_SOURCE\_READER\_DISCONNECT\_MEDIASOURCE\_ON\_SHUTDOWN attribute

Specifies whether the [Source Reader](source-reader.md) shuts down the media source.

## Data type

**UINT32**

## Get/set

To get this attribute, call [**IMFAttributes::GetUINT32**](imfattributes-getuint32.md).

To set this attribute, call [**IMFAttributes::SetUINT32**](imfattributes-setuint32.md).

## Remarks

This attribute applies only when the application creates the source reader from an existing media source object, either by calling [**MFCreateSourceReaderFromMediaSource**](mfcreatesourcereaderfrommediasource.md) or by calling [**IMFReadWriteClassFactory::CreateInstanceFromObject**](imfreadwriteclassfactory-createinstancefromobject.md).

By default, when the application releases the source reader, the source reader shuts down the media source by calling [**IMFMediaSource::Shutdown**](imfmediasource-shutdown.md) on the media source. At that point, the application can no longer use the media source.

However, if the MF\_SOURCE\_READER\_DISCONNECT\_MEDIASOURCE\_ON\_SHUTDOWN attribute is **TRUE**, the source reader does not shut down the media source. That means the application can still use the media source after the application releases the source reader. It also means the application is responsible for calling [**IMFMediaSource::Shutdown**](imfmediasource-shutdown.md) on the media source.

If the application creates the source reader from a URL or from a byte stream, the source reader always shuts down the media source. The MF\_SOURCE\_READER\_DISCONNECT\_MEDIASOURCE\_ON\_SHUTDOWN attribute is ignored in this case.

## Requirements



|                                     |                                                                                          |
|-------------------------------------|------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 7 \[desktop apps \| UWP apps\]<br/>                                        |
| Minimum supported server<br/> | Windows Server 2008 R2 \[desktop apps \| UWP apps\]<br/>                           |
| Header<br/>                   | <dl> <dt>Mfreadwrite.h</dt> </dl> |



## See also

<dl> <dt>

[Alphabetical List of Media Foundation Attributes](alphabetical-list-of-media-foundation-attributes.md)
</dt> <dt>

[Source Reader](source-reader.md)
</dt> <dt>

[Source Reader Attributes](source-reader-attributes.md)
</dt> </dl>

 

 




