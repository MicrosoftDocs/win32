---
title: UserPolicy.EncryptedAppData property
description: Gets the app specific data.
audience: developer
author: REDMOND\\bruceper
manager: REDMOND\\mbaldwin
ms.assetid: PMicrosoft.RightsManagement.UserPolicy.EncryptedAppData
ms.prod: windows-server-dev
ms.technology: active-directory-rights-management
ms.tgt_platform: multiple
keywords:
- EncryptedAppData property
- EncryptedAppData property, UserPolicy class
- UserPolicy class, EncryptedAppData property
topic_type:
- apiref
api_name:
- Microsoft.RightsManagement.UserPolicy.EncryptedAppData
- Microsoft.RightsManagement.UserPolicy.
api_location:
- Microsoft.RightsManagement.dll
api_type:
- Assembly
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# UserPolicy.EncryptedAppData property

Gets the app specific data

## Syntax


```C++
public:
property IMapView<String^,String^>^ EncryptedAppData { 
   IMapView<String^,String^>^ get();
}
```



## Property value

Type: [IMapView](https://msdn.microsoft.com/library/windows/apps/xaml/br226037.aspx)

App specific data accessed via [IMapView](https://msdn.microsoft.com/library/windows/apps/br226037.aspx).

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

 

 





