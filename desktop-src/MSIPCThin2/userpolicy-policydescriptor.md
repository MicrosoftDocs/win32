---
title: UserPolicy.PolicyDescriptor property
description: Gets the policy descriptor.
audience: developer
author: REDMOND\\bruceper
manager: REDMOND\\mbaldwin
ms.assetid: P:Microsoft.RightsManagement.UserPolicy.PolicyDescriptor
ms.prod: windows-server-dev
ms.technology: active-directory-rights-management
ms.tgt_platform: multiple
keywords:
- PolicyDescriptor property
- PolicyDescriptor property, UserPolicy class
- UserPolicy class, PolicyDescriptor property
topic_type:
- apiref
api_name:
- Microsoft.RightsManagement.UserPolicy.PolicyDescriptor
- Microsoft.RightsManagement.UserPolicy.
api_location:
- Microsoft.RightsManagement.dll
api_type:
- Assembly
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# UserPolicy.PolicyDescriptor property

Gets the policy descriptor.

> [!Note]  
> This property will be null for template based policies.

 

## Syntax


```C++
public:
property PolicyDescriptor^ PolicyDescriptor { 
   PolicyDescriptor^ get();
}
```



## Property value

Type: [**PolicyDescriptor**](https://msdn.microsoft.com/library/windows/desktop/dn920762)

The policy descriptor.

> [!Note]  
> ApiNamespace()::PolicyDescriptor

 

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

[**UserPolicy**](userpolicy.md)
</dt> </dl>

 

 





