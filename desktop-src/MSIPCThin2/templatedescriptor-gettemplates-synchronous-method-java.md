---
title: TemplateDescriptor.getTemplates synchronous method
description: Synchronously queries the server for the tenants policy templates.
audience: developer
author: REDMOND\\bruceper
manager: REDMOND\\mbaldwin
ms.assetid: 8E76D445-DF64-4BA5-8A93-EDD6FE5A030B
ms.prod: windows-server-dev
ms.technology: active-directory-rights-management
ms.tgt_platform: multiple
keywords:
- TemplateDescriptor.getTemplates synchronous method
topic_type:
- apiref
api_name:
- TemplateDescriptor.getTemplates synchronous method
api_type:
- NA
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# TemplateDescriptor.getTemplates synchronous method

Synchronously queries the server for the tenant's policy templates. This method could launch the Authentication UI if no valid authentication token is present.

## Signature

``` syntax
public static List<TemplateDescriptor> getTemplates(
                                             String userId,
                                             AuthenticationRequestCallback authenticationCallback,
                                             Context applicationContext)
                              throws ProtectionException
```

## Parameters



| Name                                | Datatype                                                                                         | Notes                                                                                                                                                                                                                               |
|-------------------------------------|--------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| *userId*<br/>                 | **String**<br/>                                                                            | This *userId* (email address) is used to discover the RMS service instance (either ADRMS server or Azure RMS) that the user's organization is using. *userId* is used for caching user policy as well for offline usage.<br/> |
| *authenticationCallback*<br/> | [**AuthenticationRequestCallback**](authenticationrequestcallback-interface-java.md)<br/> |                                                                                                                                                                                                                                     |
| *applicationContext*<br/>     | **Context**<br/>                                                                           |                                                                                                                                                                                                                                     |



 

## Returns

List&lt;[**TemplateDescriptor**](templatedescriptor-class-java.md)&gt;

## Throws

[**ProtectionException**](protectionexception-class-java.md)

## Defined in

TemplateDescriptor.java

## Supported Platforms



|                                             |                                         |
|---------------------------------------------|-----------------------------------------|
| **Minimum supported OS version**<br/> | Android 4.0.3 (API level 15)<br/> |



 

 

 





