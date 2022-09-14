---
title: UI_PKEY_StandardColorsTooltips
description: Identifies the UI\_PKEY\_StandardColorsTooltips property.
ms.assetid: 78786f72-69d3-44f6-bef4-51d0f4497dfb
ms.topic: article
ms.date: 05/31/2018
---

# UI\_PKEY\_StandardColorsTooltips

Identifies the UI\_PKEY\_StandardColorsTooltips property.

```
propertyDescription
   name = UI_PKEY_StandardColorsTooltips
   shellPKey = UI_PKEY_StandardColorsTooltips
   formatID = 00000412-7363-696e-8441798acf5aebb7
   propID = 412
   typeInfo
      type = VT_VECTOR | VT_LPWSTR
```

## Remarks

UI\_PKEY\_StandardColorsTooltips is used by an application to query the color swatch tooltips of a [**DropDownColorPicker**](windowsribbon-element-dropdowncolorpicker.md).

The property value is an array of string values.

Each string value corresponds to the tooltip for a color swatch in a [**DropDownColorPicker**](windowsribbon-element-dropdowncolorpicker.md) regardless of the value specified for the **ColorTemplate** attribute.

## Related topics

<dl> <dt>

[Color Picker Properties](windowsribbon-reference-properties-colorpicker.md)
</dt> </dl>

 

 




