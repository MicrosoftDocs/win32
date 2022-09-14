---
title: UI_PKEY_ThemeColors
description: Identifies the UI\_PKEY\_ThemeColors property.
ms.assetid: d539cbaa-45dc-4f9e-830e-e81fb289b4ac
ms.topic: article
ms.date: 05/31/2018
---

# UI\_PKEY\_ThemeColors

Identifies the UI\_PKEY\_ThemeColors property.

```
propertyDescription
   name = UI_PKEY_ThemeColors
   shellPKey = UI_PKEY_ThemeColors
   formatID = 00000409-7363-696e-8441798acf5aebb7
   propID = 409
   typeInfo
      type = VT_VECTOR | VT_UI4
```

## Remarks

UI\_PKEY\_ThemeColors is used by an application to query the color swatch values of a [**DropDownColorPicker**](windowsribbon-element-dropdowncolorpicker.md).

Each [COLORREF](../gdi/colorref.md) value corresponds to a color swatch in a [**DropDownColorPicker**](windowsribbon-element-dropdowncolorpicker.md) where `ThemeColors` is specified as the value of the **ColorTemplate** attribute.

The property value is an array of [COLORREF](../gdi/colorref.md) values.

## Related topics

<dl> <dt>

[Color Picker Properties](windowsribbon-reference-properties-colorpicker.md)
</dt> </dl>

 

 