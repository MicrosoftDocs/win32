---
description: Specifies how the decoder reproduces dual mono audio.
ms.assetid: 3ef1f52c-13b2-4d9f-99fe-3317846be8a0
title: AVDecAudioDualMonoReproMode property (Codecapi.h)
ms.topic: reference
ms.date: 05/31/2018
---

# AVDecAudioDualMonoReproMode property

Specifies how the decoder reproduces dual mono audio.

This property is read/write.

## Data type

**UINT32** (**VT\_UI4**)

## Property GUID

**CODECAPI\_AVDecAudioDualMonoReproMode**

## Property value

The value of this property is a member of the [**eAVDecAudioDualMonoReproMode**](/windows/desktop/api/codecapi/ne-codecapi-eavdecaudiodualmonorepromode) enumeration.

## Remarks

This properties applies only when the decoder's input bit stream contains dual mono audio. To test this condition, get the value of the [AVDecAudioDualMono](avdecaudiodualmono-property.md) property.

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

 

 




