---
title: AmbientAttributes.verticalAlignment
description: The verticalAlignment attribute specifies or retrieves a value indicating the vertical placement of the control when the VIEW or parent SUBVIEW is stretched.
ms.assetid: 08ef483a-58ee-4a35-9973-2567076d07f7
keywords:
- AmbientAttributes.verticalAlignment Windows Media Player
topic_type:
- apiref
api_name:
- AmbientAttributes.verticalAlignment
api_type:
- NA
ms.topic: reference
ms.date: 05/31/2018
---

# AmbientAttributes.verticalAlignment

The **verticalAlignment** attribute specifies or retrieves a value indicating the vertical placement of the control when the **VIEW** or parent **SUBVIEW** is stretched.

``` syntax
        elementID.verticalAlignment
```

## Possible Values

This attribute is a read/write **String**.



| Value   | Description                                                                                                                                                                                                                                                                                                                                     |
|---------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| top     | Default. Maintains the placement of the control relative to the top of the **VIEW** or parent **SUBVIEW** when the view is resized.                                                                                                                                                                                                             |
| bottom  | Maintains the placement of the control relative to the bottom of the **VIEW** or parent **SUBVIEW** when the view is resized.                                                                                                                                                                                                                   |
| center  | Maintains the placement of the control relative to the vertical center of the **VIEW** or parent **SUBVIEW** when the view is resized.                                                                                                                                                                                                          |
| stretch | Maintains the placement of the control relative to both the top and bottom margins of the View when resized. The control stretches to fit when the **VIEW** or parent **SUBVIEW** is stretched. The actual image does not grow or shrink unless it is resizable, but the clickable area grows or shrinks if not bounded by a **clippingImage**. |



 

## Remarks

Unless **verticalAlignment** is set to "center", the control retains its original distance from the specified edge, or from both edges if "stretch" is specified and the control is resizable. If the control is not resizable and "stretch" is specified, the clickable region is stretched instead.

You can set any combination of the **horizontalAlignment** and **verticalAlignment** attributes. For example, if you want a control to be centered both horizontally and vertically, set **horizontalAlignment** to "center" and **verticalAlignment** to "center".

## Requirements



| Requirement | Value |
|--------------------|------------------------------------------------------|
| Version<br/> | Windows Media Player version 7.0 or later<br/> |



## See also

<dl> <dt>

[**Ambient Attributes**](ambient-attributes.md)
</dt> <dt>

[**AmbientAttributes.horizontalAlignment**](ambientattributes-horizontalalignment.md)
</dt> </dl>

 

 





