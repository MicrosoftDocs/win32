---
Description: 'Contains a pointer to the application''s callback interface for the Source Reader.'
ms.assetid: 'de226a5a-03c0-4bfe-bb20-8969ce43cf53'
title: 'MF\_SOURCE\_READER\_ASYNC\_CALLBACK attribute'
---

# MF\_SOURCE\_READER\_ASYNC\_CALLBACK attribute

Contains a pointer to the application's callback interface for the [Source Reader](source-reader.md).

## Data type

**IMFSourceReaderCallback\*** stored as **IUnknown\***

## Get/set

To get this attribute, call [**IMFAttributes::GetUnknown**](imfattributes-getunknown.md).

To set this attribute, call [**IMFAttributes::SetUnknown**](imfattributes-setunknown.md).

## Remarks

The value of this attribute is a pointer to the application's [**IMFSourceReaderCallback**](imfsourcereadercallback.md) interface.

Use this attribute with the following functions:

-   [**MFCreateSourceReaderFromByteStream**](mfcreatesourcereaderfrombytestream.md)
-   [**MFCreateSourceReaderFromMediaSource**](mfcreatesourcereaderfrommediasource.md)
-   [**MFCreateSourceReaderFromURL**](mfcreatesourcereaderfromurl.md)

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

 

 




