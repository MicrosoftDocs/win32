---
description: Byte Stream Attributes
ms.assetid: d57a57e9-87e4-4f7f-943a-63fd2ad1d1a6
title: Byte Stream Attributes
ms.topic: article
ms.date: 05/31/2018
---

# Byte Stream Attributes

The following attributes apply to some byte streams. To find out whether a byte stream supports attributes, query the byte stream object for the [**IMFAttributes**](/windows/desktop/api/mfobjects/nn-mfobjects-imfattributes) interface.



| Attribute                                                                                  | Description                                                       |
|--------------------------------------------------------------------------------------------|-------------------------------------------------------------------|
| [**MF\_BYTESTREAM\_CONTENT\_TYPE**](mf-bytestream-content-type-attribute.md)              | Specifies the MIME type of a byte stream.                         |
| [**MF\_BYTESTREAM\_DURATION**](mf-bytestream-duration-attribute.md)                       | Specifies the duration of a byte stream, in 100-nanosecond units. |
| [MF\_BYTESTREAM\_IFO\_FILE\_URI](mf-bytestream-ifo-file-uri.md)                           | Specifies the URL of an associated IFO file.                      |
| [**MF\_BYTESTREAM\_LAST\_MODIFIED\_TIME**](mf-bytestream-last-modified-time-attribute.md) | Specifies when a byte stream was last modified.                   |
| [**MF\_BYTESTREAM\_ORIGIN\_NAME**](mf-bytestream-origin-name-attribute.md)                | Specifies the original URL for a byte stream.                     |



 

The following attributes apply to byte-stream handlers.



| Attribute                                                                                    | Description                                                                                                |
|----------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------|
| [MF\_BYTESTREAMHANDLER\_ACCEPTS\_SHARE\_WRITE](mf-bytestreamhandler-accepts-share-write.md) | Specifies whether a byte-stream handler can use a byte stream that is opened for writing by another thread |



 

## Related topics

<dl> <dt>

[**IMFByteStream**](/windows/desktop/api/mfobjects/nn-mfobjects-imfbytestream)
</dt> <dt>

[Media Foundation Attributes](media-foundation-attributes.md)
</dt> </dl>

 

 



