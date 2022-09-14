---
description: Specifies whether the encoder adds a sequence end code at the end of the stream. This property applies to MPEG video encoders.
ms.assetid: ef606207-2ee3-420b-afae-67c764e05e54
title: AVEncMPVAddSeqEndCode property (Codecapi.h)
ms.topic: reference
ms.date: 05/31/2018
---

# AVEncMPVAddSeqEndCode property

Specifies whether the encoder adds a sequence end code at the end of the stream. This property applies to MPEG video encoders.

This property is read/write.

## Data type

**VARIANT\_BOOL** (**VT\_BOOL**)

## Property GUID

**CODECAPI\_AVEncMPVAddSeqEndCode**

## Remarks

If the value is **VARIANT\_TRUE**, the encoder adds a sequence end code at the end of the stream.

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

 

 




