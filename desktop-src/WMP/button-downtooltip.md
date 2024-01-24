---
title: BUTTON.downToolTip
description: The downToolTip attribute specifies or retrieves the ToolTip text that appears when the mouse is over the BUTTON and the BUTTON is in the down state.
ms.assetid: 53a13aaf-34c8-4730-98b7-c9c3a4b64721
keywords:
- BUTTON.downToolTip Windows Media Player
topic_type:
- apiref
api_name:
- BUTTON.downToolTip
api_type:
- NA
ms.topic: reference
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# BUTTON.downToolTip

\[The feature associated with this page, [Windows Media Player SDK](/windows/win32/wmp/windows-media-player-sdk), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer). **MediaPlayer** has been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** instead of **Windows Media Player SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

The **downToolTip** attribute specifies or retrieves the ToolTip text that appears when the mouse is over the **BUTTON** and the **BUTTON** is in the down state.

``` syntax
        elementID.downToolTip
```

## Possible Values

This attribute is a read/write **String** with a default value of "" (empty string) and a maximum length of 1024 characters.

## Remarks

When this attribute is set to "" (empty string), no ToolTip is displayed.

## Requirements



| Requirement | Value |
|--------------------|------------------------------------------------------|
| Version<br/> | Windows Media Player version 7.0 or later<br/> |



## See also

<dl> <dt>

[**BUTTON Element**](button-element.md)
</dt> <dt>

[**BUTTON.down**](button-down.md)
</dt> </dl>

 

 





