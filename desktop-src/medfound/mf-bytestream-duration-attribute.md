---
description: Specifies the duration of a byte stream, in 100-nanosecond units.
ms.assetid: afa4930c-544b-4d66-94fe-9795bb526e0a
title: MF_BYTESTREAM_DURATION attribute (Mfobjects.h)
ms.topic: reference
ms.date: 05/31/2018
---

# MF\_BYTESTREAM\_DURATION attribute

Specifies the duration of a byte stream, in 100-nanosecond units.

## Data type

**UINT64**

Treat as a **LONGLONG** value.

## Remarks

This attribute is optional. If the object that creates the byte stream can determine the duration, it can set this attribute. (For example, in a network stream, the duration might be part of the session description.)

To get the attribute value, call **QueryInterface** on the byte stream to get a pointer to the [**IMFAttributes**](/windows/desktop/api/mfobjects/nn-mfobjects-imfattributes) interface.

This attribute is a signed value, although it is stored as a **UINT64**.

The GUID constant for this attribute is exported from mfuuid.lib.

## Requirements



| Requirement | Value |
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

[**IMFAttributes::GetUINT64**](/windows/desktop/api/mfobjects/nf-mfobjects-imfattributes-getuint64)
</dt> <dt>

[**IMFAttributes::SetUINT64**](/windows/desktop/api/mfobjects/nf-mfobjects-imfattributes-setuint64)
</dt> <dt>

[**IMFByteStream**](/windows/desktop/api/mfobjects/nn-mfobjects-imfbytestream)
</dt> </dl>

 

 




