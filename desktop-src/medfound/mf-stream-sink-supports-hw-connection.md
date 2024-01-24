---
description: Indicates whether a media sink supports hardware data flow.
ms.assetid: 15838467-D253-4ECE-B9E7-AFD3A21B3AF2
title: MF_STREAM_SINK_SUPPORTS_HW_CONNECTION attribute (Mfidl.h)
ms.topic: reference
ms.date: 05/31/2018
---

# MF\_STREAM\_SINK\_SUPPORTS\_HW\_CONNECTION attribute

Indicates whether a media sink supports hardware data flow.

## Data type

**BOOL** stored as **UINT32**

## Remarks

This attribute is used when a media sink proxies a hardware device and is able to receive data over a hardware bus. For example, a hardware audio decoder might send audio data directly to the audio rendering hardware.

In this scenario, the decoder and the sink are still represented in the Microsoft Media Foundation by a [Media Foundation transform](media-foundation-transforms.md) (MFT) and a media sink. However, no data flows between these two objects at the pipeline layer, only at the hardware layer, as shown in the following diagram.

![a diagram that shows a hardware proxy source.](images/proxy-mft4.png)

The connection between the MFT and the media sink is negotiated as follows.

1.  The pipeline checks if the MFT is a hardware proxy, by checking for the [MFT\_ENUM\_HARDWARE\_URL\_Attribute](mft-enum-hardware-url-attribute.md) attribute on the MFT. For details, see [Hardware MFTs](hardware-mfts.md).
2.  The pipeline gets a pointer to the [**IMFStreamSink**](/windows/desktop/api/mfidl/nn-mfidl-imfstreamsink) interface of the stream sink on the media sink.
3.  The pipeline uses the [**IMFStreamSink**](/windows/desktop/api/mfidl/nn-mfidl-imfstreamsink) pointer to query for the MF\_STREAM\_SINK\_SUPPORTS\_HW\_CONNECTION attribute. If this attribute is present and equal to **TRUE**, the media source supports hardware connections.
4.  The pipeline sets the [MFT\_CONNECTED\_STREAM\_ATTRIBUTE](mft-connected-stream-attribute.md) attribute on the stream sink. The value of this attribute is the [**IMFAttribute**](/windows/desktop/api/mfobjects/nn-mfobjects-imfattributes) pointer from the MFT.
5.  The pipeline sets the [MFT\_CONNECTED\_TO\_HW\_STREAM](mft-connected-to-hw-stream.md) attribute to **TRUE** on both the stream sink and the MFT.

## Requirements



| Requirement | Value |
|-------------------------------------|------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 8 \[desktop apps \| UWP apps\]<br/>                                  |
| Minimum supported server<br/> | Windows Server 2012 \[desktop apps \| UWP apps\]<br/>                        |
| Header<br/>                   | <dl> <dt>Mfidl.h</dt> </dl> |



## See also

<dl> <dt>

[Alphabetical List of Media Foundation Attributes](alphabetical-list-of-media-foundation-attributes.md)
</dt> </dl>

 

 




