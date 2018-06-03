---
title: AuthenticationParameters.Authority property
description: Gets authority with which the request is being made.
audience: developer
author: REDMOND\\bruceper
manager: REDMOND\\mbaldwin
ms.assetid: P:Microsoft.RightsManagement.AuthenticationParameters.Authority
ms.prod: windows-server-dev
ms.technology: active-directory-rights-management
ms.tgt_platform: multiple
keywords:
- Authority property
- Authority property, AuthenticationParameters class
- AuthenticationParameters class, Authority property
topic_type:
- apiref
api_name:
- Microsoft.RightsManagement.AuthenticationParameters.Authority
- Microsoft.RightsManagement.AuthenticationParameters.
api_location:
- Microsoft.RightsManagement.dll
api_type:
- Assembly
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# AuthenticationParameters.Authority property

Gets authority with which the request is being made.

## Syntax


```C++
public:
property String^ Authority { 
   String^ get();
}
```



## Property value

Type: **String**

Authority with which the request is being made

## Remarks

An example **authority** string would be, `https://login.windows.net/common/oauth2/token`

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

 

 





