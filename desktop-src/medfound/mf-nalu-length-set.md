---
description: Indicates that NALU length information will be sent as a BLOB with each compressed H.264 or H.265 sample.
ms.assetid: 71B50B44-6025-4EEC-8B37-53D80CF37B07
title: MF_NALU_LENGTH_SET attribute (Mfidl.h)
ms.topic: reference
ms.date: 05/31/2018
---

# MF\_NALU\_LENGTH\_SET attribute

Indicates that NALU length information will be sent as a **BLOB** with each compressed H.264 or H.265 sample.

## Data type

**UINT32**

## Remarks

This attribute can be set on the input media type of the H.264 decoder or H.265 decoder.  This attribute can also be set on the output type of the H.264 encoder or H.265 encoder.

When MF\_NALU\_LENGTH\_SET is set on input media type of a decoder, MF\_NALU\_LENGTH\_SET indicates to the decoder that each input sample will have a NALU length available and each input sample contains one complete primary picture.

When MF\_NALU\_LENGTH\_SET is set on the output type of an encoder, MF\_NALU\_LENGTH\_SET requests that the encoder emit NALU length information on each output sample.

The **BLOB** containing the NALU length information can be retrieved from [MF\_NALU\_LENGTH\_INFORMATION](mf-nalu-length-information.md) attribute on the input sample.

## Requirements



| Requirement | Value |
|-------------------------------------|------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 8 \[desktop apps \| UWP apps\]<br/>                                  |
| Minimum supported server<br/> | Windows Server 2012 \[desktop apps \| UWP apps\]<br/>                        |
| Header<br/>                   | <dl> <dt>Mfidl.h</dt> </dl> |



## See also

<dl> <dt>

[Alphabetical List of Media Foundation Attributes](alphabetical-list-of-media-foundation-attributes.md)
</dt> <dt>

[Media Type Attributes](media-type-attributes.md)
</dt> </dl>

 

 




