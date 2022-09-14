---
title: UI_PKEY_FontProperties_Bold
description: Identifies the UI\_PKEY\_FontProperties\_Bold property.
ms.assetid: 9d33142a-bd63-423e-ba77-083c86bce1e7
ms.topic: article
ms.date: 05/31/2018
---

# UI\_PKEY\_FontProperties\_Bold

Identifies the UI\_PKEY\_FontProperties\_Bold property.

```
propertyDescription
   name = UI_PKEY_FontProperties_Bold
   shellPKey = UI_PKEY_FontProperties_Bold
   formatID = 00000303-7363-696e-8441798acf5aebb7
   propID = 303
   typeInfo
      type = UI_FONTPROPERTIES
```

## Remarks

UI\_PKEY\_FontProperties\_Bold is used by an application to query the state of the **Bold** button.

The property value is from the [**UI\_FONTPROPERTIES**](/windows/desktop/api/uiribbon/ne-uiribbon-ui_fontproperties) enumeration.

The default value is `UI_FONTPROPERTIES_NOTSET`.

The following table describes the properties and the UI result.



|      Property                    |    UI Result                                                        |
|----------------------------------|---------------------------------------------------------------------|
| `UI_FONTPROPERTIES_NOTAVAILABLE` | **Bold** button is disabled and can only be set by the application. |
| `UI_FONTPROPERTIES_NOTSET`       | **Bold** button is not selected.                                    |
| `UI_FONTPROPERTIES_SET`          | **Bold** button is selected.                                        |



 

## Related topics

<dl> <dt>

[Font Control Properties](windowsribbon-reference-properties-fontcontrol.md)
</dt> <dt>

[**UI\_FONTPROPERTIES**](/windows/desktop/api/uiribbon/ne-uiribbon-ui_fontproperties)
</dt> <dt>

[Font Control](windowsribbon-controls-fontcontrol.md)
</dt> </dl>

 

 