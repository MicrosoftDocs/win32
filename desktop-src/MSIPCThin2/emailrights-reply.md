---
title: EmailRights.Reply property
description: Gets a right that allows a protected email message to be replied to with a message that includes a copy of the protected content.
audience: developer
author: REDMOND\\bruceper
manager: REDMOND\\mbaldwin
ms.assetid: PMicrosoft.RightsManagement.EmailRights.Reply
ms.prod: windows-server-dev
ms.technology: active-directory-rights-management
ms.tgt_platform: multiple
keywords:
- Reply property
- Reply property, EmailRights class
- EmailRights class, Reply property
topic_type:
- apiref
api_name:
- Microsoft.RightsManagement.EmailRights.Reply
- Microsoft.RightsManagement.EmailRights.
api_location:
- Microsoft.RightsManagement.dll
api_type:
- Assembly
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# EmailRights.Reply property

Gets a right that allows a protected email message to be replied to with a message that includes a copy of the protected content.

## Syntax


```C++
public:
static property 
    
    String^ Reply { 
   
    
    String^ get();
}
```



## Property value

Type: **String^**

The reply right.

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

[**EmailRights**](emailrights.md)
</dt> </dl>

 

 





