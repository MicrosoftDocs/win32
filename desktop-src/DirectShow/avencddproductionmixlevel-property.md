---
Description: 'Specifies the mixing level, in decibels (dB), in a Dolby Digital audio stream. This property applies to Dolby Digital audio encoders.'
ms.assetid: 'fcb16d02-af4f-4626-99ee-2831172e5280'
title: AVEncDDProductionMixLevel property
---

# AVEncDDProductionMixLevel property

Specifies the mixing level, in decibels (dB), in a Dolby Digital audio stream. This property applies to Dolby Digital audio encoders.

This property is read/write.

## Data type

**UINT32** (**VT\_UI4**)

## Property GUID

**CODECAPI\_AVEncDDProductionMixLevel**

## Property value

This property has a linear range of values. To get the supported range, call [**ICodecAPI::GetParameterRange**](icodecapi-getparameterrange.md).

## Remarks

If you set this property, set the [**AVEncDDProductionInfoExists**](avencddproductioninfoexists-property.md) property to **TRUE**.

## Requirements



|                                     |                                                                                       |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional \[desktop apps \| UWP apps\]<br/>                     |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps \| UWP apps\]<br/>                           |
| Header<br/>                   | <dl> <dt>Codecapi.h</dt> </dl> |



## See also

<dl> <dt>

[Codec API Properties](codec-api-properties.md)
</dt> <dt>

[**ICodecAPI Interface**](icodecapi.md)
</dt> </dl>

 

 




