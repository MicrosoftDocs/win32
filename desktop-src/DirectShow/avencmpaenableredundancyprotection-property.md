---
description: Specifies whether to add a cyclic redundancy check (CRC) to the frame header. This property applies to MPEG audio encoders.
ms.assetid: 55f0de8b-26dd-4d48-b7ed-2ddcef630227
title: AVEncMPAEnableRedundancyProtection property (Codecapi.h)
ms.topic: reference
ms.date: 05/31/2018
---

# AVEncMPAEnableRedundancyProtection property

Specifies whether to add a cyclic redundancy check (CRC) to the frame header. This property applies to MPEG audio encoders.

This property is read/write.

## Data type

**VARIANT\_BOOL** (**VT\_BOOL**)

## Property GUID

**CODECAPI\_AVEncMPAEnableRedundancyProtection**

## Property value

This property can have the following values.



| Value          | Description                |
|----------------|----------------------------|
| VARIANT\_FALSE | Do not add a CRC checksum. |
| VARIANT\_TRUE  | Add a CRC checksum.        |



 

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

 

 




