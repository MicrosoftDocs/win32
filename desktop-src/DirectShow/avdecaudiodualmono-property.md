---
description: AVDecAudioDualMono property - Specifies whether 2-channel audio is encoded as stereo or dual mono.
ms.assetid: 96cb9e17-588c-4a1a-a7ba-7f8439d5b79a
title: AVDecAudioDualMono property (Codecapi.h)
ms.topic: reference
ms.date: 05/31/2018
---

# AVDecAudioDualMono property

Specifies whether 2-channel audio is encoded as stereo or dual mono.

This property is read-only.

## Data type

**UINT32** (**VT\_UI4**)

## Property GUID

**CODECAPI\_AVDecAudioDualMono**

## Property value

The value of this property is a member of the [**eAVDecAudioDualMono**](/windows/desktop/api/codecapi/ne-codecapi-eavdecaudiodualmono) enumeration.

## Remarks

This property applies only when the decoder's input bit stream contains two-channel audio. A two-channel audio stream might be encoded as stereo or as dual mono. If the audio is dual mono, you can set the [**AVDecAudioDualMonoReproMode**](avdecaudiodualmonorepromode-property.md) property to configure how the decoder reproduces the audio.

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

 

 




