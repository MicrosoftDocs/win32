---
title: CommonRights.Owner property
description: Gets a right that represents content ownership.
audience: developer
author: REDMOND\\bruceper
manager: REDMOND\\mbaldwin
ms.assetid: P:Microsoft.RightsManagement.CommonRights.Owner
ms.prod: windows-server-dev
ms.technology: active-directory-rights-management
ms.tgt_platform: multiple
keywords:
- Owner property
- Owner property, CommonRights class
- CommonRights class, Owner property
topic_type:
- apiref
api_name:
- Microsoft.RightsManagement.CommonRights.Owner
- Microsoft.RightsManagement.CommonRights.
api_location:
- Microsoft.RightsManagement.dll
api_type:
- Assembly
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# CommonRights.Owner property

Gets a right that represents content ownership. This right grants full control over the protected content.

## Syntax


```C++
public:
static property 
    String^ Owner { 
   
    String^ get();
}
```



## Property value

Type: **String^**

The owner right.

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

 

 





