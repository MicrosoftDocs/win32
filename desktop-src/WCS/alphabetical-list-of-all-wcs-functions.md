---
title: Alphabetical List of All WCS Functions
description: The following is a complete alphabetical list of the WCS 1.0 API functions provided by Windows \ 160;98 and later and Windows \ 160;2000 and later.
ms.assetid: 'aba45dbd-6fc2-4788-87f0-043579fa53f9'
keywords: ["Windows Color System (WCS),functions", "WCS (Windows Color System),functions", "image color management,functions", "color management,functions", "colors,functions", "WCS reference,functions", "reference for WCS,functions"]
---

# Alphabetical List of All WCS Functions

The following is a complete alphabetical list of the WCS 1.0 API functions provided by Windows 98 and later and Windows 2000 and later.



| Function or Structure                                                                  | Description                                                                                                                                          |
|----------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------|
| [*ApplyCallbackFunction*](apply.md)                                                   | Callback function that can be used to update WCS configuration data.                                                                                 |
| [**AssociateColorProfileWithDevice**](associatecolorprofilewithdevice.md)             | Associates a color profile with a device.                                                                                                            |
| [**CheckBitmapBits**](checkbitmapbits.md)                                             | Checks bitmap colors against a gamut.                                                                                                                |
| [**CheckColors**](checkcolors.md)                                                     | Checks colors against a device output gamut.                                                                                                         |
| [**CheckColorsInGamut**](checkcolorsingamut.md)                                       | Checks if given colors are in a device's gamut.                                                                                                      |
| [**CloseColorProfile**](closecolorprofile.md)                                         | Closes a profile.                                                                                                                                    |
| [**CMCheckColors**](cmcheckcolors.md)                                                 | Checks colors against an output gamut.                                                                                                               |
| [**CMCheckColorsInGamut**](cmcheckcolorsingamut.md)                                   | Checks RGB triplets against an output gamut.                                                                                                         |
| [**CMCheckRGBs**](cmcheckrgbs.md)                                                     | Checks bitmap colors against an output gamut.                                                                                                        |
| [**CMConvertColorNameToIndex**](cmconvertcolornametoindex.md)                         | Converts color names in a named color space to index numbers in a color profile.                                                                     |
| [**CMConvertIndexToColorName**](cmconvertindextocolorname.md)                         | Converts indices in a color space to an array of names in a named color space.                                                                       |
| [**CMCreateDeviceLinkProfile**](cmcreatedevicelinkprofile.md)                         | Creates an ICC device link profile.                                                                                                                  |
| [**CMCreateMultiProfileTransform**](cmcreatemultiprofiletransform.md)                 | Creates a transform from an array of profiles.                                                                                                       |
| [**CMCreateProfile**](cmcreateprofile.md)                                             | Creates an ICC profile from a [**LOGCOLORSPACE**](logcolorspace.md) structure (ANSI).                                                               |
| [**CMCreateProfileW**](cmcreateprofilew.md)                                           | Creates an ICC profile from a [**LOGCOLORSPACE**](logcolorspace.md) structure (Unicode).                                                            |
| [CMCreateTransform](cmcreatetransform.md)                                             | Creates a color transform (ANSI).                                                                                                                    |
| [**CMCreateTransformExt**](cmcreatetransformext.md)                                   | Creates an extended color transform (ANSI).                                                                                                          |
| [**CMCreateTransformExtW**](cmcreatetransformextw.md)                                 | Creates an extended color transform (Unicode).                                                                                                       |
| [CMCreateTransformW](cmcreatetransformw.md)                                           | Creates a color transform (Unicode).                                                                                                                 |
| [**CMDeleteTransform**](cmdeletetransform.md)                                         | Deletes a color transform.                                                                                                                           |
| [**CMGetInfo**](cmgetinfo.md)                                                         | Returns information about a given CMM.                                                                                                               |
| [**CMGetNamedProfileInfo**](cmgetnamedprofileinfo.md)                                 | Retrieves information about a named color profile.                                                                                                   |
| [**CMGetPS2ColorRenderingDictionary**](cmgetps2colorrenderingdictionary.md)           | Gets a PostScript color rendering dictionary.                                                                                                        |
| [**CMGetPS2ColorRenderingIntent**](cmgetps2colorrenderingintent.md)                   | Gets a PostScript color rendering intent.                                                                                                            |
| [**CMGetPS2ColorSpaceArray**](cmgetps2colorspacearray.md)                             | Gets a PostScript color space array.                                                                                                                 |
| [**CMIsProfileValid**](cmisprofilevalid.md)                                           | Checks that a profile is a valid ICC profile.                                                                                                        |
| [**CMTranslateColors**](cmtranslatecolors.md)                                         | Translates colors using a color transform.                                                                                                           |
| [**CMTranslateRGB**](cmtranslatergb.md)                                               | Translates an RGB color using a color transform.                                                                                                     |
| [**CMTranslateRGBs**](cmtranslatergbs.md)                                             | Translates bitmap colors using a color transform.                                                                                                    |
| [**CMTranslateRGBsExt**](cmtranslatergbsext.md)                                       | Translates bitmap colors with callback progress reporting.                                                                                           |
| [**ColorCorrectPalette**](colorcorrectpalette.md)                                     | Corrects the entries in a palette for a device context.                                                                                              |
| [**ColorMatchToTarget**](colormatchtotarget.md)                                       | Performs color mapping for preview purposes.                                                                                                         |
| [**ConvertColorNameToIndex**](convertcolornametoindex.md)                             | Converts color names in a named color space to index numbers in a color profile.                                                                     |
| [**ConvertIndexToColorName**](convertindextocolorname.md)                             | Converts indices in a color space to an array of names in a named color space.                                                                       |
| [**CreateColorSpace**](createcolorspace.md)                                           | Creates a color space.                                                                                                                               |
| [**CreateColorTransform**](createcolortransform.md)                                   | Creates a color transform.                                                                                                                           |
| [CreateDeviceLinkProfile](createdevicelinkprofile.md)                                 | Creates an ICC device-link profile.                                                                                                                  |
| [**CreateMultiProfileTransform**](createmultiprofiletransform.md)                     | Creates a transform from multiple profiles.                                                                                                          |
| [**CreateProfileFromLogColorSpace**](createprofilefromlogcolorspace.md)               | Creates a device profile from a logical color space                                                                                                  |
| [**DeleteColorSpace**](deletecolorspace.md)                                           | Deletes a color space.                                                                                                                               |
| [**DeleteColorTransform**](deletecolortransform.md)                                   | Deletes a color transform.                                                                                                                           |
| [**DisassociateColorProfileFromDevice**](disassociatecolorprofilefromdevice.md)       | Disassociates a color profile from a device.                                                                                                         |
| [**EnumColorProfiles**](enumcolorprofiles.md)                                         | Enumerates color profiles satisfying specified criteria.                                                                                             |
| [**EnumICMProfiles**](enumicmprofiles.md)                                             | Enumerates output color profiles available for a given device context.                                                                               |
| [**EnumICMProfilesProcCallback**](enumicmprofilesproccallback.md)                     | Application-defined callback function for [**EnumICMProfiles**](enumicmprofiles.md).                                                                |
| [**GetCMMInfo**](getcmminfo.md)                                                       | Identifies the CMM that created a transform.                                                                                                         |
| [**GetColorDirectory**](getcolordirectory.md)                                         | Identifies the system color directory.                                                                                                               |
| [**GetColorProfileElement**](getcolorprofileelement.md)                               | Retrieves data from a given profile element.                                                                                                         |
| [**GetColorProfileElementTag**](getcolorprofileelementtag.md)                         | Retrieves the tag name from a profile element.                                                                                                       |
| [**GetColorProfileFromHandle**](getcolorprofilefromhandle.md)                         | Retrieves the color profile contents given a handle to an open color profile.                                                                        |
| [**GetColorProfileHeader**](getcolorprofileheader.md)                                 | Retrieves the header from a profile.                                                                                                                 |
| [**GetColorSpace**](getcolorspace.md)                                                 | Gets the current input color space in a device context.                                                                                              |
| [**GetCountColorProfileElements**](getcountcolorprofileelements.md)                   | Counts the tagged elements in a profile.                                                                                                             |
| [**GetDeviceGammaRamp**](getdevicegammaramp.md)                                       | Gets the gamma ramp from direct color display boards.                                                                                                |
| [**GetICMProfile**](geticmprofile.md)                                                 | Gets the current output color profile of a device context.                                                                                           |
| [**GetLogColorSpace**](getlogcolorspace.md)                                           | Gets the [**LOGCOLORSPACE**](logcolorspace.md) structure of a device context.                                                                       |
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
| [**SetColorSpace**](setcolorspace.md)                                                 | Sets a device context's input color space.                                                                                                           |
| [**SetDeviceGammaRamp**](setdevicegammaramp.md)                                       | Sets the gamma ramp on direct color display boards.                                                                                                  |
| [**SetICMMode**](seticmmode.md)                                                       | Turns color management on or off in a device context.                                                                                                |
| [**SetICMProfile**](seticmprofile.md)                                                 | Sets the output color profile for a given device context.                                                                                            |
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



 

 

 




