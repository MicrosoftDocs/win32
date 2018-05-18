---
title: EmailRights.Print property
description: Gets a right that allows protected email content to be printed. Same value as EditableDocumentRights.Print.
audience: developer
author: REDMOND\\bruceper
manager: REDMOND\\mbaldwin
ms.assetid: 'P:Microsoft.RightsManagement.EmailRights.Print'
ms.prod: 'windows-server-dev'
ms.technology: 'active-directory-rights-management'
ms.tgt_platform: multiple
keywords: ["Print property", "Print property, EmailRights class", "EmailRights class, Print property"]
topic_type:
- apiref
api_name:
- Microsoft.RightsManagement.EmailRights.Print
- Microsoft.RightsManagement.EmailRights.
api_location:
- Microsoft.RightsManagement.dll
api_type:
- Assembly
---

# EmailRights.Print property

Gets a right that allows protected email content to be printed. Same value as [**EditableDocumentRights.Print**](editabledocumentrights-print.md).

## Syntax


```C++
public:
static property 
    
    String^ Print { 
   
    
    String^ get();
}
```



## Property value

Type: **String^**

The print right.

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

 

 





