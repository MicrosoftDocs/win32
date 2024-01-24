---
title: VIEW.backgroundTiled
description: The backgroundTiled attribute specifies or retrieves a value indicating whether the background image of the VIEW or SUBVIEW is tiled.
ms.assetid: 5eeb89cd-6dc4-4399-b894-82531d8bc04d
keywords:
- VIEW.backgroundTiled Windows Media Player
topic_type:
- apiref
api_name:
- VIEW.backgroundTiled
api_type:
- NA
ms.topic: reference
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# VIEW.backgroundTiled

\[The feature associated with this page, [Windows Media Player SDK](/windows/win32/wmp/windows-media-player-sdk), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer). **MediaPlayer** has been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** instead of **Windows Media Player SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

The **backgroundTiled** attribute specifies or retrieves a value indicating whether the background image of the **VIEW** or **SUBVIEW** is tiled.

``` syntax
        elementID.backgroundTiled
```

## Possible Values

This attribute is a read/write **Boolean**.



| Value | Description                                        |
|-------|----------------------------------------------------|
| true  | The image is repeated horizontally and vertically. |
| false | Default. The image is not repeated.                |



 

## Requirements



| Requirement | Value |
|--------------------|------------------------------------------------------|
| Version<br/> | Windows Media Player version 7.0 or later<br/> |



## See also

<dl> <dt>

[**VIEW Element**](view-element.md)
</dt> </dl>

 

 





