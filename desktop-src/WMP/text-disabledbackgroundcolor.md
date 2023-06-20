---
title: TEXT.disabledBackgroundColor
description: The disabledBackgroundColor attribute specifies or retrieves the background color used for the Text control when it is disabled.
ms.assetid: bc902778-ef3c-4181-9c3b-a8c9d3ef2306
keywords:
- TEXT.disabledBackgroundColor Windows Media Player
topic_type:
- apiref
api_name:
- TEXT.disabledBackgroundColor
api_type:
- NA
ms.topic: reference
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# TEXT.disabledBackgroundColor

\[The feature associated with this page, [Windows Media Player SDK](/windows/win32/wmp/windows-media-player-sdk), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer). **MediaPlayer** has been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** instead of **Windows Media Player SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

The **disabledBackgroundColor** attribute specifies or retrieves the background color used for the Text control when it is disabled.

``` syntax
        elementID.disabledBackgroundColor
```

## Possible Values

This attribute is a read/write **String** containing any Microsoft Internet Explorer color value.

## Remarks

If the **disabledBackgroundColor** is not specified, the **backgroundColor** is used.

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

[**TEXT.backgroundColor**](text-backgroundcolor.md)
</dt> </dl>

 

 





