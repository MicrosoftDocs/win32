---
description: Enables or disables hardware acceleration for VC-1 video decoding.
ms.assetid: eee85330-098e-4f21-81b7-a493abbd599b
title: AVDecVideoAcceleration_VC1 property (Codecapi.h)
ms.topic: reference
ms.date: 05/31/2018
---

# AVDecVideoAcceleration\_VC1 property

Enables or disables hardware acceleration for VC-1 video decoding.

This property is read/write.

## Data type

**UINT32** (**VT\_UI4**)

## Property GUID

**CODECAPI\_AVDecVideoAcceleration\_VC1**

## Remarks

If the value is zero, the decoder does not use DirectX Video Acceleration (DXVA) for VC-1 video decoding. For DirectShow filters, set this property before the decoder's output pin is connected.

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

 

 




