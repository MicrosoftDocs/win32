---
Description: Specifies whether a byte-stream handler can use a byte stream that is opened for writing by another thread.
ms.assetid: d9d97880-a563-420c-b598-c3ebd1ae8b74
title: MF\_BYTESTREAMHANDLER\_ACCEPTS\_SHARE\_WRITE attribute
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# MF\_BYTESTREAMHANDLER\_ACCEPTS\_SHARE\_WRITE attribute

Specifies whether a byte-stream handler can use a byte stream that is opened for writing by another thread.

## Data type

**UINT32**

## Get/set

To get this attribute, call [**IMFAttributes::GetUINT32**](/windows/win32/mfobjects/nf-mfobjects-imfattributes-getuint32?branch=master).

To set this attribute, call [**IMFAttributes::SetUINT32**](/windows/win32/mfobjects/nf-mfobjects-imfattributes-setuint32?branch=master).

## Remarks

Byte-stream handlers can support this attribute. To get or set the attribute, first query the byte-stream handler for the [**IMFAttributes**](/windows/win32/mfobjects/nn-mfobjects-imfattributes?branch=master) interface. Then call [**IMFAttributes::GetUINT32**](/windows/win32/mfobjects/nf-mfobjects-imfattributes-getuint32?branch=master) or [**IMFAttributes::SetUINT32**](/windows/win32/mfobjects/nf-mfobjects-imfattributes-setuint32?branch=master)

If this attribute is **TRUE**, it means that the byte-stream handler can read from a stream while another thread writes to the same stream. When a stream is opened for writing by another thread, the [**IMFByteStream::GetCapabilities**](/windows/win32/mfobjects/nf-mfobjects-imfbytestream-getcapabilities?branch=master) method returns the **MFBYTESTREAM\_SHARE\_WRITE** flag.

This attribute affects source resolution. If a byte stream has the **MFBYTESTREAM\_SHARE\_WRITE** flag set, the [Source Resolver](source-resolver.md) will not pass that stream to a byte-stream handler unless the handler has the MF\_BYTESTREAMHANDLER\_ACCEPTS\_SHARE\_WRITE attribute set to **TRUE**.

The **MFBYTESTREAM\_SHARE\_WRITE** flag is a hint that the length of the stream might change while the handler is reading from it.

The GUID constant for this attribute is exported from mfuuid.lib.

## Requirements



|                                     |                                                                                    |
|-------------------------------------|------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 7 \[desktop apps \| UWP apps\]<br/>                                  |
| Minimum supported server<br/> | Windows Server 2008 R2 \[desktop apps \| UWP apps\]<br/>                     |
| Header<br/>                   | <dl> <dt>Mfidl.h</dt> </dl> |



## See also

<dl> <dt>

[Alphabetical List of Media Foundation Attributes](alphabetical-list-of-media-foundation-attributes.md)
</dt> <dt>

[Scheme Handlers and Byte-Stream Handlers](scheme-handlers-and-byte-stream-handlers.md)
</dt> </dl>

 

 




