---
description: Gets the speaker configuration for the audio channels in the audio bit stream.
ms.assetid: ec13bb55-47af-4d79-9560-d297bce8e236
title: AVAudioChannelConfig property (Codecapi.h)
ms.topic: reference
ms.date: 05/31/2018
---

# AVAudioChannelConfig property

Gets the speaker configuration for the audio channels in the audio bit stream.

This property is read-only.

## Data type

**UINT32** (**VT\_UI4**)

## Property GUID

**CODECAPI\_AVAudioChannelConfig**

## Property value

The value of this property is a bitwise OR of members of the [**eAVAudioChannelConfig**](/windows/desktop/api/codecapi/ne-codecapi-eavaudiochannelconfig) enumeration.

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

 

 




