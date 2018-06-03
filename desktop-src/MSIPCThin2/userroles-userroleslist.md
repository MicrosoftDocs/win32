---
title: PolicyDescriptor.UserRolesList property
description: Gets the user's roles list.
audience: developer
author: REDMOND\\bruceper
manager: REDMOND\\mbaldwin
ms.assetid: P:Microsoft.RightsManagement.PolicyDescriptor.UserRolesList
ms.prod: windows-server-dev
ms.technology: active-directory-rights-management
ms.tgt_platform: multiple
keywords:
- UserRolesList property
- UserRolesList property, PolicyDescriptor class
- PolicyDescriptor class, UserRolesList property
topic_type:
- apiref
api_name:
- Microsoft.RightsManagement.PolicyDescriptor.UserRolesList
- Microsoft.RightsManagement.PolicyDescriptor.
api_location:
- Microsoft.RightsManagement.dll
api_type:
- Assembly
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# PolicyDescriptor.UserRolesList property

\[Some information relates to pre-released product which may be substantially modified before it's commercially released. Microsoft makes no warranties, express or implied, with respect to the information provided here.\]

Gets the user's roles list.

## Syntax


```C++
public:
property IIterable<UserRoles> UserRolesList { 
   IIterable<UserRoles> get();
}
```



## Property value

Type: **UserRoles**

The user's roles list.

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

[**PolicyDescriptor**](policydescriptor.md)
</dt> <dt>

[**UserRoles**](userroles.md)
</dt> </dl>

 

 





