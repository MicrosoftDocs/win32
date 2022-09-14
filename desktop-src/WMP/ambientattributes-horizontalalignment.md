---
title: AmbientAttributes.horizontalAlignment
description: The horizontalAlignment attribute specifies or retrieves a value that indicates the horizontal placement of the control when the VIEW or parent SUBVIEW is resized.
ms.assetid: 97ca23b9-2046-45ee-b2da-ea388e7ab8d8
keywords:
- AmbientAttributes.horizontalAlignment Windows Media Player
topic_type:
- apiref
api_name:
- AmbientAttributes.horizontalAlignment
api_type:
- NA
ms.topic: reference
ms.date: 05/31/2018
---

# AmbientAttributes.horizontalAlignment

The **horizontalAlignment** attribute specifies or retrieves a value that indicates the horizontal placement of the control when the **VIEW** or parent **SUBVIEW** is resized.

``` syntax
        elementID.horizontalAlignment
```

## Possible Values

This attribute is a read/write **String**.



| Value   | Description                                                                                                                                                                                                                                                                                                                                                        |
|---------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| left    | Default. Maintains the placement of the control relative to the left of the **VIEW** or parent **SUBVIEW** when the view is resized.                                                                                                                                                                                                                               |
| right   | Maintains the placement of the control relative to the right of the **VIEW** or parent **SUBVIEW** when the view is resized.                                                                                                                                                                                                                                       |
| center  | Maintains the placement of the control relative to the horizontal center of the **VIEW** or parent **SUBVIEW** when the view is resized.                                                                                                                                                                                                                           |
| stretch | Maintains the placement of the control relative to both the left and right margins of the **VIEW** or parent **SUBVIEW** when resized. The control stretches to fit when the **VIEW** or **SUBVIEW** is stretched. The actual image does not grow or shrink unless it is resizable, but the clickable area grows or shrinks if not bounded by a **clippingImage**. |



 

## Remarks

Unless **horizontalAlignment** is set to "center", the control retains its original distance from the specified edge, or from both edges if "stretch" is specified and the control is resizable. If the control is not resizable and "stretch" is specified, the clickable region is stretched instead.

You can set any combination of **horizontalAlignment** and **verticalAlignment**. For example, if you want to center a control both horizontally and vertically, set horizontalAlignment="center" verticalAlignment="center".

## Requirements



| Requirement | Value |
|--------------------|------------------------------------------------------|
| Version<br/> | Windows Media Player version 7.0 or later<br/> |



## See also

<dl> <dt>

[**Ambient Attributes**](ambient-attributes.md)
</dt> <dt>

[**AmbientAttributes.verticalAlignment**](ambientattributes-verticalalignment.md)
</dt> <dt>

[**AmbientAttributes.clippingImage**](ambientattributes-clippingimage.md)
</dt> </dl>

 

 





