---
title: REPEATBUTTON
description: This is a predefined BUTTON with the following default values. | REPEATBUTTON
ms.assetid: 4322ee45-c2b2-4fa0-aa9c-624be5d464ea
keywords:
- REPEATBUTTON Windows Media Player
topic_type:
- apiref
api_name:
- REPEATBUTTON
api_type:
- NA
ms.topic: reference
ms.date: 4/26/2023
api_location: 
ms.custom: UpdateFrequency5
---

# REPEATBUTTON

\[The feature associated with this page, [Windows Media Player SDK](/windows/win32/wmp/windows-media-player-sdk), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer). **MediaPlayer** has been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** instead of **Windows Media Player SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

This is a predefined **BUTTON** with the following default values.

``` syntax
onclick="jscript:player.settings.setMode('loop',down);"
upToolTip="Turn Repeat On"
downToolTip="Turn Repeat Off"
down="wmpprop:player.settings.getMode('loop')"
sticky="true"
```

## Remarks

This creates a **BUTTON** control that toggles Repeat on and off. The ToolTips are localized. All properties of this **BUTTON** can be overridden by explicitly specifying them.

## Requirements



| Requirement | Value |
|--------------------|----------------------------------------------|
| Version<br/> | Windows Media Player 7.0 or later<br/> |



## See also

<dl> <dt>

[**BUTTON Element**](button-element.md)
</dt> </dl>

 

 





