---
title: VOLUMESLIDER
description: This is a predefined SLIDER with the following default values. | VOLUMESLIDER
ms.assetid: 7533863b-49de-4c1b-8750-fd333c573a17
keywords:
- VOLUMESLIDER Windows Media Player
topic_type:
- apiref
api_name:
- VOLUMESLIDER
api_type:
- NA
ms.topic: reference
ms.date: 05/31/2018
api_location: 
---

# VOLUMESLIDER

This is a predefined SLIDER with the following default values.

``` syntax
toolTip="Volume"
max="100"
min="0"
value="wmpprop:player.settings.volume"
value_onchange="jscript:player.settings.volume=value;
player.settings.mute=false;"
```

## Remarks

This creates a SLIDER control that sets the audio volume. The ToolTips are localized. All properties of this SLIDER can be overridden by explicitly specifying them.

## Requirements



|                    |                                              |
|--------------------|----------------------------------------------|
| Version<br/> | Windows Media Player 7.0 or later<br/> |



## See also

<dl> <dt>

[**SLIDER Element**](slider-element.md)
</dt> </dl>

 

 





