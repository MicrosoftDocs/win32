---
Description: 'Contains the sample description box for an MP4 or 3GP file.'
ms.assetid: 'ea157988-bd15-465c-bd6a-6d33cc1a0323'
title: 'MF\_MT\_MPEG4\_SAMPLE\_DESCRIPTION attribute'
---

# MF\_MT\_MPEG4\_SAMPLE\_DESCRIPTION attribute

Contains the sample description box for an MP4 or 3GP file.

## Data type

**BYTE\[\]**

## Get/set

To get this attribute, call [**IMFAttributes::GetBlob**](imfattributes-getblob.md).

To set this attribute, call [**IMFAttributes::SetBlob**](imfattributes-setblob.md).

## Applies to

[**IMFMediaType**](imfmediatype.md)

## Remarks

The sample description box describes the encoding used for a stream in the file.

The MPEG-4 file source sets this attribute on the media type for each stream. The value of the attribute is the raw data in the sample description box. If the MPEG-4 file source can parse the sample description, it also adds the format details to the media type. Otherwise, the application or the decoder must parse the sample description from the MF\_MT\_MPEG4\_SAMPLE\_DESCRIPTION attribute.

When setting this attribute on MPEG-4 sink through [**IMFMediaTypeHandler::SetCurrentMediaType**](imfmediatypehandler-setcurrentmediatype.md) method, the data for the attribute MF\_MT\_MPEG4\_SAMPLE\_DESCRIPTION should not change after one or more samples have been sent to the sink on the corresponding stream's [**IMFStreamSink::ProcessSample**](imfstreamsink-processsample.md) interface.

The GUID constant for this attribute is exported from mfuuid.lib.

## Requirements



|                                     |                                                                                    |
|-------------------------------------|------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 7 \[desktop apps \| UWP apps\]<br/>                                  |
| Minimum supported server<br/> | Windows Server 2008 R2 \[desktop apps \| UWP apps\]<br/>                     |
| Header<br/>                   | <dl> <dt>Mfapi.h</dt> </dl> |



## See also

<dl> <dt>

[Alphabetical List of Media Foundation Attributes](alphabetical-list-of-media-foundation-attributes.md)
</dt> <dt>

[Media Type Attributes](media-type-attributes.md)
</dt> </dl>

 

 




