---
title: CUSTOMSLIDER.image
description: The image attribute specifies or retrieves the name of the file containing the images corresponding to the various states of the custom slider.
ms.assetid: 7db4f924-76af-4451-831c-1ed8ab1315ee
keywords:
- CUSTOMSLIDER.image Windows Media Player
topic_type:
- apiref
api_name:
- CUSTOMSLIDER.image
api_type:
- NA
ms.topic: reference
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# CUSTOMSLIDER.image

\[The feature associated with this page, [Windows Media Player SDK](/windows/win32/wmp/windows-media-player-sdk), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer). **MediaPlayer** has been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** instead of **Windows Media Player SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

The **image** attribute specifies or retrieves the name of the file containing the images corresponding to the various states of the custom slider.

``` syntax
        elementID.image
```

## Possible Values

This attribute is a read/write **String** containing the name of an image file.

## Remarks

The **image** attribute is required. It specifies an image file that consists of one or more sub-images, arranged either horizontally or vertically, representing the various states of the custom slider. Each sub-image must have the same dimensions as the **positionImage** or the custom slider will not work correctly. The height or width of the overall image must therefore be an even multiple of the height or width of the **positionImage**.

The supported image file types are BMP, JPG, PNG, and GIF (not including animated GIFs).

## Examples

The following is an example of a custom slider image. The corresponding **positionImage** is shown in the example section of the **positionImage** property.

![sample customslider image](images/dial.png)

The **positionImage** attribute also contains a code sample illustrating how the attributes of the **CUSTOMSLIDER** element are used.

## Requirements



| Requirement | Value |
|--------------------|------------------------------------------------------|
| Version<br/> | Windows Media Player version 7.0 or later<br/> |



## See also

<dl> <dt>

[**CUSTOMSLIDER Element**](customslider-element.md)
</dt> <dt>

[**CUSTOMSLIDER.positionImage**](customslider-positionimage.md)
</dt> </dl>

 

 





