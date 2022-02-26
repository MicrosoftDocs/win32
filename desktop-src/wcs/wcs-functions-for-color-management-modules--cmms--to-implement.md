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


ms.topic: article
ms.date: 05/31/2018
---

# WCS Functions for Color Management Modules (CMMs) to Implement

The following functions are to be implemented by color management modules (CMMs), and exported for the operating system to call.



| Function                                                                     | Description                                                                               |
|------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------|
| [**CMCheckColors**](/windows/win32/api/icm/nf-icm-cmcheckcolors) | Determines whether given colors lie within the output [gamut](./g.md) of a specified transform. |
| [**CMCheckColorsInGamut**](/windows/win32/api/icm/nf-icm-cmcheckcolorsingamut) | Determines whether specified RGB triples lie in the output [gamut](./g.md) of a specified transform. |
| [**CMCheckRGBs**](/windows/desktop/api/Wingdi/)                                           | Checks bitmap colors against an output gamut.                                             |
| [**CMConvertColorNameToIndex**](/windows/win32/api/icm/nf-icm-cmconvertcolornametoindex) | Converts color names in a named color space to index numbers in a color profile |
| [**CMConvertIndexToColorName**](/windows/win32/api/icm/nf-icm-cmconvertindextocolorname) | Transforms indices in a color space to an array of names in a named color space. |
| [**CMCreateDeviceLinkProfile**](/windows/win32/api/icm/nf-icm-cmcreatedevicelinkprofile) | Creates a [device link profile](./d.md) in the format specified by the International Color Consortium in its ICC Profile Format Specification. |
| [**CMCreateMultiProfileTransform**](/windows/win32/api/icm/nf-icm-cmcreatemultiprofiletransform) | Accepts an array of profiles or a single [device link profile](./d.md) and creates a color transform. This transform is a mapping from the color space specified by the first profile to that of the second profile and so on to the last one. |
| [**CMCreateProfile**](/windows/win32/api/icm/nf-icm-cmcreateprofile) | Creates a display color profile from a [**LOGCOLORSPACEA**](/windows/win32/api/wingdi/ns-wingdi-logcolorspacea) structure. |
| [**CMCreateProfileW**](/windows/win32/api/icm/nf-icm-cmcreateprofilew) | Creates a display color profile from a [**LOGCOLORSPACEW**](/windows/win32/api/wingdi/ns-wingdi-logcolorspacew) structure. |
| [**CMCreateTransform**](/windows/win32/api/icm/nf-icm-cmcreatetransform) | Deprecated. There is no replacement API because this one was no longer being used. Developers of alternate CMM modules are not required to implement it. |
| [**CMCreateTransformExt**](/windows/win32/api/icm/nf-icm-cmcreatetransformext) | Creates a color transform that maps from an input [**LOGCOLORSPACEA**](/windows/win32/api/wingdi/ns-wingdi-logcolorspacea) to an optional target space and then to an output device, using a set of flags that define how the transform should be created. |
| [**CMCreateTransformExtW**](/windows/win32/api/icm/nf-icm-cmcreatetransformextw) | Creates a color transform that maps from an input [**LOGCOLORSPACEW**](/windows/win32/api/wingdi/ns-wingdi-logcolorspacew) to an optional target space and then to an output device, using a set of flags that define how the transform should be created. |
| [**CMCreateTransformW**](/windows/win32/api/icm/nf-icm-cmcreatetransformw) | Deprecated. There is no replacement API because this one was no longer being used. Developers of alternate CMM modules are not required to implement it. |
| [**CMDeleteTransform**](/windows/win32/api/icm/nf-icm-cmdeletetransform) | Deletes a specified color transform, and frees any memory associated with it. |
| [**CMGetInfo**](/windows/win32/api/icm/nf-icm-cmgetinfo) | Retrieves various information about the color management module (CMM). |
| [**CMGetNamedProfileInfo**](/windows/win32/api/icm/nf-icm-cmgetnamedprofileinfo) | Retrieves information about the specified named color profile. |
| [**CMGetPS2ColorRenderingDictionary**](/windows/desktop/api/Wingdi/) | Gets a PostScript color rendering dictionary.                                             |
| [**CMGetPS2ColorRenderingIntent**](/windows/win32/api/icm/nf-icm-cmgetps2colorrenderingintent) | Retrieves the PostScript Level 2 color [rendering intent](rendering-intents.md) from a profile. |
| [**CMGetPS2ColorSpaceArray**](/windows/desktop/api/Wingdi/)                   | Gets a PostScript color space array.                                                      |
| [**CMIsProfileValid**](/windows/win32/api/icm/nf-icm-cmisprofilevalid) | Reports whether the given profile is a valid ICC profile that can be used for color management. |
| [**CMTranslateColors**](/windows/win32/api/icm/nf-icm-cmtranslatecolors) | Translates an array of colors from a source [color space](rendering-intents.md) to a destination color space using a color transform. |
| [**CMTranslateRGB**](/windows/win32/api/icm/nf-icm-cmtranslatergb) | Translates an application-supplied RGBQuad into the device [color space](color-spaces.md). |
| [**CMTranslateRGBs**](/windows/win32/api/icm/nf-icm-cmtranslatergbs) | Translates a bitmap from one [color space](color-spaces.md) to another using a color transform. |
| [**CMTranslateRGBsExt**](/windows/win32/api/icm/nf-icm-cmtranslatergbsext) | Translates a bitmap from one defined format into a different defined format and calls a callback function periodically, if one is specified, to report progress and permit the calling application to terminate the translation. |



 

 

 
