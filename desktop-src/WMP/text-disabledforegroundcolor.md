---
title: TEXT.disabledForegroundColor
description: The disabledForegroundColor attribute specifies or retrieves the text color used for the Text control when it is disabled.
ms.assetid: 0ac2dc0c-817f-4902-b03b-072dbda45c3d
keywords:
- TEXT.disabledForegroundColor Windows Media Player
topic_type:
- apiref
api_name:
- TEXT.disabledForegroundColor
api_type:
- NA
ms.topic: reference
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# TEXT.disabledForegroundColor

\[The feature associated with this page, [Windows Media Player SDK](/windows/win32/wmp/windows-media-player-sdk), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer). **MediaPlayer** has been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** instead of **Windows Media Player SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

The **disabledForegroundColor** attribute specifies or retrieves the text color used for the Text control when it is disabled.

``` syntax
        elementID.disabledForegroundColor
```

## Possible Values

This attribute is a read/write **String** containing any Microsoft Internet Explorer color value.

## Remarks

If **disabledForegroundColor** is not specified, **foregroundColor** is used.

See the [value](text-value.md) attribute for a sample illustrating how the attributes of the **TEXT** element are used.

## Requirements



| Requirement | Value |
|--------------------|------------------------------------------------------|
| Version<br/> | Windows Media Player version 7.0 or later<br/> |



## See also

<dl> <dt>

[**Color Reference**](color-reference.md)
</dt> <dt>

[**TEXT Element**](text-element.md)
</dt> <dt>

[**TEXT.foregroundColor**](text-foregroundcolor.md)
</dt> </dl>

 

 





