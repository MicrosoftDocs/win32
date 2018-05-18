---
Description: 'Specifies the MIME type of a byte stream.'
ms.assetid: 'bcf86ece-2673-4ed8-98fd-cd0e2154b4a8'
title: 'MF\_BYTESTREAM\_CONTENT\_TYPE attribute'
---

# MF\_BYTESTREAM\_CONTENT\_TYPE attribute

Specifies the MIME type of a byte stream.

## Data type

Wide-character string

## Remarks

To get the attribute value, query the byte stream object for the [**IMFAttributes**](imfattributes.md) interface.

The GUID constant for this attribute is exported from mfuuid.lib.

## Requirements



|                                     |                                                                                                          |
|-------------------------------------|----------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps \| UWP apps\]<br/>                                                    |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps \| UWP apps\]<br/>                                              |
| Header<br/>                   | <dl> <dt>Mfobjects.h (include Mfidl.h)</dt> </dl> |



## See also

<dl> <dt>

[Alphabetical List of Media Foundation Attributes](alphabetical-list-of-media-foundation-attributes.md)
</dt> <dt>

[Byte Stream Attributes](byte-stream-attributes.md)
</dt> <dt>

[**IMFAttributes::GetString**](imfattributes-getstring.md)
</dt> <dt>

[**IMFAttributes::SetString**](imfattributes-setstring.md)
</dt> <dt>

[**IMFByteStream**](imfbytestream.md)
</dt> </dl>

 

 




