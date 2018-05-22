---
title: WCS Functions for Color Management Modules (CMMs) to Implement
description: The following functions are to be implemented by color management modules (CMMs), and exported for the operating system to call.
ms.assetid: 'e05129ec-9128-44f0-82c7-f4e01536d7a8'
keywords: ["Windows Color System (WCS),functions", "WCS (Windows Color System),functions", "image color management,functions", "color management,functions", "colors,functions", "WCS reference,functions", "reference for WCS,functions", "Windows Color System (WCS),Color Management Module (CMM)", "WCS (Windows Color System),Color Management Module (CMM)", "image color management,Color Management Module (CMM)", "color management,Color Management Module (CMM)", "colors,Color Management Module (CMM)", "WCS reference,Color Management Module (CMM)", "reference for WCS,Color Management Module (CMM)", "Color Management Module (CMM)", "CMM (Color Management Module)"]
---

# WCS Functions for Color Management Modules (CMMs) to Implement

The following functions are to be implemented by color management modules (CMMs), and exported for the operating system to call.



| Function                                                                     | Description                                                                               |
|------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------|
| [**CMCheckColors**](cmcheckcolors.md)                                       | Checks colors against an output gamut.                                                    |
| [**CMCheckColorsInGamut**](cmcheckcolorsingamut.md)                         | Checks RGB triplets against an output gamut.                                              |
| [**CMCheckRGBs**](cmcheckrgbs.md)                                           | Checks bitmap colors against an output gamut.                                             |
| [**CMConvertColorNameToIndex**](cmconvertcolornametoindex.md)               | Converts color names in a named color space to index numbers in a color profile.          |
| [**CMConvertIndexToColorName**](cmconvertindextocolorname.md)               | Converts indices in a color space to an array of names in a named color space.            |
| [**CMCreateDeviceLinkProfile**](cmcreatedevicelinkprofile.md)               | Creates an ICC device link profile.                                                       |
| [**CMCreateMultiProfileTransform**](cmcreatemultiprofiletransform.md)       | Creates a transform from an array of profiles.                                            |
| [**CMCreateProfile**](cmcreateprofile.md)                                   | Creates an ICC profile from a [**LOGCOLORSPACE**](logcolorspace.md) structure (ANSI).    |
| [**CMCreateProfileW**](cmcreateprofilew.md)                                 | Creates an ICC profile from a [**LOGCOLORSPACE**](logcolorspace.md) structure (Unicode). |
| [CMCreateTransform](cmcreatetransform.md)                                   | Creates a color transform (ANSI).                                                         |
| [**CMCreateTransformExt**](cmcreatetransformext.md)                         | Creates an extended color transform (ANSI).                                               |
| [**CMCreateTransformExtW**](cmcreatetransformextw.md)                       | Creates an extended color transform (Unicode).                                            |
| [CMCreateTransformW](cmcreatetransformw.md)                                 | Creates a color transform (Unicode).                                                      |
| [**CMDeleteTransform**](cmdeletetransform.md)                               | Deletes a color transform.                                                                |
| [**CMGetInfo**](cmgetinfo.md)                                               | Returns information about a given CMM.                                                    |
| [**CMGetNamedProfileInfo**](cmgetnamedprofileinfo.md)                       | Retrieves information about a named color profile.                                        |
| [**CMGetPS2ColorRenderingDictionary**](cmgetps2colorrenderingdictionary.md) | Gets a PostScript color rendering dictionary.                                             |
| [**CMGetPS2ColorRenderingIntent**](cmgetps2colorrenderingintent.md)         | Gets a PostScript color rendering intent.                                                 |
| [**CMGetPS2ColorSpaceArray**](cmgetps2colorspacearray.md)                   | Gets a PostScript color space array.                                                      |
| [**CMIsProfileValid**](cmisprofilevalid.md)                                 | Checks that a profile is a valid ICC profile.                                             |
| [**CMTranslateColors**](cmtranslatecolors.md)                               | Translates colors using a color transform.                                                |
| [**CMTranslateRGB**](cmtranslatergb.md)                                     | Translates an RGB color using a color transform.                                          |
| [**CMTranslateRGBs**](cmtranslatergbs.md)                                   | Translates bitmap colors using a color transform.                                         |
| [**CMTranslateRGBsExt**](cmtranslatergbsext.md)                             | Translates bitmap colors with callback progress reporting.                                |



 

 

 




