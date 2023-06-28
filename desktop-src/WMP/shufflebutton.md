---
title: SHUFFLEBUTTON
description: This is a predefined BUTTON with the following default values. | SHUFFLEBUTTON
ms.assetid: 45b3c985-81fb-4af3-89a7-e68ee9724f09
keywords:
- SHUFFLEBUTTON Windows Media Player
topic_type:
- apiref
api_name:
- SHUFFLEBUTTON
api_type:
- NA
ms.topic: reference
ms.date: 4/26/2023
api_location: 
ms.custom: UpdateFrequency5
---

# SHUFFLEBUTTON

\[The feature associated with this page, [Windows Media Player SDK](/windows/win32/wmp/windows-media-player-sdk), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer). **MediaPlayer** has been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** instead of **Windows Media Player SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

This is a predefined **BUTTON** with the following default values.

``` syntax
onclick="jscript:player.settings.setMode('shuffle',down);"
upToolTip="Turn Shuffle On"
downToolTip="Turn Shuffle Off"
down="wmpprop:player.settings.getMode('shuffle')"
sticky="true"
```

## Remarks

This creates a **BUTTON** control that toggles Shuffle on and off. The ToolTips are localized. All properties of this **BUTTON** can be overridden by explicitly specifying them.

## Requirements



| Requirement | Value |
|--------------------|----------------------------------------------|
| Version<br/> | Windows Media Player 7.0 or later<br/> |



## See also

<dl> <dt>

[**BUTTON Element**](button-element.md)
</dt> </dl>

 

 





