---
title: TemplateDescriptor class
description: Template information.
audience: developer
author: REDMOND\\bruceper
manager: REDMOND\\mbaldwin
ms.assetid: TMicrosoft.RightsManagement.TemplateDescriptor
ms.prod: windows-server-dev
ms.technology: active-directory-rights-management
ms.tgt_platform: multiple
keywords:
- TemplateDescriptor class
topic_type:
- apiref
api_name:
- Microsoft.RightsManagement.TemplateDescriptor
api_location:
- Microsoft.RightsManagement.dll
api_type:
- Assembly
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# TemplateDescriptor class

Template information

## Syntax


```C++
public ref class TemplateDescriptor sealed 
```



## Members

The **TemplateDescriptor** class inherits from [IInspectable](https://msdn.microsoft.com/library/windows/apps/br205821). **TemplateDescriptor** also has these types of members:

-   [Methods](#methods)
-   [Properties](#properties)

### Methods

The **TemplateDescriptor** class has these methods. It also inherits methods from the **Object** class.



| Method                                                                  | Description        |
|:------------------------------------------------------------------------|:-------------------|
| [**GetTemplateListAsync**](templatedescriptor-gettemplatelistasync.md) | Get the templates. |



 

### Properties

The **TemplateDescriptor** class has these properties.



| Property                                                         | Access type          | Description                                                             |
|:-----------------------------------------------------------------|:---------------------|:------------------------------------------------------------------------|
| [**Description**](templatedescriptor-description.md)<br/> | Read-only<br/> | Gets the description for the policy template on the TemplateDescriptor. |
| [**Name**](templatedescriptor-name.md)<br/>               | Read-only<br/> | Gets the name of the policy template.                                   |
| [**TemplateId**](templatedescriptor-templateid.md)<br/>   | Read-only<br/> | Gets the policy template ID.                                            |



 

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

 

 





