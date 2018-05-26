---
Description: Windows Color System
ms.assetid: 9297de48-c327-4e8b-9563-b2c7b15408fa
title: Windows Color System
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Windows Color System

This section describes the functions, interfaces, and enumerations defined for the Windows Color System (WCS), which is available beginning with Windows Vista. The following topics are provided.

**Functions**

<dl>

[CheckBitmapBits](http://msdn.microsoft.com/en-us/library/windows/desktop/dd371821.aspx)  
[CheckColors](http://msdn.microsoft.com/en-us/library/windows/desktop/dd371823.aspx)  
[TranslateBitmapBits](http://msdn.microsoft.com/en-us/library/windows/desktop/dd372203.aspx)  
[TranslateColors](http://msdn.microsoft.com/en-us/library/windows/desktop/dd372204.aspx)  
[**WcsCheckColors**](wcscheckcolors.md)  
[**WcsTranslateColors**](wcstranslatecolors.md)  
</dl>

**Enumerations**

<dl>

[**BMFORMAT**](bmformat.md)  
[**COLORDATATYPE**](colordatatype.md)  
[**COLORTYPE**](colortype.md)  
</dl>

**Color Profile Management**

The following functions and enumerations support both WCS and Image Color Management (ICM) 2.0 pixel formats. They supplement the existing ICM 2.0 functions and enumerations (described in the Windows SDK documentation).

**Functions**

<dl>

[**WcsAssociateColorProfileWithDevice**](wcsassociatecolorprofilewithdevice.md)  
[**WcsCreateIccProfile**](wcscreateiccprofile.md)  
[**WcsDisassociateColorProfileFromDevice**](wcsdisassociatecolorprofilefromdevice.md)  
[**WcsEnumColorProfiles**](wcsenumcolorprofiles.md)  
[**WcsEnumColorProfilesSize**](wcsenumcolorprofilessize.md)  
[**WcsGetDefaultColorProfile**](wcsgetdefaultcolorprofile.md)  
[**WcsGetDefaultColorProfileSize**](wcsgetdefaultcolorprofilesize.md)  
[**WcsGetUsePerUserProfiles**](wcsgetuseperuserprofiles.md)  
[**WcsOpenColorProfile**](wcsopencolorprofile.md)  
[**WcsSetDefaultColorProfile**](wcssetdefaultcolorprofile.md)  
[**WcsSetUsePerUserProfiles**](wcssetuseperuserprofiles.md)  
</dl>

**Enumerations**

<dl>

[**COLORPROFILESUBTYPE**](colorprofilesubtype.md)  
[**COLORPROFILETYPE**](colorprofiletype.md)  
[**WCS\_PROFILE\_MANAGEMENT\_SCOPE**](wcs-profile-management-scope.md)  
</dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bprint\print%5D:%20Windows%20Color%20System%20%20RELEASE:%20%285/12/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/en-us/default.aspx. "Send comments about this topic to Microsoft")



