---
description: Specifies the dialog normalization level, in decibels (dB), in a Dolby Digital audio stream. This property applies to Dolby Digital audio encoders.
ms.assetid: c347f8b2-5132-45d6-af66-43d3c409b0d7
title: AVEncDDDialogNormalization property (Codecapi.h)
ms.topic: reference
ms.date: 05/31/2018
---

# AVEncDDDialogNormalization property

Specifies the dialog normalization level, in decibels (dB), in a Dolby Digital audio stream. This property applies to Dolby Digital audio encoders.

This property is read/write.

## Data type

**UINT32** (**VT\_UI4**)

## Property GUID

**CODECAPI\_AVEncDDDialogNormalization**

## Property value

This property has a linear range of values. To get the supported range, call [**ICodecAPI::GetParameterRange**](/windows/desktop/api/Strmif/nf-strmif-icodecapi-getparameterrange).

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

 

 




