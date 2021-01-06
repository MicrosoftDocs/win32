---
description: Specifies the final level of the encoding buffer, in bits, at the end of the encoding process. This property applies only to constant bit rate (CBR) and variable bit rate (VBR) encoding modes.
ms.assetid: d5bcdf54-061a-436b-8b1a-61ef7d7c90bf
title: AVEncCommonBufferOutLevel property (Codecapi.h)
ms.topic: reference
ms.date: 05/31/2018
---

# AVEncCommonBufferOutLevel property

Specifies the final level of the encoding buffer, in bits, at the end of the encoding process. This property applies only to constant bit rate (CBR) and variable bit rate (VBR) encoding modes.

This property is read/write.

## Data type

**UINT32** (**VT\_UI4**)

## Property GUID

**CODECAPI\_AVEncCommonBufferOutLevel**

## Property value

This property has a linear range of values. To get the supported range, call [**ICodecAPI::GetParameterRange**](/windows/desktop/api/Strmif/nf-strmif-icodecapi-getparameterrange).

## Remarks

The property is available only if the encoding duration is defined in advance, using the [**AVEncVideoNoOfFieldsToEncode**](avencvideonooffieldstoencode-property.md) property or [**AVEncAudioIntervalToEncode**](avencaudiointervaltoencode-property.md) property.

For MPEG video, this property defines the video buffer verifier (VBV) fullness at the end of the encoding process. It supports the concatenation of streams during encoding.

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

 

 




