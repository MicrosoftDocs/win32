---
title: ProtectedFileStream.Policy property
description: Gets user policy associated with this ProtectedFileStream object.
audience: developer
author: REDMOND\\bruceper
manager: REDMOND\\mbaldwin
ms.assetid: PMicrosoft.RightsManagement.ProtectedFileStream.Policy
ms.prod: windows-server-dev
ms.technology: active-directory-rights-management
ms.tgt_platform: multiple
keywords:
- Policy property
- Policy property, ProtectedFileStream class
- ProtectedFileStream class, Policy property
topic_type:
- apiref
api_name:
- Microsoft.RightsManagement.ProtectedFileStream.Policy
- Microsoft.RightsManagement.ProtectedFileStream.
api_location:
- Microsoft.RightsManagement.dll
api_type:
- Assembly
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# ProtectedFileStream.Policy property

Gets user policy associated with this [**ProtectedFileStream**](protectedfilestream.md) object.

## Syntax


```C++
public:
property UserPolicy^ Policy { 
   UserPolicy^ get();
}
```



## Property value

Type: [**UserPolicy**](userpolicy.md)

The protection policy associated with the content.

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

[**ProtectedFileStream**](protectedfilestream.md)
</dt> </dl>

 

 





