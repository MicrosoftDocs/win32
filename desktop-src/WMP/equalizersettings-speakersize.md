---
title: EQUALIZERSETTINGS.speakerSize
description: The speakerSize attribute specifies or retrieves the index number of the current speaker size.
ms.assetid: 454d07bf-49cd-48a5-9724-6415a925367a
keywords:
- EQUALIZERSETTINGS.speakerSize Windows Media Player
topic_type:
- apiref
api_name:
- EQUALIZERSETTINGS.speakerSize
api_type:
- NA
ms.topic: reference
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# EQUALIZERSETTINGS.speakerSize

\[The feature associated with this page, [Windows Media Player SDK](/windows/win32/wmp/windows-media-player-sdk), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer). **MediaPlayer** has been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** instead of **Windows Media Player SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

The **speakerSize** attribute specifies or retrieves the index number of the current speaker size.

``` syntax
        elementID.speakerSize
```

## Possible Values

This attribute is a read/write **Number** (long) containing one of the following values.



| Value | Description                              |
|-------|------------------------------------------|
| 0     | The current speakers are headphones.     |
| 1     | The current speakers are of normal size. |
| 2     | The current speakers are large.          |



 

## Remarks

The friendly name of the speaker size can be retrieved using the **currentSpeakerName** attribute.

This attribute is ignored if **enhancedAudio** is set to false.

## Requirements



| Requirement | Value |
|--------------------|---------------------------------------------------|
| Version<br/> | Windows Media Player 9 Series or later<br/> |



## See also

<dl> <dt>

[**EQUALIZERSETTINGS Element**](equalizersettings-element.md)
</dt> <dt>

[**EQUALIZERSETTINGS.currentSpeakerName**](equalizersettings-currentspeakername.md)
</dt> <dt>

[**EQUALIZERSETTINGS.enhancedAudio**](equalizersettings-enhancedaudio.md)
</dt> </dl>

 

 





