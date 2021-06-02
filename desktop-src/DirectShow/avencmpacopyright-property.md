---
description: Specifies the default setting for the copyright bit in the MPEG-1 audio stream. This property applies to MPEG audio encoders.
ms.assetid: 6029c96f-b1dd-402f-9bac-9021bd897ee4
title: AVEncMPACopyright property (Codecapi.h)
ms.topic: reference
ms.date: 05/31/2018
---

# AVEncMPACopyright property

Specifies the default setting for the copyright bit in the MPEG-1 audio stream. This property applies to MPEG audio encoders.

This property is read/write.

## Data type

**VARIANT\_BOOL** (**VT\_BOOL**)

## Property GUID

**CODECAPI\_AVEncMPACopyright**

## Property value

This property can have the following values.



| Value          | Description           |
|----------------|-----------------------|
| VARIANT\_FALSE | Copyright bit is off. |
| VARIANT\_TRUE  | Copyright bit is on.  |



 

## Remarks

The encoder might override this setting, based on the contents of the input stream.

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

 

 




