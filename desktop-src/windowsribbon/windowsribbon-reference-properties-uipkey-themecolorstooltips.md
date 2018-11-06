---
title: UI_PKEY_ThemeColorsTooltips
description: Identifies the UI\_PKEY\_ThemeColorsTooltips property.
ms.assetid: 69b23ea7-fdce-4894-94a8-d77d087872a3
ms.topic: article
ms.date: 05/31/2018
---

# UI\_PKEY\_ThemeColorsTooltips

Identifies the UI\_PKEY\_ThemeColorsTooltips property.

```
propertyDescription
   name = UI_PKEY_ThemeColorsTooltips
   shellPKey = UI_PKEY_ThemeColorsTooltips
   formatID = 00000411-7363-696e-8441798acf5aebb7
   propID = 411
   typeInfo
      type = VT_VECTOR | VT_LPWSTR
```

## Remarks

UI\_PKEY\_ThemeColorsTooltips is used by an application to query the color swatch tooltips of a [**DropDownColorPicker**](windowsribbon-element-dropdowncolorpicker.md).

The property value is an array of string values.

Each string value corresponds to the tooltip for a color swatch in a [**DropDownColorPicker**](windowsribbon-element-dropdowncolorpicker.md) where `ThemeColors` is specified as the value of the **ColorTemplate** attribute.

## Related topics

<dl> <dt>

[Color Picker Properties](windowsribbon-reference-properties-colorpicker.md)
</dt> </dl>

 

 




