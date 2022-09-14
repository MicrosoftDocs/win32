---
title: WMPEFFECTS
description: This is a predefined EFFECTS with the following default values.
ms.assetid: 'ebee17e3-96b0-4748-b69f-4ff41d0bc386'
keywords:
- WMPEFFECTS Windows Media Player
topic_type:
- apiref
api_name:
- WMPEFFECTS
api_type:
- NA
ms.topic: reference
ms.date: 05/31/2018
api_location: 
---

# WMPEFFECTS

This is a predefined **EFFECTS** with the following default values.

``` syntax
horizontalAlignment="stretch"
verticalAlignment="stretch"
height="200"
width="250"
tabStop="false"
onclick="next();"
```

## Remarks

This will create an **EFFECTS** element that will step through the visualization presets when the user clicks the control. It will also stretch the visualizations when the player is resized.

The initial visualization preset shown is the one selected on the **View** menu under **Visualizations**. Changing the selection on this menu will automatically change the preset displayed by this element when the Player is in skin mode. The **View** menu is displayed in the full mode of the Player or when the **VIEW.titleBar** attribute is set to true in a skin.

All properties of this **EFFECTS** element can be overridden by explicitly specifying them.

## Requirements



| Requirement | Value |
|--------------------|----------------------------------------------|
| Version<br/> | Windows Media Player 7.0 or later<br/> |



## See also

<dl> <dt>

[**EFFECTS Element**](effects-element.md)
</dt> </dl>

 

 





