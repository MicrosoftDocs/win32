---
title: UserRights.UserRights constructor
description: Creates a UserRights object.
audience: developer
author: REDMOND\\bruceper
manager: REDMOND\\mbaldwin
ms.assetid: MMicrosoft.RightsManagement.UserRights.UserRights(Windows.Foundation.Collections.IIterable\`1,Windows.Foundation.Collections.IIterable\`1)
ms.prod: windows-server-dev
ms.technology: active-directory-rights-management
ms.tgt_platform: multiple
keywords:
- UserRights constructor
- UserRights constructor, UserRights class
- UserRights class, UserRights constructor
topic_type:
- apiref
api_name:
- Microsoft.RightsManagement.UserRights..ctor
api_location:
- Microsoft.RightsManagement.dll
api_type:
- Assembly
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# UserRights.UserRights constructor

Creates a [**UserRights**](userrights.md) object.

## Syntax


```C++
public:
UserRights(
  IIterable<String^>^ users, 
  IIterable<String^>^ rights
)
```



## Parameters

<dl> <dt>

*users* 
</dt> <dd>

Type: **IIterable&lt;String^&gt;^**

The users to whom the rights are granted.

</dd> <dt>

*rights* 
</dt> <dd>

Type: **IIterable&lt;String^&gt;^**

The rights that are granted.

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

[**UserRights**](userrights.md)
</dt> <dt>

[**Users**](userrights-users.md)
</dt> </dl>

 

 





