---
description: The IAutomaticUpdatesSettings interface defines the following methods.
ms.assetid: 2c6df896-bb59-4d77-acde-64e36ecb7d75
title: IAutomaticUpdatesSettings Methods
ms.topic: reference
ms.date: 05/31/2018
---

# IAutomaticUpdatesSettings Methods

The [**IAutomaticUpdatesSettings**](/windows/desktop/api/Wuapi/nn-wuapi-iautomaticupdatessettings) interface defines the following methods.



| Method                                               | Description                                      |
|------------------------------------------------------|--------------------------------------------------|
| [**Refresh**](/windows/desktop/api/Wuapi/nf-wuapi-iautomaticupdatessettings-refresh) | Retrieves the latest Automatic Updates settings. |
| [**Save**](/windows/desktop/api/Wuapi/nf-wuapi-iautomaticupdatessettings-save)       | Applies the current Automatic Updates settings.  |



 

> [!Note]  
> On Windows RT, you can no longer use the [**IAutomaticUpdatesSettings::Save**](/windows/desktop/api/Wuapi/nf-wuapi-iautomaticupdatessettings-save) method to configure Windows Update settings programmatically. The configuration operation fails if you use **Save** to set any value other than 4 ([**aunlScheduledInstallation**](/windows/win32/api/wuapi/ne-wuapi-automaticupdatesnotificationlevel)).

 

 

 



