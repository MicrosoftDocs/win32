---
description: Sets the threshold at which the encoder considers a video field redundant.
ms.assetid: db6c2f0e-f451-4d2d-984f-b507083e8358
title: AVEncVideoInverseTelecineThreshold property (Codecapi.h)
ms.topic: reference
ms.date: 05/31/2018
---

# AVEncVideoInverseTelecineThreshold property

Sets the threshold at which the encoder considers a video field redundant.

This property is read/write.

## Data type

**UINT32** (**VT\_UI4**)

## Property GUID

**CODECAPI\_AVEncVideoInverseTelecineThreshold**

## Property value

The value of this property has the following range.



| Value | Description                                                    |
|-------|----------------------------------------------------------------|
| 0     | The encoder is less likely to consider video fields redundant. |
| 100   | The encoder is more likely to consider video fields redundant. |



 

## Remarks

Set this property if the encoder is performing inverse telecine with an analog video source.

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

 

 




