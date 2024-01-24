---
title: SLIDER.disabledColor
description: The disabledColor attribute specifies or retrieves the color of the slider control when it is disabled.
ms.assetid: 47b9f5c6-12ea-4654-a9c0-d15d41ea2766
keywords:
- SLIDER.disabledColor Windows Media Player
topic_type:
- apiref
api_name:
- SLIDER.disabledColor
api_type:
- NA
ms.topic: reference
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# SLIDER.disabledColor

\[The feature associated with this page, [Windows Media Player SDK](/windows/win32/wmp/windows-media-player-sdk), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer). **MediaPlayer** has been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** instead of **Windows Media Player SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

The **disabledColor** attribute specifies or retrieves the color of the slider control when it is disabled.

``` syntax
        elementID.disabledColor
```

## Possible Values

This attribute is a read/write **String** containing any Microsoft Internet Explorer color value. It has no default value.

## Remarks

When the slider control is specified using foreground and background colors, the disabled color specifies the color of the control when **enabled** is set to false.

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

[**AmbientAttributes.enabled**](ambientattributes-enabled.md)
</dt> </dl>

 

 





