---
title: SLIDER.direction
description: The direction attribute specifies or retrieves the direction that slider images are laid out.
ms.assetid: a6add56b-3fc6-4c78-90e4-6daafd701eda
keywords:
- SLIDER.direction Windows Media Player
topic_type:
- apiref
api_name:
- SLIDER.direction
api_type:
- NA
ms.topic: reference
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# SLIDER.direction

\[The feature associated with this page, [Windows Media Player SDK](/windows/win32/wmp/windows-media-player-sdk), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer). **MediaPlayer** has been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** instead of **Windows Media Player SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

The **direction** attribute specifies or retrieves the direction that slider images are laid out.

``` syntax
        elementID.direction
```

## Possible Values

This attribute is a read/write **String**.



| Value      | Description                                                                             |
|------------|-----------------------------------------------------------------------------------------|
| horizontal | Default. The minimum position is at the left, and the maximum position is at the right. |
| vertical   | The minimum position is at the bottom, and the maximum position is at the top.          |



 

## Remarks

The fill or movement of the **foregroundColor** or **foregroundImage** is along the vertical or horizontal axis according to the specified value.

## Requirements



| Requirement | Value |
|--------------------|------------------------------------------------------|
| Version<br/> | Windows Media Player version 7.0 or later<br/> |



## See also

<dl> <dt>

[**SLIDER Element**](slider-element.md)
</dt> <dt>

[**SLIDER.foregroundColor**](slider-foregroundcolor.md)
</dt> <dt>

[**SLIDER.foregroundImage**](slider-foregroundimage.md)
</dt> </dl>

 

 





