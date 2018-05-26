---
title: ErrorInfomation.AUTHENTICATION\_FAILED property
description: The authentication failed.
audience: developer
author: REDMOND\\bruceper
manager: REDMOND\\mbaldwin
ms.assetid: PMicrosoft.RightsManagement.ErrorInfomation.AUTHENTICATION\_FAILED
ms.prod: windows-server-dev
ms.technology: active-directory-rights-management
ms.tgt_platform: multiple
keywords:
- AUTHENTICATION_FAILED property
- AUTHENTICATION_FAILED property, ErrorInfomation class
- ErrorInfomation class, AUTHENTICATION_FAILED property
topic_type:
- apiref
api_name:
- Microsoft.RightsManagement.ErrorInfomation.AUTHENTICATION_FAILED
- Microsoft.RightsManagement.ErrorInfomation.
api_location:
- Microsoft.RightsManagement.dll
api_type:
- Assembly
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# ErrorInfomation.AUTHENTICATION\_FAILED property

\[Some information relates to pre-released product which may be substantially modified before it's commercially released. Microsoft makes no warranties, express or implied, with respect to the information provided here.\]

The authentication failed and could possibly be caused by one of the following.

-   Authentication error (HTTP error 401) returned by an Internet request
-   The current user does not have valid domain credentials in a silent user activation attempt
-   The certification server, in silent user activation, is not in the local intranet or trusted sites zone

## Syntax


```C++
public:
static property ErrorInfomation^ AUTHENTICATION_FAILED { 
   ErrorInfomation^ get();
}
```



## Property value

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

[**ErrorInfomation**](errorinfomation.md)
</dt> </dl>

 

 





