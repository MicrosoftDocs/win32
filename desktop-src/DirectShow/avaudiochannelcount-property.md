---
description: Gets the number of channels in the audio bit stream.
ms.assetid: e395ce9c-3f11-41e9-8c8c-48c17b217ebc
title: AVAudioChannelCount property (Codecapi.h)
ms.topic: reference
ms.date: 05/31/2018
---

# AVAudioChannelCount property

Gets the number of channels in the audio bit stream.

This property is read-only.

## Data type

**UINT32** (**VT\_UI4**)

## Property GUID

**CODECAPI\_AVAudioChannelCount**

## Remarks

The number of channels includes the low frequency effect (LFE) channel, if present.

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

 

 




