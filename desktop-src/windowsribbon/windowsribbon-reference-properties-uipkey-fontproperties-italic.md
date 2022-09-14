---
title: UI_PKEY_FontProperties_Italic
description: Identifies the UI\_PKEY\_FontProperties\_Italic property.
ms.assetid: 53edd88e-ed7e-4385-9fd9-bfa90be348cd
ms.topic: article
ms.date: 05/31/2018
---

# UI\_PKEY\_FontProperties\_Italic

Identifies the UI\_PKEY\_FontProperties\_Italic property.

```
propertyDescription
   name = UI_PKEY_FontProperties_Italic
   shellPKey = UI_PKEY_FontProperties_Italic
   formatID = 00000304-7363-696e-8441798acf5aebb7
   propID = 304
   typeInfo
      type = UI_FONTPROPERTIES
```

## Remarks

UI\_PKEY\_FontProperties\_Italic is used by an application to query the state of the **Italic** button.

The property value is from the [**UI\_FONTPROPERTIES**](/windows/desktop/api/uiribbon/ne-uiribbon-ui_fontproperties) enumeration.

The default value is `UI_FONTPROPERTIES_NOTSET`.

The following table describes the properties and the UI result.



|    Property                      |       UI Result                                                       |
|----------------------------------|-----------------------------------------------------------------------|
| `UI_FONTPROPERTIES_NOTAVAILABLE` | **Italic** button is disabled and can only be set by the application. |
| `UI_FONTPROPERTIES_NOTSET`       | **Italic** button is not selected.                                    |
| `UI_FONTPROPERTIES_SET`          | **Italic** button is selected.                                        |



 

## Related topics

<dl> <dt>

[Font Control Properties](windowsribbon-reference-properties-fontcontrol.md)
</dt> <dt>

[**UI\_FONTPROPERTIES**](/windows/desktop/api/uiribbon/ne-uiribbon-ui_fontproperties)
</dt> <dt>

[Font Control](windowsribbon-controls-fontcontrol.md)
</dt> </dl>

 

 