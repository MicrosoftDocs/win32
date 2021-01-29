---
title: WCS Functions for Color Management Modules (CMMs) to Implement
description: The following functions are to be implemented by color management modules (CMMs), and exported for the operating system to call.
ms.assetid: e05129ec-9128-44f0-82c7-f4e01536d7a8
keywords:
- Windows Color System (WCS),functions
- WCS (Windows Color System),functions
- image color management,functions
- color management,functions
- colors,functions
- WCS reference,functions
- reference for WCS,functions
- Windows Color System (WCS),Color Management Module (CMM)
- WCS (Windows Color System),Color Management Module (CMM)
- image color management,Color Management Module (CMM)
- color management,Color Management Module (CMM)
- colors,Color Management Module (CMM)
- WCS reference,Color Management Module (CMM)
- reference for WCS,Color Management Module (CMM)
- Color Management Module (CMM)
- CMM (Color Management Module)
ms.localizationpriority: high


ms.topic: article
ms.date: 05/31/2018
---

# WCS Functions for Color Management Modules (CMMs) to Implement

The following functions are to be implemented by color management modules (CMMs), and exported for the operating system to call.



| Function                                                                     | Description                                                                               |
|------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------|
| [**CMCheckColors**](/windows/win32/api/icm/nf-icm-cmcheckcolors) | Determines whether given colors lie within the output [gamut](/windows/win32/wcs/g) of a specified transform. |
| [**CMCheckColorsInGamut**](/windows/win32/api/icm/nf-icm-cmcheckcolorsingamut) | Determines whether specified RGB triples lie in the output [gamut](/windows/win32/wcs/g) of a specified transform. |
| [**CMCheckRGBs**](/windows/desktop/api/Wingdi/)                                           | Checks bitmap colors against an output gamut.                                             |
| [**CMConvertColorNameToIndex**](/windows/win32/api/icm/nf-icm-cmconvertcolornametoindex) | Converts color names in a named color space to index numbers in a color profile |
| [**CMConvertIndexToColorName**](/windows/win32/api/icm/nf-icm-cmconvertindextocolorname) | Transforms indices in a color space to an array of names in a named color space. |
| [**CMCreateDeviceLinkProfile**](/windows/win32/api/icm/nf-icm-cmcreatedevicelinkprofile) | Creates a [device link profile](/windows/win32/wcs/d) in the format specified by the International Color Consortium in its ICC Profile Format Specification. |
| [**CMCreateMultiProfileTransform**](/windows/win32/api/icm/nf-icm-cmcreatemultiprofiletransform) | Accepts an array of profiles or a single [device link profile](/windows/win32/wcs/d) and creates a color transform. This transform is a mapping from the color space specified by the first profile to that of the second profile and so on to the last one. |
| [**CMCreateProfile**](/windows/desktop/api/Wingdi/)                                   | Creates an ICC profile from a [**LOGCOLORSPACE**](/windows/desktop/api/Wingdi/ns-wingdi-taglogcolorspacea) structure (ANSI).    |
| [**CMCreateProfileW**](/windows/desktop/api/Wingdi/)                                 | Creates an ICC profile from a [**LOGCOLORSPACE**](/windows/desktop/api/Wingdi/ns-wingdi-taglogcolorspacea) structure (Unicode). |
| [CMCreateTransform](cmcreatetransform.md)                                   | Creates a color transform (ANSI).                                                         |
| [**CMCreateTransformExt**](/windows/desktop/api/Wingdi/)                         | Creates an extended color transform (ANSI).                                               |
| [**CMCreateTransformExtW**](/windows/desktop/api/Wingdi/)                       | Creates an extended color transform (Unicode).                                            |
| [CMCreateTransformW](cmcreatetransformw.md)                                 | Creates a color transform (Unicode).                                                      |
| [**CMDeleteTransform**](/windows/desktop/api/Wingdi/)                               | Deletes a color transform.                                                                |
| [**CMGetInfo**](/windows/desktop/api/Wingdi/)                                               | Returns information about a given CMM.                                                    |
| [**CMGetNamedProfileInfo**](/windows/desktop/api/Wingdi/)                       | Retrieves information about a named color profile.                                        |
| [**CMGetPS2ColorRenderingDictionary**](/windows/desktop/api/Wingdi/) | Gets a PostScript color rendering dictionary.                                             |
| [**CMGetPS2ColorRenderingIntent**](/windows/desktop/api/Wingdi/)         | Gets a PostScript color rendering intent.                                                 |
| [**CMGetPS2ColorSpaceArray**](/windows/desktop/api/Wingdi/)                   | Gets a PostScript color space array.                                                      |
| [**CMIsProfileValid**](/windows/desktop/api/Wingdi/)                                 | Checks that a profile is a valid ICC profile.                                             |
| [**CMTranslateColors**](/windows/desktop/api/Wingdi/)                               | Translates colors using a color transform.                                                |
| [**CMTranslateRGB**](/windows/desktop/api/Wingdi/)                                     | Translates an RGB color using a color transform.                                          |
| [**CMTranslateRGBs**](/windows/desktop/api/Wingdi/)                                   | Translates bitmap colors using a color transform.                                         |
| [**CMTranslateRGBsExt**](/windows/desktop/api/Wingdi/)                             | Translates bitmap colors with callback progress reporting.                                |



 

 

 




