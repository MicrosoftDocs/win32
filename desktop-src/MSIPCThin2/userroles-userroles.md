---
title: UserRoles.UserRoles constructor
description: Constructor for UserRoles object.
audience: developer
author: REDMOND\\bruceper
manager: REDMOND\\mbaldwin
ms.assetid: MMicrosoft.RightsManagement.UserRoles.UserRoles
ms.prod: windows-server-dev
ms.technology: active-directory-rights-management
ms.tgt_platform: multiple
keywords:
- UserRoles constructor
- UserRoles constructor, UserRoles class
- UserRoles class, UserRoles constructor
topic_type:
- apiref
api_name:
- Microsoft.RightsManagement.UserRoles..ctor
api_location:
- Microsoft.RightsManagement.dll
api_type:
- Assembly
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# UserRoles.UserRoles constructor

\[Some information relates to pre-released product which may be substantially modified before it's commercially released. Microsoft makes no warranties, express or implied, with respect to the information provided here.\]

Constructor for [**UserRoles**](userroles.md) object.

## Syntax


```C++
public:
UserRoles(
          IIterable<String^>^ users, 
          IIterable<String^>^ roles
)
```



## Parameters

<dl> <dt>

*users* 
</dt> <dd>

Type: **IIterable&lt;String^&gt;^**

Users

</dd> <dt>

*roles* 
</dt> <dd>

Type: **IIterable&lt;String^&gt;^**

Roles

</dd> </dl>

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

 

 





