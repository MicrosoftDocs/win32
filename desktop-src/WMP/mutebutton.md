---
title: MUTEBUTTON
description: This is a predefined BUTTON with the following default values. | MUTEBUTTON
ms.assetid: eee00161-c0c4-4e26-a7d2-6357034fcdfd
keywords:
- MUTEBUTTON Windows Media Player
topic_type:
- apiref
api_name:
- MUTEBUTTON
api_type:
- NA
ms.topic: reference
ms.date: 4/26/2023
api_location: 
ms.custom: UpdateFrequency5
---

# MUTEBUTTON

\[The feature associated with this page, [Windows Media Player SDK](/windows/win32/wmp/windows-media-player-sdk), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer). **MediaPlayer** has been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** instead of **Windows Media Player SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

This is a predefined BUTTON with the following default values.

``` syntax
onclick="jscript:player.settings.mute=down;"
upToolTip="Mute"
downToolTip="Sound"
down="wmpprop:player.settings.mute"
sticky="true"
```

## Remarks

This creates a **BUTTON** control that will mute and un-mute the audio. The ToolTips are localized. All properties of this **BUTTON** can be overridden by explicitly specifying them.

## Requirements



| Requirement | Value |
|--------------------|----------------------------------------------|
| Version<br/> | Windows Media Player 7.0 or later<br/> |



## See also

<dl> <dt>

[**BUTTON Element**](button-element.md)
</dt> </dl>

 

 





