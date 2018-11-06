---
title: UI_PKEY_StandardColorsCategoryLabel
description: Identifies the UI\_PKEY\_StandardColorsCategoryLabel property.
ms.assetid: 59452d4b-acc9-4a5f-a06c-a67b0e676a57
ms.topic: article
ms.date: 05/31/2018
---

# UI\_PKEY\_StandardColorsCategoryLabel

Identifies the UI\_PKEY\_StandardColorsCategoryLabel property.

```
propertyDescription
   name = UI_PKEY_StandardColorsCategoryLabel
   shellPKey = UI_PKEY_StandardColorsCategoryLabel
   formatID = 00000404-7363-696e-8441798acf5aebb7
   propID = 404
   typeInfo
      type = VT_LPWSTR
```

## Remarks

UI\_PKEY\_StandardColorsCategoryLabel is used by an application to query the value of the label associated with the **Standard Colors** category of a [**DropDownColorPicker**](windowsribbon-element-dropdowncolorpicker.md).

UI\_PKEY\_StandardColorsCategoryLabel is valid only for a [**DropDownColorPicker**](windowsribbon-element-dropdowncolorpicker.md) where `ThemeColors` is specified as the value of the **ColorTemplate** attribute (this is the only template that contains labeled categories).

The following screen shot shows a `ThemeColors` [**DropDownColorPicker**](windowsribbon-element-dropdowncolorpicker.md).

![screen shot of the dropdowncolorpicker element with the colortemplate attribute set to themecolors.](images/markup/colortemplate.themedcolors.1.png)

## Related topics

<dl> <dt>

[Color Picker Properties](windowsribbon-reference-properties-colorpicker.md)
</dt> </dl>

 

 




