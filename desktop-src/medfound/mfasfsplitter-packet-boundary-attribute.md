---
description: Specifies whether a buffer contains the start of an Advanced Systems Format (ASF) packet.
ms.assetid: eca3f9b7-6051-4654-8016-a9c679519bc7
title: MFASFSPLITTER_PACKET_BOUNDARY attribute (Wmcontainer.h)
ms.topic: reference
ms.date: 05/31/2018
---

# MFASFSPLITTER\_PACKET\_BOUNDARY attribute

Specifies whether a buffer contains the start of an Advanced Systems Format (ASF) packet.

## Data type

**UINT32**

Treat as a Boolean value.

## Remarks

If a media buffer exposes the [**IMFAttributes**](/windows/desktop/api/mfobjects/nn-mfobjects-imfattributes) interface through **QueryInterface**, and the value of this attribute is nonzero, the ASF splitter treats the buffer as the start of a new packet.

This attribute applies if you are using the ASF splitter to parse ASF data. If your ASF data has variable packet lengths, you must set this attribute on the media buffers that you pass to the [**IMFASFSplitter::ParseData**](/windows/desktop/api/wmcontainer/nf-wmcontainer-imfasfsplitter-parsedata) method. Set the attribute to **TRUE** if the buffer contains the start of a new packet. If the buffer contains a continuation of the previous packet, set the attribute to **FALSE**. The buffers cannot span multiple packets.

For ASF data with fixed packet sizes, this attribute is not required, and a buffer can can span multiple packets.

Note that the standard implementations of the [**IMFMediaBuffer**](/windows/desktop/api/mfobjects/nn-mfobjects-imfmediabuffer) provided by Media Foundation do not expose [**IMFAttributes**](/windows/desktop/api/mfobjects/nn-mfobjects-imfattributes). To use this attribute, you must provide your own implementation of **IMFMediaBuffer**; for example, by wrapping the buffers returned by [**MFCreateMemoryBuffer**](/windows/desktop/api/mfapi/nf-mfapi-mfcreatememorybuffer).

## Requirements



| Requirement | Value |
|-------------------------------------|------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                           |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/>                                     |
| Header<br/>                   | <dl> <dt>Wmcontainer.h</dt> </dl> |



## See also

<dl> <dt>

[Alphabetical List of Media Foundation Attributes](alphabetical-list-of-media-foundation-attributes.md)
</dt> <dt>

[ASF Attributes](asf-attributes.md)
</dt> <dt>

[**IMFAttributes::GetUINT32**](/windows/desktop/api/mfobjects/nf-mfobjects-imfattributes-getuint32)
</dt> <dt>

[**IMFAttributes::SetUINT32**](/windows/desktop/api/mfobjects/nf-mfobjects-imfattributes-setuint32)
</dt> <dt>

[**IMFMediaBuffer**](/windows/desktop/api/mfobjects/nn-mfobjects-imfmediabuffer)
</dt> </dl>

 

 




