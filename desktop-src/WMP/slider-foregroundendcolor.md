---
title: SLIDER.foregroundEndColor
description: The foregroundEndColor attribute specifies or retrieves the foreground ending color of the slider control.
ms.assetid: a13dbd62-dda3-40e9-9700-1e53c9fc26aa
keywords:
- SLIDER.foregroundEndColor Windows Media Player
topic_type:
- apiref
api_name:
- SLIDER.foregroundEndColor
api_type:
- NA
ms.topic: reference
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# SLIDER.foregroundEndColor

\[The feature associated with this page, [Windows Media Player SDK](/windows/win32/wmp/windows-media-player-sdk), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer). **MediaPlayer** has been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** instead of **Windows Media Player SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

The **foregroundEndColor** attribute specifies or retrieves the foreground ending color of the slider control.

``` syntax
        elementID.foregroundEndColor
```

## Possible Values

This attribute is a read/write **String** containing any Microsoft Internet Explorer color value. It has no default value.

## Remarks

The **foregroundEndColor** is used in conjunction with a **foregroundColor**. The effect created is a gradient fade from the **foregroundColor** to the **foregroundEndColor**.

## Requirements



| Requirement | Value |
|--------------------|------------------------------------------------------|
| Version<br/> | Windows Media Player version 7.0 or later<br/> |



## See also

<dl> <dt>

[**Color Reference**](color-reference.md)
</dt> <dt>

[**SLIDER Element**](slider-element.md)
</dt> <dt>

[**SLIDER.foregroundColor**](slider-foregroundcolor.md)
</dt> </dl>

 

 





