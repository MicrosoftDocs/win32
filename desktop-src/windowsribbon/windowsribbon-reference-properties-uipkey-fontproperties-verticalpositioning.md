---
title: UI_PKEY_FontProperties_VerticalPositioning
description: Identifies the UI\_PKEY\_FontProperties\_VerticalPositioning property.
ms.assetid: a92f845e-b0fc-4e23-9d06-ca16d2becf0b
ms.topic: article
ms.date: 05/31/2018
---

# UI\_PKEY\_FontProperties\_VerticalPositioning

Identifies the UI\_PKEY\_FontProperties\_VerticalPositioning property.

```
propertyDescription
   name = UI_PKEY_FontProperties_VerticalPositioning
   shellPKey = UI_PKEY_FontProperties_VerticalPositioning
   formatID = 00000307-7363-696e-8441798acf5aebb7
   propID = 307
   typeInfo
      type = UI_FONTVERTICALPOSITION
```

## Remarks

UI\_PKEY\_FontProperties\_VerticalPositioning is used by an application to query the value of the **Superscript** and **Subscript** controls.

The property value is from the [**UI\_FONTVERTICALPOSITION**](/windows/desktop/api/uiribbon/ne-uiribbon-ui_fontverticalposition) enumeration.

The default value is `UI_FONTVERTICALPOSITION_NOTSET`.

The following screen shot shows the **Superscript** and **Subscript** buttons of the Ribbon [**FontControl**](windowsribbon-element-fontcontrol.md).

![screen shot of the fontcontrol element with the richfont attribute set to true.](images/markup/fontcontrol-subsuper.png)

The following table describes the properties and the UI result.



|     Property                           |          UI Result                                                                             |
|----------------------------------------|------------------------------------------------------------------------------------------------|
| `UI_FONTVERTICALPOSITION_NOTAVAILABLE` | **Superscript** and **Subscript** buttons are disabled and can only be set by the application. |
| `UI_FONTVERTICALPOSITION_NOTSET`       | **Superscript** and **Subscript** buttons are not selected.                                    |
| `UI_FONTVERTICALPOSITION_SUPERSCRIPT`  | **Superscript** button is selected.                                                            |
| `UI_FONTVERTICALPOSITION_SUBSCRIPT`    | **Subscript** button is selected.                                                              |



 

> [!Note]  
> The **Superscript** and **Subscript** buttons cannot both be selected.

 

## Related topics

<dl> <dt>

[Font Control Properties](windowsribbon-reference-properties-fontcontrol.md)
</dt> <dt>

[**UI\_FONTVERTICALPOSITION**](/windows/desktop/api/uiribbon/ne-uiribbon-ui_fontverticalposition)
</dt> <dt>

[Font Control](windowsribbon-controls-fontcontrol.md)
</dt> </dl>

 

 