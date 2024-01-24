---
title: TEXT.fontFace
description: The fontFace attribute specifies or retrieves the typeface for the Text control.
ms.assetid: 3b39e245-139a-4361-b678-0f9e962996b7
keywords:
- TEXT.fontFace Windows Media Player
topic_type:
- apiref
api_name:
- TEXT.fontFace
api_type:
- NA
ms.topic: reference
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# TEXT.fontFace

\[The feature associated with this page, [Windows Media Player SDK](/windows/win32/wmp/windows-media-player-sdk), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer). **MediaPlayer** has been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** instead of **Windows Media Player SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

The **fontFace** attribute specifies or retrieves the typeface for the Text control.

``` syntax
        elementID.fontFace
```

## Possible Values

This attribute is a read/write **String**.

## Remarks

This attribute can be the name of any valid font available on Windows. Windows Media Player will not support installing fonts, so choose a font that you know will be on the intended system.

If the **fontFace** specified is not available on the user's system, the Text control defaults to the Windows system font.

See the [value](text-value.md) attribute for a sample illustrating how the attributes of the **TEXT** element are used.

## Requirements



| Requirement | Value |
|--------------------|------------------------------------------------------|
| Version<br/> | Windows Media Player version 7.0 or later<br/> |



## See also

<dl> <dt>

[**TEXT Element**](text-element.md)
</dt> <dt>

[**TEXT.fontSize**](text-fontsize.md)
</dt> </dl>

 

 





