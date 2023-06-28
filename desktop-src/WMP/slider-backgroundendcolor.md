---
title: SLIDER.backgroundEndColor
description: The backgroundEndColor attribute specifies or retrieves the background ending color of the slider control.
ms.assetid: 6406bb81-d5a7-4da1-abc3-51da1ff00a46
keywords:
- SLIDER.backgroundEndColor Windows Media Player
topic_type:
- apiref
api_name:
- SLIDER.backgroundEndColor
api_type:
- NA
ms.topic: reference
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# SLIDER.backgroundEndColor

\[The feature associated with this page, [Windows Media Player SDK](/windows/win32/wmp/windows-media-player-sdk), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer). **MediaPlayer** has been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** instead of **Windows Media Player SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

The **backgroundEndColor** attribute specifies or retrieves the background ending color of the slider control.

``` syntax
        elementID.backgroundEndColor
```

## Possible Values

This attribute is a read/write **String** containing any Microsoft Internet Explorer color value. It has no default value.

## Remarks

The **backgroundEndColor** is used in conjunction with a **backgroundColor**. The effect created is a gradient fade from the **backgroundColor** to the **backgroundEndColor**.

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

[**SLIDER.backgroundColor**](slider-backgroundcolor.md)
</dt> </dl>

 

 





