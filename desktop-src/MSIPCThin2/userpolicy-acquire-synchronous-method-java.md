---
title: UserPolicy.acquire synchronous method
description: Asynchronously acquires a UserPolicy object based on a serialized content policy.
audience: developer
author: REDMOND\\bruceper
manager: REDMOND\\mbaldwin
ms.assetid: 28900F92-1C41-4870-BD57-6A8F31D85336
ms.prod: windows-server-dev
ms.technology: active-directory-rights-management
ms.tgt_platform: multiple
keywords:
- UserPolicy.acquire synchronous method
topic_type:
- apiref
api_name:
- UserPolicy.acquire synchronous method
api_type:
- NA
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# UserPolicy.acquire synchronous method

\[Some information relates to pre-released product which may be substantially modified before it's commercially released. Microsoft makes no warranties, express or implied, with respect to the information provided here.\]

Asynchronously acquires a [**UserPolicy**](userpolicy-class-java.md) object based on a serialized content policy. The I/O call is made on the calling thread.

## Signature

``` syntax
public static UserPolicy acquire(
                                     final byte[] serializedContentPolicy,
                                     final String userId,
                                     final AuthenticationRequestCallback authenticationCallback,
                                     final ConsentCallback consentCallback,
                                     final int policyAcquisitionFlags,
                                     final Context applicationContext) 
                               throws ProtectionException
```

## Parameters



| Name                                 | Datatype                                                                                         | Notes                                                                                                                                                                                                                                                                                                                                                                                               |
|--------------------------------------|--------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| *serializedContentPolicy*<br/> | **byte**\[\]<br/>                                                                          | A serialized content policy<br/>                                                                                                                                                                                                                                                                                                                                                              |
| *userId*<br/>                  | **String**<br/>                                                                            | Optional.<br/> A *userId* is used for caching a user policy for offline usage. For multiple user scenarios, caller must supply a *userId*.<br/> If *userId* is null, then the user policy is cached without *userId* and is retrievable with null *userId* as well. A null *userId* also retrieves any matching offline user policy cached without *userId* or any *userId*.<br/> |
| *authenticationCallback*<br/>  | [**AuthenticationRequestCallback**](authenticationrequestcallback-interface-java.md)<br/> |                                                                                                                                                                                                                                                                                                                                                                                                     |
| *consentCallback*<br/>         | [**ConsentCallback**](https://msdn.microsoft.com/library/windows/desktop/dn833503)<br/>                     |                                                                                                                                                                                                                                                                                                                                                                                                     |
| *policyAcquisitionFlags*<br/>  | **int**<br/>                                                                               | For more information, see [**PolicyAcquisitionFlags**](policyacquisitionflags-class-java.md)<br/>                                                                                                                                                                                                                                                                                            |
| *applicationContext*<br/>      |                                                                                                  |                                                                                                                                                                                                                                                                                                                                                                                                     |



 

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



 

 

 





