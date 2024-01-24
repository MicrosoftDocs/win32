---
title: EQUALIZERSETTINGS.truBassLevel
description: The truBassLevel attribute specifies or retrieves the SRS TruBass level.
ms.assetid: 9f8c9dbe-d535-42af-8ea7-74fc10526fba
keywords:
- EQUALIZERSETTINGS.truBassLevel Windows Media Player
topic_type:
- apiref
api_name:
- EQUALIZERSETTINGS.truBassLevel
api_type:
- NA
ms.topic: reference
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# EQUALIZERSETTINGS.truBassLevel

\[The feature associated with this page, [Windows Media Player SDK](/windows/win32/wmp/windows-media-player-sdk), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer). **MediaPlayer** has been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** instead of **Windows Media Player SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

The **truBassLevel** attribute specifies or retrieves the SRS TruBass level.

``` syntax
        elementID.truBassLevel
```

## Possible Values

This attribute is a read/write **Number** (**long**) ranging from 0 to 100 with a default value of 50.

## Remarks

TruBass is an effect that enhances the sound of the bass levels of the audio track. This attribute is ignored if **enhancedAudio** is set to false.

## Requirements



| Requirement | Value |
|--------------------|---------------------------------------------------|
| Version<br/> | Windows Media Player 9 Series or later<br/> |



## See also

<dl> <dt>

[**EQUALIZERSETTINGS Element**](equalizersettings-element.md)
</dt> <dt>

[**EQUALIZERSETTINGS.enhancedAudio**](equalizersettings-enhancedaudio.md)
</dt> </dl>

 

 





