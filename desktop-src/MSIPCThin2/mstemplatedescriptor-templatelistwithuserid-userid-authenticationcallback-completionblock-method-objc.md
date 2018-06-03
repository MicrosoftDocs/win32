---
title: MSTemplateDescriptor templateListWithUserId userId authenticationCallback completionBlock method
description: Get the templates.
audience: developer
author: REDMOND\\bruceper
manager: REDMOND\\mbaldwin
ms.assetid: 4E6C0C85-4D46-466F-A5F0-7B37E8D9EDA2
ms.prod: windows-server-dev
ms.technology: active-directory-rights-management
ms.tgt_platform: multiple
keywords:
- MSTemplateDescriptor templateListWithUserId userId authenticationCallback completionBlock method
topic_type:
- apiref
api_name:
- MSTemplateDescriptor templateListWithUserId userId authenticationCallback completionBlock method
api_type:
- NA
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# MSTemplateDescriptor templateListWithUserId:userId:authenticationCallback:completionBlock method

Get the templates.

> [!Note]  
> **templateListWithUserId** should be invoked from the main thread.

 

## Signature

``` syntax
+ (MSAsyncControl *)templateListWithUserId:(NSString *)userId
                    authenticationCallback:(id<MSAuthenticationCallback>)authenticationCallback
                           completionBlock:(void(^)(NSArray/*MSTemplateDescriptor*/ *templates, NSError *error))completionBlock;
```

## Parameters



| Name                                | Datatype                                                                                         | Notes                                                                                                                                                                                                                                            |
|-------------------------------------|--------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| *userId*<br/>                 | **NSString** \*<br/>                                                                       | The email address of the user for whom the templates are being retrieved. <br/> This email address will be used to discover the RMS service instance (either ADRMS server or Azure RMS) that the user's organization is using. <br/> |
| *authenticationCallback*<br/> | id&lt;[**MSAuthenticationCallback**](msauthenticationcallback-protocol-objc.md)&gt; <br/> | authentication callback to be used for auth.<br/>                                                                                                                                                                                          |
| *completionBlock*<br/>        | (**NSArray** \*templates, **NSError** \*error)<br/>                                        | An array of [**MSTemplateDescriptor**](mstemplatedescriptor-interface-objc.md) matching the user's tenant template and error code.<br/>                                                                                                   |



 

## Returns

An array of [**MSTemplateDescriptor**](mstemplatedescriptor-interface-objc.md) matching the user's tenant template.

## Defined in

MSTemplateDescriptor.h

## Supported Platforms



|                                              |                                  |
|----------------------------------------------|----------------------------------|
| **Minimum supported OS versions**<br/> | iOS 7.0 and OS X 10.8<br/> |



 

## Remarks

**templateListWithUserId** should be invoked from the main thread.

 

 





