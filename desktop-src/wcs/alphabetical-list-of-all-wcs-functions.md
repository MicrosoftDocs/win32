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
ms.localizationpriority: high


ms.topic: article
ms.date: 05/31/2018
---

# Alphabetical List of All WCS Functions

The following is a complete alphabetical list of the WCS 1.0 API functions provided by Windows 98 and later and Windows 2000 and later.



| Function or Structure                                                                 | Description                                                                                                                                          |
|---------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**PCMSCALLBACKW**](/windows/win32/api/icm/nc-icm-pcmscallbackw) | \**PCMSCALLBACKW** (or **ApplyCallbackFunction**) is a callback function that you implement that updates the WCS configuration data while the dialog box displayed by the [**SetupColorMatching**](setupcolormatching.md) function is executing. |
| [**AssociateColorProfileWithDeviceW**](/windows/win32/api/icm/nf-icm-associatecolorprofilewithdevicew)             | Associates a specified color profile with a specified device.                                                                                                            |
| [**CheckBitmapBits**](/windows/win32/api/icm/nf-icm-checkbitmapbits) | Checks whether the pixels in a specified bitmap lie within the output [gamut](g.md) of a specified transform. |
| [**CheckColors**](/windows/win32/api/icm/nf-icm-checkbitmapbits) | Determines whether the colors in an array lie within the output [gamut](g.md) of a specified transform. |
| [**CheckColorsInGamut**](/windows/desktop/api/Wingdi/nf-wingdi-checkcolorsingamut)                                       | Checks if given colors are in a device's gamut.                                                                                                      |
| [**CloseColorProfile**](/windows/win32/api/icm/nf-icm-closecolorprofile) | Closes an open profile handle. |
| [**CMCheckColors**](/windows/win32/api/icm/nf-icm-cmcheckcolors) | Determines whether given colors lie within the output [gamut](/windows/win32/wcs/g) of a specified transform. |
| [**CMCheckColorsInGamut**](/windows/win32/api/icm/nf-icm-cmcheckcolorsingamut) | Determines whether specified RGB triples lie in the output [gamut](/windows/win32/wcs/g) of a specified transform. |
| [**CMCheckRGBs**](/windows/desktop/api/Wingdi/)                                                     | Checks bitmap colors against an output gamut.                                                                                                        |
| [**CMConvertColorNameToIndex**](/windows/win32/api/icm/nf-icm-cmconvertcolornametoindex) | Converts color names in a named color space to index numbers in a color profile |
| [**CMConvertIndexToColorName**](/windows/win32/api/icm/nf-icm-cmconvertindextocolorname) | Transforms indices in a color space to an array of names in a named color space. |
| [**CMCreateDeviceLinkProfile**](/windows/win32/api/icm/nf-icm-cmcreatedevicelinkprofile) | Creates a [device link profile](/windows/win32/wcs/d) in the format specified by the International Color Consortium in its ICC Profile Format Specification. |
| [**CMCreateMultiProfileTransform**](/windows/win32/api/icm/nf-icm-cmcreatemultiprofiletransform) | Accepts an array of profiles or a single [device link profile](/windows/win32/wcs/d) and creates a color transform. This transform is a mapping from the color space specified by the first profile to that of the second profile and so on to the last one. |
| [**CMCreateProfile**](/windows/win32/api/icm/nf-icm-cmcreateprofile) | Creates a display color profile from a [**LOGCOLORSPACEA**](/windows/win32/api/wingdi/ns-wingdi-logcolorspacea) structure. |
| [**CMCreateProfileW**](/windows/win32/api/icm/nf-icm-cmcreateprofilew) | Creates a display color profile from a [**LOGCOLORSPACEW**](/windows/win32/api/wingdi/ns-wingdi-logcolorspacew) structure. |
| [**CMCreateTransform**](/windows/win32/api/icm/nf-icm-cmcreatetransform) | Deprecated. There is no replacement API because this one was no longer being used. Developers of alternate CMM modules are not required to implement it. |
| [**CMCreateTransformExt**](/windows/win32/api/icm/nf-icm-cmcreatetransformext) | Creates a color transform that maps from an input [**LOGCOLORSPACEA**](/windows/win32/api/wingdi/ns-wingdi-logcolorspacea) to an optional target space and then to an output device, using a set of flags that define how the transform should be created. |
| [**CMCreateTransformExtW**](/windows/win32/api/icm/nf-icm-cmcreatetransformextw) | Creates a color transform that maps from an input [**LOGCOLORSPACEW**](/windows/win32/api/wingdi/ns-wingdi-logcolorspacew) to an optional target space and then to an output device, using a set of flags that define how the transform should be created. |
| [**CMCreateTransformW**](/windows/win32/api/icm/nf-icm-cmcreatetransformw) | Deprecated. There is no replacement API because this one was no longer being used. Developers of alternate CMM modules are not required to implement it. |
| [**CMDeleteTransform**](/windows/win32/api/icm/nf-icm-cmdeletetransform) | Deletes a specified color transform, and frees any memory associated with it. |
| [**CMGetInfo**](/windows/win32/api/icm/nf-icm-cmgetinfo) | Retrieves various information about the color management module (CMM). |
| [**CMGetNamedProfileInfo**](/windows/win32/api/icm/nf-icm-cmgetnamedprofileinfo) | Retrieves information about the specified named color profile. |
| [**CMGetPS2ColorRenderingDictionary**](/windows/desktop/api/Wingdi/)           | Gets a PostScript color rendering dictionary.                                                                                                        |
| [**CMGetPS2ColorRenderingIntent**](/windows/win32/api/icm/nf-icm-cmgetps2colorrenderingintent) | Retrieves the PostScript Level 2 color [rendering intent](ms536500\(v=vs.85\).md) from a profile. |
| [**CMGetPS2ColorSpaceArray**](/windows/desktop/api/Wingdi/)                             | Gets a PostScript color space array.                                                                                                                 |
| [**CMIsProfileValid**](/windows/win32/api/icm/nf-icm-cmisprofilevalid) | Reports whether the given profile is a valid ICC profile that can be used for color management. |
| [**CMTranslateColors**](/windows/win32/api/icm/nf-icm-cmtranslatecolors) | Translates an array of colors from a source [color space](ms536506\(v=vs.85\).md) to a destination color space using a color transform. |
| [**CMTranslateRGB**](/windows/win32/api/icm/nf-icm-cmtranslatergb) | Translates an application-supplied RGBQuad into the device [color space](https://msdn.microsoft.com/en-us/library/dd371818\(v=vs.85\)). |
| [**CMTranslateRGBs**](/windows/win32/api/icm/nf-icm-cmtranslatergbs) | Translates a bitmap from one [color space](https://msdn.microsoft.com/en-us/library/dd371818\(v=vs.85\)) to another using a color transform. |
| [**CMTranslateRGBsExt**](/windows/win32/api/icm/nf-icm-cmtranslatergbsext) | Translates a bitmap from one defined format into a different defined format and calls a callback function periodically, if one is specified, to report progress and permit the calling application to terminate the translation. |
| [**ColorCorrectPalette**](/windows/desktop/api/Wingdi/nf-wingdi-colorcorrectpalette)                                     | Corrects the entries in a palette for a device context.                                                                                              |
| [**ColorMatchToTarget**](/windows/desktop/api/Wingdi/nf-wingdi-colormatchtotarget)                                       | Performs color mapping for preview purposes.                                                                                                         |
| [**ConvertColorNameToIndex**](/windows/win32/api/icm/nf-icm-convertcolornametoindex) | Converts color names in a named color space to index numbers in an International Color Consortium (ICC) color profile. |
| [**ConvertIndexToColorName**](/windows/win32/api/icm/nf-icm-convertindextocolorname) | Transforms indices in a color space to an array of names in a named color space. |
| [**CreateColorSpace**](/windows/desktop/api/Wingdi/nf-wingdi-createcolorspacea)                                           | Creates a color space.                                                                                                                               |
| [**CreateColorTransformW**](/windows/win32/api/icm/nf-icm-createcolortransforma) | Transforms indices in a color space to an array of names in a named color space. |
| [**CreateColorTransformW**](/windows/win32/api/icm/nf-icm-createcolortransformw) | Transforms indices in a color space to an array of names in a named color space. |
| [**CreateMultiProfileTransform**](/windows/win32/api/icm/nf-icm-createmultiprofiletransform) | Accepts an array of profiles or a single [device link profile](d.md) and creates a color transform that applications can use to perform color mapping. |
| [**CreateProfileFromLogColorSpaceW**]((/windows/win32/api/icm/nf-icm-createprofilefromlogcolorspacew) | Converts a logical [color space](c.md) to a [device profile](d.md). |
| [**DeleteColorSpace**](/windows/desktop/api/Wingdi/nf-wingdi-deletecolorspace)                                           | Deletes a color space.                                                                                                                               |
| [**DeleteColorTransform**](deletecolortransform.md)                                   | Deletes a color transform.                                                                                                                           |
| [**DisassociateColorProfileFromDevice**](disassociatecolorprofilefromdevice.md)       | Disassociates a color profile from a device.                                                                                                         |
| [**EnumColorProfiles**](enumcolorprofiles.md)                                         | Enumerates color profiles satisfying specified criteria.                                                                                             |
| [**EnumICMProfiles**](/windows/desktop/api/Wingdi/nf-wingdi-enumicmprofilesa)                                             | Enumerates output color profiles available for a given device context.                                                                               |
| [**EnumICMProfilesProcCallback**](/windows/desktop/api/Wingdi/)                     | Application-defined callback function for [**EnumICMProfiles**](/windows/desktop/api/Wingdi/nf-wingdi-enumicmprofilesa).                                                                |
| [**GetCMMInfo**](getcmminfo.md)                                                       | Identifies the CMM that created a transform.                                                                                                         |
| [**GetColorDirectory**](getcolordirectory.md)                                         | Identifies the system color directory.                                                                                                               |
| [**GetColorProfileElement**](getcolorprofileelement.md)                               | Retrieves data from a given profile element.                                                                                                         |
| [**GetColorProfileElementTag**](getcolorprofileelementtag.md)                         | Retrieves the tag name from a profile element.                                                                                                       |
| [**GetColorProfileFromHandle**](getcolorprofilefromhandle.md)                         | Retrieves the color profile contents given a handle to an open color profile.                                                                        |
| [**GetColorProfileHeader**](getcolorprofileheader.md)                                 | Retrieves the header from a profile.                                                                                                                 |
| [**GetColorSpace**](getcolorspace.md)                                                 | Gets the current input color space in a device context.                                                                                              |
| [**GetCountColorProfileElements**](getcountcolorprofileelements.md)                   | Counts the tagged elements in a profile.                                                                                                             |
| [**GetDeviceGammaRamp**](/windows/desktop/api/Wingdi/nf-wingdi-getdevicegammaramp)                                       | Gets the gamma ramp from direct color display boards.                                                                                                |
| [**GetICMProfile**](/windows/desktop/api/Wingdi/nf-wingdi-geticmprofilea)                                                 | Gets the current output color profile of a device context.                                                                                           |
| [**GetLogColorSpace**](/windows/desktop/api/Wingdi/nf-wingdi-getlogcolorspacea)                                           | Gets the [**LOGCOLORSPACE**](/windows/desktop/api/Wingdi/ns-wingdi-taglogcolorspacea) structure of a device context.                                                                       |
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
| [**SetColorSpace**](/windows/desktop/api/Wingdi/nf-wingdi-setcolorspace)                                                 | Sets a device context's input color space.                                                                                                           |
| [**SetDeviceGammaRamp**](/windows/desktop/api/Wingdi/nf-wingdi-setdevicegammaramp)                                       | Sets the gamma ramp on direct color display boards.                                                                                                  |
| [**SetICMMode**](/windows/desktop/api/Wingdi/nf-wingdi-seticmmode)                                                       | Turns color management on or off in a device context.                                                                                                |
| [**SetICMProfile**](/windows/desktop/api/Wingdi/nf-wingdi-seticmprofilea)                                                 | Sets the output color profile for a given device context.                                                                                            |
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



 

 

 




