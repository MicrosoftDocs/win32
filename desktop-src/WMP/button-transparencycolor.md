---
title: BUTTON.transparencyColor
description: The transparencyColor attribute specifies or retrieves the color that will be transparent in the BUTTON images.
ms.assetid: c22f9965-3118-4c96-8ff5-7fbaa28cbb57
keywords:
- BUTTON.transparencyColor Windows Media Player
topic_type:
- apiref
api_name:
- BUTTON.transparencyColor
api_type:
- NA
ms.topic: reference
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# BUTTON.transparencyColor

\[The feature associated with this page, [Windows Media Player SDK](/windows/win32/wmp/windows-media-player-sdk), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer). **MediaPlayer** has been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** instead of **Windows Media Player SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

The **transparencyColor** attribute specifies or retrieves the color that will be transparent in the **BUTTON** images.

``` syntax
        elementID.transparencyColor
```

## Possible Values

This attribute is a read/write **String** with no default containing one of the following values.



| Value                                    | Description                                                                                               |
|------------------------------------------|-----------------------------------------------------------------------------------------------------------|
| Auto                                     | The color of the pixel at location 0,0 in the image becomes the transparent color.                        |
| Any Internet Explorer color format value | An Internet Explorer color format value becomes the transparent color (for example, "red" or "\#FF0000"). |
| None                                     | No transparency.                                                                                          |



 

## Remarks

A transparent color in an image allows whatever is behind the image to show through the transparent areas. The **BUTTON** will still receive clicks on the transparent region.

The transparent color can be any Internet Explorer color value. If the value of the **transparencyColor** attribute is set to "Auto", the color of the pixel at location 0,0 in the image is used.

If the color specified is not one of the valid IE colors, the previous value is maintained.

Because JPGs are lossy and therefore subject to unexpected color change, they are not recommended when **transparencyColor** is used.

## Requirements



| Requirement | Value |
|--------------------|------------------------------------------------------|
| Version<br/> | Windows Media Player version 7.0 or later<br/> |



## See also

<dl> <dt>

[**BUTTON Element**](button-element.md)
</dt> <dt>

[**BUTTON.image**](button-image.md)
</dt> <dt>

[**Color Reference**](color-reference.md)
</dt> </dl>

 

 





