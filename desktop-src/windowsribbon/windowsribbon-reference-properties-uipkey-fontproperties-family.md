---
title: UI_PKEY_FontProperties_Family
description: Identifies the UI\_PKEY\_FontProperties\_Family property.
ms.assetid: 95064588-9c14-401f-a86e-7b11e86faaf9
ms.topic: article
ms.date: 05/31/2018
---

# UI\_PKEY\_FontProperties\_Family

Identifies the UI\_PKEY\_FontProperties\_Family property.

```
propertyDescription
   name = UI_PKEY_FontProperties_Family
   shellPKey = UI_PKEY_FontProperties_Family
   formatID = 00000301-7363-696e-8441798acf5aebb7
   propID = 301
   typeInfo
      type = VT_LPWSTR
```

## Remarks

UI\_PKEY\_FontProperties\_Family is used by an application to query the value of the **Font family** drop-down gallery.

The value of UI\_PKEY\_FontProperties\_Family matches a [Windows GDI Font Families](../gdi/font-families.md) name retrieved with the [EnumFontFamilies function](/windows/win32/api/wingdi/nf-wingdi-enumfontfamiliesa) or [EnumFontFamiliesEx function](/windows/win32/api/wingdi/nf-wingdi-enumfontfamiliesexa).

The default value is an empty string.

If an empty string is supplied for the value for UI\_PKEY\_FontProperties\_Family, then the font selection is cleared.

## Related topics

<dl> <dt>

[Font Control Properties](windowsribbon-reference-properties-fontcontrol.md)
</dt> <dt>

[Font Control](windowsribbon-controls-fontcontrol.md)
</dt> </dl>

 

 