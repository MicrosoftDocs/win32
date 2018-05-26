---
Description: Specifies the original URL for a byte stream.
ms.assetid: 31d7de71-5bbb-4c29-8ce0-df3684c56916
title: MF\_BYTESTREAM\_ORIGIN\_NAME attribute
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# MF\_BYTESTREAM\_ORIGIN\_NAME attribute

Specifies the original URL for a byte stream.

## Data type

Wide-character string

## Remarks

File-based byte streams can support this attribute. The attribute value is set when the byte stream is created. To get the attribute value, query the byte stream object for the [**IMFAttributes**](/windows/win32/mfobjects/nn-mfobjects-imfattributes?branch=master) interface.

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

[**IMFAttributes::GetString**](/windows/win32/mfobjects/nf-mfobjects-imfattributes-getstring?branch=master)
</dt> <dt>

[**IMFAttributes::SetString**](/windows/win32/mfobjects/nf-mfobjects-imfattributes-setstring?branch=master)
</dt> <dt>

[**IMFByteStream**](/windows/win32/mfobjects/nn-mfobjects-imfbytestream?branch=master)
</dt> </dl>

 

 




