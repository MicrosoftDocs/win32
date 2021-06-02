---
description: Specifies the audio production information flag in a Dolby Digital audio stream. This property applies to Dolby Digital audio encoders.
ms.assetid: 72f5f988-37c3-40d4-9c1c-07086e60ea51
title: AVEncDDProductionInfoExists property (Codecapi.h)
ms.topic: reference
ms.date: 05/31/2018
---

# AVEncDDProductionInfoExists property

Specifies the audio production information flag in a Dolby Digital audio stream. This property applies to Dolby Digital audio encoders.

This property is read/write.

## Data type

**VARIANT\_BOOL** (**VT\_BOOL**)

## Property GUID

**CODECAPI\_AVEncDDProductionInfoExists**

## Remarks

If the value is **VARIANT\_TRUE**, the mixing level and room type settings are valid. Specify these settings with the [**AVEncDDProductionRoomType**](avencddproductionroomtype-property.md) and [**AVEncDDProductionMixLevel**](avencddproductionmixlevel-property.md) properties.

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

 

 




