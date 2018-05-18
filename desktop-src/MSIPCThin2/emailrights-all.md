---
title: EmailRights.All property
description: Gets a list of all the rights that apply to emails.
audience: developer
author: REDMOND\\bruceper
manager: REDMOND\\mbaldwin
ms.assetid: 'P:Microsoft.RightsManagement.EmailRights.All'
ms.prod: 'windows-server-dev'
ms.technology: 'active-directory-rights-management'
ms.tgt_platform: multiple
keywords: ["All property", "All property, EmailRights class", "EmailRights class, All property"]
topic_type:
- apiref
api_name:
- Microsoft.RightsManagement.EmailRights.All
- Microsoft.RightsManagement.EmailRights.
api_location:
- Microsoft.RightsManagement.dll
api_type:
- Assembly
---

# EmailRights.All property

Gets a list of all the rights that apply to emails.

## Syntax


```C++
public:
static property 
    IIterable<String^>^ All { 
   
    IIterable<String^>^ get();
}
```



## Property value

Type: **IIterable&lt;String^&gt;^**

A list of all rights for emails.

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

 

 





