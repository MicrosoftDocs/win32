---
title: LISTBOX.focusItem
description: The focusItem attribute specifies or retrieves the line that contains focus.
ms.assetid: 0d568bc5-6770-4e04-b99f-f535b806f865
keywords:
- LISTBOX.focusItem Windows Media Player
topic_type:
- apiref
api_name:
- LISTBOX.focusItem
api_type:
- NA
ms.topic: reference
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# LISTBOX.focusItem

\[The feature associated with this page, [Windows Media Player SDK](/windows/win32/wmp/windows-media-player-sdk), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer). **MediaPlayer** has been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** instead of **Windows Media Player SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

The **focusItem** attribute specifies or retrieves the line that contains focus.

``` syntax
        elementID.focusItem
```

## Possible Values

This attribute is a read/write **Number** (**long**).

## Remarks

The focus item and selected item could be different. An item can be selected through script, but another item can be given focus through script. The item with focus will have a dotted rectangle around it, and will be selected if the ENTER key is pressed.

## Requirements



| Requirement | Value |
|--------------------|---------------------------------------------------------|
| Version<br/> | Windows Media Player for Windows XP or later<br/> |



## See also

<dl> <dt>

[**LISTBOX Element**](listbox-element.md)
</dt> </dl>

 

 





