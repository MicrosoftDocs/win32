---
title: PolicyDescriptor.PolicyDescriptor(userRightsList) constructor
description: Constructor for PolicyDescriptor which initializes the object with a list of user rights.
audience: developer
author: REDMOND\\bruceper
manager: REDMOND\\mbaldwin
ms.assetid: M:Microsoft.RightsManagement.PolicyDescriptor.PolicyDescriptor(Windows.Foundation.Collections.IIterable\`1)
ms.prod: windows-server-dev
ms.technology: active-directory-rights-management
ms.tgt_platform: multiple
keywords:
- PolicyDescriptor(userRightsList) constructor
- PolicyDescriptor(userRightsList) constructor, PolicyDescriptor class
- PolicyDescriptor class, PolicyDescriptor(userRightsList) constructor
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

# PolicyDescriptor.PolicyDescriptor(userRightsList) constructor

Constructor for [**PolicyDescriptor**](https://msdn.microsoft.com/library/windows/desktop/dn920762) which initializes the object with a list of user rights.

## Syntax


```C++
public:
PolicyDescriptor(userRightsList)(
  IIterable<UserRights>^ userRightsList
)
```



## Parameters

<dl> <dt>

*userRightsList* 
</dt> <dd>

Type: [**UserRights**](userrights.md)

A collection of user rights.

</dd> </dl>

## Requirements



|                                     |                                                                                                             |
|-------------------------------------|-------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                                   |
| Minimum supported server<br/> | None supported<br/>                                                                                   |
| Minimum supported phone<br/>  | Windows Phone 8.1<br/>                                                                                |
| Namespace<br/>                | Microsoft::RightsManagement<br/>                                                                      |
| Metadata<br/>                 | <dl> <dt>Microsoft.RightsManagement.winmd</dt> </dl> |



 

 





