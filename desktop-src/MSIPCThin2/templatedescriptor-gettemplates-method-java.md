---
title: TemplateDescriptor getTemplates asynchronous method
description: Asynchronously queries the server for the tenant's policy templates.
audience: developer
author: REDMOND\\bruceper
manager: REDMOND\\mbaldwin
ms.assetid: 'F4308E31-7ECA-4A61-8CBA-1A0E25F65DDD'
ms.prod: 'windows-server-dev'
ms.technology: 'active-directory-rights-management'
ms.tgt_platform: multiple
keywords: ["TemplateDescriptor getTemplates asynchronous method"]
topic_type:
- apiref
api_name:
- TemplateDescriptor getTemplates asynchronous method
api_type:
- NA
---

# TemplateDescriptor getTemplates asynchronous method

Asynchronously queries the server for the tenant's policy templates.

## Signature

``` syntax
public static IAsyncControl getTemplates(String userId,
                              AuthenticationRequestCallback authenticationCallback,
                              CreationCallback<List<TemplateDescriptor>> callback)
                              throws InvalidParameterException
```

## Parameters



| Name                                | Datatype                                                                                                   | Notes                                                                                                                                                                                                                               |
|-------------------------------------|------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| *userId*<br/>                 | **String**<br/>                                                                                      | This *userId* (email address) is used to discover the RMS service instance (either ADRMS server or Azure RMS) that the user's organization is using. *userId* is used for caching user policy as well for offline usage.<br/> |
| *authenticationCallback*<br/> | [**AuthenticationRequestCallback**](authenticationrequestcallback-interface-java.md)<br/>           |                                                                                                                                                                                                                                     |
| *callback*<br/>               | CreationCallback&lt;List&lt;[**TemplateDescriptor**](templatedescriptor-class-java.md)&gt;&gt;<br/> |                                                                                                                                                                                                                                     |



 

## Returns

[**IAsyncControl**](iasynccontrol-interface.md)

## Throws

[**InvalidParameterException**](invalidparameterexception-class-java.md)

## Defined in

TemplateDescriptor.java

## Supported Platforms



|                                             |                                         |
|---------------------------------------------|-----------------------------------------|
| **Minimum supported OS version**<br/> | Android 4.0.3 (API level 15)<br/> |



 

## Remarks

This method could launch the Authentication UI if no valid authentication token is present.

 

 





