---
title: VIEW.transparencyColor
description: The transparencyColor attribute specifies or retrieves the transparency color of the background image.
ms.assetid: f9351df1-d502-4a96-9250-13b805c115c8
keywords:
- VIEW.transparencyColor Windows Media Player
topic_type:
- apiref
api_name:
- VIEW.transparencyColor
api_type:
- NA
ms.topic: reference
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# VIEW.transparencyColor

\[The feature associated with this page, [Windows Media Player SDK](/windows/win32/wmp/windows-media-player-sdk), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer). **MediaPlayer** has been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** instead of **Windows Media Player SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

The **transparencyColor** attribute specifies or retrieves the transparency color of the background image.

``` syntax
        elementID.transparencyColor
```

## Possible Values

This attribute is a read/write **String** containing any Microsoft Internet Explorer color value. It has no default value.

Because JPGs are lossy and therefore subject to unexpected color change, they are not recommended when **transparencyColor** is used.

## Requirements



| Requirement | Value |
|--------------------|------------------------------------------------------|
| Version<br/> | Windows Media Player version 7.0 or later<br/> |



## See also

<dl> <dt>

[**VIEW Element**](view-element.md)
</dt> <dt>

[**Color Reference**](color-reference.md)
</dt> </dl>

 

 





