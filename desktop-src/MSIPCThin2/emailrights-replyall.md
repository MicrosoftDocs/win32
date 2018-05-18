---
title: EmailRights.ReplyAll property
description: Gets a right that allows reply-all to a protected email message with a message that includes a copy of the protected content.
audience: developer
author: REDMOND\\bruceper
manager: REDMOND\\mbaldwin
ms.assetid: 'P:Microsoft.RightsManagement.EmailRights.ReplyAll'
ms.prod: 'windows-server-dev'
ms.technology: 'active-directory-rights-management'
ms.tgt_platform: multiple
keywords: ["ReplyAll property", "ReplyAll property, EmailRights class", "EmailRights class, ReplyAll property"]
topic_type:
- apiref
api_name:
- Microsoft.RightsManagement.EmailRights.ReplyAll
- Microsoft.RightsManagement.EmailRights.
api_location:
- Microsoft.RightsManagement.dll
api_type:
- Assembly
---

# EmailRights.ReplyAll property

Gets a right that allows reply-all to a protected email message with a message that includes a copy of the protected content.

## Syntax


```C++
public:
static property 
    
    String^ ReplyAll { 
   
    
    String^ get();
}
```



## Property value

Type: **String^**

The reply-all right.

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

 

 





