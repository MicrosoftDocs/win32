---
title: VIEW.backgroundColor
description: The backgroundColor attribute specifies or retrieves the background color of the VIEW or SUBVIEW.
ms.assetid: 02804e03-3518-4825-8ad0-bf91f74b5f74
keywords:
- VIEW.backgroundColor Windows Media Player
topic_type:
- apiref
api_name:
- VIEW.backgroundColor
api_type:
- NA
ms.topic: reference
ms.date: 05/31/2018
---

# VIEW.backgroundColor

The **backgroundColor** attribute specifies or retrieves the background color of the **VIEW** or **SUBVIEW**.

``` syntax
        elementID.backgroundColor
```

## Possible Values

This attribute is a read/write **String** containing any Microsoft Internet Explorer color value or the value "none". It has a default value of "white" for **VIEW** elements or "none" for **SUBVIEW** elements.

In a Windows Media Download package, if you specify the backgroundImage attribute for a **VIEW** element, then you must also specify the **backgroundColor** attribute for that element.

## Requirements



| Requirement | Value |
|--------------------|------------------------------------------------------|
| Version<br/> | Windows Media Player version 7.0 or later<br/> |



## See also

<dl> <dt>

[**Color Reference**](color-reference.md)
</dt> <dt>

[**VIEW Element**](view-element.md)
</dt> </dl>

 

 





