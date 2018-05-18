---
title: UserRoles.Users property
description: Users to whom the rights are granted.
audience: developer
author: REDMOND\\bruceper
manager: REDMOND\\mbaldwin
ms.assetid: 'P:Microsoft.RightsManagement.UserRoles.Users'
ms.prod: 'windows-server-dev'
ms.technology: 'active-directory-rights-management'
ms.tgt_platform: multiple
keywords: ["Users property", "Users property, UserRoles class", "UserRoles class, Users property"]
topic_type:
- apiref
api_name:
- Microsoft.RightsManagement.UserRoles.Users
- Microsoft.RightsManagement.UserRoles.
api_location:
- Microsoft.RightsManagement.dll
api_type:
- Assembly
---

# UserRoles.Users property

\[Some information relates to pre-released product which may be substantially modified before it's commercially released. Microsoft makes no warranties, express or implied, with respect to the information provided here.\]

Users to whom the rights are granted.

## Syntax


```C++
public:
property         IIterable<String^>^ Users { 
           IIterable<String^>^ get();
}
```



## Property value

Type: **IIterable&lt;String^&gt;^**

Users to whom roles are granted.

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

[**UserRoles**](userroles.md)
</dt> </dl>

 

 





