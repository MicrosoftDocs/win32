---
title: CommonRights.All property
description: Gets a set of all CommonRights.
audience: developer
author: REDMOND\\bruceper
manager: REDMOND\\mbaldwin
ms.assetid: PMicrosoft.RightsManagement.CommonRights.All
ms.prod: windows-server-dev
ms.technology: active-directory-rights-management
ms.tgt_platform: multiple
keywords:
- All property
- All property, CommonRights class
- CommonRights class, All property
topic_type:
- apiref
api_name:
- Microsoft.RightsManagement.CommonRights.All
- Microsoft.RightsManagement.CommonRights.
api_location:
- Microsoft.RightsManagement.dll
api_type:
- Assembly
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# CommonRights.All property

Gets a set of all [**CommonRights**](commonrights.md).

## Syntax


```C++
public:
static property IIterable<String^> All { 
   IIterable<String^> get();
}
```



## Property value

Type: [IIterable](https://msdn.microsoft.com/library/windows/apps/xaml/br226024.aspx)

A collection of all [**CommonRights**](commonrights.md).

## Remarks

For more information about the built-in rights and the usage restrictions associated with them that apps should observe, see [Built-in Rights Usage Restriction Reference](built-in-rights-usage-restriction-reference.md).

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

[**CommonRights**](commonrights.md)
</dt> </dl>

 

 





