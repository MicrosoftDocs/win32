---
title: Roles.Viewer property
description: User will only be able to view the document.
audience: developer
author: REDMOND\\bruceper
manager: REDMOND\\mbaldwin
ms.assetid: 'P:Microsoft.RightsManagement.Roles.Viewer'
ms.prod: 'windows-server-dev'
ms.technology: 'active-directory-rights-management'
ms.tgt_platform: multiple
keywords: ["Viewer property", "Viewer property, Roles class", "Roles class, Viewer property"]
topic_type:
- apiref
api_name:
- Microsoft.RightsManagement.Roles.Viewer
- Microsoft.RightsManagement.Roles.
api_location:
- Microsoft.RightsManagement.dll
api_type:
- Assembly
---

# Roles.Viewer property

\[Some information relates to pre-released product which may be substantially modified before it's commercially released. Microsoft makes no warranties, express or implied, with respect to the information provided here.\]

User will only be able to view the document. They cannot edit, copy, or print it.

## Syntax


```C++
public:
property String^ Viewer { 
   String^ get();
}
```



## Property value

Type: **String**

Role is VIEWER.

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

[**Roles**](roles.md)
</dt> </dl>

 

 





