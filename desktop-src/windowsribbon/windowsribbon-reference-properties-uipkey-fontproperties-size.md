---
title: UI_PKEY_FontProperties_Size
description: Identifies the UI\_PKEY\_FontProperties\_Size property.
ms.assetid: bd426910-9852-48e1-91c8-b94be5ef7199
ms.topic: article
ms.date: 05/31/2018
---

# UI\_PKEY\_FontProperties\_Size

Identifies the UI\_PKEY\_FontProperties\_Size property.

```
propertyDescription
   name = UI_PKEY_FontProperties_Size
   shellPKey = UI_PKEY_FontProperties_Size
   formatID = 00000302-7363-696e-8441798acf5aebb7
   propID = 302
   typeInfo
      type = VT_DECIMAL
```

## Remarks

UI\_PKEY\_FontProperties\_Size is used by an application to query the value of the **Font size** control.

Valid values for this property range from 1 to 9999, inclusive. If a user tries to enter an invalid value, the entry is rejected and the **Font size** control reverts to the last valid value.

If an application attempts to set font size programmatically to a value outside the valid range, the Ribbon framework invalidates all font properties and sets the font controls (**Font size** and **Font face**) to blank or to their default state, where appropriate.

The default value is 0.

A value of 0 specifies that no single point size is selected (either no text, or a run of heterogeneously sized text, is selected).

A user cannot set the **Font size** control to 0.

Other than 0, valid values for UI\_PKEY\_FontProperties\_Size range between *MinimumFontSize* and *MaximumFontSize* as declared in the [Font Control](windowsribbon-controls-fontcontrol.md) markup.

> [!Note]  
> The **Font size** control is set to blank when the font size is programmatically set to 0, such as when a run of heterogeneously sized text is highlighted.

 

Where a run of heterogeneously sized text is selected, the application should query [UI\_PKEY\_FontProperties\_DeltaSize](windowsribbon-reference-properties-uipkey-fontproperties-deltasize.md) to capture **Grow font** and **Shrink font** commands.

## Related topics

<dl> <dt>

[Font Control Properties](windowsribbon-reference-properties-fontcontrol.md)
</dt> <dt>

[Font Control](windowsribbon-controls-fontcontrol.md)
</dt> </dl>

 

 




