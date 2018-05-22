---
title: Basic Functions for Use Within a Device Context
description: The following WCS functions deliver basic color mapping capabilities within device contexts. They are useful to all applications that need to implement color management with low overhead and minimal user intervention.
ms.assetid: '199fac5e-daba-4aa3-a631-bb1eb2270b2e'
keywords: ["Windows Color System (WCS),functions", "WCS (Windows Color System),functions", "image color management,functions", "color management,functions", "colors,functions", "WCS reference,functions", "reference for WCS,functions", "Windows Color System (WCS),device contexts", "WCS (Windows Color System),device contexts", "image color management,device contexts", "color management,device contexts", "colors,device contexts", "WCS reference,device contexts", "reference for WCS,device contexts", "device contexts"]
---

# Basic Functions for Use Within a Device Context

The following WCS functions deliver basic [color mapping](c.md#-color-wcs-1-0-glossary-color-mapping-gloss) capabilities within device contexts. They are useful to all applications that need to implement color management with low overhead and minimal user intervention.



| Function                                                           | Description                                                                                                                                         |
|--------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------|
| [**CheckColorsInGamut**](checkcolorsingamut.md)                   | Checks if given colors are in a device's gamut.                                                                                                     |
| [**ColorCorrectPalette**](colorcorrectpalette.md)                 | Corrects the entries in a palette for a device context.                                                                                             |
| [**ColorMatchToTarget**](colormatchtotarget.md)                   | Performs color mapping for preview purposes.                                                                                                        |
| [**CreateColorSpace**](createcolorspace.md)                       | Creates a color space.                                                                                                                              |
| [**DeleteColorSpace**](deletecolorspace.md)                       | Deletes a color space.                                                                                                                              |
| [**EnumICMProfiles**](enumicmprofiles.md)                         | Enumerates output color profiles available for a given device context.                                                                              |
| [**EnumICMProfilesProcCallback**](enumicmprofilesproccallback.md) | Application-defined callback function for [**EnumICMProfiles**](enumicmprofiles.md). The name of this function is also defined by the application. |
| [**GetColorSpace**](getcolorspace.md)                             | Gets the current input color space in a device context.                                                                                             |
| [**GetICMProfile**](geticmprofile.md)                             | Gets the current output color profile of a device context.                                                                                          |
| [**GetLogColorSpace**](getlogcolorspace.md)                       | Gets the [**LOGCOLORSPACE**](logcolorspace.md) structure of a device context.                                                                      |
| [**SetColorSpace**](setcolorspace.md)                             | Sets a device context's input color space.                                                                                                          |
| [**SetICMMode**](seticmmode.md)                                   | Turns color management on or off in a device context.                                                                                               |
| [**SetICMProfile**](seticmprofile.md)                             | Sets the output color profile for a given device context.                                                                                           |
| [**WcsEnumColorProfiles**](wcsenumcolorprofiles.md)               | Enumerates all color profiles that satisfy the enumeration criteria in the specified profile management scope.                                      |



 

 

 




