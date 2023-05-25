---
title: BUTTONELEMENT.upToolTip
description: The upToolTip attribute specifies or retrieves the ToolTip text that appears when the mouse is over the BUTTONELEMENT and the BUTTONELEMENT is in the up state.
ms.assetid: ca9334df-8054-481d-966c-58c84d734adf
keywords:
- BUTTONELEMENT.upToolTip Windows Media Player
topic_type:
- apiref
api_name:
- BUTTONELEMENT.upToolTip
api_type:
- NA
ms.topic: reference
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# BUTTONELEMENT.upToolTip

\[The feature associated with this page, [Windows Media Player SDK](/windows/win32/wmp/windows-media-player-sdk), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer). **MediaPlayer** has been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** instead of **Windows Media Player SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

The **upToolTip** attribute specifies or retrieves the ToolTip text that appears when the mouse is over the **BUTTONELEMENT** and the **BUTTONELEMENT** is in the up state.

``` syntax
        elementID.upToolTip
```

## Possible Values

This attribute is a read/write **String** with a default value of "" (empty string) with a maximum length of 1024 characters.

## Remarks

When this attribute is set to "" (empty string), no ToolTip is displayed.

## Examples

See the [mappingColor](buttonelement-mappingcolor.md) attribute for a sample illustrating the use of this attribute.

## Requirements



| Requirement | Value |
|--------------------|------------------------------------------------------|
| Version<br/> | Windows Media Player version 7.0 or later<br/> |



## See also

<dl> <dt>

[**BUTTONELEMENT Element**](buttonelement-element.md)
</dt> </dl>

 

 





