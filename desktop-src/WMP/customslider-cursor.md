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
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# CUSTOMSLIDER.cursor

\[The feature associated with this page, [Windows Media Player SDK](/windows/win32/wmp/windows-media-player-sdk), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer). **MediaPlayer** has been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** instead of **Windows Media Player SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

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

 

 





