---
title: CUSTOMSLIDER.cursor
description: The cursor attribute specifies or retrieves the value of the slider control cursor that appears when the mouse is over the slider.
ms.assetid: 965c21ab-18a0-4459-9d5b-0a35ea2c212f
keywords:
- CUSTOMSLIDER.cursor Windows Media Player
topic_type:
- apiref
api_name:
- CUSTOMSLIDER.cursor
api_type:
- NA
ms.topic: reference
ms.date: 05/31/2018
---

# CUSTOMSLIDER.cursor

The **cursor** attribute specifies or retrieves the value of the slider control cursor that appears when the mouse is over the slider.

``` syntax
        elementID.cursor
```

## Possible Values

This attribute is a read/write **String**.



| Value            | Description                                                                                 |
|------------------|---------------------------------------------------------------------------------------------|
| system           | Platform-dependent cursor (usually an arrow).                                               |
| hand             | Default. Cursor is a hand.                                                                  |
| help             | Arrow with question mark indicating Help is available.                                      |
| sizeall          | Four-pointed arrow pointing north, south, east, and west.                                   |
| sizenesw         | Double-pointed arrow pointing northeast and southwest.                                      |
| sizens           | Double-pointed arrow pointing north and south.                                              |
| sizenwse         | Double-pointed arrow pointing northwest and southeast.                                      |
| sizewe           | Double-pointed arrow pointing west and east.                                                |
| uparrow          | Vertical arrow pointing upward.                                                             |
| \*.ani or \*.cur | Any .ani or .cur file (must be in the same directory as the .wms file or in the .wmz file). |



 

## Requirements



| Requirement | Value |
|--------------------|------------------------------------------------------|
| Version<br/> | Windows Media Player version 7.0 or later<br/> |



## See also

<dl> <dt>

[**CUSTOMSLIDER Element**](customslider-element.md)
</dt> </dl>

 

 





