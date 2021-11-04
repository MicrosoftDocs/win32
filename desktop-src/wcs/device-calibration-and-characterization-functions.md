---
title: Device Calibration and Characterization Functions
description: The following functions are useful for writing device calibration and characterization tools needed for installing and calibrating color display devices such as monitors and printers.
ms.assetid: e66115cc-b6a9-4df5-b774-38619881bdb0
keywords:
- Windows Color System (WCS),functions
- WCS (Windows Color System),functions
- image color management,functions
- color management,functions
- colors,functions
- WCS reference,functions
- reference for WCS,functions
- Windows Color System (WCS),device calibration
- WCS (Windows Color System),device calibration
- image color management,device calibration
- color management,device calibration
- colors,device calibration
- WCS reference,device calibration
- reference for WCS,device calibration
- Windows Color System (WCS),characterization
- WCS (Windows Color System),characterization
- image color management,characterization
- color management,characterization
- colors,characterization
- WCS reference,characterization
- reference for WCS,characterization
- device calibration
- calibration
- characterization
ms.localizationpriority: high


ms.topic: article
ms.date: 05/31/2018
---

# Device Calibration and Characterization Functions

The following functions are useful for writing device calibration and characterization tools needed for installing and calibrating color display devices such as monitors and printers.



| Function | Description |
|-|-|
| [**CloseColorProfile**](/windows/win32/api/icm/nf-icm-closecolorprofile) | Closes an open profile handle. |
| [**CreateDeviceLinkProfile**](/windows/win32/api/icm/nf-icm-createdevicelinkprofile) | Creates an International Color Consortium (ICC) *device link profile* from a set of color profiles, using the specified intents. |
| [**GetColorProfileElement**](/windows/win32/api/icm/nf-icm-getcolorprofileelement) | Copies data from a specified tagged profile element of a specified color profile into a buffer. |
| [**GetColorProfileElementTag**](/windows/win32/api/icm/nf-icm-getcolorprofileelementtag) | Retrieves the tag name specified by *dwIndex* in the tag table of a given International Color Consortium (ICC) color profile, where *dwIndex* is a one-based index into that table. |
| [**GetColorProfileFromHandle**](/windows/win32/api/icm/nf-icm-getcolorprofilefromhandle)| Retrieves the color profile contents given a handle to an open color profile.     |
| [**GetColorProfileHeader**](/windows/win32/api/icm/nf-icm-getcolorprofileheader) | Retrieves or derives ICC header structure from either ICC color profile or WCS XML profile. Drivers and applications should assume returning **TRUE** only indicates that a properly structured header is returned. Each tag will still need to be validated independently using either legacy ICM2 APIs or XML schema APIs. |
| [**GetCountColorProfileElements**](/windows/win32/api/icm/nf-icm-getcountcolorprofileelements) | Retrieves the number of tagged elements in a given color profile. |
| [**GetPS2ColorRenderingDictionary**](/windows/win32/api/icm/nf-icm-getps2colorrenderingdictionary) | Retrieves the PostScript Level 2 color rendering dictionary from the specified ICC color profile. |
| [**GetPS2ColorRenderingIntent**](/windows/win32/api/icm/nf-icm-getps2colorrenderingintent) | Retrieves the PostScript Level 2 color [rendering intent](r.md) from an ICC color profile. |
| [**GetPS2ColorSpaceArray**](/windows/win32/api/icm/nf-icm-getps2colorspacearray) | Retrieves the PostScript Level 2 [color space](c.md) array from an ICC color profile. |
| [**IsColorProfileTagPresent**](/windows/win32/api/icm/nf-icm-iscolorprofiletagpresent) | Reports whether a specified International Color Consortium (ICC) tag is present in the specified color profile. |
| [**IsColorProfileValid**](/windows/win32/api/icm/nf-icm-iscolorprofilevalid) | Allows you to determine whether the specified profile is a valid International Color Consortium (ICC) profile, or a valid Windows Color System (WCS) profile handle that can be used for color management. |
| [**OpenColorProfileW**](/windows/win32/api/icm/nf-icm-opencolorprofilew) | Creates a handle to a specified color profile. The handle can then be used in other profile management functions. |
| [**SetColorProfileElement**](/windows/win32/api/icm/nf-icm-setcolorprofileelement) | Sets the element data for a tagged profile element in an ICC color profile. |
| [**SetColorProfileElementReference**](/windows/win32/api/icm/nf-icm-setcolorprofileelementreference) | Creates in a specified ICC color profile a new tag that references the same data as an existing tag. |
| [**SetColorProfileElementSize**](/windows/win32/api/icm/nf-icm-setcolorprofileelementsize) | Sets the size of a tagged element in an ICC color profile. |
| [**SetColorProfileHeader**](/windows/win32/api/icm/nf-icm-setcolorprofileheader) | Sets the header data in a specified ICC color profile. |
| [**WcsGetCalibrationManagementState**](/windows/win32/api/icm/nf-icm-wcsgetcalibrationmanagementstate) | Determines whether system management of the display calibration state is enabled. |
| [**WcsSetCalibrationManagementState**](/windows/win32/api/icm/nf-icm-wcssetcalibrationmanagementstate) | Determines whether system management of the display calibration state is enabled. |



 

 

 




