---
title: PolicyDescriptor.PolicyDescriptor(userRolesList) constructor
description: Constructor for PolicyDescriptor which initializes the object with a list of user roles.
audience: developer
author: REDMOND\\bruceper
manager: REDMOND\\mbaldwin
ms.assetid: M:Microsoft.RightsManagement.PolicyDescriptor.PolicyDescriptor(Windows.Foundation.Collections.IIterable\`2)
ms.prod: windows-server-dev
ms.technology: active-directory-rights-management
ms.tgt_platform: multiple
keywords:
- PolicyDescriptor(userRolesList) constructor
- PolicyDescriptor(userRolesList) constructor, PolicyDescriptor class
- PolicyDescriptor class, PolicyDescriptor(userRolesList) constructor
topic_type:
- apiref
api_name:
- Microsoft.RightsManagement.PolicyDescriptor..ctor
api_location:
- Microsoft.RightsManagement.dll
api_type:
- Assembly
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# PolicyDescriptor.PolicyDescriptor(userRolesList) constructor

\[Some information relates to pre-released product which may be substantially modified before it's commercially released. Microsoft makes no warranties, express or implied, with respect to the information provided here.\]

Constructor for [**PolicyDescriptor**](https://msdn.microsoft.com/library/windows/desktop/dn920762) which initializes the object with a list of user roles.

## Syntax


```C++
public:
PolicyDescriptor(userRolesList)(
  IIterable<UserRoles>^ userRolesList
)
```



## Parameters

<dl> <dt>

*userRolesList* 
</dt> <dd>

Type: [**UserRoles**](userroles.md)

A collection of user roles.

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

[**PolicyDescriptor**](policydescriptor.md)
</dt> </dl>

 

 





