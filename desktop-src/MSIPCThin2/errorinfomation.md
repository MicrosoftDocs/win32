---
title: ErrorInfomation class
description: Enables access to error information.
audience: developer
author: REDMOND\\bruceper
manager: REDMOND\\mbaldwin
ms.assetid: T:Microsoft.RightsManagement.ErrorInfomation
ms.prod: windows-server-dev
ms.technology: active-directory-rights-management
ms.tgt_platform: multiple
keywords:
- ErrorInfomation class
topic_type:
- apiref
api_name:
- Microsoft.RightsManagement.ErrorInfomation
api_location:
- Microsoft.RightsManagement.dll
api_type:
- Assembly
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# ErrorInfomation class

\[Some information relates to pre-released product which may be substantially modified before it's commercially released. Microsoft makes no warranties, express or implied, with respect to the information provided here.\]

Enables access to error information.

## Syntax


```C++
public ref class ErrorInfomation sealed 
```



## Members

The **ErrorInfomation** class inherits from [IInspectable](https://msdn.microsoft.com/library/windows/apps/br205821). **ErrorInfomation** also has these types of members:

-   [Properties](#properties)

### Properties

The **ErrorInfomation** class has these properties.



| Property                                                                                         | Access type          | Description                                                                                                                                        |
|:-------------------------------------------------------------------------------------------------|:---------------------|:---------------------------------------------------------------------------------------------------------------------------------------------------|
| [**AUTHENTICATION\_FAILED**](errorinfomation-authentication-failed.md)<br/>               | Read-only<br/> | The authentication failed                                                                                                                          |
| [**DEVICE\_REJECTED**](errorinfomation-device-rejected.md)<br/>                           | Read-only<br/> | This device is disabled by the tenant admin.                                                                                                       |
| [**HResult**](errorinfomation-hresult.md)<br/>                                            | Read-only<br/> | Retrieves the HResult for the exception.                                                                                                           |
| [**INVALID\_PL**](errorinfomation-invalid-pl.md)<br/>                                     | Read-only<br/> | Invalid PL was passed to the Active Directory Rights Management client.                                                                            |
| [**NEEDS\_ONLINE**](errorinfomation-needs-online.md)<br/>                                 | Read-only<br/> | The Active Directory Rights Management Services client needs network access to complete the operation, but the application requested offline mode. |
| [**REST\_SERVICE\_DISABLED**](errorinfomation-rest-service-disabled.md)<br/>              | Read-only<br/> | The REST service is disabled for this tenant.                                                                                                      |
| [**RIGHT\_NOT\_GRANTED**](errorinfomation-right-not-granted.md)<br/>                      | Read-only<br/> | You have not been granted the rights necessary to complete the specified operation.                                                                |
| [**SERVER\_ERROR**](errorinfomation-server-error.md)<br/>                                 | Read-only<br/> | An error occurred while trying to contact the Active Directory Rights Management Services server.                                                  |
| [**SERVICE\_NOT\_AVAILABLE\_ERROR**](errorinfomation-service-not-available-error.md)<br/> | Read-only<br/> | HTTP status 404 returned when contacting Active Directory Rights Management Services server.                                                       |
| [**USER\_NOT\_CONSENTED**](errorinfomation-user-not-consented.md)<br/>                    | Read-only<br/> | The user has not given consent.                                                                                                                    |



 

## Requirements



|                                     |                                                                                                             |
|-------------------------------------|-------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                                   |
| Minimum supported server<br/> | None supported<br/>                                                                                   |
| Minimum supported phone<br/>  | Windows Phone 8.1<br/>                                                                                |
| Namespace<br/>                | Microsoft::RightsManagement<br/>                                                                      |
| Metadata<br/>                 | <dl> <dt>Microsoft.RightsManagement.winmd</dt> </dl> |



## See also

<dl> <dt>

[IInspectable](https://msdn.microsoft.com/library/windows/apps/br205821)
</dt> </dl>

 

 





