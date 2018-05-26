---
title: PolicyDescriptor.UserRightsList property
description: Gets the UserRightsList for the PolicyDescriptor.
audience: developer
author: REDMOND\\bruceper
manager: REDMOND\\mbaldwin
ms.assetid: PMicrosoft.RightsManagement.PolicyDescriptor.UserRightsList
ms.prod: windows-server-dev
ms.technology: active-directory-rights-management
ms.tgt_platform: multiple
keywords:
- UserRightsList property
- UserRightsList property, PolicyDescriptor class
- PolicyDescriptor class, UserRightsList property
topic_type:
- apiref
api_name:
- Microsoft.RightsManagement.PolicyDescriptor.UserRightsList
- Microsoft.RightsManagement.PolicyDescriptor.
api_location:
- Microsoft.RightsManagement.dll
api_type:
- Assembly
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# PolicyDescriptor.UserRightsList property

Gets the **UserRightsList** for the [**PolicyDescriptor**](https://msdn.microsoft.com/library/windows/desktop/dn920762).

> [!Note]  
> The value of the **UserRightsList** property will be null if the current user does not have access to the user rights information, meaning they do not have the [OWNER](https://msdn.microsoft.com/library/cc542546.aspx) right, the [VIEWRIGHTSDATA](https://msdn.microsoft.com/library/cc542546.aspx) right or the [EDITRIGHTSDATA](https://msdn.microsoft.com/library/cc542546.aspx) right.

 

For more information on these rights, see [Understanding XrML Rights](https://msdn.microsoft.com/library/cc542546.aspx).

## Syntax


```C++
public:
property IIterable<UserRights>^ UserRightsList { 
   IIterable<UserRights>^ get();
}
```



## Property value

Type: [**UserRights**](userrights.md)

The **UserRightsList** for the [**PolicyDescriptor**](https://msdn.microsoft.com/library/windows/desktop/dn920762).

## Requirements



|                                     |                                                                                                             |
|-------------------------------------|-------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                                   |
| Minimum supported server<br/> | None supported<br/>                                                                                   |
| Minimum supported phone<br/>  | Windows Phone 8.1<br/>                                                                                |
| Namespace<br/>                | Microsoft::RightsManagement<br/>                                                                      |
| Metadata<br/>                 | <dl> <dt>Microsoft.RightsManagement.winmd</dt> </dl> |



 

 





