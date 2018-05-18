---
title: AuthenticationParameters class
description: Authentication info to be used to get an access token.
audience: developer
author: REDMOND\\bruceper
manager: REDMOND\\mbaldwin
ms.assetid: 'T:Microsoft.RightsManagement.AuthenticationParameters'
ms.prod: 'windows-server-dev'
ms.technology: 'active-directory-rights-management'
ms.tgt_platform: multiple
keywords: ["AuthenticationParameters class"]
topic_type:
- apiref
api_name:
- Microsoft.RightsManagement.AuthenticationParameters
api_location:
- Microsoft.RightsManagement.dll
api_type:
- Assembly
---

# AuthenticationParameters class

Authentication info to be used to get an access token.

## Syntax


```C++
public ref class AuthenticationParameters sealed 
```



## Members

The **AuthenticationParameters** class inherits from [IInspectable](https://msdn.microsoft.com/library/windows/apps/br205821). **AuthenticationParameters** also has these types of members:

-   [Properties](#properties)

### Properties

The **AuthenticationParameters** class has these properties.



| Property                                                           | Access type          | Description                                          |
|:-------------------------------------------------------------------|:---------------------|:-----------------------------------------------------|
| [**Authority**](authenticationparameters-authority.md)<br/> | Read-only<br/> | Gets authority with which the request is being made. |
| [**Resource**](authenticationparameters-resource.md)<br/>   | Read-only<br/> | Gets resource being requested.                       |
| [**Scope**](authenticationparameters-scope.md)<br/>         | Read-only<br/> | Gets the scope of the authentication request.        |
| [**UserId**](authenticationparameters-userid.md)<br/>       | Read-only<br/> | Gets unique user ID of the requestor.                |



 

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

 

 





