---
title: CUSTOMSLIDER.transparencyColor
description: The transparencyColor attribute specifies or retrieves the transparency color of the custom slider images.
ms.assetid: 39bdac82-7c84-4c79-b3f0-ec4828263ccd
keywords:
- CUSTOMSLIDER.transparencyColor Windows Media Player
topic_type:
- apiref
api_name:
- CUSTOMSLIDER.transparencyColor
api_type:
- NA
ms.topic: reference
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# CUSTOMSLIDER.transparencyColor

\[The feature associated with this page, [Windows Media Player SDK](/windows/win32/wmp/windows-media-player-sdk), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer). **MediaPlayer** has been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** instead of **Windows Media Player SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

The **transparencyColor** attribute specifies or retrieves the transparency color of the custom slider images.

``` syntax
        elementID.transparencyColor
```

## Possible Values

This attribute is a read/write **String** containing any Microsoft Internet Explorer color value. It has no default value.

## Remarks

Any part of the custom slider images containing the **transparencyColor** will allow the background to show through.

Because JPGs are lossy and therefore subject to unexpected color change, they are not recommended when **transparencyColor** is used.

## Examples

See the [positionImage](customslider-positionimage.md) attribute for a sample illustrating how the attributes of the **CUSTOMSLIDER** element are used.

## Requirements



| Requirement | Value |
|--------------------|------------------------------------------------------|
| Version<br/> | Windows Media Player version 7.0 or later<br/> |



## See also

<dl> <dt>

[**Color Reference**](color-reference.md)
</dt> <dt>

[**CUSTOMSLIDER Element**](customslider-element.md)
</dt> </dl>

 

 





