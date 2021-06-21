---
title: UI_PKEY_FontProperties_Strikethrough
description: Identifies the UI\_PKEY\_FontProperties\_Strikethrough property.
ms.assetid: 18ee653d-db01-4615-a85d-ad4ac6a0f422
ms.topic: article
ms.date: 05/31/2018
---

# UI\_PKEY\_FontProperties\_Strikethrough

Identifies the UI\_PKEY\_FontProperties\_Strikethrough property.

```
propertyDescription
   name = UI_PKEY_FontProperties_Strikethrough
   shellPKey = UI_PKEY_FontProperties_Strikethrough
   formatID = 00000306-7363-696e-8441798acf5aebb7
   propID = 306
   typeInfo
      type = UI_FONTPROPERTIES
```

## Remarks

UI\_PKEY\_FontProperties\_Strikethrough is used by an application to query the state of the **Strikethrough** button.

The property value is from the [**UI\_FONTPROPERTIES**](/windows/desktop/api/uiribbon/ne-uiribbon-ui_fontproperties) enumeration.

The default value is `UI_FONTPROPERTIES_NOTSET`.

The following screen shot shows the **Strikethrough** button of the Ribbon [**FontControl**](windowsribbon-element-fontcontrol.md).

![screen shot of the fontcontrol element with the richfont attribute set to true.](images/markup/fontcontrol-strikethrough.png)

The following table describes the properties and the UI result.



|   Property                       |    UI Result                                                                 |
|----------------------------------|------------------------------------------------------------------------------|
| `UI_FONTPROPERTIES_NOTAVAILABLE` | **Strikethrough** button is disabled and can only be set by the application. |
| `UI_FONTPROPERTIES_NOTSET`       | **Strikethrough** button is not selected.                                    |
| `UI_FONTPROPERTIES_SET`          | **Strikethrough** button is selected.                                        |



 

## Related topics

<dl> <dt>

[Font Control Properties](windowsribbon-reference-properties-fontcontrol.md)
</dt> <dt>

[**UI\_FONTPROPERTIES**](/windows/desktop/api/uiribbon/ne-uiribbon-ui_fontproperties)
</dt> <dt>

[Font Control](windowsribbon-controls-fontcontrol.md)
</dt> </dl>

 

 