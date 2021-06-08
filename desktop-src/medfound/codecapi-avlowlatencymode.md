---
description: Enables low-latency mode in a codec.
ms.assetid: 15E8FF6F-AD8C-436F-B3C0-5062B1F86E32
title: CODECAPI_AVLowLatencyMode property (Codecapi.h)
ms.topic: reference
ms.date: 05/31/2018
---

# CODECAPI\_AVLowLatencyMode property

Enables low-latency mode in a codec.

## Data type

**ULONG** (**VT\_BOOL**)

## Property GUID

**CODECAPI\_AVLowLatencyMode**

## Property value

If the value is nonzero, low-latency mode is enabled. If the value is zero, low-latency mode is disabled.

## Remarks

This property applies to both encoders and decoders.

Low-latency mode is useful for real-time communications or live capture, when latency should be minimized. However, low-latency mode might also reduce the decoding or encoding quality.

The encoder is expected to not add any sample delay due to frame reordering in encoding process, and one input sample shall produce one output sample. B slices/frames can be present as long as they do not introduce any frame re-ordering in the encoder.

> [!WARNING] In the current implementation, the Media Foundation H.264 decoder uses the type **VT_UI4** for this property. All other implementations, including the H.264 encoder, use the type **VT_BOOL**.

## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 8 \[desktop apps \| UWP apps\]<br/>                                     |
| Minimum supported server<br/> | Windows Server 2012 \[desktop apps \| UWP apps\]<br/>                           |
| Header<br/>                   | <dl> <dt>Codecapi.h</dt> </dl> |



## See also

<dl> <dt>

[Media Foundation Properties](media-foundation-properties.md)
</dt> <dt>

[**ICodecAPI**](/windows/desktop/api/strmif/nn-strmif-icodecapi)
</dt> </dl>

 

