---
title: WCS Registry Keys
description: WCS uses registry keys to signal that certain color profile events have occurred. Apps should query these registry keys for updated system color profile state.
ms.assetid: e728efa0-e547-45b9-af85-1312766d2fe7
keywords:
- Windows Color System (WCS),registry keys
- WCS (Windows Color System),registry keys
- image color management,registry keys
- color management,registry keys
- colors,registry keys
- WCS reference,registry keys
- reference for WCS,registry keys
- Windows Color System (WCS),registry
- WCS (Windows Color System),registry
- image color management,registry
- color management,registry
- colors,registry
- WCS reference,registry
- reference for WCS,registry
ms.localizationpriority: high


ms.topic: article
ms.date: 05/31/2018
---

# WCS Registry Keys

WCS uses registry keys to signal that certain color profile events have occurred. Apps should query these registry keys for updated system color profile state.

## Active color profile changed

Apps may want to respond to color profile change events for a monitor device; this ensures that they always have accurate color information for their target, even if the user or another app has changed the active profile for the device.

### Desktop applications

Desktop apps should listen for changes to the registry to determine when a color profile associations has changed using [**RegNotifyChangeKeyValue**](/windows/win32/api/winreg/nf-winreg-regnotifychangekeyvalue). An app should register both for per-user profile association changes, and for system-wide changes.

[**RegNotifyChangeKeyValue**](/windows/win32/api/winreg/nf-winreg-regnotifychangekeyvalue) should be initialized with an HKEY provided by [**RegOpenKeyEx**](/windows/win32/api/winreg/nf-winreg-regopenkeyexa). **RegOpenKeyEx** should be initialized using the following registry tree locations:



|    &nbsp;  |  &nbsp;      | 
|----------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------|
| Per-user profile associations    | **HKEY\_CURRENT\_USER SOFTWARE\\Microsoft\\Windows NT\\CurrentVersion\\ICM\\ProfileAssociations\\Display\\{4d36e96e-e325-11ce-bfc1-08002be10318}** |
| System-wide profile associations | **HKEY\_LOCAL\_MACHINE\\SYSTEM\\CurrentControlSet\\Control\\Class\\{4d36e96e-e325-11ce-bfc1-08002be10318}**                                        |



 

When the app is notified of a registry key change, it should first query whether per-user or system-wide associations are being used by calling [**WcsGetUsePerUserProfiles**](/windows/win32/api/icm/nf-icm-wcsgetdefaultrenderingintent). It should then call [**WcsGetDefaultColorProfile**](/windows/win32/api/icm/nf-icm-wcsgetdefaultcolorprofile) with the right [**WCS\_PROFILE\_MANAGEMENT\_SCOPE**](/windows/win32/api/icm/ne-icm-wcs_profile_management_scope) value to obtain the new active color profile for the monitor. Note that not all registry key changes will correspond to an actual change in the currently active color profile; the app mush check whether the profile returned by **WcsGetDefaultColorProfile** has actually changed.

### Universal Windows (UWP) apps

Universal Windows Apps do not have access to the above registry keys. Instead, they should register a handler for the [**DisplayInformation.ColorProfileChanged**](/uwp/api/Windows.Graphics.Display.DisplayInformation) event. This event fires whenever the active color profile for the monitor on which the application is running has changed. ColorProfileChanged takes into account whether per-user or system-wide profile associations are being used; this information is abstracted from UWP apps.

When responding to the ColorProfileChanged event, the app should query the currently active profile using [**DisplayInformation.GetColorProfileAsync**](/uwp/api/Windows.Graphics.Display.DisplayInformation).

 

 