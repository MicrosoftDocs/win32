---
description: The IAutomaticUpdatesSettings interface defines the following properties.
ms.assetid: 663aaf7d-c701-4da8-ba92-7e0a6d0f35ba
title: IAutomaticUpdatesSettings Properties
ms.topic: article
ms.date: 05/31/2018
---

# IAutomaticUpdatesSettings Properties

The [**IAutomaticUpdatesSettings**](/windows/desktop/api/Wuapi/nn-wuapi-iautomaticupdatessettings) interface defines the following properties.



| Property                                                                                 | Description                                                                                      |
|------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------|
| [**NotificationLevel**](/windows/desktop/api/Wuapi/nf-wuapi-iautomaticupdatessettings-get_notificationlevel)                 | Gets and sets how users are notified about Automatic Update events.                              |
| [**ReadOnly**](/windows/desktop/api/Wuapi/nf-wuapi-iautomaticupdatessettings-get_readonly)                                   | Gets a Boolean value that indicates whether the Automatic Update settings are read-only.         |
| [**Required**](/windows/desktop/api/Wuapi/nf-wuapi-iautomaticupdatessettings-get_required)                                   | Gets a Boolean value that indicates whether Group Policy requires the Automatic Updates service. |
| [**ScheduledInstallationDay**](/windows/desktop/api/Wuapi/nf-wuapi-iautomaticupdatessettings-get_scheduledinstallationday)   | Gets and sets the days of the week on which Automatic Updates installs or uninstalls updates.    |
| [**ScheduledInstallationTime**](/windows/desktop/api/Wuapi/nf-wuapi-iautomaticupdatessettings-get_scheduledinstallationtime) | Gets and sets the time at which Automatic Updates installs or uninstalls updates.                |



 

> [!Note]  
> Windows 8, Windows 8.1, Windows Server 2012, and Windows Server 2012 R2 provide only limited support for [**ScheduledInstallationDay**](/windows/desktop/api/Wuapi/nf-wuapi-iautomaticupdatessettings-get_scheduledinstallationday) and [**ScheduledInstallationTime**](/windows/desktop/api/Wuapi/nf-wuapi-iautomaticupdatessettings-get_scheduledinstallationtime). If the computer has been configured through Group Policy to use a scheduled installation day and time, the **ScheduledInstallationDay** and **ScheduledInstallationTime** properties return this scheduled day and time. If the computer hasn't been configured through Group Policy in this way, the **ScheduledInstallationDay** and **ScheduledInstallationTime** properties return default and unreliable values. If you try to modify the scheduled installation day and time on these operating systems, **ScheduledInstallationDay** and **ScheduledInstallationTime** appear to succeed but have no effect.

 

 

 



