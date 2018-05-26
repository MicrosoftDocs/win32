---
title: Advanced Functions for Use Outside of a Device Context
description: These functions provide advanced color management capabilities outside of device contexts.
ms.assetid: 2f742743-094a-44b8-816b-24246607caeb
keywords:
- Windows Color System (WCS),functions
- WCS (Windows Color System),functions
- image color management,functions
- color management,functions
- colors,functions
- WCS reference,functions
- reference for WCS,functions
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Advanced Functions for Use Outside of a Device Context

These functions provide advanced color management capabilities outside of device contexts.



| Function                                                           | Description                                                                                                                                                              |
|--------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**ApplyCallbackFunction**](apply.md)                             | Callback function which updates the WCS configuration data while the dialog box displayed by the [**SetupColorMatching**](setupcolormatching.md) function is executing. |
| [**CheckBitmapBits**](checkbitmapbits.md)                         | Checks bitmap colors against a gamut.                                                                                                                                    |
| [**CheckColors**](checkcolors.md)                                 | Checks colors against a device output gamut.                                                                                                                             |
| [**ConvertColorNameToIndex**](convertcolornametoindex.md)         | Converts color names in a named color space to index numbers in a color profile.                                                                                         |
| [**ConvertIndexToColorName**](convertindextocolorname.md)         | Converts indices in a color space to an array of names in a named color space.                                                                                           |
| [**CreateColorTransform**](createcolortransform.md)               | Creates a color transform.                                                                                                                                               |
| [**CreateMultiProfileTransform**](createmultiprofiletransform.md) | Creates a transform from multiple profiles.                                                                                                                              |
| [**DeleteColorTransform**](deletecolortransform.md)               | Deletes a color transform.                                                                                                                                               |
| [**GetCMMInfo**](getcmminfo.md)                                   | Identifies the CMM that created a transform.                                                                                                                             |
| [**GetNamedProfileInfo**](getnamedprofileinfo.md)                 | Retrieves information about a named color profile.                                                                                                                       |
| [**ICMProgressProcCallback**](icmprogressproccallback.md)         | Application-supplied callback function to report progress. The name of this function is also defined by the application.                                                 |
| [**SelectCMM**](selectcmm.md)                                     | Specifies a preferred CMM to use.                                                                                                                                        |
| [**SetupColorMatching**](setupcolormatching.md)                   | Provides user control over color management by way of a dialog box.                                                                                                      |
| [**TranslateBitmapBits**](translatebitmapbits.md)                 | Converts bitmap colors using a color transform.                                                                                                                          |
| [**TranslateColors**](translatecolors.md)                         | Converts colors using a color transform.                                                                                                                                 |
| [**WcsCheckColors**](wcscheckcolors.md)                           | Determines whether the colors in an array are within the output gamut of a specified WCS color transform.                                                                |
| [**WcsTranslateColors**](wcstranslatecolors.md)                   | Translates an array of colors from the source color space to the destination color space as defined by a color transform.                                                |



 

 

 




