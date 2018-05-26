---
title: AuthenticationParameters.UserId property
description: Gets unique user ID of the requestor.
audience: developer
author: REDMOND\\bruceper
manager: REDMOND\\mbaldwin
ms.assetid: PMicrosoft.RightsManagement.AuthenticationParameters.UserId
ms.prod: windows-server-dev
ms.technology: active-directory-rights-management
ms.tgt_platform: multiple
keywords:
- UserId property
- UserId property, AuthenticationParameters class
- AuthenticationParameters class, UserId property
topic_type:
- apiref
api_name:
- Microsoft.RightsManagement.AuthenticationParameters.UserId
- Microsoft.RightsManagement.AuthenticationParameters.
api_location:
- Microsoft.RightsManagement.dll
api_type:
- Assembly
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# AuthenticationParameters.UserId property

Gets unique user ID of the requestor.

## Syntax


```C++
public:
property String^ UserId { 
   String^ get();
}
```



## Property value

Type: **String**

Unique user ID of the requestor.

## Remarks

An example **userId** string would be, `user@domain.com`

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

[**AuthenticationParameters**](authenticationparameters.md)
</dt> </dl>

 

 





