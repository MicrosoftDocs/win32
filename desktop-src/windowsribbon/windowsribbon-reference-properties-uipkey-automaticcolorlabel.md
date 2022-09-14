---
title: UI_PKEY_AutomaticColorLabel
description: Identifies the UI\_PKEY\_AutomaticColorLabel property.
ms.assetid: 736259f1-b536-40a5-bce7-98602a0ab041
ms.topic: article
ms.date: 05/31/2018
---

# UI\_PKEY\_AutomaticColorLabel

Identifies the UI\_PKEY\_AutomaticColorLabel property.

```
propertyDescription
   name = UI_PKEY_AutomaticColorLabel
   shellPKey = UI_PKEY_AutomaticColorLabel
   formatID = 00000406-7363-696e-8441798acf5aebb7
   propID = 406
   typeInfo
      type = VT_LPWSTR
```

## Remarks

UI\_PKEY\_AutomaticColorLabel is used by an application to query the value of the label associated with the **Automatic** button of a [**DropDownColorPicker**](windowsribbon-element-dropdowncolorpicker.md). This button is used by the application to specify a default color as required.

UI\_PKEY\_AutomaticColorLabel is only valid for a [**DropDownColorPicker**](windowsribbon-element-dropdowncolorpicker.md) where `ThemeColors` or `StandardColors` is specified as the value of the **ColorTemplate** attribute.

## Related topics

<dl> <dt>

[Color Picker Properties](windowsribbon-reference-properties-colorpicker.md)
</dt> </dl>

 

 




