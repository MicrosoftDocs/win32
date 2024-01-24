---
title: AmbientAttributes.nineGridMargins
description: The nineGridMargins attribute specifies margin widths for non-uniform scaling of the skin element.
ms.assetid: b8a7efd0-6c12-4436-9d53-0dcfa1600aa5
keywords:
- AmbientAttributes.nineGridMargins Windows Media Player
topic_type:
- apiref
api_name:
- AmbientAttributes.nineGridMargins
api_type:
- NA
ms.topic: reference
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# AmbientAttributes.nineGridMargins

\[The feature associated with this page, [Windows Media Player SDK](/windows/win32/wmp/windows-media-player-sdk), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer). **MediaPlayer** has been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** instead of **Windows Media Player SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

The **nineGridMargins** attribute specifies margin widths for non-uniform scaling of the skin element.

``` syntax
        elementID.nineGridMargins
```

## Possible Values

This attribute is a read/write **String** that contains the widths of the margins in the form "*widthLeft*,*widthTop*,*widthRight*,*widthBottom*". Each width value is a number representing the width, in pixels, of a margin for the nine grid.

## Remarks

A *nine grid* is a technique used to divide user interface elements into nine rectangular regions arranged in a 3 by 3 matrix. When an element is resized, the nine grid regions can each scale by a different factor.

Each of the four width values you specify represents the width of a row or column of three adjacent regions. Each row or column forms the left side, top, right side, or bottom of the nine grid.

[AmbientAttributes.resizeImages](ambientattributes-resizeimages.md) must be set to true for this attribute to work.

## Requirements



| Requirement | Value |
|--------------------|------------------------------------|
| Version<br/> | Windows Media Player 11<br/> |



## See also

<dl> <dt>

[**Ambient Attributes**](ambient-attributes.md)
</dt> </dl>

 

 





