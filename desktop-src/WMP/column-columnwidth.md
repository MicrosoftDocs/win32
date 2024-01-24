---
title: COLUMN.columnWidth
description: The columnWidth attribute specifies or retrieves a column width in the PLAYLIST control.
ms.assetid: 4c6fabf9-fca0-433a-87bd-17f5d74a0a74
keywords:
- COLUMN.columnWidth Windows Media Player
topic_type:
- apiref
api_name:
- COLUMN.columnWidth
api_type:
- NA
ms.topic: reference
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# COLUMN.columnWidth

\[The feature associated with this page, [Windows Media Player SDK](/windows/win32/wmp/windows-media-player-sdk), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer). **MediaPlayer** has been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** instead of **Windows Media Player SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

The **columnWidth** attribute specifies or retrieves a column width in the **PLAYLIST** control.

``` syntax
        elementID.columnWidth
```

## Possible Values

This attribute is a read/write **Number** (**long**) representing the width of the column in pixels.

## Remarks

The **columnResizeMode** property must be set to "fixed" for this property to work.

## Requirements



| Requirement | Value |
|--------------------|---------------------------------------------------|
| Version<br/> | Windows Media Player 9 Series or later<br/> |



## See also

<dl> <dt>

[**COLUMN Element**](column-element.md)
</dt> </dl>

 

 





