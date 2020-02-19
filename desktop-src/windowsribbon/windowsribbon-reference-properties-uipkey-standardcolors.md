---
title: UI_PKEY_StandardColors
description: Identifies the UI\_PKEY\_StandardColors property.
ms.assetid: fbdce7ba-4417-4f7f-928b-fba6af6eb396
ms.topic: article
ms.date: 05/31/2018
---

# UI\_PKEY\_StandardColors

Identifies the UI\_PKEY\_StandardColors property.

```
propertyDescription
   name = UI_PKEY_StandardColors
   shellPKey = UI_PKEY_StandardColors
   formatID = 00000410-7363-696e-8441798acf5aebb7
   propID = 410
   typeInfo
      type = VT_VECTOR | VT_UI4
```

## Remarks

UI\_PKEY\_StandardColors is used by an application to query the color swatch values of a [**DropDownColorPicker**](windowsribbon-element-dropdowncolorpicker.md).

Each [COLORREF](https://msdn.microsoft.com/library/dd183449(VS.85).aspx) value corresponds to a color swatch in a [**DropDownColorPicker**](windowsribbon-element-dropdowncolorpicker.md) regardless of the value specified for the **ColorTemplate** attribute.

The property value is an array of [COLORREF](https://msdn.microsoft.com/library/dd183449(VS.85).aspx) values.

## Related topics

<dl> <dt>

[Color Picker Properties](windowsribbon-reference-properties-colorpicker.md)
</dt> </dl>

 

 




