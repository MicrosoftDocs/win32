---
description: Specifies whether the output stream should be structured so that the encoded stream has a low decoding latency.
ms.assetid: a000a2d4-afcf-4b88-9bbc-f42758744de2
title: AVEncCommonLowLatency property (Codecapi.h)
ms.topic: reference
ms.date: 05/31/2018
---

# AVEncCommonLowLatency property

Specifies whether the output stream should be structured so that the encoded stream has a low decoding latency.

This property is read/write.

## Data type

**VARIANT\_BOOL** (**VT\_BOOL**)

## Property GUID

**CODECAPI\_AVEncCommonLowLatency**

## Remarks

Decoding latency is defined as the amount of data the decoder must buffer. For example, setting this property to **VARIANT\_TRUE** on an MPEG video encoder limits the types of GOP structures the encoder can use.

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

 

 




