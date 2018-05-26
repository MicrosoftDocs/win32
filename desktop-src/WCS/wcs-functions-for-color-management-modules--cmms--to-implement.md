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
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# WCS Functions for Color Management Modules (CMMs) to Implement

The following functions are to be implemented by color management modules (CMMs), and exported for the operating system to call.



| Function                                                                     | Description                                                                               |
|------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------|
| [**CMCheckColors**](/windows/win32/Wingdi/?branch=master)                                       | Checks colors against an output gamut.                                                    |
| [**CMCheckColorsInGamut**](/windows/win32/Wingdi/?branch=master)                         | Checks RGB triplets against an output gamut.                                              |
| [**CMCheckRGBs**](/windows/win32/Wingdi/?branch=master)                                           | Checks bitmap colors against an output gamut.                                             |
| [**CMConvertColorNameToIndex**](/windows/win32/Wingdi/?branch=master)               | Converts color names in a named color space to index numbers in a color profile.          |
| [**CMConvertIndexToColorName**](/windows/win32/Wingdi/?branch=master)               | Converts indices in a color space to an array of names in a named color space.            |
| [**CMCreateDeviceLinkProfile**](/windows/win32/Wingdi/?branch=master)               | Creates an ICC device link profile.                                                       |
| [**CMCreateMultiProfileTransform**](/windows/win32/Wingdi/?branch=master)       | Creates a transform from an array of profiles.                                            |
| [**CMCreateProfile**](/windows/win32/Wingdi/?branch=master)                                   | Creates an ICC profile from a [**LOGCOLORSPACE**](/windows/win32/Wingdi/ns-wingdi-taglogcolorspacea?branch=master) structure (ANSI).    |
| [**CMCreateProfileW**](/windows/win32/Wingdi/?branch=master)                                 | Creates an ICC profile from a [**LOGCOLORSPACE**](/windows/win32/Wingdi/ns-wingdi-taglogcolorspacea?branch=master) structure (Unicode). |
| [CMCreateTransform](cmcreatetransform.md)                                   | Creates a color transform (ANSI).                                                         |
| [**CMCreateTransformExt**](/windows/win32/Wingdi/?branch=master)                         | Creates an extended color transform (ANSI).                                               |
| [**CMCreateTransformExtW**](/windows/win32/Wingdi/?branch=master)                       | Creates an extended color transform (Unicode).                                            |
| [CMCreateTransformW](cmcreatetransformw.md)                                 | Creates a color transform (Unicode).                                                      |
| [**CMDeleteTransform**](/windows/win32/Wingdi/?branch=master)                               | Deletes a color transform.                                                                |
| [**CMGetInfo**](/windows/win32/Wingdi/?branch=master)                                               | Returns information about a given CMM.                                                    |
| [**CMGetNamedProfileInfo**](/windows/win32/Wingdi/?branch=master)                       | Retrieves information about a named color profile.                                        |
| [**CMGetPS2ColorRenderingDictionary**](/windows/win32/Wingdi/?branch=master) | Gets a PostScript color rendering dictionary.                                             |
| [**CMGetPS2ColorRenderingIntent**](/windows/win32/Wingdi/?branch=master)         | Gets a PostScript color rendering intent.                                                 |
| [**CMGetPS2ColorSpaceArray**](/windows/win32/Wingdi/?branch=master)                   | Gets a PostScript color space array.                                                      |
| [**CMIsProfileValid**](/windows/win32/Wingdi/?branch=master)                                 | Checks that a profile is a valid ICC profile.                                             |
| [**CMTranslateColors**](/windows/win32/Wingdi/?branch=master)                               | Translates colors using a color transform.                                                |
| [**CMTranslateRGB**](/windows/win32/Wingdi/?branch=master)                                     | Translates an RGB color using a color transform.                                          |
| [**CMTranslateRGBs**](/windows/win32/Wingdi/?branch=master)                                   | Translates bitmap colors using a color transform.                                         |
| [**CMTranslateRGBsExt**](/windows/win32/Wingdi/?branch=master)                             | Translates bitmap colors with callback progress reporting.                                |



 

 

 




