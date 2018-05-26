---
title: EditableDocumentRights.Extract property
description: Gets a right that allows content to be extracted from a protected format and placed in an unprotected, or a different protected, format. Same value as EmailRights.Extract.
audience: developer
author: REDMOND\\bruceper
manager: REDMOND\\mbaldwin
ms.assetid: PMicrosoft.RightsManagement.EditableDocumentRights.Extract
ms.prod: windows-server-dev
ms.technology: active-directory-rights-management
ms.tgt_platform: multiple
keywords:
- Extract property
- Extract property, EditableDocumentRights class
- EditableDocumentRights class, Extract property
topic_type:
- apiref
api_name:
- Microsoft.RightsManagement.EditableDocumentRights.Extract
- Microsoft.RightsManagement.EditableDocumentRights.
api_location:
- Microsoft.RightsManagement.dll
api_type:
- Assembly
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# EditableDocumentRights.Extract property

Gets a right that allows content to be extracted from a protected format and placed in an unprotected, or a different protected, format. Same value as [**EmailRights.Extract**](emailrights-extract.md).

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

[**EditableDocumentRights**](editabledocumentrights.md)
</dt> </dl>

 

 





