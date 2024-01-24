---
title: PLAYLIST.allowItemEditing
description: The allowItemEditing attribute specifies or retrieves a value indicating whether items in a playlist will support in-place editing.
ms.assetid: fc6120d9-0424-4c42-8aa9-ba4bbbd580fe
keywords:
- PLAYLIST.allowItemEditing Windows Media Player
topic_type:
- apiref
api_name:
- PLAYLIST.allowItemEditing
api_type:
- NA
ms.topic: reference
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# PLAYLIST.allowItemEditing

\[The feature associated with this page, [Windows Media Player SDK](/windows/win32/wmp/windows-media-player-sdk), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer). **MediaPlayer** has been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** instead of **Windows Media Player SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

The **allowItemEditing** attribute specifies or retrieves a value indicating whether items in a playlist will support in-place editing.

``` syntax
        elementID.allowItemEditing
```

## Possible Values

This attribute is a read/write **Boolean**.



| Value | Description                           |
|-------|---------------------------------------|
| true  | Default. In-place editing is allowed. |
| false | In-place editing is not allowed.      |



 

## Requirements



| Requirement | Value |
|--------------------|------------------------------------------------------|
| Version<br/> | Windows Media Player version 7.0 or later<br/> |



## See also

<dl> <dt>

[**PLAYLIST Element**](playlist-element.md)
</dt> </dl>

 

 





