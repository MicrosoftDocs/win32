---
title: TEXT.hoverForegroundColor
description: The hoverForegroundColor attribute specifies or retrieves the text color used for the Text control when the mouse cursor hovers over it.
ms.assetid: 6d956ea3-8395-416f-ad22-a70b7beaf9c4
keywords:
- TEXT.hoverForegroundColor Windows Media Player
topic_type:
- apiref
api_name:
- TEXT.hoverForegroundColor
api_type:
- NA
ms.topic: reference
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# TEXT.hoverForegroundColor

\[The feature associated with this page, [Windows Media Player SDK](/windows/win32/wmp/windows-media-player-sdk), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer). **MediaPlayer** has been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** instead of **Windows Media Player SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

The **hoverForegroundColor** attribute specifies or retrieves the text color used for the Text control when the mouse cursor hovers over it.

``` syntax
        elementID.hoverForegroundColor
```

## Possible Values

This attribute is a read/write **String** containing any Microsoft Internet Explorer color value.

## Remarks

If **hoverForegroundColor** is not specified, **foregroundColor** is used.

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

 

 





