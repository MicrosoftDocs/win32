---
title: BUTTONGROUP.transparencyColor
description: The transparencyColor attribute specifies or retrieves the transparent color of the BUTTONGROUP images.
ms.assetid: 604c5b29-50b9-4df6-9e48-488bf4fb7227
keywords:
- BUTTONGROUP.transparencyColor Windows Media Player
topic_type:
- apiref
api_name:
- BUTTONGROUP.transparencyColor
api_type:
- NA
ms.topic: reference
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# BUTTONGROUP.transparencyColor

\[The feature associated with this page, [Windows Media Player SDK](/windows/win32/wmp/windows-media-player-sdk), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer). **MediaPlayer** has been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** instead of **Windows Media Player SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

The **transparencyColor** attribute specifies or retrieves the transparent color of the **BUTTONGROUP** images.

``` syntax
        elementID.transparencyColor
```

## Possible Values

This attribute is a read/write **String** with no default, containing one of the following values.



| Value                                       | Description                                                                                        |
|---------------------------------------------|----------------------------------------------------------------------------------------------------|
| Auto                                        | The pixel at location 0,0 in the image becomes the transparent color.                              |
| any Microsoft Internet Explorer color value | An Internet Explorer color value becomes the transparent color (for example, "red" or "\#FF0000"). |
| None                                        | Default. No transparency.                                                                          |



 

## Remarks

A transparent color in an image will allow whatever is behind the image to show through the areas of transparency. The transparent region is clickable unless clipped by the **clippingImage** tag.

The color can be any Microsoft Internet Explorer color value. If the value is Auto, then the color of the pixel at location 0,0 in the image is used.

If the color specified is not one of the valid Internet Explorer colors, a warning is returned and the previous value is maintained.

Because JPGs are lossy and therefore subject to unexpected color change, they are not recommended when **transparencyColor** is used.

## Requirements



| Requirement | Value |
|--------------------|------------------------------------------------------|
| Version<br/> | Windows Media Player version 7.0 or later<br/> |



## See also

<dl> <dt>

[**BUTTONGROUP Element**](buttongroup-element.md)
</dt> <dt>

[**Color Reference**](color-reference.md)
</dt> </dl>

 

 





