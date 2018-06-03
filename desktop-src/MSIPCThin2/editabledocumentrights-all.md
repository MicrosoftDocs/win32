---
title: EditableDocumentRights.All property
description: Gets a collection of all the rights that apply to editable documents.
audience: developer
author: REDMOND\\bruceper
manager: REDMOND\\mbaldwin
ms.assetid: P:Microsoft.RightsManagement.EditableDocumentRights.All
ms.prod: windows-server-dev
ms.technology: active-directory-rights-management
ms.tgt_platform: multiple
keywords:
- All property
- All property, EditableDocumentRights class
- EditableDocumentRights class, All property
topic_type:
- apiref
api_name:
- Microsoft.RightsManagement.EditableDocumentRights.All
- Microsoft.RightsManagement.EditableDocumentRights.
api_location:
- Microsoft.RightsManagement.dll
api_type:
- Assembly
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# EditableDocumentRights.All property

Gets a collection of all the rights that apply to editable documents.

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

The collection rights that apply to editable documents.

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

 

 





