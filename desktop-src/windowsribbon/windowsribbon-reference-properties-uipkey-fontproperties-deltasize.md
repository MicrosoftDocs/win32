---
title: UI_PKEY_FontProperties_DeltaSize
description: Identifies the UI\_PKEY\_FontProperties\_DeltaSize property.
ms.assetid: 021a6c79-1d3e-47d2-9601-cdaa2e66a50a
ms.topic: article
ms.date: 05/31/2018
---

# UI\_PKEY\_FontProperties\_DeltaSize

Identifies the UI\_PKEY\_FontProperties\_DeltaSize property.

```
propertyDescription
   name = UI_PKEY_FontProperties_DeltaSize
   shellPKey = UI_PKEY_FontProperties_DeltaSize
   formatID = 00000309-7363-696e-8441798acf5aebb7
   propID = 313
   typeInfo
      type = UI_FONTDELTASIZE
```

## Remarks

UI\_PKEY\_FontProperties\_DeltaSize is used by an application in cases where it is not possible for the application to specify a value for **Font size**, such as when a run of heterogeneously sized text is selected. The **Font size** control is set to blank and UI\_PKEY\_FontProperties\_DeltaSize is used to capture user interaction with the **Font grow** and **Font shrink** buttons.

UI\_PKEY\_FontProperties\_DeltaSize is included in [UI\_PKEY\_FontProperties\_ChangedProperties](windowsribbon-reference-properties-uipkey-fontproperties-changedproperties.md).

The following screen shot shows the **Font grow** and **Font shrink** buttons of the Ribbon [**FontControl**](windowsribbon-element-fontcontrol.md).

![screen shot of the font grow and font shrink buttons on the fontcontrol.](images/markup/fontcontrol-incdec.png)

The following table describes the property values.



|     Value                 |  Description                    |
|---------------------------|---------------------------------|
| `UI_FONTDELTASIZE_GROW`   | **Grow font** button clicked.   |
| `UI_FONTDELTASIZE_SHRINK` | **Shrink font** button clicked. |



 

## Related topics

<dl> <dt>

[Font Control Properties](windowsribbon-reference-properties-fontcontrol.md)
</dt> <dt>

[**UI\_FONTDELTASIZE**](/windows/desktop/api/uiribbon/ne-uiribbon-ui_fontdeltasize)
</dt> <dt>

[Font Control](windowsribbon-controls-fontcontrol.md)
</dt> </dl>

 

 