---
Description: 'Specifies when a byte stream was last modified.'
ms.assetid: 'dceff922-44eb-478f-842a-8ac0e73a02ee'
title: 'MF\_BYTESTREAM\_LAST\_MODIFIED\_TIME attribute'
---

# MF\_BYTESTREAM\_LAST\_MODIFIED\_TIME attribute

Specifies when a byte stream was last modified.

## Data type

Byte array

## Remarks

This attribute is optional. The value of the attribute is a [**FILETIME**](base.filetime_str) structure.

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

[**IMFAttributes::GetBlob**](imfattributes-getblob.md)
</dt> <dt>

[**IMFAttributes::SetBlob**](imfattributes-setblob.md)
</dt> <dt>

[**IMFByteStream**](imfbytestream.md)
</dt> </dl>

 

 




