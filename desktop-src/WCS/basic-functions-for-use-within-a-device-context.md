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
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Basic Functions for Use Within a Device Context

The following WCS functions deliver basic [color mapping](c.md#-color-wcs-1-0-glossary-color-mapping-gloss) capabilities within device contexts. They are useful to all applications that need to implement color management with low overhead and minimal user intervention.



| Function                                                           | Description                                                                                                                                         |
|--------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------|
| [**CheckColorsInGamut**](/windows/win32/Wingdi/nf-wingdi-checkcolorsingamut?branch=master)                   | Checks if given colors are in a device's gamut.                                                                                                     |
| [**ColorCorrectPalette**](/windows/win32/Wingdi/nf-wingdi-colorcorrectpalette?branch=master)                 | Corrects the entries in a palette for a device context.                                                                                             |
| [**ColorMatchToTarget**](/windows/win32/Wingdi/nf-wingdi-colormatchtotarget?branch=master)                   | Performs color mapping for preview purposes.                                                                                                        |
| [**CreateColorSpace**](/windows/win32/Wingdi/nf-wingdi-createcolorspacea?branch=master)                       | Creates a color space.                                                                                                                              |
| [**DeleteColorSpace**](/windows/win32/Wingdi/nf-wingdi-deletecolorspace?branch=master)                       | Deletes a color space.                                                                                                                              |
| [**EnumICMProfiles**](/windows/win32/Wingdi/nf-wingdi-enumicmprofilesa?branch=master)                         | Enumerates output color profiles available for a given device context.                                                                              |
| [**EnumICMProfilesProcCallback**](/windows/win32/Wingdi/?branch=master) | Application-defined callback function for [**EnumICMProfiles**](/windows/win32/Wingdi/nf-wingdi-enumicmprofilesa?branch=master). The name of this function is also defined by the application. |
| [**GetColorSpace**](getcolorspace.md)                             | Gets the current input color space in a device context.                                                                                             |
| [**GetICMProfile**](/windows/win32/Wingdi/nf-wingdi-geticmprofilea?branch=master)                             | Gets the current output color profile of a device context.                                                                                          |
| [**GetLogColorSpace**](/windows/win32/Wingdi/nf-wingdi-getlogcolorspacea?branch=master)                       | Gets the [**LOGCOLORSPACE**](/windows/win32/Wingdi/ns-wingdi-taglogcolorspacea?branch=master) structure of a device context.                                                                      |
| [**SetColorSpace**](/windows/win32/Wingdi/nf-wingdi-setcolorspace?branch=master)                             | Sets a device context's input color space.                                                                                                          |
| [**SetICMMode**](/windows/win32/Wingdi/nf-wingdi-seticmmode?branch=master)                                   | Turns color management on or off in a device context.                                                                                               |
| [**SetICMProfile**](/windows/win32/Wingdi/nf-wingdi-seticmprofilea?branch=master)                             | Sets the output color profile for a given device context.                                                                                           |
| [**WcsEnumColorProfiles**](wcsenumcolorprofiles.md)               | Enumerates all color profiles that satisfy the enumeration criteria in the specified profile management scope.                                      |



 

 

 




