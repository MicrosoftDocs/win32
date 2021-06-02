---
description: The IUpdateInstallationResult interface defines the following properties.
ms.assetid: 7e8f7125-f89b-416f-bcc5-422eecabe0c4
title: IUpdateInstallationResult Properties
ms.topic: article
ms.date: 05/31/2018
---

# IUpdateInstallationResult Properties

The [**IUpdateInstallationResult**](/windows/desktop/api/Wuapi/nn-wuapi-iupdateinstallationresult) interface defines the following properties.



| Property                                                           | Description                                                                                                                       |
|--------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------|
| [**HResult**](/windows/desktop/api/Wuapi/nf-wuapi-iupdateinstallationresult-get_hresult)               | Gets the **HRESULT** exception value that is raised during the operation on an update.                                            |
| [**RebootRequired**](/windows/desktop/api/Wuapi/nf-wuapi-iupdateinstallationresult-get_rebootrequired) | Gets a Boolean value that indicates whether a system restart is required on a computer to complete the installation of an update. |
| [**ResultCode**](/windows/desktop/api/Wuapi/nf-wuapi-iupdateinstallationresult-get_resultcode)         | Gets an [**OperationResultCode**](/windows/win32/api/wuapi/ne-wuapi-operationresultcode) value that specifies the result of an operation on an update.          |



 

 

 



