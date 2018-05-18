---
title: EditableDocumentRights.Print property
description: Gets a right that allows protected content to be printed. Same value as EmailRights.Print.
audience: developer
author: REDMOND\\bruceper
manager: REDMOND\\mbaldwin
ms.assetid: 'P:Microsoft.RightsManagement.EditableDocumentRights.Print'
ms.prod: 'windows-server-dev'
ms.technology: 'active-directory-rights-management'
ms.tgt_platform: multiple
keywords: ["Print property", "Print property, EditableDocumentRights class", "EditableDocumentRights class, Print property"]
topic_type:
- apiref
api_name:
- Microsoft.RightsManagement.EditableDocumentRights.Print
- Microsoft.RightsManagement.EditableDocumentRights.
api_location:
- Microsoft.RightsManagement.dll
api_type:
- Assembly
---

# EditableDocumentRights.Print property

Gets a right that allows protected content to be printed. Same value as [**EmailRights.Print**](emailrights-print.md).

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

[**EditableDocumentRights**](editabledocumentrights.md)
</dt> </dl>

 

 





