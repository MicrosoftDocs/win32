---
title: BUTTONGROUP.saturation
description: The saturation attribute specifies or retrieves the saturation value of the BUTTONGROUP images.
ms.assetid: bfd957f0-8201-4a4f-9162-a397ed97c747
keywords:
- BUTTONGROUP.saturation Windows Media Player
topic_type:
- apiref
api_name:
- BUTTONGROUP.saturation
api_type:
- NA
ms.topic: reference
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# BUTTONGROUP.saturation

\[The feature associated with this page, [Windows Media Player SDK](/windows/win32/wmp/windows-media-player-sdk), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer). **MediaPlayer** has been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** instead of **Windows Media Player SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

The **saturation** attribute specifies or retrieves the saturation value of the **BUTTONGROUP** images.

``` syntax
        elementID.saturation
```

## Possible Values

This attribute is a read/write **Number** (**float**) with a value ranging from 0.0 to 2.0 with a default value of 1.0.

## Remarks

This attribute changes the saturation value of the images specified by the **disabledImage**, **downImage**, **hoverDownImage**, **hoverImage**, and **image** attributes if they have been specified and they refer to 8-bit BMP images.

## Requirements



| Requirement | Value |
|--------------------|---------------------------------------------------|
| Version<br/> | Windows Media Player 9 Series or later<br/> |



## See also

<dl> <dt>

[**BUTTONGROUP Element**](buttongroup-element.md)
</dt> <dt>

[**BUTTONGROUP.disabledImage**](buttongroup-disabledimage.md)
</dt> <dt>

[**BUTTONGROUP.downImage**](buttongroup-downimage.md)
</dt> <dt>

[**BUTTONGROUP.hoverDownImage**](buttongroup-hoverdownimage.md)
</dt> <dt>

[**BUTTONGROUP.hoverImage**](buttongroup-hoverimage.md)
</dt> <dt>

[**BUTTONGROUP.hueShift**](buttongroup-hueshift.md)
</dt> <dt>

[**BUTTONGROUP.image**](buttongroup-image.md)
</dt> </dl>

 

 





