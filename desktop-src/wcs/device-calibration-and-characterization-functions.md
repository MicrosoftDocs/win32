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
| [**GetColorProfileElement**](getcolorprofileelement.md)                     | Retrieves data from a given profile element.                                      |
| [**GetColorProfileElementTag**](getcolorprofileelementtag.md)               | Retrieves the tag name from a profile element.                                    |
| [**GetColorProfileFromHandle**](getcolorprofilefromhandle.md)               | Retrieves the color profile contents given a handle to an open color profile.     |
| [**GetColorProfileHeader**](getcolorprofileheader.md)                       | Retrieves the header from a profile.                                              |
| [**GetCountColorProfileElements**](getcountcolorprofileelements.md)         | Counts the tagged elements in a profile.                                          |
| [**GetPS2ColorRenderingDictionary**](getps2colorrenderingdictionary.md)     | Gets a PostScript color rendering dictionary.                                     |
| [**GetPS2ColorRenderingIntent**](getps2colorrenderingintent.md)             | Gets a PostScript color rendering intents.                                        |
| [**GetPS2ColorSpaceArray**](getps2colorspacearray.md)                       | Gets a PostScript color space from a profile.                                     |
| [**IsColorProfileTagPresent**](iscolorprofiletagpresent.md)                 | Checks that a given tag is present in a profile.                                  |
| [**IsColorProfileValid**](iscolorprofilevalid.md)                           | Checks that a profile is a valid ICC profile.                                     |
| [**OpenColorProfile**](opencolorprofile.md)                                 | Opens a profile and returns a handle to it.                                       |
| [**SetColorProfileElement**](setcolorprofileelement.md)                     | Writes data for a given profile element.                                          |
| [**SetColorProfileElementReference**](setcolorprofileelementreference.md)   | Creates a tag that refers to existing tag data.                                   |
| [**SetColorProfileElementSize**](setcolorprofileelementsize.md)             | Sets the size of a given profile element.                                         |
| [**SetColorProfileHeader**](setcolorprofileheader.md)                       | Sets the header information in a given profile.                                   |
| [**WcsGetCalibrationManagementState**](wcsgetcalibrationmanagementstate.md) | Determines whether system management of the display calibration state is enabled. |
| [**WcsSetCalibrationManagementState**](wcssetcalibrationmanagementstate.md) | Determines whether system management of the display calibration state is enabled. |



 

 

 




