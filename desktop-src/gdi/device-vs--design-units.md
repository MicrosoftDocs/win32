---
description: An application can retrieve font metrics for a physical font only after the font has been selected into a device context.
ms.assetid: 3eaabc8b-e244-4b65-918b-a20043afa535
title: Device vs. Design Units
ms.topic: article
ms.date: 05/31/2018
---

# Device vs. Design Units

An application can retrieve font metrics for a physical font only after the font has been selected into a device context. When a font is selected into a device context, it is scaled for the device. The font metrics specific to the device are known as device units.

Portable metrics in fonts are known as design units. To apply to a specified device, design units must be converted to device units. Use the following formula to convert design units to device units.

*DeviceUnits* = (*DesignUnits*/*unitsPerEm*) \* (*PointSize*/72) \* *DeviceResolution*

The variables in this formula have the following meanings.



| Variable           | Description                                                                                                                                                                |
|--------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| *DeviceUnits*      | Specifies the *DesignUnits* font metric converted to device units. This value is in the same units as the value specified for *DeviceResolution*.                          |
| *DesignUnits*      | Specifies the font metric to be converted to device units. This value can be any font metric, including the width of a character or the ascender value for an entire font. |
| *unitsPerEm*       | Specifies the em square size for the font.                                                                                                                                 |
| *PointSize*        | Specifies size of the font, in points. (One point equals 1/72 of an inch.)                                                                                                 |
| *DeviceResolution* | Specifies number of device units (pixels) per inch. Typical values might be 300 for a laser printer or 96 for a VGA screen.                                                |



 

This formula should not be used to convert device units back to design units. Device units are always rounded to the nearest pixel. The propagated round-off error can become very large, especially when an application is working with screen sizes.

To request design units, create a logical font whose height is specified as *unitsPerEm*. Applications can retrieve the value for *unitsPerEm* by calling the [**EnumFontFamilies**](/windows/desktop/api/Wingdi/nf-wingdi-enumfontfamiliesa) function and checking the **ntmSizeEM** member of the [**NEWTEXTMETRIC**](/windows/win32/api/wingdi/ns-wingdi-newtextmetrica) structure.

 

 



