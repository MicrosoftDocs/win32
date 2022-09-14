---
description: Specifies the room type for a Dolby Digital audio stream. This property applies to Dolby Digital audio encoders.
ms.assetid: d19b6b9d-9606-48a8-ac8e-cdbf15588a8f
title: AVEncDDProductionRoomType property (Codecapi.h)
ms.topic: reference
ms.date: 05/31/2018
---

# AVEncDDProductionRoomType property

Specifies the room type for a Dolby Digital audio stream. This property applies to Dolby Digital audio encoders.

This property is read/write.

## Data type

**UINT32** (**VT\_UI4**)

## Property GUID

**CODECAPI\_AVEncDDProductionRoomType**

## Property value

The value of this property is a member of the [**eAVEncDDProductionRoomType**](/windows/win32/api/codecapi/ne-codecapi-eavencddproductionroomtype) enumeration.

## Remarks

*Room type* refers to the size of the room used during production. If you set this property, set the [**AVEncDDProductionInfoExists**](avencddproductioninfoexists-property.md) property to **TRUE**.

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

 

