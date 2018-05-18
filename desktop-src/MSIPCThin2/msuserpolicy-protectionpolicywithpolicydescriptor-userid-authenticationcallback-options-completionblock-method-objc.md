---
title: MSUserPolicy userPolicyWithPolicyDescriptor userId authenticationCallback options completionBlock method
description: Creates a user policy based on the supplied policy descriptor.
audience: developer
author: REDMOND\\bruceper
manager: REDMOND\\mbaldwin
ms.assetid: '1CDCA4A2-5F34-4AAF-979C-A828D593A4CC'
ms.prod: 'windows-server-dev'
ms.technology: 'active-directory-rights-management'
ms.tgt_platform: multiple
keywords: ["MSUserPolicy userPolicyWithPolicyDescriptor userId authenticationCallback options completionBlock method"]
topic_type:
- apiref
api_name:
- MSUserPolicy userPolicyWithPolicyDescriptor userId authenticationCallback options completionBlock method
api_type:
- NA
---

# MSUserPolicy userPolicyWithPolicyDescriptor:userId:authenticationCallback:options:completionBlock method

Creates a user policy based on the supplied policy descriptor. The following method should be invoked from the main thread.

## Signature

``` syntax
+ (MSAsyncControl *)userPolicyWithPolicyDescriptor:(MSPolicyDescriptor *)policyDescriptor
                                                  userId:(NSString *)userId
                                    authenticationCallback:(id<MSAuthenticationCallback>)authenticationCallback
                                                   options:(MSUserPolicyCreationOptions)options
                                           completionBlock:(void(^)(MSUserPolicy *userPolicy, NSError *error))completionBlock;
```

## Parameters



| Name                                | Datatype                                                                                                  | Notes                                                                                                                                                                                                                                            |
|-------------------------------------|-----------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| *policyDescriptor*<br/>       | [**MSPolicyDescriptor**](mspolicydescriptor-interface-objc.md) \*<br/>                             | Required. The object which defines the policy.<br/>                                                                                                                                                                                        |
| *userId*<br/>                 | **NSString** \*<br/>                                                                                | The email address of the user for whom the templates are being retrieved. <br/> This email address will be used to discover the RMS service instance (either ADRMS server or Azure RMS) that the user's organization is using. <br/> |
| *authenticationCallback*<br/> | id&lt;[**MSAuthenticationCallback**](msauthenticationcallback-protocol-objc.md)&gt;) \*<br/>       | Callback Id to be used for authorization.<br/>                                                                                                                                                                                             |
| *options*<br/>                | [**MSUserPolicyCreationOptions**](msprotectionpolicycreationoptions-enum-objc.md)<br/>             | Options for creating the user policy object<br/>                                                                                                                                                                                           |
| *completionBlock*<br/>        | void(^)([**MSUserPolicy**](msuserpolicy-interface-objc.md) \*userPolicy, **NSError** \*error)<br/> | The created protection policy.<br/>                                                                                                                                                                                                        |



 

## Returns

A pointer to an [**MSAsyncControl**](msasynccontrol-class.md) object.

## Defined in

MSUserPolicy.h

## Supported Platforms



|                                              |                                  |
|----------------------------------------------|----------------------------------|
| **Minimum supported OS versions**<br/> | iOS 7.0 and OS X 10.8<br/> |



 

 

 





