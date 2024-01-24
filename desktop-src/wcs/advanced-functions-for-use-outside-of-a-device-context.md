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


ms.topic: article
ms.date: 05/31/2018
---

# Advanced Functions for Use Outside of a Device Context

These functions provide advanced color management capabilities outside of device contexts.



| Function                                                           | Description                                                                                                                                                              |
|--------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**PCMSCALLBACKW**](/windows/win32/api/icm/nc-icm-pcmscallbackw) | \**PCMSCALLBACKW** (or **ApplyCallbackFunction**) is a callback function that you implement that updates the WCS configuration data while the dialog box displayed by the [**SetupColorMatchingW**](/windows/win32/api/icm/nf-icm-setupcolormatchingw) function is executing. |
| [**CheckBitmapBits**](/windows/win32/api/icm/nf-icm-checkbitmapbits) | Checks whether the pixels in a specified bitmap lie within the output [gamut](g.md) of a specified transform. |
| [**CheckColors**](/windows/win32/api/icm/nf-icm-checkbitmapbits) | Determines whether the colors in an array lie within the output [gamut](g.md) of a specified transform. |
| [**ConvertColorNameToIndex**](/windows/win32/api/icm/nf-icm-convertcolornametoindex) | Converts color names in a named color space to index numbers in an International Color Consortium (ICC) color profile. |
| [**ConvertIndexToColorName**](/windows/win32/api/icm/nf-icm-convertindextocolorname) | Transforms indices in a color space to an array of names in a named color space. |
| [**CreateColorTransformW**](/windows/win32/api/icm/nf-icm-createcolortransformw) | Transforms indices in a color space to an array of names in a named color space. |
| [**CreateMultiProfileTransform**](/windows/win32/api/icm/nf-icm-createmultiprofiletransform) | Accepts an array of profiles or a single [device link profile](d.md) and creates a color transform that applications can use to perform color mapping. |
| [**DeleteColorTransform**](/windows/win32/api/icm/nf-icm-deletecolortransform) | Deletes a given color transform. |
| [**GetCMMInfo**](/windows/win32/api/icm/nf-icm-getcmminfo) | Retrieves various information about the color management module (CMM) that created the specified color transform. |
| [**GetNamedProfileInfo**](/windows/win32/api/icm/nf-icm-getnamedprofileinfo) | Retrieves information about the International Color Consortium (ICC) named color profile that is specified in the first parameter. |
| [**ICMProgressProcCallback**](icmprogressproccallback.md)         | Application-supplied callback function to report progress. The name of this function is also defined by the application.                                                 |
| [**SelectCMM**](/windows/win32/api/icm/nf-icm-selectcmm) | Allows you to select the preferred color management module (CMM) to use. |
| [**SetupColorMatchingW**](/windows/win32/api/icm/nf-icm-setupcolormatchingw)                   | Provides user control over color management by way of a dialog box.                                                                                                      |
| [**TranslateBitmapBits**](/windows/win32/api/icm/nf-icm-translatebitmapbits)                 | Converts bitmap colors using a color transform.                                                                                                                          |
| [**TranslateColors**](/windows/win32/api/icm/nf-icm-translatecolors) | Translates an array of colors from the source [color space](c.md) to the destination color space as defined by a color transform. |
| [**WcsCheckColors**](/windows/win32/api/icm/nf-icm-wcsassociatecolorprofilewithdevice)                           | Determines whether the colors in an array are within the output gamut of a specified WCS color transform.                                                                |
| [**WcsTranslateColors**](/windows/win32/api/icm/nf-icm-wcstranslatecolors) | Translates an array of colors from the source color space to the destination color space as defined by a color transform.                                                |



 

 

 




