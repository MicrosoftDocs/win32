---
title: UserPolicy.SerializedPolicy property
description: Gets the serialized policy.
audience: developer
author: REDMOND\\bruceper
manager: REDMOND\\mbaldwin
ms.assetid: P:Microsoft.RightsManagement.UserPolicy.SerializedPolicy
ms.prod: windows-server-dev
ms.technology: active-directory-rights-management
ms.tgt_platform: multiple
keywords:
- SerializedPolicy property
- SerializedPolicy property, UserPolicy class
- UserPolicy class, SerializedPolicy property
topic_type:
- apiref
api_name:
- Microsoft.RightsManagement.UserPolicy.SerializedPolicy
- Microsoft.RightsManagement.UserPolicy.
api_location:
- Microsoft.RightsManagement.dll
api_type:
- Assembly
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# UserPolicy.SerializedPolicy property

Gets the serialized policy.

## Syntax


```C++
public:
property IBuffer^ SerializedPolicy { 
   IBuffer^ get();
}
```



## Property value

Type: [IBuffer](https://msdn.microsoft.com/library/windows/apps/windows.storage.streams.iinputstream.aspx)

The serialized policy.

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

 

 





