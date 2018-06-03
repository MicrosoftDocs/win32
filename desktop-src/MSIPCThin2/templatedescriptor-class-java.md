---
title: TemplateDescriptor class
description: Information associated with a user's tenant template policy.
audience: developer
author: REDMOND\\bruceper
manager: REDMOND\\mbaldwin
ms.assetid: 1ED36F7E-FC7D-474C-8B39-615C8AC4DEA5
ms.prod: windows-server-dev
ms.technology: active-directory-rights-management
ms.tgt_platform: multiple
keywords:
- TemplateDescriptor class
topic_type:
- apiref
api_name:
- TemplateDescriptor class
api_type:
- NA
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# TemplateDescriptor class

Information associated with a user's tenant template policy.

## Signature

``` syntax
public class TemplateDescriptor implements Serializable
```

## Methods



| Name                                                                                                   | Description                                                                     |
|--------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------|
| [**getDescription**](templatedescriptor-getdescription-method-java.md)<br/>                     | Gets the template description.<br/>                                       |
| [**getName**](templatedescriptor-getname-method-java.md)<br/>                                   | Gets the template name.<br/>                                              |
| [**getTemplateId**](templatedescriptor-gettemplateid-method-java.md)<br/>                       | Gets the template ID.<br/>                                                |
| [**getTemplates asynchronous**](templatedescriptor-gettemplates-method-java.md)<br/>            | Asynchronously queries the server for the tenant's policy templates.<br/> |
| [**getTemplates synchronous**](templatedescriptor-gettemplates-synchronous-method-java.md)<br/> | Synchronously queries the server for the tenant's policy templates.<br/>  |
| [**setTemplateId**](templatedescriptor-setid-method-java.md)<br/>                               | Sets the template ID.<br/>                                                |
| [**setDescription**](templatedescriptor-setdescription-method-java.md)<br/>                     | Sets the template description.<br/>                                       |
| [**setName**](templatedescriptor-setname-method.md)<br/>                                        | Sets the template name.<br/>                                              |



 

## Defined in

TemplateDescriptor.java

## Supported Platforms



|                                             |                                         |
|---------------------------------------------|-----------------------------------------|
| **Minimum supported OS version**<br/> | Android 4.0.3 (API level 15)<br/> |



 

## Package

com.microsoft.rightsmanagement

## Thread Safety

Members of this class are not guaranteed to be thread safe.

 

 





