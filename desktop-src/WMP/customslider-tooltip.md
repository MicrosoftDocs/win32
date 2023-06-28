---
title: CUSTOMSLIDER.toolTip
description: The toolTip attribute specifies or retrieves the ToolTip text for the slider.
ms.assetid: ac82b811-8396-4a02-b617-627e808b8faf
keywords:
- CUSTOMSLIDER.toolTip Windows Media Player
topic_type:
- apiref
api_name:
- CUSTOMSLIDER.toolTip
api_type:
- NA
ms.topic: reference
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# CUSTOMSLIDER.toolTip

\[The feature associated with this page, [Windows Media Player SDK](/windows/win32/wmp/windows-media-player-sdk), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer). **MediaPlayer** has been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** instead of **Windows Media Player SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

The **toolTip** attribute specifies or retrieves the ToolTip text for the slider.

``` syntax
        elementID.toolTip
```

## Possible Values

This attribute is a read/write **String** with a maximum length of 1024 characters. It has no default value.

## Remarks

When this attribute is set to "" (empty string), no ToolTip is displayed.

## Examples

See the [positionImage](customslider-positionimage.md) attribute for a sample illustrating how the attributes of the **CUSTOMSLIDER** element are used.

## Requirements



| Requirement | Value |
|--------------------|------------------------------------------------------|
| Version<br/> | Windows Media Player version 7.0 or later<br/> |



## See also

<dl> <dt>

[**CUSTOMSLIDER Element**](customslider-element.md)
</dt> </dl>

 

 





