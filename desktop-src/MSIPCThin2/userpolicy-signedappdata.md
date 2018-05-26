---
title: UserPolicy.SignedAppData property
description: Gets app specific data.
audience: developer
author: REDMOND\\bruceper
manager: REDMOND\\mbaldwin
ms.assetid: PMicrosoft.RightsManagement.UserPolicy.SignedAppData
ms.prod: windows-server-dev
ms.technology: active-directory-rights-management
ms.tgt_platform: multiple
keywords:
- SignedAppData property
- SignedAppData property, UserPolicy class
- UserPolicy class, SignedAppData property
topic_type:
- apiref
api_name:
- Microsoft.RightsManagement.UserPolicy.SignedAppData
- Microsoft.RightsManagement.UserPolicy.
api_location:
- Microsoft.RightsManagement.dll
api_type:
- Assembly
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# UserPolicy.SignedAppData property

\[Some information relates to pre-released product which may be substantially modified before it's commercially released. Microsoft makes no warranties, express or implied, with respect to the information provided here.\]

Gets app specific data.

## Syntax


```C++
public:
property IMapView<String^, String^>^ SignedAppData { 
   IMapView<String^, String^>^ get();
}
```



## Property value

Type: [IMapView](https://msdn.microsoft.com/library/windows/apps/xaml/br226037.aspx)

Signed app data accessed via [IMapView](https://msdn.microsoft.com/library/windows/apps/br226037.aspx).

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

 

 





