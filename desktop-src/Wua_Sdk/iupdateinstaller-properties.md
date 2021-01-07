---
description: The IUpdateInstaller interface defines the following properties.
ms.assetid: 876a2150-40a1-42a3-bc9a-05dec94fccd3
title: IUpdateInstaller Properties
ms.topic: article
ms.date: 05/31/2018
---

# IUpdateInstaller Properties

The [**IUpdateInstaller**](/windows/desktop/api/Wuapi/nn-wuapi-iupdateinstaller) interface defines the following properties.



| Property                                                                                      | Description                                                                                                                           |
|-----------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------|
| [**AllowSourcePrompts**](/windows/desktop/api/Wuapi/nf-wuapi-iupdateinstaller-get_allowsourceprompts)                             | Gets and sets a Boolean value that indicates whether to show source prompts to the user when installing the updates.                  |
| [**ClientApplicationID**](/windows/desktop/api/Wuapi/nf-wuapi-iupdateinstaller-get_clientapplicationid)                           | Gets and sets the current client application.                                                                                         |
| [**IsBusy**](/windows/desktop/api/Wuapi/nf-wuapi-iupdateinstaller-get_isbusy)                                                     | Gets a Boolean value that indicates whether an installation or uninstallation is in progress on a computer at a specific time.        |
| [**IsForced**](/windows/desktop/api/Wuapi/nf-wuapi-iupdateinstaller-get_isforced)                                                 | Gets or sets a Boolean value that indicates whether to forcibly install or uninstall an update.                                       |
| [**ParentHwnd**](/windows/desktop/api/Wuapi/nf-wuapi-iupdateinstaller-get_parenthwnd)                                             | Gets and sets a handle to the parent window that can contain a dialog box.                                                            |
| [**ParentWindow**](/windows/desktop/api/Wuapi/nf-wuapi-iupdateinstaller-get_parentwindow)                                         | Gets and sets the interface that represents the parent window that can contain a dialog box.                                          |
| [**RebootRequiredBeforeInstallation**](/windows/desktop/api/Wuapi/nf-wuapi-iupdateinstaller-get_rebootrequiredbeforeinstallation) | Gets a Boolean value that indicates whether a system restart is required before installing or uninstalling updates.                   |
| [**Updates**](/windows/desktop/api/Wuapi/nf-wuapi-iupdateinstaller-get_updates)                                                   | Gets and sets an interface that contains a read-only collection of the updates that are specified for installation or uninstallation. |



 

 

 



