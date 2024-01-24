---
title: ITEMSPLAYLIST
description: This is a predefined PLAYLIST element with the following default values. | ITEMSPLAYLIST
ms.assetid: 0621885c-04e3-4de7-a4cc-2eb4e94de53c
keywords:
- ITEMSPLAYLIST Windows Media Player
topic_type:
- apiref
api_name:
- ITEMSPLAYLIST
api_type:
- NA
ms.topic: reference
ms.date: 4/26/2023
api_location: 
ms.custom: UpdateFrequency5
---

# ITEMSPLAYLIST

\[The feature associated with this page, [Windows Media Player SDK](/windows/win32/wmp/windows-media-player-sdk), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer). **MediaPlayer** has been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** instead of **Windows Media Player SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

This is a predefined **PLAYLIST** element with the following default values.

``` syntax
backgroundColor="black"
columns="name=Name;Duration=Time"
columnsVisible="false"
dropDownVisible="false"
foregroundColor="white"
```

## Remarks

This will create a simple **PLAYLIST** that displays the items in a playlist with no drop-down or column headers visible. All properties of this **PLAYLIST** can be overridden by explicitly specifying them.

## Requirements



| Requirement | Value |
|--------------------|----------------------------------------------|
| Version<br/> | Windows Media Player 7.0 or later<br/> |



## See also

<dl> <dt>

[**PLAYLIST Element**](playlist-element.md)
</dt> </dl>

 

 





