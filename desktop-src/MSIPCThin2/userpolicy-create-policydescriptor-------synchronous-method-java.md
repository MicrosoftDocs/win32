---
title: UserPolicy.create(PolicyDescriptor, ...) synchronous method
description: Asynchronously creates a new UserPolicy object from a policy descriptor.
audience: developer
author: REDMOND\\bruceper
manager: REDMOND\\mbaldwin
ms.assetid: '4BC6BED2-C4BD-47BA-BB1A-63CA897F6163'
ms.prod: 'windows-server-dev'
ms.technology: 'active-directory-rights-management'
ms.tgt_platform: multiple
keywords: ["UserPolicy.create(PolicyDescriptor, ...) synchronous method"]
topic_type:
- apiref
api_name:
- UserPolicy.create(PolicyDescriptor, ...) synchronous method
api_type:
- NA
---

# UserPolicy.create(PolicyDescriptor, ...) synchronous method

Asynchronously creates a new [**UserPolicy**](userpolicy-class-java.md) object from a policy descriptor.

## Signature

``` syntax
public static UserPolicy create(
                                     PolicyDescriptor policyDescriptor,
                                     String userId,
                                     AuthenticationRequestCallback authenticationContext,
                                     int userPolicyCreationFlags,
                                     final Context applicationContext) 
                              throws ProtectionException
```

## Parameters



| Name                                 | Datatype                                                                                         | Notes                                                                                                                                                                                                                                                                             |
|--------------------------------------|--------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| *policyDescriptor*<br/>        | [**PolicyDescriptor**](policydescriptor-interface-java.md)<br/>                           |                                                                                                                                                                                                                                                                                   |
| *userId*<br/>                  | **String**<br/>                                                                            | A unique user identifier such as an email address.<br/> This *userId* is used to discover the RMS service instance (either ADRMS server or Azure RMS) that the user's organization is using. *userId* is used for caching user policy as well for offline usage.<br/> |
| *authenticationContext*<br/>   | [**AuthenticationRequestCallback**](authenticationrequestcallback-interface-java.md)<br/> |                                                                                                                                                                                                                                                                                   |
| *userPolicyCreationFlags*<br/> | **int**<br/>                                                                               | For more information, see [**UserPolicyCreationFlags**](userpolicycreationflags-class-java.md)).<br/>                                                                                                                                                                      |
| *applicationContext*<br/>      | **Context**<br/>                                                                           |                                                                                                                                                                                                                                                                                   |



 

## Throws

[**ProtectionException**](protectionexception-class-java.md)

## Returns

[**UserPolicy**](userpolicy-class-java.md)

## Defined in

UserPolicy.java

## Supported Platforms



|                                             |                                         |
|---------------------------------------------|-----------------------------------------|
| **Minimum supported OS version**<br/> | Android 4.0.3 (API level 15)<br/> |



 

 

 





