---
Description: Specifies the duration of a byte stream, in 100-nanosecond units.
ms.assetid: afa4930c-544b-4d66-94fe-9795bb526e0a
title: MF\_BYTESTREAM\_DURATION attribute
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# MF\_BYTESTREAM\_DURATION attribute

Specifies the duration of a byte stream, in 100-nanosecond units.

## Data type

**UINT64**

Treat as a **LONGLONG** value.

## Remarks

This attribute is optional. If the object that creates the byte stream can determine the duration, it can set this attribute. (For example, in a network stream, the duration might be part of the session description.)

To get the attribute value, call **QueryInterface** on the byte stream to get a pointer to the [**IMFAttributes**](/windows/win32/mfobjects/nn-mfobjects-imfattributes?branch=master) interface.

This attribute is a signed value, although it is stored as a **UINT64**.

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

[**IMFAttributes::GetUINT64**](/windows/win32/mfobjects/nf-mfobjects-imfattributes-getuint64?branch=master)
</dt> <dt>

[**IMFAttributes::SetUINT64**](/windows/win32/mfobjects/nf-mfobjects-imfattributes-setuint64?branch=master)
</dt> <dt>

[**IMFByteStream**](/windows/win32/mfobjects/nn-mfobjects-imfbytestream?branch=master)
</dt> </dl>

 

 




