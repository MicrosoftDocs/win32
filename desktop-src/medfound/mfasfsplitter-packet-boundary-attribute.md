---
Description: 'Specifies whether a buffer contains the start of an Advanced Systems Format (ASF) packet.'
ms.assetid: 'eca3f9b7-6051-4654-8016-a9c679519bc7'
title: 'MFASFSPLITTER\_PACKET\_BOUNDARY attribute'
---

# MFASFSPLITTER\_PACKET\_BOUNDARY attribute

Specifies whether a buffer contains the start of an Advanced Systems Format (ASF) packet.

## Data type

**UINT32**

Treat as a Boolean value.

## Remarks

If a media buffer exposes the [**IMFAttributes**](imfattributes.md) interface through **QueryInterface**, and the value of this attribute is nonzero, the ASF splitter treats the buffer as the start of a new packet.

This attribute applies if you are using the ASF splitter to parse ASF data. If your ASF data has variable packet lengths, you must set this attribute on the media buffers that you pass to the [**IMFASFSplitter::ParseData**](imfasfsplitter-parsedata.md) method. Set the attribute to **TRUE** if the buffer contains the start of a new packet. If the buffer contains a continuation of the previous packet, set the attribute to **FALSE**. The buffers cannot span multiple packets.

For ASF data with fixed packet sizes, this attribute is not required, and a buffer can can span multiple packets.

Note that the standard implementations of the [**IMFMediaBuffer**](imfmediabuffer.md) provided by Media Foundation do not expose [**IMFAttributes**](imfattributes.md). To use this attribute, you must provide your own implementation of **IMFMediaBuffer**; for example, by wrapping the buffers returned by [**MFCreateMemoryBuffer**](mfcreatememorybuffer.md).

## Requirements



|                                     |                                                                                          |
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

[**IMFAttributes::GetUINT32**](imfattributes-getuint32.md)
</dt> <dt>

[**IMFAttributes::SetUINT32**](imfattributes-setuint32.md)
</dt> <dt>

[**IMFMediaBuffer**](imfmediabuffer.md)
</dt> </dl>

 

 




