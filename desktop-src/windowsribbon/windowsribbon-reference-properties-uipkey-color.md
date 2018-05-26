---
title: UI\_PKEY\_Color
description: Identifies the UI\_PKEY\_Color property.
ms.assetid: cf0d1bea-0d31-4136-b077-27f4e40ed301
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# UI\_PKEY\_Color

Identifies the UI\_PKEY\_Color property.

```
propertyDescription
   name = UI_PKEY_Color
   shellPKey = UI_PKEY_Color
   formatID = 00000400-7363-696e-8441798acf5aebb7
   propID = 400
   typeInfo
      type = VT_UI4
```

## Remarks

UI\_PKEY\_Color is used by an application to query the color value of the [**DropDownColorPicker**](windowsribbon-element-dropdowncolorpicker.md) control.

The property value is a [COLORREF](http://go.microsoft.com/fwlink/p/?linkid=133391) value.

The high-order byte of the [COLORREF](http://go.microsoft.com/fwlink/p/?linkid=133391) value is ignored.

## Related topics

<dl> <dt>

[Color Picker Properties](windowsribbon-reference-properties-colorpicker.md)
</dt> </dl>

 

 




