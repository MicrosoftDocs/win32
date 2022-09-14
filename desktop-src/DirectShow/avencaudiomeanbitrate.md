---
description: Specifies the average bit rate of the encoded audio stream, in bits per second. This property applies only to constant bit rate (CBR) and variable bit rate (VBR) encoding modes.
ms.assetid: 9513ad64-2de9-497d-86ce-46cfdf87e0f8
title: AVEncAudioMeanBitRate property (Codecapi.h)
ms.topic: reference
ms.date: 05/31/2018
---

# AVEncAudioMeanBitRate property

Specifies the average bit rate of the encoded audio stream, in bits per second. This property applies only to constant bit rate (CBR) and variable bit rate (VBR) encoding modes.

This property is read/write.

## Data type

**UINT32** (**VT\_UI4**)

## Property GUID

**CODECAPI\_AVEncCommonMeanBitRate**

## Property value

Encoders can implement this property as an enumerated set or as a linear range.

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

 

 




