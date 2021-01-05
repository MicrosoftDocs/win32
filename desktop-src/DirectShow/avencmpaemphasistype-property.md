---
description: Specifies the type of de-emphasis filter that should be used when decoding. This property applies to MPEG audio encoders.
ms.assetid: 1c1f7ac0-48a1-46d6-a131-fe281f2c86ba
title: AVEncMPAEmphasisType property (Codecapi.h)
ms.topic: reference
ms.date: 05/31/2018
---

# AVEncMPAEmphasisType property

Specifies the type of de-emphasis filter that should be used when decoding. This property applies to MPEG audio encoders.

This property is read/write.

## Data type

**UINT32** (**VT\_UI4**)

## Property GUID

**CODECAPI\_AVEncMPAEmphasisType**

## Property value

The value of this property is a member of the [**eAVEncMPAEmphasisType**](/windows/win32/api/codecapi/ne-codecapi-eavencmpaemphasistype) enumeration.

## Remarks

This property sets the emphasis bits in the frame header.

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

 

