---
title: UserPolicy.TemplateDescriptor property
description: Gets the template used to publish the content.
audience: developer
author: REDMOND\\bruceper
manager: REDMOND\\mbaldwin
ms.assetid: PMicrosoft.RightsManagement.UserPolicy.TemplateDescriptor
ms.prod: windows-server-dev
ms.technology: active-directory-rights-management
ms.tgt_platform: multiple
keywords:
- TemplateDescriptor property
- TemplateDescriptor property, UserPolicy class
- UserPolicy class, TemplateDescriptor property
topic_type:
- apiref
api_name:
- Microsoft.RightsManagement.UserPolicy.TemplateDescriptor
- Microsoft.RightsManagement.UserPolicy.
api_location:
- Microsoft.RightsManagement.dll
api_type:
- Assembly
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# UserPolicy.TemplateDescriptor property

Gets the template used to publish the content.

> [!Note]  
> This property will be null for custom (adhoc) policies.

 

## Syntax


```C++
public:
property TemplateDescriptor^ TemplateDescriptor { 
   TemplateDescriptor^ get();
}
```



## Property value

Type: [**TemplateDescriptor**](https://msdn.microsoft.com/library/windows/desktop/dn920793)

The template used to publish (encrypt) the content.

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

[**UserPolicy**](userpolicy.md)
</dt> </dl>

 

 





