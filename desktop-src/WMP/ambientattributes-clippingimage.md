---
title: AmbientAttributes.clippingImage
description: The clippingImage attribute specifies or retrieves the region to clip the control to.
ms.assetid: e4b51d31-f9c7-4398-983d-95867a2cab45
keywords:
- AmbientAttributes.clippingImage Windows Media Player
topic_type:
- apiref
api_name:
- AmbientAttributes.clippingImage
api_type:
- NA
ms.topic: reference
ms.date: 05/31/2018
---

# AmbientAttributes.clippingImage

The **clippingImage** attribute specifies or retrieves the region to clip the control to.

``` syntax
        elementID.clippingImage
```

## Possible Values

This attribute is a read/write **String** indicating the image file name. It has no default value.

## Remarks

The **clippingImage** attribute supports PNG, JPG, BMP, and GIF files (not including animated GIFs). Because JPGs are lossy and therefore subject to unexpected color change, they are not recommended for clipping images.

This attribute is useful when you want to display only a part of the control image and not the entire rectangular area. The **clippingColor** attribute indicates the regions of the clipping image that correspond to transparent, non-clickable portions of the control. The control can therefore be of any shape. For best results, the clipping image should be the same size as the control image.

The **clippingImage** attribute is not supported by the **PLAYLIST**, **VIEW**, and **SUBVIEW** elements. A clipping image will not work with the **VIDEO** element if *VIDEO*.**windowless** is set to false, nor with the **EFFECTS** element if *EFFECTS*.**windowed** is set to true.

Because the use of clipping images imposes a performance penalty, they should not be used when efficiency is an issue.

## Examples

See the [BUTTONELEMENT.mappingColor](buttonelement-mappingcolor.md) attribute for a sample illustrating the use of this attribute.

## Requirements



| Requirement | Value |
|--------------------|------------------------------------------------------|
| Version<br/> | Windows Media Player version 7.0 or later<br/> |



## See also

<dl> <dt>

[**Ambient Attributes**](ambient-attributes.md)
</dt> <dt>

[**AmbientAttributes.clippingColor**](ambientattributes-clippingcolor.md)
</dt> </dl>

 

 





