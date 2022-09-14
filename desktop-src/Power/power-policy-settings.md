---
description: Describes the power policy settings that make up a power scheme.
ms.assetid: cd515cd6-67f4-45d0-b769-3abc7a56faa8
title: Power Policy Settings
ms.topic: article
ms.date: 05/31/2018
---

# Power Policy Settings

Power plans and schemes consist of preferences and policy settings.

A power plan consists of a group of power setting preferences. These preferences consist of both an AC and DC value for each of the power settings. Each power plan is identified through a unique **GUID** as well as a friendly name. Windows Vista has three default power plans: Power Saver, Balanced, and High Performance. These plans can be customized, and additional plans can be created. All power plans have a personality attribute that indicates the overall power savings behavior of the plan.

The following table shows the three power plan personalities. 

| Display name     | Description                                                                   | **GUID**                             |
|------------------|-------------------------------------------------------------------------------|--------------------------------------|
| Power Saver      | Delivers reduced performance which may increase power savings.                | a1841308-3541-4fab-bc81-f71556f20b4a |
| Balanced         | Automatically balances performance and power consumption according to demand. | 381b4222-f694-41f0-9685-ff5bb260df2e |
| High Performance | Delivers maximum performance at the expense of higher power consumption.      | 8c5e7fda-e8bf-4a96-9a85-a6e23a8c635c |



 

> [!Note]  
> Devices that support [Modern Standby](/windows-hardware/design/device-experiences/modern-standby) mode only allow the **Balanced** power plan, or power plans derived from **Balanced**. **Modern Standby** is the newer, more streamlined solution to power settings management.

 

Each computer has a single, active power plan. By default, nonprivileged users are able to access system power settings. Access to all or individual power settings can be controlled through ACLs on the power settings or through Group Policy. Applications should call [**PowerSettingAccessCheck**](/windows/desktop/api/PowrProf/nf-powrprof-powersettingaccesscheck) to determine if the user has access to the power setting.

Each power setting is identified by a unique **GUID** and includes a friendly name, description, allowable values, and default values for AC and DC. Custom power settings can be created using the [**PowerCreateSetting**](/windows/desktop/api/PowrProf/nf-powrprof-powercreatesetting) function.

## Related topics

<dl> <dt>

[Power Schemes](power-schemes.md)
</dt> </dl>

 

 
