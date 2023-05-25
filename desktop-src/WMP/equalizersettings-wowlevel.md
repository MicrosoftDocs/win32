---
title: EQUALIZERSETTINGS.wowLevel
description: The wowLevel attribute specifies or retrieves the SRS WOW Effect level.
ms.assetid: 8f99d7e1-39b9-42be-ab6d-8435ba7022fa
keywords:
- EQUALIZERSETTINGS.wowLevel Windows Media Player
topic_type:
- apiref
api_name:
- EQUALIZERSETTINGS.wowLevel
api_type:
- NA
ms.topic: reference
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# EQUALIZERSETTINGS.wowLevel

\[The feature associated with this page, [Windows Media Player SDK](/windows/win32/wmp/windows-media-player-sdk), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer). **MediaPlayer** has been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** instead of **Windows Media Player SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

The **wowLevel** attribute specifies or retrieves the SRS WOW Effect level.

``` syntax
        elementID.wowLevel
```

## Possible Values

This attribute is a read/write **Number** (**long**) ranging from 0 to 100 with a default value of 50.

## Remarks

The SRS WOW Effect is an audio enhancement effect. This attribute is ignored if **enhancedAudio** is set to false.

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

 

 





