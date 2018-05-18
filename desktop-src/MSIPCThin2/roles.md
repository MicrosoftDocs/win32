---
title: Roles class
description: Implementation of roles for protecting documents.
audience: developer
author: REDMOND\\bruceper
manager: REDMOND\\mbaldwin
ms.assetid: 'T:Microsoft.RightsManagement.Roles'
ms.prod: 'windows-server-dev'
ms.technology: 'active-directory-rights-management'
ms.tgt_platform: multiple
keywords: ["Roles class"]
topic_type:
- apiref
api_name:
- Microsoft.RightsManagement.Roles
api_location:
- Microsoft.RightsManagement.dll
api_type:
- Assembly
---

# Roles class

Implementation of roles for protecting documents.

## Syntax


```C++
public ref class Roles 
```



## Members

The **Roles** class inherits from [IInspectable](https://msdn.microsoft.com/library/windows/apps/br205821). **Roles** also has these types of members:

-   [Properties](#properties)

### Properties

The **Roles** class has these properties.



| Property                                      | Access type          | Description                                                    |
|:----------------------------------------------|:---------------------|:---------------------------------------------------------------|
| [**Author**](roles-author.md)<br/>     | Read-only<br/> | User will be able to view, edit, copy, and print the document. |
| [**CoOwner**](roles-coowner.md)<br/>   | Read-only<br/> | User will have all permissions; view, edit, copy and print.    |
| [**Reviewer**](roles-reviewer.md)<br/> | Read-only<br/> | User will be able to view and edit the document,               |
| [**Viewer**](roles-viewer.md)<br/>     | Read-only<br/> | User will only be able to view the document.                   |



 

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

 

 





