---
description: The IInstallationBehavior interface defines the following properties.
ms.assetid: abb8e247-44c4-491c-b8ea-9f32d7420c45
title: IInstallationBehavior Properties
ms.topic: article
ms.date: 05/31/2018
---

# IInstallationBehavior Properties

The [**IInstallationBehavior**](/windows/desktop/api/Wuapi/nn-wuapi-iinstallationbehavior) interface defines the following properties.



| Property                                                                                 | Description                                                                                                                                                                    |
|------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**CanRequestUserInput**](/windows/desktop/api/Wuapi/nf-wuapi-iinstallationbehavior-get_canrequestuserinput)                 | Gets a Boolean value thast indicates whether the installation or uninstallation of an update can prompt for user input.                                                        |
| [**Impact**](/windows/desktop/api/Wuapi/nf-wuapi-iinstallationbehavior-get_impact)                                           | Gets an [**InstallationImpact**](/windows/win32/api/wuapi/ne-wuapi-installationimpact) enumeration that indicates how the installation or uninstallation of the update affects the computer.                 |
| [**RebootBehavior**](/windows/desktop/api/Wuapi/nf-wuapi-iinstallationbehavior-get_rebootbehavior)                           | Gets an [**InstallationRebootBehavior**](/windows/win32/api/wuapi/ne-wuapi-installationrebootbehavior) enumeration that specifies the restart behavior that occurs when you install or uninstall the update. |
| [**RequiresNetworkConnectivity**](/windows/desktop/api/Wuapi/nf-wuapi-iinstallationbehavior-get_requiresnetworkconnectivity) | Gets a Boolean value that indicates whether the installation or uninstallation of an update requires network connectivity.                                                     |



 

 

 



