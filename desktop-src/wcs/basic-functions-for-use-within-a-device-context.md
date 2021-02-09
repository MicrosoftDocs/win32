---
title: Basic Functions for Use Within a Device Context
description: The following WCS functions deliver basic color mapping capabilities within device contexts. They are useful to all applications that need to implement color management with low overhead and minimal user intervention.
ms.assetid: 199fac5e-daba-4aa3-a631-bb1eb2270b2e
keywords:
- Windows Color System (WCS),functions
- WCS (Windows Color System),functions
- image color management,functions
- color management,functions
- colors,functions
- WCS reference,functions
- reference for WCS,functions
- Windows Color System (WCS),device contexts
- WCS (Windows Color System),device contexts
- image color management,device contexts
- color management,device contexts
- colors,device contexts
- WCS reference,device contexts
- reference for WCS,device contexts
- device contexts
ms.localizationpriority: high


ms.topic: article
ms.date: 05/31/2018
---

# Basic Functions for Use Within a Device Context

The following WCS functions deliver basic [color mapping](c.md) capabilities within device contexts. They are useful to all applications that need to implement color management with low overhead and minimal user intervention.



| Function                                                           | Description                                                                                                                                         |
|--------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------|
| [**CheckColorsInGamut**](/windows/desktop/api/Wingdi/nf-wingdi-checkcolorsingamut)                   | Checks if given colors are in a device's gamut.                                                                                                     |
| [**ColorCorrectPalette**](/windows/desktop/api/Wingdi/nf-wingdi-colorcorrectpalette)                 | Corrects the entries in a palette for a device context.                                                                                             |
| [**ColorMatchToTarget**](/windows/desktop/api/Wingdi/nf-wingdi-colormatchtotarget)                   | Performs color mapping for preview purposes.                                                                                                        |
| [**CreateColorSpace**](/windows/desktop/api/Wingdi/nf-wingdi-createcolorspacea)                       | Creates a color space.                                                                                                                              |
| [**DeleteColorSpace**](/windows/desktop/api/Wingdi/nf-wingdi-deletecolorspace)                       | Deletes a color space.                                                                                                                              |
| [**EnumICMProfiles**](/windows/desktop/api/Wingdi/nf-wingdi-enumicmprofilesa)                         | Enumerates output color profiles available for a given device context.                                                                              |
| [**EnumICMProfilesProcCallback**](/windows/desktop/api/Wingdi/) | Application-defined callback function for [**EnumICMProfiles**](/windows/desktop/api/Wingdi/nf-wingdi-enumicmprofilesa). The name of this function is also defined by the application. |
| [**GetColorSpace**](/windows/win32/api/wingdi/nf-wingdi-getcolorspace) | Gets the current input color space in a device context. |
| [**GetICMProfile**](/windows/desktop/api/Wingdi/nf-wingdi-geticmprofilea)                             | Gets the current output color profile of a device context.                                                                                          |
| [**GetLogColorSpace**](/windows/desktop/api/Wingdi/nf-wingdi-getlogcolorspacea)                       | Gets the [**LOGCOLORSPACE**](/windows/desktop/api/Wingdi/ns-wingdi-taglogcolorspacea) structure of a device context.                                                                      |
| [**SetColorSpace**](/windows/desktop/api/Wingdi/nf-wingdi-setcolorspace)                             | Sets a device context's input color space.                                                                                                          |
| [**SetICMMode**](/windows/desktop/api/Wingdi/nf-wingdi-seticmmode)                                   | Turns color management on or off in a device context.                                                                                               |
| [**SetICMProfile**](/windows/desktop/api/Wingdi/nf-wingdi-seticmprofilea)                             | Sets the output color profile for a given device context.                                                                                           |
| [**WcsEnumColorProfiles**](/windows/win32/api/icm/nf-icm-wcsenumcolorprofiles)               | Enumerates all color profiles that satisfy the enumeration criteria in the specified profile management scope.                                      |



 

 

 




