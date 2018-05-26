---
title: Whats New in Windows Vista
description: Version 1.0 of Image Color Management (ICM) was delivered in Microsoft Windows 95, and provides basic color management capabilities within Windows device contexts.
ms.assetid: 3079f84c-0d6c-4f87-a041-de86f5f7d99b
keywords:
- Windows Color System (WCS),Windows Vista
- WCS (Windows Color System),Windows Vista
- image color management,Windows Vista
- color management,Windows Vista
- colors,Windows Vista
- Windows Color System (WCS),operating systems
- WCS (Windows Color System),operating systems
- image color management,operating systems
- color management,operating systems
- colors,operating systems
- Image Color Management (ICM)
- ICM (Image Color Management)
- Windows Vista color management
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# What's New in Windows Vista

Version 1.0 of Image Color Management (ICM) was delivered in Microsoft Windows 95, and provides basic color management capabilities within Windows device contexts.

ICM version 2.0 was delivered in Windows 98, Windows Millennium Edition, Windows 2000, and WindowsXP and included a variety of new functions that implemented color management outside of device contexts. These new functions were suitable for more demanding color management requirements, and gave applications greater control over the color-management process.

With the release of Windows Vista, ICM 2.0 is now included in Windows Color System (WCS) 1.0, which adds more functionality. The following table lists new application programming interfaces (API) that ship in Windows Vista.

## New API Shipping in Windows Vista



Enumerations

API Name

Header

Library

[**COLORDATATYPE**](colordatatype.md)

icm.h

mscms.lib

[**COLORPROFILESUBTYPE**](colorprofilesubtype.md)

icm.h

mscms.lib

[**COLORPROFILETYPE**](colorprofiletype.md)

icm.h

mscms.lib

[**WCS\_PROFILE\_MANAGEMENT\_SCOPE**](wcs-profile-management-scope.md)

icm.h

mscms.lib



 



Functions

API Name

Header

Library

[**WcsAssociateColorProfileWithDevice**](wcsassociatecolorprofilewithdevice.md)

icm.h

mscms.lib

[**WcsCheckColors**](wcscheckcolors.md)

icm.h

mscms.lib

[**WcsCreateIccProfile**](wcscreateiccprofile.md)

icm.h

mscms.lib

[**WcsDisassociateColorProfileFromDevice**](wcsdisassociatecolorprofilefromdevice.md)

icm.h

mscms.lib

[**WcsEnumColorProfiles**](wcsenumcolorprofiles.md)

icm.h

mscms.lib

[**WcsEnumColorProfilesSize**](wcsenumcolorprofilessize.md)

icm.h

mscms.lib

[**WcsGetDefaultColorProfile**](wcsgetdefaultcolorprofile.md)

icm.h

mscms.lib

[**WcsGetDefaultColorProfileSize**](wcsgetdefaultcolorprofilesize.md)

icm.h

mscms.lib

[**WcsGetDefaultRenderingIntent**](wcsgetdefaultrenderingintent.md)

icm.h

mscms.lib

[**WcsGetUsePerUserProfiles**](wcsgetuseperuserprofiles.md)

icm.h

mscms.lib

[**WcsOpenColorProfile**](wcsopencolorprofile.md)

icm.h

mscms.lib

[**WcsSetDefaultColorProfile**](wcssetdefaultcolorprofile.md)

icm.h

mscms.lib

[**WcsSetDefaultRenderingIntent**](wcssetdefaultrenderingintent.md)

icm.h

mscms.lib

[**WcsSetUsePerUserProfiles**](wcssetuseperuserprofiles.md)

icm.h

mscms.lib

[**WcsTranslateColors**](wcstranslatecolors.md)

icm.h

mscms.lib



 



Interfaces and Their Functions

API Name

Header

Library

[**IDeviceModelPlugin**](/windows/previous-versions/wcsplugin/nn-wcsplugin-idevicemodelplugin?branch=master)

WcsPlugIn.h

N/A

[**IDeviceModelPlugin::ColorimetricToDeviceColors**](https://msdn.microsoft.com/library/windows/desktop/dd372120)

WcsPlugIn.h

N/A

[**IDeviceModelPlugin::ColorimetricToDeviceColorsWithBlack**](https://msdn.microsoft.com/library/windows/desktop/dd372122)

WcsPlugIn.h

N/A

[**IDeviceModelPlugin::DeviceToColorimetricColors**](https://msdn.microsoft.com/library/windows/desktop/dd372126)

WcsPlugIn.h

N/A

[**IDeviceModelPlugin::GetGamutBoundaryMesh**](https://msdn.microsoft.com/library/windows/desktop/dd372127)

WcsPlugIn.h

N/A

[**IDeviceModelPlugin::GetGamutBoundaryMeshSize**](https://msdn.microsoft.com/library/windows/desktop/dd372132)

WcsPlugIn.h

N/A

[**IDeviceModelPlugin::GetNeutralAxis**](https://msdn.microsoft.com/library/windows/desktop/dd372135)

WcsPlugIn.h

N/A

[**IDeviceModelPlugin::GetNeutralAxisSize**](https://msdn.microsoft.com/library/windows/desktop/dd372137)

WcsPlugIn.h

N/A

[**IDeviceModelPlugin::GetNumChannels**](https://msdn.microsoft.com/library/windows/desktop/dd372139)

WcsPlugIn.h

N/A

[**IDeviceModelPlugin::GetPrimarySamples**](https://msdn.microsoft.com/library/windows/desktop/dd372141)

WcsPlugIn.h

N/A

[**IDeviceModelPlugin::Initialize**](https://msdn.microsoft.com/library/windows/desktop/dd372143)

WcsPlugIn.h

N/A

[**IDeviceModelPlugin::SetTransformDeviceModelInfo**](https://msdn.microsoft.com/library/windows/desktop/dd372145)

WcsPlugIn.h

N/A

[**IGamutMapModelPlugin**](/windows/previous-versions/wcsplugin/nn-wcsplugin-igamutmapmodelplugin?branch=master)

WcsPlugIn.h

N/A

[**IGamutMapModelPlugin::Initialize**](https://msdn.microsoft.com/library/windows/desktop/dd372148)

WcsPlugIn.h

N/A

[**IGamutMapModelPlugin::SourceToDestinationAppearanceColors**](https://msdn.microsoft.com/library/windows/desktop/dd372151)

WcsPlugIn.h

N/A



 



Structures

API Name

Header

Library

[**BlackInformation**](/windows/previous-versions/WcsPlugIn/ns-wcsplugin-_blackinformation?branch=master)

WcsPlugIn.h

N/A

[**GamutBoundaryDescription**](/windows/previous-versions/WcsPlugIn/ns-wcsplugin-_gamutboundarydescription?branch=master)

WcsPlugIn.h

N/A

[**XYZColorF**](wcs-gamut_map_model_color_structures)

WcsPlugIn.h

N/A

[**JChColorF**](wcs-gamut_map_model_color_structures)

WcsPlugIn.h

N/A

[**JabColorF**](wcs-gamut_map_model_color_structures)

WcsPlugIn.h

N/A

[**GamutShell**](/windows/previous-versions/WcsPlugIn/ns-wcsplugin-_gamutshell?branch=master)

WcsPlugIn.h

N/A

[**GamutShellTriangle**](/windows/previous-versions/WcsPlugIn/ns-wcsplugin-_gamutshelltriangle?branch=master)

WcsPlugIn.h

N/A

[**PrimaryJabColors**](/windows/previous-versions/WcsPlugIn/ns-wcsplugin-_primaryjabcolors?branch=master)

WcsPlugIn.h

N/A

[**PrimaryXYZColors**](/windows/previous-versions/WcsPlugIn/ns-wcsplugin-_primaryxyzcolors?branch=master)

WcsPlugIn.h

N/A



 

 

 




