---
title: AmbientAttributes.width
description: The width attribute specifies or retrieves the width of the control.
ms.assetid: f246958a-563c-40c0-8a74-4511103b95b2
keywords:
- AmbientAttributes.width Windows Media Player
topic_type:
- apiref
api_name:
- AmbientAttributes.width
api_type:
- NA
ms.topic: reference
ms.date: 05/31/2018
---

# AmbientAttributes.width

The **width** attribute specifies or retrieves the width of the control.

``` syntax
        elementID.width
```

## Possible Values

This attribute is a read/write 16-bit **Integer** (0 to 32,767) representing the width of the control in pixels. The default value is zero or the width of the image specified in the control's **image** attribute.

## Remarks

If the width specified is narrower than the width of the image provided, then the image will be clipped. If the width is wider than the width of the image, then the click region will go beyond the image boundary. No matter what value is given to this attribute, the image cannot grow beyond its parent **VIEW** or **SUBVIEW**.

## Requirements



| Requirement | Value |
|--------------------|------------------------------------------------------|
| Version<br/> | Windows Media Player version 7.0 or later<br/> |



## See also

<dl> <dt>

[**Ambient Attributes**](ambient-attributes.md)
</dt> </dl>

 

 





