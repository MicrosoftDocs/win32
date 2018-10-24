---
Description: Specifies when a byte stream was last modified.
ms.assetid: dceff922-44eb-478f-842a-8ac0e73a02ee
title: MF_BYTESTREAM_LAST_MODIFIED_TIME attribute
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# MF\_BYTESTREAM\_LAST\_MODIFIED\_TIME attribute

Specifies when a byte stream was last modified.

## Data type

Byte array

## Remarks

This attribute is optional. The value of the attribute is a [**FILETIME**](https://msdn.microsoft.com/en-us/library/ms724284(v=VS.85).aspx) structure.

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

[**IMFAttributes::GetBlob**](/windows/desktop/api/mfobjects/nf-mfobjects-imfattributes-getblob)
</dt> <dt>

[**IMFAttributes::SetBlob**](/windows/desktop/api/mfobjects/nf-mfobjects-imfattributes-setblob)
</dt> <dt>

[**IMFByteStream**](/windows/desktop/api/mfobjects/nn-mfobjects-imfbytestream)
</dt> </dl>

 

 




