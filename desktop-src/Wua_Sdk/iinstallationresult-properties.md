---
description: The IInstallationResult interface defines the following properties.
ms.assetid: bd6cd5ae-2e43-4ac3-8ce7-ac80b7fc5cb8
title: IInstallationResult Properties
ms.topic: article
ms.date: 05/31/2018
---

# IInstallationResult Properties

The [**IInstallationResult**](/windows/desktop/api/Wuapi/nn-wuapi-iinstallationresult) interface defines the following properties.



| Property                                                     | Description                                                                                                                            |
|--------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------|
| [**HResult**](/windows/desktop/api/Wuapi/nf-wuapi-iinstallationresult-get_hresult)               | Gets the **HRESULT** of the exception, if any, that is raised during the installation.                                                 |
| [**RebootRequired**](/windows/desktop/api/Wuapi/nf-wuapi-iinstallationresult-get_rebootrequired) | Gets a Boolean value that indicates whether you must restart the computer to complete the installation or uninstallation of an update. |
| [**ResultCode**](/windows/desktop/api/Wuapi/nf-wuapi-iinstallationresult-get_resultcode)         | Gets an [**OperationResultCode**](/windows/win32/api/wuapi/ne-wuapi-operationresultcode) value that specifies the result of an operation on an update.               |



 

 

 



