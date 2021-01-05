---
description: Enables or disables hardware acceleration for MPEG-2 video decoding.
ms.assetid: 2e05f9e5-28a6-48f3-956d-a14eaf3bf4ba
title: AVDecVideoAcceleration_MPEG2 property (Codecapi.h)
ms.topic: reference
ms.date: 05/31/2018
---

# AVDecVideoAcceleration\_MPEG2 property

Enables or disables hardware acceleration for MPEG-2 video decoding.

This property is read/write.

## Data type

**UINT32** (**VT\_UI4**)

## Property GUID

**CODECAPI\_AVDecVideoAcceleration\_MPEG2**

## Remarks

If the value is zero, the decoder does not use DirectX Video Acceleration (DXVA) for MPEG-2 video decoding. For DirectShow filters, set this property before the decoder's output pin is connected.

## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional \[desktop apps \| UWP apps\]<br/>                     |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps \| UWP apps\]<br/>                           |
| Header<br/>                   | <dl> <dt>Codecapi.h</dt> </dl> |



## See also

<dl> <dt>

[Codec API Properties](codec-api-properties.md)
</dt> <dt>

[**ICodecAPI Interface**](/windows/desktop/api/Strmif/nn-strmif-icodecapi)
</dt> </dl>

 

 




