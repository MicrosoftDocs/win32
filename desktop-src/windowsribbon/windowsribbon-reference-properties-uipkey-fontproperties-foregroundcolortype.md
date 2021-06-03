---
title: UI_PKEY_FontProperties_ForegroundColorType
description: Identifies the UI\_PKEY\_FontProperties\_ForegroundColorType property.
ms.assetid: ab04c0b0-911f-4649-9ce8-5ecd847abf9f
ms.topic: article
ms.date: 05/31/2018
---

# UI\_PKEY\_FontProperties\_ForegroundColorType

Identifies the UI\_PKEY\_FontProperties\_ForegroundColorType property.

```
propertyDescription
   name = UI_PKEY_FontProperties_ForegroundColorType
   shellPKey = UI_PKEY_FontProperties_ForegroundColorType
   formatID = 00000310-7363-696e-8441798acf5aebb7
   propID = 310
   typeInfo
      type = UI_SWATCHCOLORTYPE
```

## Remarks

UI\_PKEY\_FontProperties\_ForegroundColorType is used by an application, in conjunction with [UI\_PKEY\_FontProperties\_ForegroundColor](windowsribbon-reference-properties-uipkey-fontproperties-foregroundcolor.md), to query **Text color** gallery settings.

The property value is from the [**UI\_SWATCHCOLORTYPE**](/windows/desktop/api/uiribbon/ne-uiribbon-ui_swatchcolortype) enumeration.

The default value is `UI_SWATCHCOLORTYPE_RGB`.

The following table describes the property values.



|     Value                           |     Description                                                                                                                                                                                                                                                                                                                                                                                                                  |
|--------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `UI_SWATCHCOLORTYPE_NOCOLOR`   | Not supported by the [**FontControl**](windowsribbon-element-fontcontrol.md).                                                                                                                                                                                                                                                                                                                                        |
| `UI_SWATCHCOLORTYPE_AUTOMATIC` | Application should query the appropriate system metric for the color value typically the current Windows theme **text color** that is retrieved with GetSysColor(COLOR\_WINDOWTEXT).                                                                                                                                                                                                                                  |
| `UI_SWATCHCOLORTYPE_RGB`       | Application should query [UI\_PKEY\_FontProperties\_ForegroundColor](windowsribbon-reference-properties-uipkey-fontproperties-foregroundcolor.md) for the color value. The color value of [UI\_PKEY\_FontProperties\_ForegroundColor](windowsribbon-reference-properties-uipkey-fontproperties-foregroundcolor.md) is displayed on the **Text color** button and selected in the **Text color** gallery.<br/> |



 

UI\_PKEY\_FontProperties\_ForegroundColorType is passed to the [**IUICommandHandler::Execute**](/windows/desktop/api/uiribbon/nf-uiribbon-iuicommandhandler-execute) callback method when a color swatch is selected in a [**FontControl**](windowsribbon-element-fontcontrol.md) **Text color** gallery.

> [!Note]  
> It is highly recommended that the application only set an initial **Text color** value and not re-set this value when the cursor is repositioned within a document. The last selection should be maintained to avoid the need to re-select the desired color.

 

## Related topics

<dl> <dt>

[Font Control Properties](windowsribbon-reference-properties-fontcontrol.md)
</dt> <dt>

[**UI\_SWATCHCOLORTYPE**](/windows/desktop/api/uiribbon/ne-uiribbon-ui_swatchcolortype)
</dt> <dt>

[Font Control](windowsribbon-controls-fontcontrol.md)
</dt> </dl>

 

