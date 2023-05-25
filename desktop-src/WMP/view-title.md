---
title: VIEW.title
description: The title attribute specifies or retrieves the title of the VIEW.
ms.assetid: c23a2880-cb20-4a0f-9ce6-3fa3aec7f8ff
keywords:
- VIEW.title Windows Media Player
topic_type:
- apiref
api_name:
- VIEW.title
api_type:
- NA
ms.topic: reference
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# VIEW.title

\[The feature associated with this page, [Windows Media Player SDK](/windows/win32/wmp/windows-media-player-sdk), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer). **MediaPlayer** has been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** instead of **Windows Media Player SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

The **title** attribute specifies or retrieves the title of the **VIEW**.

``` syntax
        elementID.title
```

## Possible Values

This attribute is a **String** specified at design time and read-only thereafter. It can be up to 255 characters long and has no default value.

## Remarks

The title specified or retrieved is the display name for the theme.

## Requirements



| Requirement | Value |
|--------------------|------------------------------------------------------|
| Version<br/> | Windows Media Player version 7.0 or later<br/> |



## See also

<dl> <dt>

[**VIEW Element**](view-element.md)
</dt> <dt>

[**VIEW.titleBar**](view-titlebar.md)
</dt> </dl>

 

 





