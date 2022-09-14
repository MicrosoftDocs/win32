---
title: UI_PKEY_ThemeColorsCategoryLabel
description: Identifies the UI\_PKEY\_ThemeColorsCategoryLabel property.
ms.assetid: 704f5c3f-f222-4d98-8a1b-e18a2e094a41
ms.topic: article
ms.date: 05/31/2018
---

# UI\_PKEY\_ThemeColorsCategoryLabel

Identifies the UI\_PKEY\_ThemeColorsCategoryLabel property.

```
propertyDescription
   name = UI_PKEY_ThemeColorsCategoryLabel
   shellPKey = UI_PKEY_ThemeColorsCategoryLabel
   formatID = 00000403-7363-696e-8441798acf5aebb7
   propID = 403
   typeInfo
      type = VT_LPWSTR
```

## Remarks

UI\_PKEY\_ThemeColorsCategoryLabel is used by an application to query the value of the label associated with the **Theme Colors** category of a [**DropDownColorPicker**](windowsribbon-element-dropdowncolorpicker.md).

UI\_PKEY\_ThemeColorsCategoryLabel is valid only for a [**DropDownColorPicker**](windowsribbon-element-dropdowncolorpicker.md) where `ThemeColors` is specified as the value of the **ColorTemplate** attribute (this is the only template that contains labeled categories).

The following screen shot shows a `ThemeColors` [**DropDownColorPicker**](windowsribbon-element-dropdowncolorpicker.md).

![screen shot of the dropdowncolorpicker element with the colortemplate attribute set to themecolors.](images/markup/colortemplate.themedcolors.1.png)

## Related topics

<dl> <dt>

[Color Picker Properties](windowsribbon-reference-properties-colorpicker.md)
</dt> </dl>

 

 




