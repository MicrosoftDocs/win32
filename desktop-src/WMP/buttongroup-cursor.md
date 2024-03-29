---
title: BUTTONGROUP.cursor
description: The cursor attribute specifies or retrieves the type of cursor that appears when the mouse is over a button in the BUTTONGROUP.
ms.assetid: c1b7e3e1-862b-48c1-bd2d-d9abd9ada14c
keywords:
- BUTTONGROUP.cursor Windows Media Player
topic_type:
- apiref
api_name:
- BUTTONGROUP.cursor
api_type:
- NA
ms.topic: reference
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# BUTTONGROUP.cursor

\[The feature associated with this page, [Windows Media Player SDK](/windows/win32/wmp/windows-media-player-sdk), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer). **MediaPlayer** has been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** instead of **Windows Media Player SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

The **cursor** attribute specifies or retrieves the type of cursor that appears when the mouse is over a button in the **BUTTONGROUP**.

``` syntax
        elementID.cursor
```

## Possible Values

This attribute is a read/write **String** containing one of the following values.



| Value            | Description                                                                                 |
|------------------|---------------------------------------------------------------------------------------------|
| system           | Default. Platform-dependent cursor (usually an arrow).                                      |
| hand             | Hand.                                                                                       |
| help             | Arrow with question mark indicating Help is available.                                      |
| sizeall          | Four-pointed arrow pointing north, south, east, and west.                                   |
| sizenesw         | Double-pointed arrow pointing northeast and southwest.                                      |
| sizens           | Double-pointed arrow pointing north and south.                                              |
| sizenwse         | Double-pointed arrow pointing northwest and southeast.                                      |
| sizewe           | Double-pointed arrow pointing west and east.                                                |
| uparrow          | Vertical arrow pointing upward.                                                             |
| \*.ani or \*.cur | Any .ani or .cur file (must be in the same directory as the .wms file or in the .wmz file). |



 

## Remarks

The cursor specified applies to all buttons in the **BUTTONGROUP**.

If you specify an invalid cursor value, it remains at the previously set value.

Cursor file name paths are ignored, so the cursor file must reside in the default directory.

## Requirements



| Requirement | Value |
|--------------------|------------------------------------------------------|
| Version<br/> | Windows Media Player version 7.0 or later<br/> |



## See also

<dl> <dt>

[**BUTTONGROUP Element**](buttongroup-element.md)
</dt> </dl>

 

 





