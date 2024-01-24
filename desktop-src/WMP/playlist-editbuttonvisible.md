---
title: PLAYLIST.editButtonVisible
description: The editButtonVisible attribute specifies or retrieves a value indicating whether the Playlist edit button is visible.
ms.assetid: 716e5484-b4b0-49a6-a778-ead1479fda54
keywords:
- PLAYLIST.editButtonVisible Windows Media Player
topic_type:
- apiref
api_name:
- PLAYLIST.editButtonVisible
api_type:
- NA
ms.topic: reference
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# PLAYLIST.editButtonVisible

\[The feature associated with this page, [Windows Media Player SDK](/windows/win32/wmp/windows-media-player-sdk), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer). **MediaPlayer** has been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** instead of **Windows Media Player SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

The **editButtonVisible** attribute specifies or retrieves a value indicating whether the Playlist edit button is visible.

``` syntax
        elementID.editButtonVisible
```

## Possible Values

This attribute is a read/write **Boolean**.



| Value | Description                                       |
|-------|---------------------------------------------------|
| true  | The playlist edit button is visible.              |
| false | Default. The playlist edit button is not visible. |



 

## Remarks

When you set this attribute to true, the playlist edit button will appear in the lower-left corner of the **PLAYLIST** element. Clicking this button displays a menu of options allowing the user to edit, clear, sort, open, save, or copy a playlist.

## Requirements



| Requirement | Value |
|--------------------|---------------------------------------------------|
| Version<br/> | Windows Media Player 9 Series or later<br/> |



## See also

<dl> <dt>

[**PLAYLIST Element**](playlist-element.md)
</dt> </dl>

 

 





