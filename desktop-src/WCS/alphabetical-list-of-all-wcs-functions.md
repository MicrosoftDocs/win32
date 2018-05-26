---
title: Alphabetical List of All WCS Functions
description: The following is a complete alphabetical list of the WCS 1.0 API functions provided by Windows \ 160;98 and later and Windows \ 160;2000 and later.
ms.assetid: aba45dbd-6fc2-4788-87f0-043579fa53f9
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

# Alphabetical List of All WCS Functions

The following is a complete alphabetical list of the WCS 1.0 API functions provided by Windows 98 and later and Windows 2000 and later.



| Function or Structure                                                                  | Description                                                                                                                                          |
|----------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------|
| [*ApplyCallbackFunction*](apply.md)                                                   | Callback function that can be used to update WCS configuration data.                                                                                 |
| [**AssociateColorProfileWithDevice**](associatecolorprofilewithdevice.md)             | Associates a color profile with a device.                                                                                                            |
| [**CheckBitmapBits**](checkbitmapbits.md)                                             | Checks bitmap colors against a gamut.                                                                                                                |
| [**CheckColors**](checkcolors.md)                                                     | Checks colors against a device output gamut.                                                                                                         |
| [**CheckColorsInGamut**](/windows/win32/Wingdi/nf-wingdi-checkcolorsingamut?branch=master)                                       | Checks if given colors are in a device's gamut.                                                                                                      |
| [**CloseColorProfile**](closecolorprofile.md)                                         | Closes a profile.                                                                                                                                    |
| [**CMCheckColors**](/windows/win32/Wingdi/?branch=master)                                                 | Checks colors against an output gamut.                                                                                                               |
| [**CMCheckColorsInGamut**](/windows/win32/Wingdi/?branch=master)                                   | Checks RGB triplets against an output gamut.                                                                                                         |
| [**CMCheckRGBs**](/windows/win32/Wingdi/?branch=master)                                                     | Checks bitmap colors against an output gamut.                                                                                                        |
| [**CMConvertColorNameToIndex**](/windows/win32/Wingdi/?branch=master)                         | Converts color names in a named color space to index numbers in a color profile.                                                                     |
| [**CMConvertIndexToColorName**](/windows/win32/Wingdi/?branch=master)                         | Converts indices in a color space to an array of names in a named color space.                                                                       |
| [**CMCreateDeviceLinkProfile**](/windows/win32/Wingdi/?branch=master)                         | Creates an ICC device link profile.                                                                                                                  |
| [**CMCreateMultiProfileTransform**](/windows/win32/Wingdi/?branch=master)                 | Creates a transform from an array of profiles.                                                                                                       |
| [**CMCreateProfile**](/windows/win32/Wingdi/?branch=master)                                             | Creates an ICC profile from a [**LOGCOLORSPACE**](/windows/win32/Wingdi/ns-wingdi-taglogcolorspacea?branch=master) structure (ANSI).                                                               |
| [**CMCreateProfileW**](/windows/win32/Wingdi/?branch=master)                                           | Creates an ICC profile from a [**LOGCOLORSPACE**](/windows/win32/Wingdi/ns-wingdi-taglogcolorspacea?branch=master) structure (Unicode).                                                            |
| [CMCreateTransform](cmcreatetransform.md)                                             | Creates a color transform (ANSI).                                                                                                                    |
| [**CMCreateTransformExt**](/windows/win32/Wingdi/?branch=master)                                   | Creates an extended color transform (ANSI).                                                                                                          |
| [**CMCreateTransformExtW**](/windows/win32/Wingdi/?branch=master)                                 | Creates an extended color transform (Unicode).                                                                                                       |
| [CMCreateTransformW](cmcreatetransformw.md)                                           | Creates a color transform (Unicode).                                                                                                                 |
| [**CMDeleteTransform**](/windows/win32/Wingdi/?branch=master)                                         | Deletes a color transform.                                                                                                                           |
| [**CMGetInfo**](/windows/win32/Wingdi/?branch=master)                                                         | Returns information about a given CMM.                                                                                                               |
| [**CMGetNamedProfileInfo**](/windows/win32/Wingdi/?branch=master)                                 | Retrieves information about a named color profile.                                                                                                   |
| [**CMGetPS2ColorRenderingDictionary**](/windows/win32/Wingdi/?branch=master)           | Gets a PostScript color rendering dictionary.                                                                                                        |
| [**CMGetPS2ColorRenderingIntent**](/windows/win32/Wingdi/?branch=master)                   | Gets a PostScript color rendering intent.                                                                                                            |
| [**CMGetPS2ColorSpaceArray**](/windows/win32/Wingdi/?branch=master)                             | Gets a PostScript color space array.                                                                                                                 |
| [**CMIsProfileValid**](/windows/win32/Wingdi/?branch=master)                                           | Checks that a profile is a valid ICC profile.                                                                                                        |
| [**CMTranslateColors**](/windows/win32/Wingdi/?branch=master)                                         | Translates colors using a color transform.                                                                                                           |
| [**CMTranslateRGB**](/windows/win32/Wingdi/?branch=master)                                               | Translates an RGB color using a color transform.                                                                                                     |
| [**CMTranslateRGBs**](/windows/win32/Wingdi/?branch=master)                                             | Translates bitmap colors using a color transform.                                                                                                    |
| [**CMTranslateRGBsExt**](/windows/win32/Wingdi/?branch=master)                                       | Translates bitmap colors with callback progress reporting.                                                                                           |
| [**ColorCorrectPalette**](/windows/win32/Wingdi/nf-wingdi-colorcorrectpalette?branch=master)                                     | Corrects the entries in a palette for a device context.                                                                                              |
| [**ColorMatchToTarget**](/windows/win32/Wingdi/nf-wingdi-colormatchtotarget?branch=master)                                       | Performs color mapping for preview purposes.                                                                                                         |
| [**ConvertColorNameToIndex**](convertcolornametoindex.md)                             | Converts color names in a named color space to index numbers in a color profile.                                                                     |
| [**ConvertIndexToColorName**](convertindextocolorname.md)                             | Converts indices in a color space to an array of names in a named color space.                                                                       |
| [**CreateColorSpace**](/windows/win32/Wingdi/nf-wingdi-createcolorspacea?branch=master)                                           | Creates a color space.                                                                                                                               |
| [**CreateColorTransform**](createcolortransform.md)                                   | Creates a color transform.                                                                                                                           |
| [CreateDeviceLinkProfile](createdevicelinkprofile.md)                                 | Creates an ICC device-link profile.                                                                                                                  |
| [**CreateMultiProfileTransform**](createmultiprofiletransform.md)                     | Creates a transform from multiple profiles.                                                                                                          |
| [**CreateProfileFromLogColorSpace**](createprofilefromlogcolorspace.md)               | Creates a device profile from a logical color space                                                                                                  |
| [**DeleteColorSpace**](/windows/win32/Wingdi/nf-wingdi-deletecolorspace?branch=master)                                           | Deletes a color space.                                                                                                                               |
| [**DeleteColorTransform**](deletecolortransform.md)                                   | Deletes a color transform.                                                                                                                           |
| [**DisassociateColorProfileFromDevice**](disassociatecolorprofilefromdevice.md)       | Disassociates a color profile from a device.                                                                                                         |
| [**EnumColorProfiles**](enumcolorprofiles.md)                                         | Enumerates color profiles satisfying specified criteria.                                                                                             |
| [**EnumICMProfiles**](/windows/win32/Wingdi/nf-wingdi-enumicmprofilesa?branch=master)                                             | Enumerates output color profiles available for a given device context.                                                                               |
| [**EnumICMProfilesProcCallback**](/windows/win32/Wingdi/?branch=master)                     | Application-defined callback function for [**EnumICMProfiles**](/windows/win32/Wingdi/nf-wingdi-enumicmprofilesa?branch=master).                                                                |
| [**GetCMMInfo**](getcmminfo.md)                                                       | Identifies the CMM that created a transform.                                                                                                         |
| [**GetColorDirectory**](getcolordirectory.md)                                         | Identifies the system color directory.                                                                                                               |
| [**GetColorProfileElement**](getcolorprofileelement.md)                               | Retrieves data from a given profile element.                                                                                                         |
| [**GetColorProfileElementTag**](getcolorprofileelementtag.md)                         | Retrieves the tag name from a profile element.                                                                                                       |
| [**GetColorProfileFromHandle**](getcolorprofilefromhandle.md)                         | Retrieves the color profile contents given a handle to an open color profile.                                                                        |
| [**GetColorProfileHeader**](getcolorprofileheader.md)                                 | Retrieves the header from a profile.                                                                                                                 |
| [**GetColorSpace**](getcolorspace.md)                                                 | Gets the current input color space in a device context.                                                                                              |
| [**GetCountColorProfileElements**](getcountcolorprofileelements.md)                   | Counts the tagged elements in a profile.                                                                                                             |
| [**GetDeviceGammaRamp**](/windows/win32/Wingdi/nf-wingdi-getdevicegammaramp?branch=master)                                       | Gets the gamma ramp from direct color display boards.                                                                                                |
| [**GetICMProfile**](/windows/win32/Wingdi/nf-wingdi-geticmprofilea?branch=master)                                                 | Gets the current output color profile of a device context.                                                                                           |
| [**GetLogColorSpace**](/windows/win32/Wingdi/nf-wingdi-getlogcolorspacea?branch=master)                                           | Gets the [**LOGCOLORSPACE**](/windows/win32/Wingdi/ns-wingdi-taglogcolorspacea?branch=master) structure of a device context.                                                                       |
| [**GetNamedProfileInfo**](getnamedprofileinfo.md)                                     | Gets information from a named color profile and stores it in a [**NAMED\_PROFILE\_INFO**](named-profile-info.md) structure.                         |
| [**GetPS2ColorRenderingDictionary**](getps2colorrenderingdictionary.md)               | Gets a PostScript color rendering dictionary.                                                                                                        |
| [**GetPS2ColorRenderingIntent**](getps2colorrenderingintent.md)                       | Gets a PostScript color rendering intents.                                                                                                           |
| [**GetPS2ColorSpaceArray**](getps2colorspacearray.md)                                 | Gets a PostScript color space from a profile.                                                                                                        |
| [**GetStandardColorSpaceProfile**](getstandardcolorspaceprofile.md)                   | Retrieves a registered standard space profile.                                                                                                       |
| [**ICMProgressProcCallback**](icmprogressproccallback.md)                             | Application-supplied callback to report progress.                                                                                                    |
| [**InstallColorProfile**](installcolorprofile.md)                                     | Installs a color profile for use in the system.                                                                                                      |
| [**IsColorProfileTagPresent**](iscolorprofiletagpresent.md)                           | Checks that a given tag is present in a profile.                                                                                                     |
| [**IsColorProfileValid**](iscolorprofilevalid.md)                                     | Checks that a profile is a valid ICC profile.                                                                                                        |
| [**OpenColorProfile**](opencolorprofile.md)                                           | Opens a profile and returns a handle to it.                                                                                                          |
| [**RegisterCMM**](registercmm.md)                                                     | Registers a CMM for use by the system.                                                                                                               |
| [**SelectCMM**](selectcmm.md)                                                         | Specifies a preferred CMM to use.                                                                                                                    |
| [**SetColorProfileElement**](setcolorprofileelement.md)                               | Writes data for a given profile element.                                                                                                             |
| [**SetColorProfileElementReference**](setcolorprofileelementreference.md)             | Creates a tag that refers to existing tag data.                                                                                                      |
| [**SetColorProfileElementSize**](setcolorprofileelementsize.md)                       | Sets the size of a given profile element.                                                                                                            |
| [**SetColorProfileHeader**](setcolorprofileheader.md)                                 | Sets the header information in a given profile.                                                                                                      |
| [**SetColorSpace**](/windows/win32/Wingdi/nf-wingdi-setcolorspace?branch=master)                                                 | Sets a device context's input color space.                                                                                                           |
| [**SetDeviceGammaRamp**](/windows/win32/Wingdi/nf-wingdi-setdevicegammaramp?branch=master)                                       | Sets the gamma ramp on direct color display boards.                                                                                                  |
| [**SetICMMode**](/windows/win32/Wingdi/nf-wingdi-seticmmode?branch=master)                                                       | Turns color management on or off in a device context.                                                                                                |
| [**SetICMProfile**](/windows/win32/Wingdi/nf-wingdi-seticmprofilea?branch=master)                                                 | Sets the output color profile for a given device context.                                                                                            |
| [**SetStandardColorSpaceProfile**](setstandardcolorspaceprofile.md)                   | Registers a profile for a standard color space.                                                                                                      |
| [**SetupColorMatching**](setupcolormatching.md)                                       | Provides user control over color management by way of a dialog box.                                                                                  |
| [**TranslateBitmapBits**](translatebitmapbits.md)                                     | Converts bitmap colors using a color transform.                                                                                                      |
| [**TranslateColors**](translatecolors.md)                                             | Converts colors using a color transform.                                                                                                             |
| [**UninstallColorProfile**](uninstallcolorprofile.md)                                 | Uninstalls a color profile from the system.                                                                                                          |
| [**UnregisterCMM**](unregistercmm.md)                                                 | Removes the CMM registration.                                                                                                                        |
| [**WcsAssociateColorProfileWithDevice**](wcsassociatecolorprofilewithdevice.md)       | Associates a specified WCS color profile with a specified device.                                                                                    |
| [**WcsCheckColors**](wcscheckcolors.md)                                               | Determines whether the colors in an array lie within the output gamut of a specified WCS color transform.                                            |
| [**WcsCreateIccProfile**](wcscreateiccprofile.md)                                     | Converts a WCS profile into an ICC profile.                                                                                                          |
| [**WcsDisassociateColorProfileFromDevice**](wcsdisassociatecolorprofilefromdevice.md) | Disassociates a specified WCS color profile with a specified device on a specified computer.                                                         |
| [**WcsEnumColorProfiles**](wcsenumcolorprofiles.md)                                   | Enumerates all color profiles that satisfy the enumeration criteria in the specified profile management scope.                                       |
| [**WcsEnumColorProfilesSize**](wcsenumcolorprofilessize.md)                           | Returns the size, in bytes, of the buffer required by the [**WcsEnumColorProfiles**](wcsenumcolorprofiles.md) function to enumerate color profiles. |
| [**WcsGetCalibrationManagementState**](wcsgetcalibrationmanagementstate.md)           | Determines whether system management of the display calibration state is enabled.                                                                    |
| [**WcsGetDefaultColorProfile**](wcsgetdefaultcolorprofile.md)                         | Retrieves the default color profile for a device, or the device-independent default if the device is not specified.                                  |
| [**WcsGetDefaultColorProfileSize**](wcsgetdefaultcolorprofilesize.md)                 | Returns the size, in bytes, of the default color profile name for a device, including the **NULL** terminator.                                       |
| [**WcsGetDefaultRenderingIntent**](wcsgetdefaultrenderingintent.md)                   | Returns the user or system-wide rendering intent.                                                                                                    |
| [**WcsGetUsePerUserProfiles**](wcsgetuseperuserprofiles.md)                           | Determines whether the user has chosen to use a per-user profile association list for the specified device.                                          |
| [**WcsOpenColorProfile**](wcsopencolorprofile.md)                                     | Creates a handle to a specified color profile.                                                                                                       |
| [**WcsSetCalibrationManagementState**](wcssetcalibrationmanagementstate.md)           | Enables or disables system management of the display calibration state.                                                                              |
| [**WcsSetDefaultColorProfile**](wcssetdefaultcolorprofile.md)                         | Sets the default color profile name of the specified profile type in the specified profile management scope.                                         |
| [**WcsSetDefaultRenderingIntent**](wcssetdefaultrenderingintent.md)                   | Sets the user or system-wide rendering intent.                                                                                                       |
| [**WcsSetUsePerUserProfiles**](wcssetuseperuserprofiles.md)                           | Allows the user to specify whether or not to use a per-user profile association list for the specified device.                                       |
| [**WcsTranslateColors**](wcstranslatecolors.md)                                       | Translates an array of colors from the source color space to the destination color space as defined by a color transform.                            |



 

 

 




