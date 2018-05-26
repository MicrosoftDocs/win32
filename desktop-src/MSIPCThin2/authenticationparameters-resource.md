---
title: AuthenticationParameters.Resource property
description: Gets resource being requested.
audience: developer
author: REDMOND\\bruceper
manager: REDMOND\\mbaldwin
ms.assetid: PMicrosoft.RightsManagement.AuthenticationParameters.Resource
ms.prod: windows-server-dev
ms.technology: active-directory-rights-management
ms.tgt_platform: multiple
keywords:
- Resource property
- Resource property, AuthenticationParameters class
- AuthenticationParameters class, Resource property
topic_type:
- apiref
api_name:
- Microsoft.RightsManagement.AuthenticationParameters.Resource
- Microsoft.RightsManagement.AuthenticationParameters.
api_location:
- Microsoft.RightsManagement.dll
api_type:
- Assembly
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# AuthenticationParameters.Resource property

Gets resource being requested.

## Syntax


```C++
public:
property String^ Resource { 
   String^ get();
}
```



## Property value

Type: **String**

Resource being requested

## Remarks

An example **resource** string would be, `api.aadrm.com`

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

 

 





