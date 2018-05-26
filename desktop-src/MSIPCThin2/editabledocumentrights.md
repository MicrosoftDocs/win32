---
title: EditableDocumentRights class
description: Rights that apply to editable documents.
audience: developer
author: REDMOND\\bruceper
manager: REDMOND\\mbaldwin
ms.assetid: TMicrosoft.RightsManagement.EditableDocumentRights
ms.prod: windows-server-dev
ms.technology: active-directory-rights-management
ms.tgt_platform: multiple
keywords:
- EditableDocumentRights class
topic_type:
- apiref
api_name:
- Microsoft.RightsManagement.EditableDocumentRights
api_location:
- Microsoft.RightsManagement.dll
api_type:
- Assembly
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# EditableDocumentRights class

Rights that apply to editable documents.

## Syntax


```C++
public ref class EditableDocumentRights 
```



## Members

The **EditableDocumentRights** class inherits from [IInspectable](https://msdn.microsoft.com/library/windows/apps/br205821). **EditableDocumentRights** also has these types of members:

-   [Properties](#properties)

### Properties

The **EditableDocumentRights** class has these properties.



| Property                                                     | Access type          | Description                                                                                                                                                                 |
|:-------------------------------------------------------------|:---------------------|:----------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**All**](editabledocumentrights-all.md)<br/>         | Read-only<br/> | Gets a collection of all the rights that apply to editable documents.                                                                                                       |
| [**Edit**](editabledocumentrights-edit.md)<br/>       | Read-only<br/> | Gets a right that allows the protected content to be edited and saved to the same protected format.                                                                         |
| [**Export**](editabledocumentrights-export.md)<br/>   | Read-only<br/> | Gets a right that allows content to be extracted from a protected format and placed in a different AD RMS-protected format.                                                 |
| [**Extract**](editabledocumentrights-extract.md)<br/> | Read-only<br/> | Gets a right that allows content to be extracted from a protected format and placed in an unprotected, or a different protected, format. Same value as EmailRights.Extract. |
| [**Print**](editabledocumentrights-print.md)<br/>     | Read-only<br/> | Gets a right that allows protected content to be printed. Same value as EmailRights.Print.                                                                                  |



 

## Remarks

For more information about the built-in rights and the usage restrictions associated with them that apps should observe, see [Built-in Rights Usage Restriction Reference](built-in-rights-usage-restriction-reference.md).

## Thread Safety

Members of this class are not guaranteed to be thread safe.

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

[IInspectable](https://msdn.microsoft.com/library/windows/apps/br205821)
</dt> </dl>

 

 





