---
description: Windows 10 helps your application optimize power consumption when its running on a mobile device.
ms.assetid: a956b88c-8a75-4c1c-af27-53c69feb1596
title: Whats New in Power Management
ms.topic: article
ms.date: 05/31/2018
---

# What's New in Power Management

Windows 10 helps your application optimize power consumption when it's running on a mobile device.

## Battery saver

In this release, your application can be notified when battery saver is turned on or off. By responding to changing power conditions, your application can work in concert with battery saver to save energy and help extend battery life. For general information about battery saver, see [battery saver (in the hardware component guidelines)](/windows-hardware/design/component-guidelines/battery-saver).

-   [**GUID\_POWER\_SAVING\_STATUS**](power-setting-guids.md) : Use this new GUID with the [**PowerSettingRegisterNotification**](/windows/desktop/api/Powersetting/nf-powersetting-powersettingregisternotification) function to be notified when battery saver is turned on or off.

-   [**SYSTEM\_POWER\_STATUS**](/windows/desktop/api/Winbase/ns-winbase-system_power_status) : This structure has been updated to support battery saver. The fourth member, **SystemStatusFlag** (previously named **Reserved1**), now indicates if battery saver is engaged or not. Use the [**GetSystemPowerStatus**](/windows/desktop/api/Winbase/nf-winbase-getsystempowerstatus) function to retrieve a pointer to this structure.

 

 
