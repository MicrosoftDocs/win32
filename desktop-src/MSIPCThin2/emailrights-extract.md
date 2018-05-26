---
title: EmailRights.Extract property
description: Gets a right that allows content to be extracted from a protected email and placed in an unprotected, or a different protected, format. Same value as EditableDocumentRights.Extract.
audience: developer
author: REDMOND\\bruceper
manager: REDMOND\\mbaldwin
ms.assetid: PMicrosoft.RightsManagement.EmailRights.Extract
ms.prod: windows-server-dev
ms.technology: active-directory-rights-management
ms.tgt_platform: multiple
keywords:
- Extract property
- Extract property, EmailRights class
- EmailRights class, Extract property
topic_type:
- apiref
api_name:
- Microsoft.RightsManagement.EmailRights.Extract
- Microsoft.RightsManagement.EmailRights.
api_location:
- Microsoft.RightsManagement.dll
api_type:
- Assembly
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# EmailRights.Extract property

Gets a right that allows content to be extracted from a protected email and placed in an unprotected, or a different protected, format. Same value as [**EditableDocumentRights.Extract**](editabledocumentrights-extract.md).

## Syntax


```C++
public:
static property 
    String^ Extract { 
   
    String^ get();
}
```



## Property value

Type: **String^**

The extract right.

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

 

 





