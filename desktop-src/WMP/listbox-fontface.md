---
title: LISTBOX.fontFace
description: The fontFace attribute specifies or retrieves the font for the list box control.
ms.assetid: 15e3180a-6e1e-4654-a0bb-164d66a86a26
keywords:
- LISTBOX.fontFace Windows Media Player
topic_type:
- apiref
api_name:
- LISTBOX.fontFace
api_type:
- NA
ms.topic: reference
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# LISTBOX.fontFace

\[The feature associated with this page, [Windows Media Player SDK](/windows/win32/wmp/windows-media-player-sdk), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer). **MediaPlayer** has been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** instead of **Windows Media Player SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

The **fontFace** attribute specifies or retrieves the font for the list box control.

``` syntax
        elementID.fontFace
```

## Possible Values

This attribute is a read/write **String**.

## Remarks

This attribute can be the name of any valid font available in Windows. Windows Media Player will not support installing fonts, so choose a font that you know will be on the intended system.

If the **fontFace** specified is not available on the user's system, the list box control defaults to the Windows system font. The default value for English-language systems is "Tahoma". For international systems, the default is loaded from a resource file.

## Requirements



| Requirement | Value |
|--------------------|---------------------------------------------------------|
| Version<br/> | Windows Media Player for Windows XP or later<br/> |



## See also

<dl> <dt>

[**LISTBOX Element**](listbox-element.md)
</dt> <dt>

[**LISTBOX.fontSize**](listbox-fontsize.md)
</dt> <dt>

[**LISTBOX.fontStyle**](listbox-fontstyle.md)
</dt> </dl>

 

 





