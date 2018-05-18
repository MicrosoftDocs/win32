---
Description: 'Windows 10 helps your application optimize power consumption when it's running on a mobile device.'
ms.assetid: 'a956b88c-8a75-4c1c-af27-53c69feb1596'
title: 'What's New in Power Management'
---

# What's New in Power Management

Windows 10 helps your application optimize power consumption when it's running on a mobile device.

## Battery saver

In this release, your application can be notified when battery saver is turned on or off. By responding to changing power conditions, your application can work in concert with battery saver to save energy and help extend battery life. For general information about battery saver, see [battery saver (in the hardware component guidelines)](https://msdn.microsoft.com/library/windows/hardware/mt186374).

-   [**GUID\_POWER\_SAVING\_STATUS**](power-setting-guids.md) : Use this new GUID with the [**PowerSettingRegisterNotification**](powersettingregisternotification.md) function to be notified when battery saver is turned on or off.

-   [**SYSTEM\_POWER\_STATUS**](system-power-status-str.md) : This structure has been updated to support battery saver. The fourth member, **SystemStatusFlag** (previously named **Reserved1**), now indicates if battery saver is engaged or not. Use the [**GetSystemPowerStatus**](getsystempowerstatus.md) function to retrieve a pointer to this structure.

 

 



