---
title: What's New in Windows Vista
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


ms.topic: article
ms.date: 05/31/2018
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

[**COLORDATATYPE**](/windows/win32/api/icm/ne-icm-colordatatype)

icm.h

mscms.lib

[**COLORPROFILESUBTYPE**](/windows/win32/api/icm/ne-icm-colorprofilesubtype)

icm.h

mscms.lib

[**COLORPROFILETYPE**](/windows/win32/api/icm/ne-icm-colorprofiletype)

icm.h

mscms.lib

[**WCS\_PROFILE\_MANAGEMENT\_SCOPE**](/windows/win32/api/icm/ne-icm-wcs_profile_management_scope)

icm.h

mscms.lib



 



Functions

API Name

Header

Library

[**WcsAssociateColorProfileWithDevice**](/windows/win32/api/icm/nf-icm-wcsassociatecolorprofilewithdevice)

icm.h

mscms.lib

[**WcsCheckColors**](/windows/win32/api/icm/nf-icm-wcsassociatecolorprofilewithdevice)

icm.h

mscms.lib

[**WcsCreateIccProfile**](/windows/win32/api/icm/nf-icm-wcscreateiccprofile)

icm.h

mscms.lib

[**WcsDisassociateColorProfileFromDevice**](/windows/win32/api/icm/nf-icm-wcsdisassociatecolorprofilefromdevice)

icm.h

mscms.lib

[**WcsEnumColorProfiles**](/windows/win32/api/icm/nf-icm-wcsenumcolorprofiles)

icm.h

mscms.lib

[**WcsEnumColorProfilesSize**](/windows/win32/api/icm/nf-icm-wcsenumcolorprofilessize)

icm.h

mscms.lib

[**WcsGetDefaultColorProfile**](/windows/win32/api/icm/nf-icm-wcsgetdefaultcolorprofile)

icm.h

mscms.lib

[**WcsGetDefaultColorProfileSize**](/windows/win32/api/icm/nf-icm-wcsgetdefaultcolorprofilesize)

icm.h

mscms.lib

[**WcsGetDefaultRenderingIntent**](/windows/win32/api/icm/nf-icm-wcsgetdefaultrenderingintent)

icm.h

mscms.lib

[**WcsGetUsePerUserProfiles**](/windows/win32/api/icm/nf-icm-wcsgetdefaultrenderingintent)

icm.h

mscms.lib

[**WcsOpenColorProfileW**](/windows/win32/api/icm/nf-icm-wcsopencolorprofilew)

icm.h

mscms.lib

[**WcsSetDefaultColorProfile**](/windows/win32/api/icm/nf-icm-wcssetdefaultcolorprofile)

icm.h

mscms.lib

[**WcsSetDefaultRenderingIntent**](/windows/win32/api/icm/nf-icm-wcssetdefaultrenderingintent)

icm.h

mscms.lib

[**WcsSetUsePerUserProfiles**](/windows/win32/api/icm/nf-icm-wcssetuseperuserprofiles)

icm.h

mscms.lib

[**WcsTranslateColors**](/windows/win32/api/icm/nf-icm-wcstranslatecolors)

icm.h

mscms.lib



 



Interfaces and Their Functions

API Name

Header

Library

[**IDeviceModelPlugin**](/previous-versions/windows/desktop/api/wcsplugin/nn-wcsplugin-idevicemodelplugin)

WcsPlugIn.h

N/A

[**IDeviceModelPlugin::ColorimetricToDeviceColors**](/windows/win32/api/wcsplugin/nf-wcsplugin-idevicemodelplugin-colorimetrictodevicecolors)

WcsPlugIn.h

N/A

[**IDeviceModelPlugin::ColorimetricToDeviceColorsWithBlack**](/windows/win32/api/wcsplugin/nf-wcsplugin-idevicemodelplugin-colorimetrictodevicecolorswithblack)

WcsPlugIn.h

N/A

[**IDeviceModelPlugin::DeviceToColorimetricColors**](/windows/win32/api/wcsplugin/nf-wcsplugin-idevicemodelplugin-devicetocolorimetriccolors)

WcsPlugIn.h

N/A

[**IDeviceModelPlugin::GetGamutBoundaryMesh**](/windows/win32/api/wcsplugin/nf-wcsplugin-idevicemodelplugin-getgamutboundarymesh)

WcsPlugIn.h

N/A

[**IDeviceModelPlugin::GetGamutBoundaryMeshSize**](/windows/win32/api/wcsplugin/nf-wcsplugin-idevicemodelplugin-getgamutboundarymeshsize)

WcsPlugIn.h

N/A

[**IDeviceModelPlugin::GetNeutralAxis**](/windows/win32/api/wcsplugin/nf-wcsplugin-idevicemodelplugin-getneutralaxis)

WcsPlugIn.h

N/A

[**IDeviceModelPlugin::GetNeutralAxisSize**](/windows/win32/api/wcsplugin/nf-wcsplugin-idevicemodelplugin-getneutralaxissize)

WcsPlugIn.h

N/A

[**IDeviceModelPlugin::GetNumChannels**](/windows/win32/api/wcsplugin/nf-wcsplugin-idevicemodelplugin-getnumchannels)

WcsPlugIn.h

N/A

[**IDeviceModelPlugin::GetPrimarySamples**](/windows/win32/api/wcsplugin/nf-wcsplugin-idevicemodelplugin-getprimarysamples)

WcsPlugIn.h

N/A

[**IDeviceModelPlugin::Initialize**](/windows/win32/api/wcsplugin/nf-wcsplugin-idevicemodelplugin-initialize)

WcsPlugIn.h

N/A

[**IDeviceModelPlugin::SetTransformDeviceModelInfo**](/windows/win32/api/wcsplugin/nf-wcsplugin-idevicemodelplugin-settransformdevicemodelinfo)

WcsPlugIn.h

N/A

[**IGamutMapModelPlugin**](/previous-versions/windows/desktop/api/wcsplugin/nn-wcsplugin-igamutmapmodelplugin)

WcsPlugIn.h

N/A

[**IGamutMapModelPlugin::Initialize**](/windows/win32/api/wcsplugin/nf-wcsplugin-igamutmapmodelplugin-initialize)

WcsPlugIn.h

N/A

[**IGamutMapModelPlugin::SourceToDestinationAppearanceColors**](/windows/win32/api/wcsplugin/nf-wcsplugin-igamutmapmodelplugin-sourcetodestinationappearancecolors)

WcsPlugIn.h

N/A



 



Structures

API Name

Header

Library

[**BlackInformation**](/windows/win32/api/wcsplugin/ns-wcsplugin-blackinformation)

WcsPlugIn.h

N/A

[**GamutBoundaryDescription**](/windows/win32/api/wcsplugin/ns-wcsplugin-gamutboundarydescription)

WcsPlugIn.h

N/A

[**XYZColorF**](https://www.bing.com/search?q=**XYZColorF**)

WcsPlugIn.h

N/A

[**JChColorF**](https://www.bing.com/search?q=**JChColorF**)

WcsPlugIn.h

N/A

[**JabColorF**](https://www.bing.com/search?q=**JabColorF**)

WcsPlugIn.h

N/A

[**GamutShell**](/windows/win32/api/wcsplugin/ns-wcsplugin-gamutshell)

WcsPlugIn.h

N/A

[**GamutShellTriangle**](/windows/win32/api/wcsplugin/ns-wcsplugin-gamutshelltriangle)

WcsPlugIn.h

N/A

[**PrimaryJabColors**](/windows/win32/api/wcsplugin/ns-wcsplugin-primaryjabcolors)

WcsPlugIn.h

N/A

[**PrimaryXYZColors**](/windows/win32/api/wcsplugin/ns-wcsplugin-primaryxyzcolors)

WcsPlugIn.h

N/A



 

 

 
