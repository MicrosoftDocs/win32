---
title: VIDEO.toolTip
description: The toolTip attribute specifies or retrieves the ToolTip text for the video window.
ms.assetid: 84e382b4-01b2-4be7-9768-7773a3f1300f
keywords:
- VIDEO.toolTip Windows Media Player
topic_type:
- apiref
api_name:
- VIDEO.toolTip
api_type:
- NA
ms.topic: reference
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# VIDEO.toolTip

\[The feature associated with this page, [Windows Media Player SDK](/windows/win32/wmp/windows-media-player-sdk), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer). **MediaPlayer** has been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** instead of **Windows Media Player SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

The **toolTip** attribute specifies or retrieves the ToolTip text for the video window.

``` syntax
        elementID.toolTip
```

## Possible Values

This attribute is a read/write **String**, which must not exceed 1024 characters in length. It has no default value.

## Remarks

When this attribute is set to "" (empty string), no ToolTip is displayed.

## Requirements



| Requirement | Value |
|--------------------|------------------------------------------------------|
| Version<br/> | Windows Media Player version 7.0 or later<br/> |



## See also

<dl> <dt>

[**VIDEO Element**](video-element.md)
</dt> </dl>

 

 





