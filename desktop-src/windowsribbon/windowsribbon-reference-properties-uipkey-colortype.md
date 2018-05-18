---
title: UI\_PKEY\_ColorType
description: Identifies the UI\_PKEY\_ColorType property.
ms.assetid: '7eaa9d8b-0c21-487c-9093-79ddffcae131'
---

# UI\_PKEY\_ColorType

Identifies the UI\_PKEY\_ColorType property.

```
propertyDescription
   name = UI_PKEY_ColorType
   shellPKey = UI_PKEY_ColorType
   formatID = 00000401-7363-696e-8441798acf5aebb7
   propID = 401
   typeInfo
      type = UI_SWATCHCOLORTYPE
```

## Remarks

UI\_PKEY\_ColorType is used by an application to query color setting of the [**DropDownColorPicker**](windowsribbon-element-dropdowncolorpicker.md) control.

The property value is from the [**UI\_SWATCHCOLORTYPE**](https://msdn.microsoft.com/library/windows/desktop/dd371583) enumeration.



|                                |                                                                                                                                                                                 |
|--------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| UI\_SWATCHCOLORTYPE\_NOCOLOR   | Application should treat the color setting as transparent. Typically used in conjunction with the **No color** color setting.                                                   |
| UI\_SWATCHCOLORTYPE\_AUTOMATIC | Application should query [GetSysColor(COLOR\_WINDOWTEXT)](http://go.microsoft.com/fwlink/p/?linkid=143871). Typically used in conjunction with the **Automatic** color setting. |
| UI\_SWATCHCOLORTYPE\_RGB       | Application should query [UI\_PKEY\_Color](windowsribbon-reference-properties-uipkey-color.md) for the color setting.                                                          |



 

UI\_PKEY\_ColorType is passed to the [**IUICommandHandler::Execute**](https://msdn.microsoft.com/library/windows/desktop/dd371489) callback method when a color swatch is selected in a [**DropDownColorPicker**](windowsribbon-element-dropdowncolorpicker.md).

## Related topics

<dl> <dt>

[Color Picker Properties](windowsribbon-reference-properties-colorpicker.md)
</dt> </dl>

 

 




